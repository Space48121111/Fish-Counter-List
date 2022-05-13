from __future__ import annotations

input = ''' \
nums = [2,7,11,15]
target = 9
'''

input1 = ''' \
nums = [3,2,4]
target = 6
'''
'''
output = [0, 1]
output1 = [1, 2]
'''

def two_sum(s: str) -> list(int):
    # parsing...
    line = s.splitlines()
    _, n_ss = line[0].split('[')
    n_s, _ = n_ss.split(']')
    _, tar_s = line[1].split('= ')
    nums = list(int(x) for x in n_s.split(','))
    tar = int(tar_s)

    for i in range(len(nums)):
        for j in range(len(nums)):
            print(i, j)
            sum = nums[i] + nums[j]
            if j > i:
                if sum == tar:
                    return [i, j]

print(two_sum(input1))









# end
