#coding=utf-8
import wx
import wx.grid
import time
import random
from utils import *
from new_project import NewProject
from new_patient import NewPatient
  
class MainWindow(wx.Frame):
    '''define an window class'''
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        #self.SetMaxSize((800, 600))
        
        self.colLabels = ["Name", "Gender", "Group", "Address", "Phone", 'Create Time']
        self.panel = wx.Panel(self,-1)
        #self.panel = wx.ScrolledPanel(self)
        #self.sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
        #self.sizer = wx.GridBagSizer(5,5)
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        #self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        #self.grid_sizer = wx.BoxSizer(wx.VERTICAL)
        #self.panel.SetSizer(self.sizer)

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
        try:
            print "In new project callback"
            data = {}
            if new_prj.create:
                data['prj_name'] = new_prj.prj_name
                data['partion_num'] = new_prj.partion_num
                data['prj_path'] = new_prj.path
                Utils.saveConfigFile(data, data['prj_path'])
            # init new project
            self.prjInit(data)
        except Exception, e:
            print "New project callback error: %s" %(str(e))
        finally:
            # close project frame
            new_prj.Close(True)
    
    def prjInit(self, data):
        try:
            #self.sizer.Clear()
            #self.panel.ClearBackground()
            self.main_sizer.Add((-1, 25))
            self.sizer = wx.BoxSizer(wx.HORIZONTAL)
            
            self.path = data['prj_path']
            self.partion_num = int(data['partion_num'])
            self.prj_name_label = wx.StaticText(self.panel, -1, "Project Name:")
            self.prj_name_text = wx.StaticText(self.panel, -1, data['prj_name'])
            # wx.TE_READONLY
            #self.prj_name_text = wx.TextCtrl(self.panel, -1, data['prj_name'], size=(175,-1), style=wx.TE_READONLY)

            #self.add_button = wx.Button(self.panel, label = u'添加病人信息', size = (100, 20))  
            self.add_button = wx.Button(self.panel, label = u'添加病人信息', size = (100, 20))
            #self.sizer.AddMany([self.prj_name_label, self.prj_name_text, self.add_button])
            self.sizer.Add(self.prj_name_label)
            self.sizer.Add(self.prj_name_text)
            self.sizer.Add((-1, 25))
            #self.sizer.Add(self.add_button)
            self.main_sizer.Add(self.sizer, flag=wx.ALIGN_CENTER_HORIZONTAL ,border=10)
            self.main_sizer.Add(self.add_button, flag=wx.ALIGN_CENTER_HORIZONTAL)
            #self.main_sizer.Add(self.add_button)

            self.main_sizer.Add((-1, 25))
            # Init grid to show patients information
            self.grid_sizer = wx.BoxSizer(wx.HORIZONTAL)
            self.grid = wx.grid.Grid(self.panel)
            #self.grid.Scroll(0, 0) 
            self.grid.CreateGrid(10,6)
            self.grid_rows = 10 # initially we have 5 rows
            for i in range(len(self.colLabels)):
                self.grid.SetColLabelValue(i, self.colLabels[i])

            self.grid_sizer.Add(self.grid, proportion=1, flag=wx.ALIGN_CENTER, border=100)
            self.main_sizer.Add(self.grid_sizer, proportion=1, flag=wx.ALIGN_CENTRE, border=10)

            self.panel.SetSizer(self.main_sizer)
            # bind events
            self.Bind(wx.EVT_BUTTON, self.onAdd, self.add_button)
        except Exception, e:
            print "Init project failed: %s" %(str(e))
    
    # used in open an exist project
    def loadExistData(self):
        try:
            data_file = os.path.join(self.path, 'data.csv')
            f = open(data_file, 'r')
            line = f.readline().strip('\n')
            count = 0
            while line:
                if count >= self.grid_rows:
                    self.grid.AppendRows(10)
                    self.grid_rows += 10
                
                data = line.split(',')
                for i in range(len(self.colLabels)):
                    self.grid.SetCellValue(count, i, "%s" % (data[i]))
                line = f.readline()
                count += 1
            self.grid.AutoSize()

        except Exception, e:
            print "loadExistData failed: %s" %(str(e))
    
    def newPatientCallback(self, new_pat):
        try:
            pat_name = new_pat.patient_name
            pat_gender = new_pat.patient_gender
            pat_address = new_pat.patient_address
            pat_phone = new_pat.patient_phone
            print "name %s, gender: %s" %(type(pat_name), type(pat_gender))
            
            partion = random.randint(0, self.partion_num-1)
            time_str = time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))
            line = pat_name + "," + pat_gender + "," + str(partion) + "," + pat_address + "," + pat_phone + "," + time_str
            # line is unicode
            print "line is %s" %(line.encode('utf8'))
            Utils.appendToFile(self.path, line)
            self.loadExistData()

            # TODO refresh grid
        except Exception, e:
            print "Exception in newPatientCallback: %s" %(str(e))
        finally:
            new_pat.Close(True)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow(None, 'Smart Partion')
    app.MainLoop() #listen on event