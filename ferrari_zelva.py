from zelva import Zelva

class FerrariZelva(Zelva):
    """
    Želva rdeče barve s Ferrari motorjem.
    """

    def __init__(self, ime='Ferrari želva'):
        """
        Konstruira Ferrari želvo.
        """
        Zelva.__init__(self, ime=ime, barva='red', hitrost=5)
        self.shape('turtle')
