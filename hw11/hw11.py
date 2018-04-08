import re

def read(filename):
# эта функция считывает текст из файла
    w = open(filename, 'r', encoding='utf-8')
    text = w.read()
    w.close()
    return text

def main():
    # это главная функция
    text = read('Комар обыкновенный — Википедия.html')
    result = re.sub(r'(^|[^а-яА-Я]|)комар(а|у|ом|е|ы|ов|ам|ами|ах)?([^а-яА-Я]|$)', r'\1cлон\2\3', text)
    result = re.sub(r'(^|[^а-яА-Я]|)Комар(а|у|ом|е|ы|ов|ам|ами|ах)?([^а-яА-Я]|$)', r'\1Слон\2\3', result)
    w = open('komaroslon.txt', 'a', encoding='utf-8')
    w.write(result)

               
if __name__ == '__main__':
    main()
