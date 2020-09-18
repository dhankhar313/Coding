edge_len = int(input())
pos = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]
d = [str(i) for i in input().split()]

areas = []
x = 0
while x <= edge_len:
    for i in range(4):
        if d[i] == 'U':
            if pos[i] != edge_len:
                pos[i] += s[i]
                if pos[i] > edge_len:
                    pos[i] = edge_len
        else:
            if pos[i] != edge_len:
                pos[i] -= s[i]
                if pos[i] < 0:
                    pos[i] = 0

    base = (edge_len ** 2 + abs(pos[0] - pos[-1]) ** 2) ** 0.5
    height = (edge_len ** 2 + abs(pos[-1] - pos[-2]) ** 2) ** 0.5
    area_acd = 0.5 * base * height
    base = (edge_len ** 2 + abs(pos[0] - pos[1]) ** 2) ** 0.5
    height = (edge_len ** 2 + abs(pos[1] - pos[2]) ** 2) ** 0.5
    area_abc = 0.5 * base * height
    areas.append(round(4 * ((area_abc + area_acd) ** 2)))
    x += 1

print(max(areas), min(areas))
