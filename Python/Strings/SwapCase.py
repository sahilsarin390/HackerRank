def swap_case(s):
    result = ''
    for char in s:
        if (char.isupper() == True):
            result += (char.lower())
        elif (char.islower() == True):
            result += (char.upper())
        else:
            result += char

    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
