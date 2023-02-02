while True:   
    name,age,kg=input().split()
    if int(age) > 17 or int(kg) >= 80:
        print(name, 'Senior')
    elif 0 < int(age) <= 17 or 0 < int(kg) < 80:
        print(name, 'Junior')
    elif name=='#' and int(age)==0 and int(kg)==0:
        break