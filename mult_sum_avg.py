sum = 0
for i in range(1000):
    if (i % 2 != 0):
        sum +=i
print sum


#sum list

a = [1, 2, 5, 10, 255, 3]
sum2 = 0
for i in a:
    sum2 += i
print sum2

avg = 0
for i in a:
    avg += i
avg = avg/len(a)

print avg
