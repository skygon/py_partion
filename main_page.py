#coding=utf-8
import wx
  
class MainWindow(wx.Frame):
  '''定义一个窗口类'''
  def __init__(self, parent, title):
    wx.Frame.__init__(self, parent, title=title, size=(600, 400))
    self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
  
    self.setupMenuBar()
    self.Show(True)
  
  def setupMenuBar(self):
    self.CreateStatusBar()
  
    menu_bar = wx.MenuBar()

    # File
    menufile = wx.Menu()
    menu_about = menufile.Append(wx.ID_ABOUT, 'About', 'About this shit')
    menu_exit = menufile.Append(wx.ID_EXIT, 'Exit', 'End program')
    menu_bar.Append(menufile, 'File')

    # Project
    menufile = wx.Menu()
    menu_new = menufile.Append(wx.ID_NEW, 'New Project', 'Create a new project')
    menu_open = menufile.Append(wx.ID_OPEN, 'Open Project', 'Open an exist project')
    menu_bar.Append(menufile, 'Project')

    #事件绑定
    # File
    self.Bind(wx.EVT_MENU, self.onAbout, menu_about)
    self.Bind(wx.EVT_MENU, self.onExit, menu_exit)
      
    self.SetMenuBar(menu_bar)
  
  def onAbout(self, evt):
      '''点击about的事件响应'''
      dlg = wx.MessageDialog(self, 'This app is a simple text editor', 'About my app', wx.OK)
      dlg.ShowModal()
      dlg.Destroy()
  
  def onExit(self, evt):
      '''点击退出'''
      self.Close(True)


if __name__ == "__main__":
    app = wx.App(False)
    frame2 = MainWindow(None, 'Small Editor')
    app.MainLoop() #循环监听事件