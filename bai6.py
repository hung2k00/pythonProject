'''
6.	Viết chương trình Python để loại bỏ các bản sao khỏi danh sách
'''
if __name__ == '__main__':
    a=[1,2,2,1,3,4,56,7,5,4,3,4,56]
    b=[]
    for i in a:
        if i not in b:
            b.append(i) #them gia tri thu i vao b
    print("Danh sach sau khi loai bo: ",b)
