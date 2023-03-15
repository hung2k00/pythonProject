'''
3.	Viết chương trình Python để in dãy Fibonacci đến một số cho trước
'''


def fibonacci(n):
    if (n <= 0):
        return -1;
    elif ( n == 1):
        return n;
    else:
        return fibonacci( n - 1 ) + fibonacci( n - 2 );

if __name__ == '__main__':

    n = int(input("Moi ban nhap so n: "))
    sb = "";
    for i in range( 0, n ):
        sb = sb + str( fibonacci( i ) ) + ", ";
    print( sb )