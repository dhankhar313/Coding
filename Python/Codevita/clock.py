def find_angle(h, m):
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m
    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)
    angle = "%.2f" % angle
    print(angle, end="")


hrs = int(input())
lon = float(input())
time = (hrs / 360) * lon
time = round(time, 2)
# print("Time w/o units:", time)
digits = []
for i in str(time):
    if i.isdigit():
        digits.append(i)
# print("Full List:", digits)
bef_dec = []
for i in str(time):
    if i.isdigit():
        bef_dec.append(i)
    else:
        break
# print("Hour List:", bef_dec)
hour = "".join(bef_dec)
# print("Hour:", hour)
after_dec = []
for i in str(time):
    if i.isdigit():
        after_dec.append(i)
    else:
        after_dec.clear()
if len(after_dec) == 1:
    after_dec.append('0')
minute = "".join(after_dec)
# print("Minute List:", after_dec)
minute = int((int(minute) / 100) * 60)
# print("Minute:", minute)
if hour == 12:
    hour = 0
if minute == 60:
    minute = 0
print(hour, ":", minute)

find_angle(int(hour), int(minute))