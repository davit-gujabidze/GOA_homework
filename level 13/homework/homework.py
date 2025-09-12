# A while loop repeats code as long as a condition is True; it stops when the condition becomes False.

i = 0
while i <= 4:
    print(i)
    i += 1

counter = 0
while counter < 3:
    print("Hello")
    counter += 1

num = 1
while num <= 5:
    if num == 3:
        print("Decent")
    num += 1

num = 1
while num <= 5:
    if num > 2:
        print(num)
    num += 1

counter = 0
while True:
    print("Counter is:", counter)
    if counter == 4:
        break
    counter += 1
