# A while loop repeats a block of code as long as a condition is True.

# 1) Similarities and differences between for and while loops:
# - Both repeat code multiple times
# - Both can use break and continue
# - For loop iterates over a sequence or range (fixed number of times)
# - While loop repeats based on a condition (may not know in advance how many times)

i = 0
while i <= 20:
    print(i)
    i += 1

i = 0
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1

i = 10
while i <= 50:
    if i % 5 != 0:
        print(i)
    i += 1

i = 70
while i >= 25:
    print(i)
    i -= 1
