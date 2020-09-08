xl = int(input())
yl = int(input())
xd = int(input())
yd = int(input())
f = float(input())
v = 2
dis1 = []
temp = xl
while temp <= xd:
    temp += 1
    distance = ((yl ** 2) + ((temp - xl) ** 2)) ** 0.5
    dis1.append("%.6f" % distance)
print(dis1)
dis2 = []
temp2 = xd
while temp2 >= xl:
    temp2 -= 1
    distance = ((yd ** 2) + (abs(temp2 - xd) ** 2)) ** 0.5
    dis2.append("%.6f" % distance)
print(dis2)
dist1 = ["%.6f" % (float(i) / (float(v) * f)) for i in dis1]
print(dist1)
dist2 = ["%.6f" % (float(i) / float(v)) for i in dis1]
print(dist2)
final = []
for i in dist1:
    for j in dist2:
        temp3 = float(i) + float(j)
        final.append("%.6f" % temp3)
        final.sort()
        if temp3 <= float(final[0]):
            minl = i
            mind = j
print(final)
print(minl, mind)
