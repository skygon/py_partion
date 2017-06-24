#coding=utf-8

import wx

class NewProject(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Example For TextCtrl",
                         size=(400, 150))
        panel=wx.Panel(self,-1)
        
        #添加用户名 文本输入框
        userLabel=wx.StaticText(panel,-1,"User Name:")
        userText=wx.TextCtrl(panel,-1,"Entry your name",
                             size=(175,-1))
        #设置默认的插入点，整数索引，开始位置为0
        userText.SetInsertionPoint(0)
        
        #添加密码 输入框
        passwdLabel=wx.StaticText(panel,-1,"Password:")
        passwdText=wx.TextCtrl(panel,-1,'',size=(175,-1),
                               style=wx.TE_PASSWORD)
        #用sizer控制界面布局
        sizer=wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
        sizer.AddMany([userLabel,userText,passwdLabel,passwdText])
        panel.SetSizer(sizer)

         #在Panel上添加Button  
        button = wx.Button(panel, label = 'close', pos = (200, 60), size = (60, 20))  
          
        #绑定单击事件  
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)  
          
    def OnCloseMe(self, event):  
        self.Close(True)  


if __name__ == "__main__":
    app = wx.App(False)
    frame = NewProject()
    frame.Show(True)
    app.MainLoop() #listen on event