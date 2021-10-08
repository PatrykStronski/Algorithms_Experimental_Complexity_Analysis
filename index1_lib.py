POLYNOMIAL_INPUT = 1.5

def constantFunction(v: list[int]) -> int:
    return 6

def sumOfElems(v: list[int]) -> int:
    elemSum = 0
    for elem in v:
        elemSum += elem
    return elemSum

def productOfElems(v: list[int]) -> int:
    prod = 1
    for elem in v:
        prod *= elem
    return prod

def polynomialEvaluation(v: list[int]) -> float:
    evalValue = 0
    n = len(v) - 1
    for index in range(0, len(v)):
        evalValue += v[index]*POLYNOMIAL_INPUT**(n-index)
    return evalValue

def polynomialEvaluationHorner(v: list[int]) -> float:
    res = v[0]
    for ind in range(1,len(v)):
        res = res * POLYNOMIAL_INPUT + v[ind]
    return res

def bubbleSort(v: list[int]) -> list[int]:
    length = len(v)
    for j in range(0, length-1):
        for i in range(0,length-1):
            if v[i] > v[i+1]:
                v[i+1], v[i] = v[i], v[i+1]
    return v

def pivot(v: list[int], start: int, end: int):
    pivot = v[start]
    low = start + 1
    high = end
    while True:
        while low <= high and v[high] >= pivot:
            high = high - 1
        while low <= high and v[low] <= pivot:
            low = low + 1
        if low <= high:
            v[low], v[high] = v[high], v[low]
        else:
            break
    v[start], v[high] = v[high], v[start]
    return high

def sort_alg(v: list[int], start: int, end: int) -> list[int]:
    if start >= end:
        return v
    p = pivot(v, start, end)
    sort_alg(v, start, p-1)
    sort_alg(v, p+1, end)
    return v

def quick_sort(v: list[int]) -> list[int]:
    return sort_alg(v, 0, len(v)-1)

def tim_sort(v: list[int]) -> list[int]:
    v.sort()
    return v


