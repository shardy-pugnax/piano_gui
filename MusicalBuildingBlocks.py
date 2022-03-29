"""
MusicalBuildingBlocks.py
Sam Hardy

Class module for creating musical objects.  To be imported and used by other programs.

Ver 0.1 on 1/30/20, Kickoff.

"""

class Note():
    """
    Note objects will just have a pitch (in Hz).
    """

    def __init__(self, name, pitch):
        self.name = name
        self.pitch = pitch

    def __str__(self):
        return "I'm a note ({}), pitch = {}".format(self.name, self.pitch)

class PianoKey():
    """
    Piano Key objects will have a name (alias, aka a number 1-88 starting from the left), and a color (white or black), and a size (the white keys are bigger than the black ones, and a location on the keyboard, relative to middle C)
    """

    def __init__(self, number = 0, color = None, size = None, location = None):
        self.number = number
        self.color = color
        self.size = size
        self.location = location

    def __str__(self):
        return "I'm a piano key, number = {}, color = {}, size = {}, location = {}".format(self.number, self.color, self.size, self.location)

    def press(self):
        import PlaySound
        import NoteLookup
        physical_key = self.number
        assoc_note = NoteLookup.piano_key_table[physical_key]
        freq = NoteLookup.note_table[assoc_note]
        PlaySound.playsound(freq)