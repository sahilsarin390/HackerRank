n = input()

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and n >= 2 and n <= 5:
    print("Not Weird")
elif n % 2 == 0 and n > 5 and n < 21:
    print("Weird")
else:
    print("Not Weird")
