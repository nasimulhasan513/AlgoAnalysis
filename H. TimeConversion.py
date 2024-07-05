time = input()

t = time.split(':')

a = t[2][2:]

if a == 'PM':
    hr = t[0]
    if hr != '12':
        t[0] = str(int(t[0]) + 12)
    t[2] = t[2][:2]
    print(':'.join(t))
    
else:
    if t[0] == '12':
        t[0] = '00'
    t[2] = t[2][:2]
    print(':'.join(t))
    