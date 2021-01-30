x = [1, 2, 3, 4, 5, 6, 7]
#y = 4
y = int(input('Введите число, которое надо проверить на наличие в массиве '))
mLen = len(x)
indLeft = 0
indRight = mLen - 1
left = x[indLeft]
right = x[indRight]
a = 0
if((y >= left) and (y <= right)):
    print("Число находится внутри массива")

    while(a < mLen):
        if(x[a] == y):
            print("Число есть в массиве!")
            print("Id:", a)
        a = a + 1

else:
    print("Число не находится внутри массива")