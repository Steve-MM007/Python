import random
list = []
print("20 Random numbers between 1 and 100: ")
for i in range(20):
    x = random.randint(1, 100)
    print(x)
    list.append(x)
    list.sort()
print("Average of values:", (sum(list))/20)
print("largest value:", max(list))
print("Smallest value:", min(list))
print("Second largest value:", list[-2])
print("Second smallest value:", list[1])
even = []
for x in list:
    if ((x%2) == 0 ):
        even.append(x)
print("Number of even values:", len(even))
#alternative count for even numbers
    #count = 0
    #if list%2 == 0:
        #count = count + 1