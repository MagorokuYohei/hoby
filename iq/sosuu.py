#-*-coding:utf-8-*-

def main():
    try:
        while True:
            L = int(raw_input())

            if L <3:
                print 0
                continue
            if L < 5:
                print 1
                continue

            SL = L*[0]
            SL[0] = 1
            SL[1] = 1
            p = 2
            i=2
            while True:
                SL[i*p] = 1
                i += 1
                if i*p > L-1:
                    break
            p=3
            i=p
            while p*p < L:
                i = p
                while True:
                    SL[i*p] = 1
                    i += 2
                    if i*p > L-1:
                        break

                while True:
                    p = p+1
                    if SL[p]==0:
                        break

            num = 0
            for i in SL:
                if i==0:
                    num+=1
            print num

    except EOFError:
        pass

if __name__=='__main__':
    main()
