with open("freq.txt", encoding="utf-8") as f:
    for line in f:
        words = line.split('|')
        if words[1].find('гл') != -1 and words[1].find('перех') != -1:
            print(line)
