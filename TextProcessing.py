import re 

class TextProcessing:
    def __init__(self, text=None):
        self.text = text

    def __str__(self):
        return "This is a text processing class"
    
    #Creates a method that counts the number of words in the text
    def count_words(self):
        self.matches = re.findall(r"[a-z0-9]+", self.text, re.IGNORECASE)
        self.number_of_words = len(self.matches)
        return f"The text has {self.number_of_words} words"
    
    #Creates a method that counts the number of characters in the text
    def count_characters(self):
        self.number_of_characters = 0
        for word in self.matches:
            self.number_of_characters = self.number_of_characters + len(word)
        return f"The text has {self.number_of_characters} characters"
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

    print(textProcessing.count_words())

    print(textProcessing.count_characters())

if __name__ == "__main__":
    main()