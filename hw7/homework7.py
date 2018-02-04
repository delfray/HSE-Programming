def read(filename):
# эта функция считывает текст из файла
    w = open(filename, 'r', encoding='utf-8')
    text = w.read()
    w.close()
    return text

def del_punctuation(text):
# эта функция удаляет все знаки препинания и пробельные символы из текста
    text = text.replace(' ', '.')
    text = text.replace('\n', '.')
    text = text.replace('\t', '.')
    text = text.replace(',', '.')
    text = text.replace('!', '.')
    text = text.replace('?', '.')
    text = text.replace(':', '.')
    text = text.replace('-', '.')
    text = text.replace(';', '.')
    text = text.replace('(', '.')
    text = text.replace(')', '.')
    text = text.replace('&', '.')
    text = text.replace('\'', '.')
    text = text.replace('—', '.')
    text = text.replace('*', '.')
    text = text.replace('“', '.')
    text = text.replace('”', '.')
    text = text.replace('\"', '.')
    text = text.split('.')
    return text

def proverka_ing(word):
# эта функция проверяет, заканчивается ли слово на -ing
    return word.endswith('ing')

def dob_v_slovar(word, freq):
# эта функция добавляет слово в словарь, если его не было там до этого, в ином случае увеличивает число раз, которое встретилось слово в тексте
    if word in freq:  
        freq[word] += 1
    else:
        freq[word] = 1

def slovar(text):
# эта функция создаёт словарь и наполняет его
    freq = {}
    for word in text:
        if proverka_ing(word):
            dob_v_slovar(word, freq)
    return freq

def main():
# эта функция главная
    filename = input('Введите имя файла ')
    text = read(filename)
    text = del_punctuation(text)
    freq = slovar(text)
    word = input('Введите форму на -ing ')
    print('В тексте', len(freq), 'форм на -ing.')
    if word in freq:
        print('В тексте слово', word, 'встречается', freq[word], 'раз.')
    else:
        print('В тексте слово', word, 'ни разу не встречается.')

if __name__ == '__main__':
    main()

