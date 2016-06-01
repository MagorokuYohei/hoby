#-*-coding:utf-8-*-

def japa_check(string):
    try:
        for i in string:
            d = i.encode('shift_jis')
        return False
    except:
        return True


def main():
        last_word = ''
        word= raw_input(u'')
        word = word.split(',')
        japa_check(word[0])

        if japa_check(word[0]):
            w_nin = word[0]
            neko = []
            for i in range(0, len(word[0])/2):
                neko.append((w_nin[i*2]+w_nin[(i*2)+1]))
        else:
            neko = word[0]

        for i in range(0, len(neko)):
            last_word += neko[i]
            if i < len(neko)-1:
                for t in range(0, int(word[2])):
                    last_word += word[1]
        print last_word

if __name__=='__main__':
    main()
