import os

def main():
    src = '.'
    glubina = []
    for dir_name, dirs, files in os.walk(src):
        lol = dir_name.split("\\")
        a = len(lol[1:])
        glubina.append(a)
        for i, item in enumerate(glubina):
            glubina[i] = int(item)
        maximum = max(glubina)
    print(glubina[-1:])



if __name__ == '__main__':
    main()
