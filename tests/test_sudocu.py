from helpers import solve_sudoku, checkInput

def test_checkInputs_c():
    assert checkInput("123 456 789") == True
    assert checkInput("123...789") == True
    assert checkInput(".........") == True
    
# to check the incorect length
def test_checkInputs_i_len():
    assert checkInput("1") == False
    assert checkInput("111") == False
    assert checkInput("111 111") == False
    assert checkInput("111 111 111 111") == False
    
def test_solve_soducu():
    ...