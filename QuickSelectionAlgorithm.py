#Author : Krishna Parmar
#Algorithm for Quick Selection Sort by Deterministic Pivot
#To find Kth element in Unsorted Array
#Time complexity for this algorithm is O(n) for worst case
import math
def median_of(S):       #This function will give Median element of Array
    l1=sorted(S)
    return l1[len(S)//2]
def partition(S,left,right):    #Partition as per Quick Sort
    pivot=left
    i=left+1
    j=right
    while True:
        while i<=j and S[j]>S[pivot]:
            j=j-1
        while i<=j and S[i]<=S[pivot]:
            i=i+1
        if i<=j:
            S[i],S[j]=S[j],S[i]
        else:
            break
    S[j],S[pivot]=S[pivot],S[j]
    return j
def kth_element(S,left,right,k):    #Function to Find Kth element
        if left<right:  #to stop recursion, if condition fails then one element in array
            median=[]
        #here we will take Deterministic Method to select pivot not random method
            #Which is to divide array in to n/5 rows and then sort each colomn
            #after that select row in median and take median of that row
            i=left
            j=left+5
            while j<=right:
                median.append(median_of(S[i:j]))
                i=i+5
                j=j+5
            if i<right:
                median.append(median_of(S[i:]))
            if len(median)==1:
                mom=median[0]
            else:
                mom=kth_element(median,0,len(median)-1,len(median)//2)
            for i in range(left,right+1):
                if S[i]==mom:
                    S[left],S[i]=S[i],S[left]
                    break;
            p=partition(S,left,right)
            if p+1==k:
                return p
            elif p+1>k:
                return kth_element(S,left,p-1,k)
            elif p+1<k:
                return kth_element(S,p+1,right,k)
        else:
            return left

#DRIVER CODE
S=[] #Array for elements in Sample Space
#Input Sequence : i)Size of Array (ii) Array elements (iii)Kth index
size=int(input("Enter size of array: \n"))
for i in range(size):
    S.append(int(input("Enter element: ")))
k=int(input("Enter Kth index: "))
ans=kth_element(S,0,len(S)-1,k) #Activation Key
print(f'{S[ans]} is {k}th element') #final answer