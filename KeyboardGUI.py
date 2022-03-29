"""
KeyboardGUI.py
Sam Hardy

GUI to mimic piano keyboard

Ver 0.1 on 1/30/20, Kickoff.

"""
import wx
import MusicalBuildingBlocks

FRAME_LENGTH = 1100
FRAME_WIDTH = 500


app = wx.App()
frame = wx.Frame(None, -1, 'PLAY ME SOME PIAN-E!!!')
#frame.ShowFullScreen()
frame.SetSize(0,0,FRAME_LENGTH,FRAME_WIDTH)
frame.SetBackgroundColour('yellow')


panel = wx.Panel(frame, wx.ID_ANY)


import NoteLookup as NL
for i in range(len(NL.note_table)):
    n = list(NL.note_table.keys())[i]
    if '♯' in n:
        clr = 'Black'
    else:
        clr = 'White'
    def key(event, i=i):
        k = MusicalBuildingBlocks.PianoKey(number = i+1)
        return k.press()

    KSF = 60
    if clr == 'Black':
        button = wx.Button(panel, wx.ID_ANY, list(NL.note_table.keys())[len(NL.note_table) - i-1], pos = (int(i*(FRAME_LENGTH/KSF)),0), size = (int(FRAME_LENGTH/KSF), int(0.5*FRAME_WIDTH/1.2)))
    else:
        button = wx.Button(panel, wx.ID_ANY, list(NL.note_table.keys())[len(NL.note_table) - i - 1], pos=(int(i * (FRAME_LENGTH / KSF)), 0), size=(int(FRAME_LENGTH / KSF), int(FRAME_WIDTH / 1.2)))

    button.Bind(wx.EVT_BUTTON, key)


frame.Show()
frame.Centre()
app.MainLoop()