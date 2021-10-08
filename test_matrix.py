from matrix import Matrix 

def test_matrix_creation():
    m = Matrix(5)
    assert len(m.data) == 5
    for row in m.data:
        assert len(row) == 5

def test_matrix_multiplication_simple():
    m1 = Matrix(2)
    m2 = Matrix(2)
    m1.data = [[1,1], [1,1]]
    m2.data = [[1,1], [1,1]]
    m_res = [[2,2], [2,2]]
    mult = Matrix.multiply_matrices(m1, m2)
    assert  mult.data == m_res

def test_matrix_multiplication_harder():
    m1 = Matrix(2)
    m2 = Matrix(2)
    m1.data = [[1,3], [1,3]]
    m2.data = [[1,2], [1,2]]
    m_res = [[4,8], [4,8]]
    mult = Matrix.multiply_matrices(m1, m2)
    assert  mult.data == m_res

def test_matrix_multiplication_4():
    m1 = Matrix(4)
    m2 = Matrix(4)
    m1.data = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
    m2.data = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
    m_res = [[4,4,4,4], [4,4,4,4], [4,4,4,4], [4,4,4,4]]
    mult = Matrix.multiply_matrices(m1, m2)
    assert  mult.data == m_res
