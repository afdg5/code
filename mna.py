# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul  2 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frameMain
###########################################################################

class frameMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Main", pos = wx.DefaultPosition, size = wx.Size( 1031,646 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizerFrameMain = wx.BoxSizer( wx.VERTICAL )
		
		bSizerMainFrame = wx.BoxSizer( wx.VERTICAL )
		
		self.userBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMainFrame.Add( self.userBox, 0, wx.ALIGN_TOP|wx.EXPAND, 0 )
		
		self.nameButton = wx.Button( self, wx.ID_ANY, u"Submit Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMainFrame.Add( self.nameButton, 0, wx.ALL, 5 )
		
		self.startButton = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMainFrame.Add( self.startButton, 0, 0, 0 )
		
		self.testButton = wx.Button( self, wx.ID_ANY, u"Test", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerMainFrame.Add( self.testButton, 0, wx.ALL, 5 )
		
		
		bSizerFrameMain.Add( bSizerMainFrame, 1, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizerFrameMain )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.nameButton.Bind( wx.EVT_BUTTON, self.nameSub )
		self.startButton.Bind( wx.EVT_BUTTON, self.onStart )
		self.testButton.Bind( wx.EVT_BUTTON, self.onTest )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def nameSub( self, event ):
		event.Skip()
	
	def onStart( self, event ):
		event.Skip()
	
	def onTest( self, event ):
		event.Skip()
	

