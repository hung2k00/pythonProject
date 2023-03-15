'''
4.	Viết chương trình Python để sắp xếp danh sách các số theo thứ tự tăng dần
'''
if __name__ == '__main__':
    a = [10,40,59,12,1,2,3,4,5]
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print(a)