from helpers import solve_sudoku, checkInput
from sudocu_lists import *

def test_checkInputs_c():
    assert checkInput("123456789") == True
    assert checkInput("123...789") == True
    assert checkInput(".........") == True
    
# to check the incorect length
def test_checkInputs_i_len():
    assert checkInput("1") == False
    assert checkInput("111") == False
    assert checkInput("111 111") == False
    assert checkInput("111 111 111 111") == False
    
def test_solve_soducu():
    assert solve_sudoku(s1_u) == True
    assert solve_sudoku(s1_s) == False