name = ['Denver','Rio','manika']
for x in name:
    print(x)

# or
name = ['Denver','Rio','manika']
for item in name:
    print(item)

#break
name = ['Denver','Rio','manika']
for item in name:
    if item == 'Rio':
        break
    print(item)

#continue
name = ['Denver','Rio','manika']
for item in name:
    if item == 'Rio':
        continue
    print(item)

#range()
for item in range(1,30,2):
    print(item)

#nestedforloop
name = ['Denver','Rio']
name1 = ['manika']
for x in name:
    for y in name1:
        print(x,y)