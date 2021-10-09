import math

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

def polynomialEvaluation(v: list[int]) -> (float, float):
    evalValue = 0.0
    if len(v) > 1400:
        v_1 = v[:1000]
        v_2 = v[1000:]
        return (polynomialEvaluation(v_2)[1], polynomialEvaluation(v_1)[1])
    for index in range(0, len(v)):
        evalValue += v[index]* math.pow(POLYNOMIAL_INPUT, index)
    return (0, evalValue)

def polynomialEvaluationHorner(v: list[int]) -> (float, float):
    res = v[-1]
    if len(v) > 1400:
        v_1 = v[:1000]
        v_2 = v[1000:]
        return (polynomialEvaluationHorner(v_2)[1], polynomialEvaluationHorner(v_1)[1])
    ind = len(v) - 2
    while ind >= 0:
        res = res * POLYNOMIAL_INPUT + v[ind]
        ind -= 1
    return (0, res)

def bubbleSort(v: list[int]) -> list[int]:
    length = len(v)
    for j in range(0, length-1):
        for i in range(0,length-1):
            if v[i] > v[i+1]:
                v[i+1], v[i] = v[i], v[i+1]
    return v

def pivot(v: list[int], start: int, end: int):
    piv = v[start]
    beginning = start + 1
    while True:
        while beginning <= end and v[end] >= piv:
            end = end - 1
        while beginning <= end and v[beginning] <= piv:
            beginning = beginning + 1
        if beginning <= end:
            v[beginning], v[end] = v[end], v[beginning]
        else:
            break
    v[start], v[end] = v[end], v[start]
    return end

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


