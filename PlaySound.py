"""
PlaySound.py
Sam Hardy

Module that contains a function to play sounds of a given frequency

Ver 0.1 on 1/30/20, Kickoff.
"""

def playsound(note, duration = 500):
    #winsound sucks because can only play integer frequencies, so piano will be out of tune!
    import winsound
    return winsound.Beep(int(note), duration)