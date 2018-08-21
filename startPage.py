#! /usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jul  2 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import main
import csv
###########################################################################
## Class Frame
###########################################################################

class Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )



		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.HomeButton = wx.Button( self, wx.ID_ANY, u"Home", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		bSizer1.Add( self.HomeButton, 0, wx.ALIGN_RIGHT|wx.TOP, 0 )

		self.textB1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize)
		bSizer1.Add( self.textB1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 0 )

		self.textB2 = wx.TextCtrl(self,wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer1.Add(self.textB2,0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 0 )

		self.NameButton = wx.Button(self,wx.ID_ANY,u"Submit",wx.DefaultPosition,wx.DefaultSize,wx.NO_BORDER)
		bSizer1.Add(self.NameButton,0,wx.ALIGN_LEFT|wx.TOP,0)

		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.HomeButton.Bind( wx.EVT_BUTTON, self.onHomeButton )
		self.NameButton.Bind( wx.EVT_BUTTON, self.onName)

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onName( self, event ):
		f = frameMain(None)
		self.Close()
		f.Show()

	def onName(self,event):
		str1 = self.textB1.GetValue()
		str2 = self.textB2.GetValue()
		name = [str1,str2]
		file = open('output.csv','w')
		with file:
			writer = csv.writer(file)
			writer.writerows([name])
