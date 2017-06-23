#coding=utf-8
import wx
  
class MainWindow(wx.Frame):
    '''define an window class'''
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

        # Binding events
        # File
        self.Bind(wx.EVT_MENU, self.onAbout, menu_about)
        self.Bind(wx.EVT_MENU, self.onExit, menu_exit)
        
        # Project
        self.Bind(wx.EVT_MENU, self.onNew, menu_new)
        self.Bind(wx.EVT_MENU, self.onOpen, menu_open)
        self.SetMenuBar(menu_bar)
    
    def onAbout(self, evt):
        '''click about event handler'''
        dlg = wx.MessageDialog(self, 'This app is a simple text editor', 'About my app', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    
    def onExit(self, evt):
        '''click to exit'''
        self.Close(True)
    
    def onNew(self, evt):
        dlg = wx.DirDialog(self, "Select a floder to save project", style=wx.DD_DEFAULT_STYLE)
        prj_path = ""
        if dlg.ShowModal() == wx.ID_OK:
            prj_path = dlg.GetPath()
            print "project path is %s" %(prj_path)
        else:
            print "Incorrect path"
    
    def onOpen(self, evt):
        '''select project and open'''
        dlg = wx.DirDialog(self, "Select an exist project", style=wx.DD_DEFAULT_STYLE)  
        if dlg.ShowModal() == wx.ID_OK:  
            print dlg.GetPath()

        dlg.Destroy()


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow(None, 'Smart Partion')
    app.MainLoop() #listen on event