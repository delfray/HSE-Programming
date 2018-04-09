def read(filename):
# эта функция считывает текст из файла
    w = open(filename, 'r', encoding='utf-8')
    text = w.readlines()
    w.close()
    return text

def main():
    # это главная функция
    text = read('Korpus.xml')
    a = len(text)
    w = open('number_lines.txt', 'a', encoding='utf-8')
    w.write(str(a))
    

if __name__ == '__main__':
    main()
    
    
    
    

