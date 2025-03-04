main_list = [1, 2, 3, 4, 5]
#v1
if not main_list:
    print([[], []])
elif len(main_list) == 1:
    print([[main_list[0]], []])
elif len(main_list) == 2:
    print([[main_list[0]], [main_list[1]]])
else:
    if len(main_list) == 3:
        first_list = [main_list[0], main_list[1]]
        second_list = [main_list[2]]
        print([first_list, second_list])
    elif len(main_list) == 4:
        first_list = [main_list[0], main_list[1]]
        second_list = [main_list[2], main_list[3]]
        print([first_list, second_list])
    elif len(main_list) == 5:
        first_list = [main_list[0], main_list[1], main_list[2]]
        second_list = [main_list[3], main_list[4]]
        print([first_list, second_list])
    elif len(main_list) == 6:
        first_list = [main_list[0], main_list[1], main_list[2]]
        second_list = [main_list[3], main_list[4], main_list[5]]
        print([first_list, second_list])
#v2
match len(main_list):
    case 1:
        print([[main_list[0]], []])
    case 2:
        print([[main_list[0]], [main_list[1]]])
    case 3:
        first_list = [main_list[0], main_list[1]]
        second_list = [main_list[2]]
        print([first_list, second_list])
    case 4:
        first_list = [main_list[0], main_list[1]]
        second_list = [main_list[2], main_list[3]]
        print([first_list, second_list])
    case 5:
        first_list = [main_list[0], main_list[1], main_list[2]]
        second_list = [main_list[3], main_list[4]]
        print([first_list, second_list])
    case 6:
        first_list = [main_list[0], main_list[1], main_list[2]]
        second_list = [main_list[3], main_list[4], main_list[5]]
        print([first_list, second_list])
#v3
if not main_list:
    print([[], []])
elif len(main_list) == 1:
    print([[main_list[0]], []])
else:
    center = (len(main_list) + 1) // 2
    first_list_v3 = []
    second_list_v3 = []

    for position in range(center):
        first_list_v3.append(main_list[position])

    for position in range(center, len(main_list)):
        second_list_v3.append(main_list[position])

    print([first_list_v3, second_list_v3])

#v4
if not main_list:
    first_part, second_part = [], []
elif len(main_list) == 1:
    first_part, second_part = [main_list[0]], []
else:
    mid = (len(main_list) + 1) // 2
    first_list_v4 = main_list[:mid]
    second_list_v4 = main_list[mid:]

print([first_list_v4, second_list_v4])