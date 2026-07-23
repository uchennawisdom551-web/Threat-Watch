def woo():
 with open("newfile.py",  'r' ) as file:
    events =[]
    print('=======Log-Analysis========')
    count = 0
    for substance in file:
        parts = substance.strip().split()
        part = {'Date': parts[0],
        'Time': parts[1], 'Ip' : parts[2], 'Status' :       parts[3]}
        events.append(part)
        print('-' * 35)
        count+=1
        print(f'Event-Number#{count}')
        print()
        print()
        for Key, value in part.items():
           print (f'{Key: <10}: {value}')
