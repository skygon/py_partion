#coding=utf-8

import wx

class NewProject(wx.Frame):
    def __init__(self, callback):
        wx.Frame.__init__(self,None,-1,"Create new project",
                         size=(400, 180))

        self.path = None
        self.create = False
        self.callback = callback

        # frame layout
        self.panel = wx.Panel(self,-1)
        
        # project name
        self.prj_name_label = wx.StaticText(self.panel,-1,"Project Name:")
        self.prj_name_text = wx.TextCtrl(self.panel,-1,"Entry project name", size=(175,-1))
        #设置默认的插入点，整数索引，开始位置为0
        self.prj_name_text.SetInsertionPoint(0)
        
        # partion number
        self.partion_num_label = wx.StaticText(self.panel,-1,"Partion Number:")
        self.partion_num_text = wx.TextCtrl(self.panel,-1,'2',size=(175,-1))

        # project save path
        self.path_label = wx.StaticText(self.panel, -1, "Project Directory:")
        self.path_button = wx.Button(self.panel, label = 'browse', pos = (200, 60), size = (60, 20))  

        # 用sizer控制界面布局
        self.sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
        self.sizer.AddMany([self.prj_name_label, self.prj_name_text, self.partion_num_label, self.partion_num_text, self.path_label, self.path_button])
        self.panel.SetSizer(self.sizer)

        # 在Panel上添加Button  
        self.ok_button = wx.Button(self.panel, label = 'OK', pos = (240, 100), size = (60, 20))
        self.cancel_button = wx.Button(self.panel, label = 'Cancel', pos = (320, 100), size = (60, 20))
        
        # 绑定单击事件  
        self.Bind(wx.EVT_BUTTON, self.onBrowse, self.path_button)
        self.Bind(wx.EVT_BUTTON, self.onOk, self.ok_button)
        self.Bind(wx.EVT_BUTTON, self.onCancel, self.cancel_button)
          
    def onBrowse(self, evt):
        dlg = wx.DirDialog(self, "Select an folder to save project", style=wx.DD_DEFAULT_STYLE)  
        if dlg.ShowModal() == wx.ID_OK:
            self.path = dlg.GetPath()
            self.create = True
            print "create is True"

        dlg.Destroy()
    
    def onOk(self, evt):
        print "Click OK, start to create new project"
        self.prj_name = self.prj_name_text.GetValue()
        self.partion_num = self.partion_num_text.GetValue()
        print "configure information:"
        print "prj_name: %s" %(self.prj_name)
        print "partion number: %s" %(self.partion_num)
        print "project path: %s" %(self.path)
        self.Show(False)
        self.callback(self)
        #self.Close(True)

    def onCancel(self, evt): 
        self.create = False 
        self.Close(True)


if __name__ == "__main__":
    app = wx.App(False)
    frame = NewProject()
    frame.Show(True)
    app.MainLoop() #listen on event