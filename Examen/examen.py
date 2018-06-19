import re
import os

def create(filename):
    #эта функция создает для нас таблицу
    f = open(filename, 'w', encoding='utf-8')
    table = f.write("doc_id;title;author;created;topic;tagging")
    f.close()
    return table


def read(filename):
    # эта функция считывает текст из файла
    w = open(filename, 'r', encoding='utf-8')
    text = w.read()
    w.close()
    return text


def spisok_failov():
    list_files = os.listdir('news')
    return list_files


def main():
    # это главная функция
    table = create('examen.csv')
    list_files = spisok_failov()
    for filename in list_files:
        filename = 'news\\' + filename
        text = read(filename)
        match = re.search(r'<meta content=".*" name="docid"/>', text)
        match1 = re.search(r'<meta content=".*" name="author"/>', text)
        match2 = re.search(r'<meta content=".*" name="created"/>', text)
        match3 = re.search(r'<meta content=".*" name="topic"/>', text)
        match4 = re.search(r'<meta content=".*" name="tagging"/>', text)
        match5 = re.search(r'<title>.*</title>', text)
        if match:
            table = open('examen.csv', 'a', encoding='utf-8')
            table.write(match.group())
        else:
            table.write('-')
        if match1:
            table = open('examen.csv', 'a', encoding='utf-8')
            table.write(match.group())
        else:
            table.write('-')
        if match2:
            table = open('examen.csv', 'a', encoding='utf-8')
            table.write(match.group())
        else:
            table.write('-')
        if match3:
            table = open('examen.csv', 'a', encoding='utf-8')
            table.write(match.group())
        else:
            table.write('-')
        if match4:
            table = open('examen.csv', 'a', encoding='utf-8')
            table.write(match.group())
        else:
            table.write('-')
        if match5:
            table = open('examen.csv', 'a', encoding='utf-8')
            table.write(match.group())
        else:
            table.write('-')
        

if __name__ == '__main__':
    main()
