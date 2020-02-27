# Практика
# Головоломка

print('Головоломка')
print('Возможная последовательность ходов:                               Пример правильного ввода:')
print('A - использовать символ, находящийся над пустым квадратом         ABCDE')
print('B - использовать символ, находящийся под пустым квадратом         FG IJ')
print('L - использовать символ, находящийся слева от пустого квадрата    KLMNO')
print('R - использовать символ, находящийся справа от пустого квадрата   PQRST')
print('                                                                  UVWXY')
print('                                                                  ABLR0   - последовательность действий')
print('                                                                  Z')
print('Пожалуйста, вводите в каждой головоломке только заглавные латинские буквы (по 5 в каждой строке)')
print('Каждая последовательность действий заканчивается на "0"')
print('Конец ввода заканчивается на "Z"')
print('Ввод:')
Flag=False
def commandA():
    global q
    global indi
    global indj
    m=puzzle[q][indi-1][indj]
    puzzle[q][indi]=puzzle[q][indi].replace(puzzle[q][indi][indj],',')
    puzzle[q][indi-1]=puzzle[q][indi-1].replace(puzzle[q][indi-1][indj],' ')
    puzzle[q][indi]=puzzle[q][indi].replace(puzzle[q][indi][indj],m)
    indi -= 1

def commandB():
    global q
    global indi
    global indj
    m=puzzle[q][indi+1][indj]
    puzzle[q][indi]=puzzle[q][indi].replace(puzzle[q][indi][indj],',')
    puzzle[q][indi+1]=puzzle[q][indi+1].replace(puzzle[q][indi+1][indj],' ')
    puzzle[q][indi]=puzzle[q][indi].replace(puzzle[q][indi][indj],m)           
    indi += 1

def commandL():
    global q
    global indi
    global indj
    m=puzzle[q][indi][indj-1]
    puzzle[q][indi]=puzzle[q][indi].replace(puzzle[q][indi][indj],',')
    puzzle[q][indi]=puzzle[q][indi].replace(puzzle[q][indi][indj-1],' ')
    puzzle[q][indi]=puzzle[q][indi].replace(puzzle[q][indi][indj],m)
    indj -= 1

def commandR():
    global q
    global indi
    global indj
    m=puzzle[q][indi][indj+1]
    puzzle[q][indi]=puzzle[q][indi].replace(puzzle[q][indi][indj],',')
    puzzle[q][indi]=puzzle[q][indi].replace(puzzle[q][indi][indj+1],' ')
    puzzle[q][indi]=puzzle[q][indi].replace(puzzle[q][indi][indj],m)              
    indj += 1

a=[]

n=0
while n != 'Z':
    n=input('')
    a.append(n)
a.pop()

puzzle = [a[x:6+x] for x in range(0,len(a),6)]

for q in range(len(puzzle)):
    for i in range(len(puzzle[q])):
        for j in range(len(puzzle[q][i])):
            if puzzle[q][i][j]==' ':
                indi=i
                indj=j

    for k in range(len(puzzle[q][5])):
        if puzzle[q][5][k]=='A':
            if indi-1<0:
                print('Головоломка №', q+1)
                print('Головоломка не имеет решений')
                Flag=True
                break
            else:
                commandA()
        elif puzzle[q][5][k]=='B':
            if indi+1>4:
                print('Головоломка №', q+1)
                print('Головоломка не имеет решений')
                Flag=True
                break
            else:
                commandB()
                
        elif puzzle[q][5][k]=='L':
            if indj-1<0:
                print('Головоломка №', q+1)
                print('Головоломка не имеет решений')
                Flag=True
                break
            else:
                commandL()
            
        elif puzzle[q][5][k]=='R':
            if indj+1>4:
                print('Головоломка №', q+1)
                print('Головоломка не имеет решений')
                Flag=True
                break
            else:
                commandR()
        elif puzzle[q][5][k]=='0':
            break
        else:
            print('Данные введены неверно')
       

    if Flag != True:
        print('Головоломка №', q+1)
        for i in range(len(puzzle[q])-1):
            for j in range(len(puzzle[q][i])):
                print(puzzle[q][i][j], end=' ')
            print()  
        print()
   

