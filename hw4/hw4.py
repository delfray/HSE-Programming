w = 0
l = 0
with open("text.txt", encoding="utf-8") as f:
    for line in f:
        l += 1
        words = line.split()
        for st in words:
            if st.isalpha():
                w += 1
if l == 0:
    print('Не было строк')
else:
    print(w / l)
        
