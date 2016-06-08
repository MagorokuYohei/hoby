#-*-coding:utf-8-*-

def f_numm(num,card,digit, target, sa, check, ans):
    if digit >0:
        for i in range(0, len(card)):
            if card[i] == 0:
                continue
            numr = num + int(card[i]) * digit
            sa_ = abs(target- (numr + digit-1))
            if sa_ <= sa:
                ppp = i/2
                ppp *= 2
                check.append(ppp)
                ppp += 1
                check.append(ppp)
                numm(numr, card, (digit/10), target, sa, check, ans)
                check.pop()
                check.pop()
    if digit == 0:
        ans.append(num)

def numm(num,card,digit, target, sa, check, ans):
    if digit >0:
        for i in range(0, len(card)):

            if i in check:
                continue
            numr = num + int(card[i]) * digit
            sa_ = abs(target- (numr + digit-1))
            if digit == 1:
                sa_ -=1
            if sa_ <= sa:
                ppp = i/2
                ppp *= 2
                check.append(ppp)
                ppp += 1
                check.append(ppp)
                numm(numr, card, (digit/10), target, sa, check, ans)
                check.pop()
                check.pop()
    if digit == 0:
        ans.append(num)

def make_ans(target, ans):
    maji_ans = []
    sa = 100000000
    for i in range(0, len(ans)):
        sa_= abs(ans[i] - target)
        if sa > sa_:
            sa = sa_

    for i in range(0, len(ans)):
        if sa == abs(ans[i] - target):
            maji_ans.append(i)

    return maji_ans

def bunkai(card_, card):
    omote = card_/10
    ura   = card_ - (omote*10)
    card.append(omote)
    card.append(ura)

def main():
    word = raw_input()
    word = word.split(',')
    card_ = word[2].split('/')
    card  = []

    for i in range(0, len(card_)):
        bunkai(int(card_[i]), card)

    digit  = 10**(int(word[0])-1)
    mago   = int(word[1])
    digitn = digit
    target = []
    check  = []
    ans    = []

    while digit >0:
        magorn =  mago /digit
        target.append(magorn)
        mago  -= digit*magorn
        digit /=10
    sa = 1000000000

    if word[0] == '1':
        numm(0,card,digitn, int(word[1]), sa, check, ans)
    else:
        f_numm(0,card,digitn, int(word[1]), sa, check, ans)

    if len(ans) == 0:
        print '-'
        return 0

    gans = ans
    maji_ans = make_ans(int(word[1]), ans)
    beko_ans = []
    for i in range(0, len(maji_ans)):
        beko_ans.append(str(gans[maji_ans[i]]))
    beko_ans = list(set(beko_ans))
    beko_ans.sort()

    strn = ''
    for i in range(0, len(beko_ans)):
        strn += beko_ans[i] + ','
    strn = strn.rstrip(',')
    print strn

if __name__=='__main__':
    main()
