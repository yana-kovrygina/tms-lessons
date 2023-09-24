for i in range(0, 101):
    print (i)
    n = input('Should we break? ')
    if n == 'yes':
        break
    if n == 'no':
        continue
    else:
        print("Don't understand you")