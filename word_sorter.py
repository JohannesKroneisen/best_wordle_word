import json


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i]["yellow_score"]*yellow_weight+L[i]["green_score"]*green_weight <= R[j]["yellow_score"]*yellow_weight+R[j]["green_score"]*green_weight:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 

# Feet to and from mergeSort
# open unsorted data
results_historic = json.load(open('results_historic.json', encoding='utf-8'))
results_possible = json.load(open('results_possible.json', encoding='utf-8'))

#ask for the weight between green and yellow score

green_weight=float(input("Weight of green spaces when sorting (as decimal): "))
yellow_weight=1-green_weight

n = len(results_historic)
mergeSort(results_historic, 0, n-1)

#save results
with open('results_possible_sorted.json', 'w', encoding='utf-8') as f:
        json.dump(results_possible, f, ensure_ascii=False, indent=4)
with open('results_historic_sorted.json', 'w', encoding='utf-8') as f:
        json.dump(results_historic, f, ensure_ascii=False, indent=4)