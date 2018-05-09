from zelva import Zelva

class ZelvaJaka(Zelva):
    """
    Želva rdeče barve.
    """

    def __init__(self, ime='Želva Jaka'):
        """
        Konstruira Jaka želvo.
        """
        Zelva.__init__(self, ime=ime, barva='pink', hitrost=4)
        self.shape('turtle')
