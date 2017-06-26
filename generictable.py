import wx

########################################################################
class ChartPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

########################################################################
class MainPanel(wx.Panel):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)
        chart = ChartPanel(self)
        chart.SetBackgroundColour("blue")

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer = wx.BoxSizer(wx.HORIZONTAL)
        # change to VERTICAL if the buttons need to be stacked
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        for i in range(3):
            btn = wx.Button(self, label="Button #%s" % (i+1))
            btnSizer.Add(btn, 0, wx.ALL, 5)

        # put the buttons next to the Panel on the top
        topSizer.Add(btnSizer, 0, wx.ALL, 5)
        topSizer.Add(chart, 1, wx.EXPAND)

        mainSizer.Add(topSizer, 1, wx.EXPAND)
        mainSizer.AddSpacer(150)
        self.SetSizer(mainSizer)

########################################################################
class MainFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="BoxSizer Example")
        panel = MainPanel(self)
        self.Show()

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()