def bubbleSort(L):
    n = len(L)

    for i in range(n-1):      
        for j in range(0, n-i-1):           
            if L[j] > L[j + 1]:
                swapped = True
                L[j], L[j + 1] = L[j + 1], L[j]         
        if not swapped:
            return
 
 
L = [1,9,8,7,6,5,5,4,3,2]
 
bubbleSort(L)
 
print("Una vez ordenado")
for i in range(len(L)):
    print(L[i])
#O(N-1).O(N)==> O(N^2)