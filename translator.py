from PyPDF2 import PdfFileReader
from googletrans import Translator

URL_COM = 'translate.googleapis.com'
# The Language you want you can change it here 
LANG = "hi"


def get_translated_page_content(reader, lang):
    num_pages = reader.numPages
    page_contents = []
    translator = Translator(service_urls=[URL_COM])
    for p in range(num_pages):
        page = reader.getPage(p)
        text = page.extractText()
        translation = translator.translate(text, dest=lang)
        result_text = translation.text.replace("\n", " ").replace("W", "")
        page_contents.append(result_text)
    return page_contents


def translate_word(path, lang):
    file = open(path, 'rb')
    reader = PdfFileReader(file)
    page_contents = get_translated_page_content(reader, lang)
    str = ""
    for i in page_contents:
        str += i
    str.encode("utf-8",'ignore')
    text_file = open("data.txt", "w",encoding='utf-8')
    text_file.write(str)
    text_file.close()

    print("File Created Succesfully")


if __name__ == '__main__':
    file_name = "example.pdf"
    translate_word(file_name, LANG)