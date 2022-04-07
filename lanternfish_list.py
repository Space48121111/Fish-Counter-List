# lanternfish spawn timer
# 0 -> reset to 6 + new/8 -> count down to 0
# timer: cal by days(not 0)/elements of fish no.

# txt = open('lanternfish_list.txt', 'r')
# data = txt.read().strip().split(',')
# strip() to remove the space \n
# data = list(txt.readlines())

day_list = [3, 4, 3, 1, 2]
# [2, 3, 2, 0, 1]
# after 18 days, 26 fish
# after 80 days 5934 fish

# time complexity: O(n * c)
# space complexity: O(n + n/6 + c * (n/8) )


def spawn_timer(list):
    new_list = []
    timer = 0
    counter = 0
    # brutal force
    # edge cases: whenever there's 0, counter += 1
    # before 8 decreases into 7

    while timer < 3:
        for i, v in enumerate(day_list):
            # print(day_list[i])
            if day_list[i] <= 0:
                day_list[i] = 6
                new_list.append(8)

            else:
                day_list[i] = day_list[i] - 1
                if day_list[i] == 7:
                    counter += 1
                    print(counter, timer, new_list)
                new_list = day_list


        timer += 1

    print('Counter: ', counter, new_list)

    list_len = len(new_list)

    return list_len

print(spawn_timer(day_list))

# end
