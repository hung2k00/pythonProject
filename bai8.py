'''
8.	Viết chương trình Python để tìm tổng của tất cả các số chẵn trong một danh sách
'''
if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10]
    sum = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            sum += a[i]
    print(sum)