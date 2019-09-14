import wx, time, os, shutil, json
import threading
from datetime import datetime
from os.path import expanduser as eu
from os.path import expanduser, join
import sqlite3
from contextlib import closing
import tempfile
from glob import glob

import nicovideo

class App(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500, 700), style=wx.DEFAULT_FRAME_STYLE)
        p = wx.Panel(self, wx.ID_ANY)
        layout = wx.BoxSizer(wx.VERTICAL)
        
        self.button1 = wx.Button(p, wx.ID_ANY, 'チェック')
        self.button1.Bind(wx.EVT_BUTTON, self.btn1push)
        layout.Add(self.button1, flag=wx.EXPAND | wx.ALL, border=15)
        
        self.text_entry = wx.TextCtrl(p, wx.ID_ANY, size=(400, 200), style=wx.TE_MULTILINE)
        layout.Add(self.text_entry, flag=wx.EXPAND | wx.ALL, border=10)
        self.text2 = wx.TextCtrl(p, wx.ID_ANY, size=(400, 100), style=wx.TE_MULTILINE)
        layout.Add(self.text2, flag=wx.EXPAND | wx.ALL, border=10)
        
        p.SetSizer(layout)
        icon=wx.Icon() #EmptyIcon()
        #icon_source=wx.Image('ignore/icon.jpg',wx.BITMAP_TYPE_JPEG)
        #icon.CopyFromBitmap(icon_source.ConvertToBitmap())
        self.SetIcon(icon)
        #self.taskbar = wx.adv.TaskBarIcon()
        #self.taskbar.SetIcon(icon, '')
        self.Show()
        
    def btn1push(self, event):
        v = ''
        for row in nicovideo.search_nicovideo():
            v += ''.join([str(x) for x in row]) + "\n"
        self.text_entry.SetValue(v)


app = wx.App()
App(None, -1, '')
app.MainLoop()