def part_one(data):
    n = len(data)
    for i in range(n):
        for j in range(i+1, n):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]

def part_two(data):
    n = len(data)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]


if __name__ == '__main__':
    with open('input.txt') as f:
        inp = list(map(int, f.readlines()))
    print(part_one(inp))
    print(part_two(inp))
