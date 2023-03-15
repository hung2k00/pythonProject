'''
2.	Viết chương trình Python kiểm tra một số có phải là số nguyên tố hay không
'''
import math
if __name__ == '__main__':
    n = int(input("Moi ban nhap so can kiem tra: "))
    if n < 2:
        print("khong phai so nguyen to")
    count = 0
    a= math.sqrt(n)
    for i in range(2, int(a) + 1 ):
        if n % i == 0:
            count +=1
    if count == 0:
        print(n,"La so nguyen to")
    else:
        print("Khong la so nguyen to")