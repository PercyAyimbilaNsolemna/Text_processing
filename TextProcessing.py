import re 

class TextProcessing:
    def __init__(self, text=None):
        self.text = text

    def __str__(self):
        return "This is a text processing class"
    
    #Creates a method that checks the number of characters in a text
    #def character_counter(self):
        #self.character_count = self.text.count(self.text)
        #return self.character_count

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text   

def main():
    textProcessing = TextProcessing()
    print(textProcessing)

    textProcessing.text = "I am Percy"
    print(f"Text: {textProcessing.text}")

    #print(f"Number of characters: {textProcessing.character_counter()}")

    text = "Percy"
    print(len(text))

if __name__ == "__main__":
    main()