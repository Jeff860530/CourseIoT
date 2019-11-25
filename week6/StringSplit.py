

if __name__ == '__main__':
    TimeStr2 = dt.now().strftime('%H:%M')
    TimeObj2 = dt.strptime(TimeStr2,'%H:%M')
    TimeList = str(TimeObj2).split(' ')
    print(TimeList[1][:5])
    
    Str1 = '14:59~15:20'
    StrList = Str1.split('~')
    print(type(StrList))
    print(StrList)
    print(StrList[0])
    print(StrList[1])
