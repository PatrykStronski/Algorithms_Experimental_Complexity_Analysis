import index1_lib

ARRAY = [5, 4, 12, 100, -3, -9, 6, 22, 4]
ARRAY_SORTED = [-9, -3, 4, 4, 5, 6, 12, 22, 100]
POLYNOMIAL = [1, 1, 2] 
POLYNOMIAL_EVAL = 5.75

def test_bubble_sort():
    assert ARRAY_SORTED == index1_lib.bubbleSort(ARRAY.copy())

def test_plynomial_evaluation():
    assert index1_lib.polynomialEvaluation(POLYNOMIAL.copy()) == POLYNOMIAL_EVAL

def test_plynomial_evaluation_horner():
    assert index1_lib.polynomialEvaluationHorner(POLYNOMIAL.copy()) == POLYNOMIAL_EVAL

def test_quick_sort():
    assert ARRAY_SORTED == index1_lib.quick_sort(ARRAY.copy())
