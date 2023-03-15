'''
1.	Viết chương trình Python tìm giai thừa của một số.
'''
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
if __name__ == '__main__':
    x = int(input("Moi ban nhap so x: "))
    print("Ket qua nhan duoc la: ", fact(x))
    