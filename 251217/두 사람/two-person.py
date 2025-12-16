inp = input()
inp2 = input()
arr = inp.split()
arr2 = inp2.split()

a_a = int(arr[0])
a_s = str(arr[1])

b_a = int(arr2[0])
b_s = str(arr2[1])

if (a_a >= 10 or b_a >= 19) and (a_s == 'M' or b_s == 'M') :
    print(1)
else :
    print(0)