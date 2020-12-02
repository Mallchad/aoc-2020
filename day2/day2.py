from collections import Counter
def part_one(data):
    ans = 0
    for part in data:
        part = part.split()
        cnt = Counter(part[2])
        nums = part[0].split('-')
        if int(nums[0]) <= cnt[part[1][0]] <= int(nums[1]): ans += 1

    return ans
def part_two(data):
    ans = 0
    for part in data:
        part = part.split()
        string = part[2]
        indices = list(map(int, part[0].split('-')))
        if string[indices[0]-1] == part[1][0] and string[indices[1]-1] == part[1][0]: continue
        elif string[indices[0]-1] == part[1][0] or string[indices[1]-1] == part[1][0]: ans += 1
    return ans

if __name__ == '__main__':
    with open('input.txt') as f:
        inp = list(map(str, f.readlines()))
    print(part_one(inp))
    print(part_two(inp))
