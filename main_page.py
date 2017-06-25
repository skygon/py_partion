#coding=utf-8
import wx
import time
from utils import *
from new_project import NewProject
from new_patient import NewPatient
  
class MainWindow(wx.Frame):
    '''define an window class'''
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        #self.SetMaxSize((800, 600))
        #self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.panel = wx.Panel(self,-1)
        #self.sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
        self.sizer = wx.GridBagSizer(5,5)
        self.panel.SetSizer(self.sizer)

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

    # event handlers
    def onAbout(self, evt):
        '''click about event handler'''
        dlg = wx.MessageDialog(self, 'This app is a simple text editor', 'About my app', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    
    def onExit(self, evt):
        '''click to exit'''
        self.Close(True)
    
    def onNew(self, evt):
        new_prj = NewProject(self.newPrjCallback)
        new_prj.Show(True)  
    
    def onOpen(self, evt):
        '''select project and open'''
        dlg = wx.DirDialog(self, "Select an exist project", style=wx.DD_DEFAULT_STYLE)  
        if dlg.ShowModal() == wx.ID_OK:  
            prj_path = dlg.GetPath()
            data = Utils.readConfigFile(prj_path)
            self.prjInit(data)
            self.loadExistData()

        dlg.Destroy()
    
    def onAdd(self, evt):
        add_frame = NewPatient(self.newPatientCallback)
        add_frame.Show(True)

    # ============================Logic functions============================
    # New project callback function
    def newPrjCallback(self, new_prj):
        print "In new project callback"
        data = {}
        if new_prj.create:
            data['prj_name'] = new_prj.prj_name
            data['partion_num'] = new_prj.partion_num
            data['prj_path'] = new_prj.path
            Utils.saveConfigFile(data, data['prj_path'])
        # close project frame
        new_prj.Close(True)

        # init new project
        self.prjInit(data)
    
    def prjInit(self, data):
        self.prj_name_label = wx.StaticText(self.panel, -1, "Project Name:")
        self.prj_name_text = wx.StaticText(self.panel, -1, data['prj_name'])
        # wx.TE_READONLY
        #self.prj_name_text = wx.TextCtrl(self.panel, -1, data['prj_name'], size=(175,-1), style=wx.TE_READONLY)

        self.add_button = wx.Button(self.panel, label = u'添加病人信息', size = (100, 20))  
        #self.sizer.AddMany([self.prj_name_label, self.prj_name_text, self.add_button])
        self.sizer.Add(self.prj_name_label, pos=(0,0))
        self.sizer.Add(self.prj_name_text, pos=(0,1))
        self.sizer.Add(self.add_button, pos=(1,1))

        # bind events
        self.Bind(wx.EVT_BUTTON, self.onAdd, self.add_button)
    
    # used in open an exist project
    def loadExistData(self):
        pass
    
    def newPatientCallback(self, new_pat):
        pat_name = new_pat.patient_name
        pat_gender = new_pat.patient_gender
        print "name %s, gender: %s" %(pat_name, pat_gender)
        new_pat.Close(True)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow(None, 'Smart Partion')
    app.MainLoop() #listen on event