a=[3,21,1,4,1,7,9]


for i in range(len(a)):



    for j in range(i+1,len(a)):
        if a[i]!=a[j]:
            if a[i]>a[j]:
                a[i],a[j]=a[j] , a[i]





print(a)