import re
import os

def read(filename):
# эта функция считывает текст из файла
    w = open(filename, 'r', encoding='utf-8')
    text = w.read()
    w.close()
    return text

def spisok_stran():
    list_files = os.listdir('Страны')
    return list_files
    
def main():
    # это главная функция
    list_files = spisok_stran()
    w = open('capitals.txt', 'w', encoding='utf-8')
    for filename in list_files:
        filename = 'Страны\\' + filename
        text = read(filename)
        match = re.search('Столица</a></b>\n</td>\n(.*?)title="(.*?)"', text)
        if match:
            w = open('capitals.txt', 'a', encoding='utf-8')
            w.write(match.group(2) + '\n')
        else:
            print('Nothing found')
            
if __name__ == '__main__':
    main()
