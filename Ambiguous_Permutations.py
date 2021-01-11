while (True):
    n = int(input())
    if (n == 0):
        break
    else:
        a = list(map(int , input().split()))
        flag = 0

        for i in range(len(a)):
            if (a[a[i]-1] != i+1):
                flag = 1
        
        if (flag == 0):
            print("ambiguous")
        else:
            print("not ambiguous")