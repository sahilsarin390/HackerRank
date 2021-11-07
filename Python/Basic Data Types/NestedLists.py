if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    x = 9999
    for i in range(len(students)):
        if x > float(students[i][1]):
            x = float(students[i][1])
    y = 9999
    for i in range(len(students)):
        if float(students[i][1]) > float(x) and y > float(students[i][1]):
            y = float(students[i][1])
    second_list = []
    for i in range(len(students)):
        if float(students[i][1]) == float(y):
            second_list.append(students[i][0])
    second_list = sorted(second_list)

    for i in range(len(second_list)):
        print(second_list[i])
