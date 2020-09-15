#4-3
for i in range(1,21):
    print(i)

#4-4,4-5
count = 0
list = [i for i in range(1,1_000_001)]
for i in list:
    print(i)
    count += count+i
print(max(list))
print(min(list))
print(count)

#4-6
list = range(2,21,2)
for i in list :
    print(i)


#4-7,4-9
list = range(3,31,3)
for i in list :
    print(i)

#4-8
for i in (value**3 for value in range(1,11)) :
    print(i)

