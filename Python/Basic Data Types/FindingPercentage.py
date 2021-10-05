n = int(input())
dictionary = {}
for i in range(0, n):
    Arr = input().split()
    marks = list(map(float, Arr[1:]))
    dictionary[Arr[0]] = sum(marks)/float(len(marks))
print("%.2f" % dictionary[input()])
