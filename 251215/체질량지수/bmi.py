# h: 키, w: 몸무게
h, w = map(int, input().split())

# bmi 계산
b = (10000*w)/(h*h)

print(int(b))

if b >= 25:
    print('Obesity')