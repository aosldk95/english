#1부터 5까지의 숫자를 영어로 쓰면 one, two, three, four, five 이고,
#각 단어의 길이를 더하면 3 + 3 + 5 + 4 + 4 = 19 이므로 사용된 글자는 모두 19개입니다.
#1부터 1,000까지 영어로 썼을 때는 모두 몇 개의 글자를 사용해야 할까요?

#참고: 빈 칸이나 하이픈('-')은 셈에서 제외하며, 단어 사이의 and 는 셈에 넣습니다.
#  예를 들어 342를 영어로 쓰면 three hundred and forty-two 가 되어서 23 글자,
#  115 = one hundred and fifteen 의 경우에는 20 글자가 됩니다.
numberone=["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
           "ten", "eleven", "twelve" ]
numberten = ["", "", "twen", "thir", "for", "fif", "six", "seven", "eigh", "nine"]
numberdigit = ["teen", "ty", "hundred", "and", "thousand"]
number = 55
numberlist = []
txtlist = []
for i in range(1,number + 1) :
    txt = repr(i)
    line = []
    if len(txt) == 1 :       
        line.append(numberone[i])
    elif len(txt) == 2 :
        if i < 13 :
           txtlist.append(numberone[i])
        elif 12 < i < 20 :
           line.append(numberten[int(txt[1])])
           line.append(numberdigit[0])
        else :
           line.append(numberten[int(txt[0])])
           line.append(numberdigit[1])
           line.append(numberone[int(txt[1])])
    txtlist.append(line)
print(txtlist)
    
           
           
    
