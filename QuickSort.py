import random
import time

def partisi(input_list,low,high):
    i = (low - 1)
    pivot = input_list[high]
    for j in range(low, high):
        if input_list[j] <= pivot:
            i = i + 1
            input_list[i], input_list[j] =  input_list[j], input_list[i]
    input_list[i+1],input_list[high] = input_list[high],input_list[i+1]
    return (i+1)

def quickSort(input_list, low, high):
    if low < high:
        partition_index = partisi(input_list,low,high)
        quickSort(input_list, low, partition_index - 1)
        quickSort(input_list, partition_index + 1, high)

def random_no_generator():
    randomlist = []
    for i in range(0,10):
        n = random.randint(1,500)
        time.sleep(0.5)
        print(n ,sep='',end=" ",flush=True)
        randomlist.append(n)
    return randomlist

start_time = time.time()

print('Angka Acak   :',end=' ')
numbers = random_no_generator()

quickSort(numbers, 0, len(numbers)-1)
print("\nHasil Sortir :",end=' ')
time.sleep(0.5)
for i in range(0,10):
    time.sleep(0.3)
    print(numbers[i] ,end=" ",flush=True)
