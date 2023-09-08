import time
import matplotlib.pyplot as plt
from numpy.random import randint
def mergesort(aray):
    if len(aray)>1:
        r=len(aray)//2
        L=aray[:r]
        M=aray[r:]
        mergesort(L)
        mergesort(M)
        i=j=k=0
        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                aray[k]=L[i]
                i+=1
            else:
                aray[k]=M[j]
                j+=1
            k+=1
        while i<len(L):
            aray[k]=L[i]
            i+=1
            k+=1
        while j<len(M):
            aray[k]=M[j]
            j+=1
            k+=1

def printlist(aray):
    for i in range(len(aray)):
        print(aray[i],end=" ")
    print()

def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1

def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)

def selectionsort(array,size):
    for step in range(size):
        min_idx=step
        for i in range(step+1,size):
            if array[i]<array[min_idx]:
                min_idx=i
        (array[step],array[min_idx])=(array[min_idx],array[step])

def read_input():
    a=[]
    n=int(input("Enter the number of TV channels: "))
    print("Enter the numebr of viewers: ")
    for i in range(0,n):
        l=int(input())
        a.append(l)
    return a;

elements=list()
times=list()
global labeldata
print("1.MergeSort\n2.QuickSort\n3.SelectionSort\n")
ch=int(input("Enter the choice:"))
if(ch==1):
    array=read_input()
    mergesort(array)
    labeldata="Mergesort"
    print('sorted data: ')
    print(array)
if(ch==2):
    array=read_input()
    size=len(array)
    labeldata="Quicksort"
    quicksort(array,0,size-1)
    print('sorted data: ')
    print(array)
if(ch==3):
    array=read_input()
    size=len(array)
    labeldata="Selectionsort"
    selectionsort(array,size)
    print('sorted data: ')
    print(array)
print("********************************RUNNING TIME ANALYSIS**********************************")
for i in range(1,10):
    array=randint(0,1000*i,1000*i)
    start=time.time()
    if ch==1:
        mergesort(array)
    elif ch==2:
        size=len(array)
        quicksort(array,0,size-1)
    else:
        size=len(array)
        selectionsort(array,size)
    end=time.time()
    print(len(array)," Elementa sorted by ",labeldata," in ",end-start)
    elements.append(len(array))
    times.append(end-start)

plt.xlabel('list length')
plt.ylabel('time complxty')
plt.plot(elements,times,label=labeldata)
plt.grid()
plt.legend()
plt.show()



# 1.MergeSort
# 2.QuickSort
# 3.SelectionSort

# Enter the choice:1
# Enter the number of TV channels: 5
# Enter the numebr of viewers: 
# 345
# 560
# 345
# 800
# 125
# sorted data: 
# [125, 345, 345, 560, 800]
# ********************************RUNNING TIME ANALYSIS**********************************
# 1000  Elementa sorted by  Mergesort  in  0.0030012130737304688
# 2000  Elementa sorted by  Mergesort  in  0.009052276611328125
# 3000  Elementa sorted by  Mergesort  in  0.017949581146240234
# 4000  Elementa sorted by  Mergesort  in  0.01699995994567871
# 5000  Elementa sorted by  Mergesort  in  0.02200007438659668
# 6000  Elementa sorted by  Mergesort  in  0.026997804641723633
# 7000  Elementa sorted by  Mergesort  in  0.032004594802856445
# 8000  Elementa sorted by  Mergesort  in  0.03699517250061035
# 9000  Elementa sorted by  Mergesort  in  0.0429997444152832

