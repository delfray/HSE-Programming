import re

def read(filename):
# эта функция считывает текст из файла
    w = open(filename, 'r', encoding='utf-8')
    text = w.read()
    w.close()
    return text

def main():
    # это главная функция
    filename = input('Введите имя файла: ')
    text = read(filename)
    match = re.findall(r'[оО]ткр[оы][вейлтю]*[шь|м|а|сь|ся|о|и|ший|шая|шое|шие|ши|ый]', text)
    if match:
        print(match)
    else:
        print("Zdes' nichego net")

if __name__ == '__main__':
    main()
