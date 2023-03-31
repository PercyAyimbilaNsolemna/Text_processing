from TextProcessing import TextProcessing 

def main():
    textProcessing = TextProcessing()
    print(textProcessing)

    textProcessing.text = "I am Percy. Here comes Percy"
    print(f"Text: {textProcessing.text}")

    print(textProcessing.count_words())

    print(textProcessing.count_characters())

    print(textProcessing.replace("Percy", "Agnes"))

    textProcessing.text = "Dennis has written codes. The codes are working properly"
    print(textProcessing.replace_all("codes", "lines of code"))

    print(textProcessing.search("codes"))

    print(textProcessing.search("lines"))

if __name__ == "__main__":
    main()