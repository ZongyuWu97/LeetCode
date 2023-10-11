def printLeetCodeFormat(name):
    name_in_web = name.split(' ')[1:]
    for i in range(len(name_in_web)):
        if name_in_web[i] == '-':
            name_in_web = name_in_web[:i] + name_in_web[i + 1:]
            break
    name_in_web = '-'.join(name_in_web)
    name_in_web = name_in_web.lower()

    name_part = '#### [' + name + ']'
    web_part = '(https://leetcode.com/problems/' + \
        name_in_web + '/description/), [Solution]()\n'

    print()
    print('_'.join(name.split(' ')[1:]) + '.py')
    print(name_part + web_part)


def main():
    name = '772. Basic Calculator III'
    printLeetCodeFormat(name)

if __name__ == '__main__':
    main()