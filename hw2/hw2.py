a = input("Vvedite slovo: ")

for i in range(1, len(a), 2):
    if(a[i] != 'а' and a[i] != 'к'):
        print(a[i], end='')
