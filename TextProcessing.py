

class TextProcessing:
    def __init__(self, text=None):
        self.text = text

    def __str__(self):
        return "This is a text processing class"

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text   
