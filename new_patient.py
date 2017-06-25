#coding=utf-8

import wx

class NewPatient(wx.Frame):
    def __init__(self, callback):
        wx.Frame.__init__(self,None,-1,"Add new patient",
                         size=(400, 180))
        self.callback = callback
        self.create = False

        # frame layout
        self.panel = wx.Panel(self,-1)
        
        #  name
        self.patient_name_label = wx.StaticText(self.panel,-1,"Patient Name:")
        self.patient_name_text = wx.TextCtrl(self.panel,-1,"Entry patient name", size=(175,-1))
        #设置默认的插入点，整数索引，开始位置为0
        self.patient_name_text.SetInsertionPoint(0)

        # gender
        self.patient_gender_label = wx.StaticText(self.panel,-1,"Gender:")
        self.patient_gender_text = wx.TextCtrl(self.panel,-1,"", size=(175,-1))

        # 用sizer控制界面布局
        self.sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
        self.sizer.AddMany([self.patient_name_label, self.patient_name_text, self.patient_gender_label, self.patient_gender_text])
        self.panel.SetSizer(self.sizer)

        # 在Panel上添加Button  
        self.ok_button = wx.Button(self.panel, label = 'OK', pos = (240, 100), size = (60, 20))
        self.cancel_button = wx.Button(self.panel, label = 'Cancel', pos = (320, 100), size = (60, 20))
        
        # 绑定单击事件  
        self.Bind(wx.EVT_BUTTON, self.onOk, self.ok_button)
        self.Bind(wx.EVT_BUTTON, self.onCancel, self.cancel_button)
    
    def onOk(self, evt):
        print "Click OK, start to add new patient"
        self.patient_name = self.patient_name_text.GetValue()
        self.patient_gender = self.patient_gender_text.GetValue()
        print "patient information:"
        print "patient_name: %s" %(self.patient_name)
        print "partion gender: %s" %(self.patient_gender)
        self.Show(False)
        self.create = True
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