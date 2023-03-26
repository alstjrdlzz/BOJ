while True:
    data = input()
    if data == '0':
        break
    else:
        q, r = divmod(len(data), 2)
        if r == 0:
            if data[:q] == data[q:][::-1]:
                print('yes')
            else:
                print('no')
            
        else:
            if data[:q] == data[q+1:][::-1]:
                print('yes')
            else:
                print('no')