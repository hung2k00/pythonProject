'''
5.	Viết chương trình Python để tìm phần tử lớn nhất trong một danh sách
'''
if __name__ == '__main__':
    a = [12,90,23,45,6,2,12,4,6,78,8,4,3,1,1,3,45,6778]
    max = a[0]
    for i in range(0,len(a)):
        if max < a[i]:
            max = a[i]
    print("Max: ", max)