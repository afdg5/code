#! /usr/bin/env python

import wx
import numpy as np
import os
import main
import rospy
from ws_generator.msg import WSArray
from std_msgs.msg import String

##############################################################################80
class Texture:
    """"""

    #----------------------------------------------------------------------
    def __init__(self, id, shape):
        """Constructor"""
        self.id = id
        self.shape = shape


##############################################################################80
class Frame(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self):
        """"""
        self.ws_ufm_pub = rospy.Publisher('/cursor_position/workspace/ufm', WSArray, queue_size = 0)
        self.ws_ev_pub = rospy.Publisher('/cursor_position/workspace/ev', WSArray, queue_size = 0)
        self.rospack = rospkg.RosPack()
        rospy.init_node('gui_ws')

        wx.Frame.__init__(self, None, wx.ID_ANY, "Hybridization Comparison")
        self.Maximize(True)
        self.width, self.height = wx.GetDisplaySize()
        self.width_half = self.width/2.0

        self.first_rectangle_y = 0.1*self.height
        self.bottom_space = 0.035*self.height

        self.rectangle_size = 0.175*self.height
        self.rectangle_seperation = int((self.height-self.first_rectangle_y-self.bottom_space-3*self.rectangle_size)/3.0)

        self.rectangle_color = "GREY"

        self.textbox_width = 0.20*self.width
        self.textbox_x = 0.04*self.width
        self.textbox_y = self.rectangle_size*0.35
        self.textbox_color = "WHITE"
        self.textbox_fontsize = 42

        self.haptic_width = self.width - self.textbox_width

        self.background_color = "BLACK"

        # Add a panel so it looks the correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.panel.Bind(wx.EVT_PAINT, self.OnPaint)

        textures = [Texture(0, "Bump"),
                    Texture(1, "Sinusoidal"),
                    Texture(2, "Triangular"),
                    Texture(3, "Square")]

        sampleList = []

        backButton = wx.Button(self.panel,wx.ID_ANY,'BACK')
        backButton.Bind(wx.EVT_BUTTON,self.onButton)

        self.cb = wx.ComboBox(self.panel,
                              size=wx.DefaultSize,
                              choices=sampleList,
                              pos=(0.1*self.width,0.05*self.height))
        self.widgetMaker(self.cb, textures)

        self.Centre()
        self.Show()

        #sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(self.cb, 0, wx.ALL, 5)
        #self.panel.SetSizer(sizer)

    def onButton(self,event):

        fr = main.frameMain(None)
        self.Close()
        fr.Show()

    #----------------------------------------------------------------------
    def widgetMaker(self, widget, objects):
        """"""
        for obj in objects:
            widget.Append(obj.shape, obj)
            widget.Bind(wx.EVT_COMBOBOX, self.onSelect)

    #----------------------------------------------------------------------
    def OnPaint(self, evt):
        """set up the device for painting"""
        dc = wx.PaintDC(self.panel)
        dc.BeginDrawing()
        brush = wx.Brush(self.background_color)
        dc.SetBackground(brush)
        dc.Clear()

        path = os.path.join('../code', 'haptics_symp.jpg')
        picture = wx.Bitmap(path)
        width,height = picture.GetSize()

        dc.DrawBitmap(picture,(self.width-width)/2,(self.height-height)/2,True)
        font = wx.Font(self.textbox_fontsize, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        dc.SetFont(font)

        """EV Rectangle"""
        rectangle_y = self.first_rectangle_y
        dc.SetPen(wx.Pen(self.rectangle_color))
        dc.SetBrush(wx.Brush(self.rectangle_color))
        # set x, y, w, h for rectangle
        dc.DrawRectangle(0, rectangle_y, self.width, self.rectangle_size)
        dc.SetPen(wx.Pen(self.textbox_color))
        dc.SetBrush(wx.Brush(self.textbox_color))
        dc.DrawRectangle(0, rectangle_y, self.textbox_width, self.rectangle_size)
        textbox = wx.Rect(self.textbox_x, rectangle_y+self.textbox_y)
        dc.DrawLabel("EV", textbox, alignment=1)

        """UFM Rectangle"""
        rectangle_y = self.first_rectangle_y+(self.rectangle_size+self.rectangle_seperation)
        dc.SetPen(wx.Pen(self.rectangle_color))
        dc.SetBrush(wx.Brush(self.rectangle_color))
        # set x, y, w, h for rectangle
        dc.DrawRectangle(0, rectangle_y, self.width, self.rectangle_size)
        dc.SetPen(wx.Pen(self.textbox_color))
        dc.SetBrush(wx.Brush(self.textbox_color))
        dc.DrawRectangle(0, rectangle_y, self.textbox_width, self.rectangle_size)
        textbox = wx.Rect(self.textbox_x, rectangle_y+self.textbox_y)
        dc.DrawLabel("UFM", textbox, alignment=1)

        """Hybrid Rectangle"""
        rectangle_y = self.first_rectangle_y+(self.rectangle_size+self.rectangle_seperation)*2
        dc.SetPen(wx.Pen(self.rectangle_color))
        dc.SetBrush(wx.Brush(self.rectangle_color))
        # set x, y, w, h for rectangle
        dc.DrawRectangle(0, rectangle_y, self.width, self.rectangle_size)
        dc.SetPen(wx.Pen(self.textbox_color))
        dc.SetBrush(wx.Brush(self.textbox_color))
        dc.DrawRectangle(0, rectangle_y, self.textbox_width, self.rectangle_size)
        textbox = wx.Rect(self.textbox_x, rectangle_y+self.textbox_y)
        dc.DrawLabel("Hybrid", textbox, alignment=1)

        dc.EndDrawing()
        del dc

    #----------------------------------------------------------------------
    def onSelect(self, event):
        """"""
        print ("You selected: " + self.cb.GetStringSelection())
        obj = self.cb.GetClientData(self.cb.GetSelection())
        text = """
        The object's attributes are:
        %s  %s

        """ % (obj.id, obj.shape)
        print (text)
        self.generate_workspace(self.cb.GetStringSelection())

    def generate_workspace(self, texture):

        ufm_intensity = []
        ev_intensity = []

        """Determine y workspace bounds"""
        y_ws_ufm = []
        y_ws_ev = []

        rectangle_y = self.first_rectangle_y
        y_ws_ev.append(rectangle_y)
        y_ws_ev.append(rectangle_y+self.rectangle_size)

        rectangle_y = rectangle_y + self.rectangle_size + self.rectangle_seperation
        y_ws_ufm.append(rectangle_y)
        y_ws_ufm.append(rectangle_y + self.rectangle_size)

        rectangle_y = rectangle_y + self.rectangle_size + self.rectangle_seperation
        y_ws_ev.append(rectangle_y)
        y_ws_ev.append(rectangle_y + self.rectangle_size)
        y_ws_ufm.append(rectangle_y)
        y_ws_ufm.append(rectangle_y + self.rectangle_size)

        """Determine x intensities correlating with texture"""
        if texture == "Bump":

            x_center = (self.haptic_width)/2
            x_biasedcenter = x_center+self.textbox_width

            x_haptic_switch = [x_biasedcenter-225,x_biasedcenter+225]
            x_ufm_dropoff = [x_biasedcenter-400,x_biasedcenter+400]
            x_ev_max = [x_biasedcenter-75,x_biasedcenter+75]

            c1 = (x_haptic_switch[0]-x_biasedcenter)**2
            c2 = (x_ufm_dropoff[0]-x_biasedcenter)**2
            kufm = -c1/(c2-c1)
            aufm = (1.0-kufm)/c2

            c3 = (x_ev_max[0]-x_biasedcenter)**2
            kev = -c1/(c3-c1)
            aev = (1.0-kev)/c3

            """Set haptic intensity = 0 over textbox"""
            ufm_intensity = [0]*int(self.textbox_width)
            ev_intensity = [0]*int(self.textbox_width)

            for index in range(int(self.haptic_width)):
                index = index + self.textbox_width

                #print(x_ufm_dropoff, index)
                if (index <= x_ufm_dropoff[0] or index >= x_ufm_dropoff[1]):
                    ufm_intensity.append(1.0)
                    ev_intensity.append(0.0)

                else:
                    ufm_int = aufm*(index-x_biasedcenter)**2+kufm
                    ufm_intensity.append(max(0,min(1,ufm_int)))

                    ev_int = aev*(index-x_biasedcenter)**2+kev
                    ev_intensity.append(max(0,min(1,ev_int)))

            #print (ufm_intensity)

        elif texture == "Sinusoidal":
            periods = 5

            """Set haptic intensity = 0 over textbox"""
            ufm_intensity = [0]*int(self.textbox_width)
            ev_intensity = [0]*int(self.textbox_width)

            for index in range(int(self.haptic_width)):
                sinusoid = np.sin(index/self.haptic_width*periods*2*np.pi)
                ufm_intensity.append(max(0,sinusoid))
                ev_intensity.append(max(0,-sinusoid))

        elif texture == "Triangular":
            periods = 5
            triangle_halfwidth = self.haptic_width/(2.0*2*periods)


            """Set haptic intensity = 0 over textbox"""
            ufm_intensity = [0]*int(self.textbox_width)
            ev_intensity = [0]*int(self.textbox_width)
            intensity = []
            triangle_shape = []

            for i in range(int(triangle_halfwidth)):
                intensity = i/triangle_halfwidth
                triangle_shape.append(intensity)
                ufm_intensity.append(intensity)
                ev_intensity.append(0.0)

            for intensity in reversed(triangle_shape):
                triangle_shape.append(intensity)
                ufm_intensity.append(intensity)
                ev_intensity.append(0.0)

            for intensity in triangle_shape:
                ev_intensity.append(intensity)
                ufm_intensity.append(0.0)

            if periods > 1:
                for i in range(2,periods+1):
                    for intensity in triangle_shape:
                        ufm_intensity.append(intensity)
                        ev_intensity.append(0.0)

                    for intensity in triangle_shape:
                        ufm_intensity.append(0.0)
                        ev_intensity.append(intensity)

        elif texture == "Square":
            periods = 5

            """Set haptic intensity = 0 over textbox"""
            ufm_intensity = [0]*int(self.textbox_width)
            ev_intensity = [0]*int(self.textbox_width)

            for index in range(int(self.haptic_width)):
                sinusoid = np.sin(index/self.haptic_width*periods*2*np.pi)
                if (sinusoid > 0):
                    ufm_intensity.append(1.0)
                    ev_intensity.append(0.0)
                else:
                    ufm_intensity.append(0.0)
                    ev_intensity.append(1.0)


# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = Frame()
    frame.Show()
    app.MainLoop()
