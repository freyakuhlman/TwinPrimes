import os
import NumbaTwinPrimes as ntp
import pytest
import numpy as np


def test_GenerateArrays():
    hexas_array, sextands_array, square_sextands_array = ntp.GenerateArrays(25)
    assert np.array_equal(hexas_array, [5.,  7., 11., 13., 17., 19., 23., 25., 29., 31., 35., 37., 41.,
       43., 47., 49., 53., 55., 59., 61., 65., 67., 71., 73., 77.])
    assert np.array_equal(sextands_array, [ 1.,  1.,  2.,  2.,  3.,  3.,  4.,  4.,  5.,  5.,  6.,  6.,  7.,
        7.,  8.,  8.,  9.,  9., 10., 10., 11., 11., 12., 12., 13.] )
    assert np.array_equal(square_sextands_array, [  4.,   8.,  20.,  28.,  48.,  60.,  88., 104., 140., 160., 204.,
       228., 280., 308., 368., 400., 468., 504., 580., 620., 704., 748.,
       840., 888., 988.])

def test_InitializeArrays():

    # Testing variables
    # Should pass
    size_five = 5
    size_zero = 0

    # Should fail
    size_neg = -1
    size_float = 7.8
    size_string = 'hello'

    #Initalization of arrays
    hexas_array_five, sextands_array_five, square_sextands_array_five = ntp.InitializeArrays(size_five)
    hexas_array_zero, sextands_array_zero, square_sextands_array_zero = ntp.InitializeArrays(size_zero)

    # Assertion array size = 5 
    assert len(hexas_array_five) == size_five
    assert len(sextands_array_five) == size_five
    assert len(square_sextands_array_five) == size_five

    # Asertion array size = 0
    assert len(hexas_array_zero) == size_zero
    assert len(sextands_array_zero) == size_zero
    assert len(square_sextands_array_zero) == size_zero

    with pytest.raises(Exception) as e_info:
        hexas_array_neg, sextands_array_neg, square_sextands_array_neg = ntp.InitializeArrays(size_neg)

    with pytest.raises(Exception) as e_info:
        hexas_array_float, sextands_array_float, square_sextands_array_float = ntp.InitializeArrays(size_float)

    with pytest.raises(Exception) as e_info:
        hexas_array_string, sextands_array_string, square_sextands_array_string = ntp.InitializeArrays(size_string)

def test_GenerateHexas():
    hexas_array, square_sextands_array, sextands_array = ntp.GenerateHexas(25)
        
    assert np.array_equal(hexas_array, [5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53, 55, 59, 61, 65, 67, 71, 73, 77])
    assert np.array_equal(sextands_array, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13])
    assert np.array_equal(square_sextands_array, [4, 8, 20, 28, 48, 60, 88, 104, 140, 160, 204, 228, 280, 308, 368, 400, 468, 504, 580, 620, 704, 748, 840, 888, 988])

def test_FindInvalidChains():
    max_chain, max_length, critical_zone = ntp.FindInvalidChains(3)
    assert max_chain == 13
    assert max_length == 4
    assert critical_zone == 12.0

def test_GenerateCombo():
    combo = ntp.GenerateCombo(2, 2)
    assert combo == '2 2 < '

def test_ViewCombo():
    combo_array1 = ntp.ViewCombo(3, 3, 3)
    combo_array2 = ntp.ViewCombo(3, 4, 5)
    combo_array3 = ntp.ViewCombo(3, 6, 10)
    assert np.array_equal(combo_array1, ['3: 3 3 3 < ', '4: 4 4 4 ', '5: 0 5 5 < '])
    assert np.array_equal(combo_array2, ['4: 4 4 4 ', '5: 0 5 5 < ', '6: 1 6 6 ', '7: 2 0 7 < ', '8: 3 1 8 '])
    assert np.array_equal(combo_array2, ['4: 4 4 4 ', '5: 0 5 5 < ', '6: 1 6 6 ', '7: 2 0 7 < ', '8: 3 1 8 '])
    assert np.array_equal(combo_array3, ['6: 1 6 6 ', '7: 2 0 7 < ', '8: 3 1 8 ', '9: 4 2 9 ',
       '10: 0 3 10 ', '11: 1 4 0 ', '12: 2 5 1 ', '13: 3 6 2 ',
       '14: 4 0 3 ', '15: 0 1 4 '])

def test_ViewCritCombos():
    crit_combo1 = ntp.ViewCritCombos(4)
    assert np.array_equal(crit_combo1, ['1: 1 1 1 1 ', '2: 2 2 2 2 < ', '3: 3 3 3 3 < ', '4: 4 4 4 4 ',
       '5: 0 5 5 5 < ', '6: 1 6 6 6 ', '7: 2 0 7 7 < ', '8: 3 1 8 8 ',
       '9: 4 2 9 9 ', '10: 0 3 10 10 ', '11: 1 4 0 11 ', '12: 2 5 1 12 ',
       '13: 3 6 2 0 ', '14: 4 0 3 1 ', '15: 0 1 4 2 ', '16: 1 2 5 3 ',
       '17: 2 3 6 4 < ', '18: 3 4 7 5 < ', '19: 4 5 8 6 ', '20: 0 6 9 7 ',
       '21: 1 0 10 8 ', '22: 2 1 0 9 ', '23: 3 2 1 10 ', '24: 4 3 2 11 ',
       '25: 0 4 3 12 ', '26: 1 5 4 0 ', '27: 2 6 5 1 ', '28: 3 0 6 2 < ',
       '29: 4 1 7 3 '])

    crit_combo2 = ntp.ViewCritCombos(11)
    assert np.array_equal(crit_combo2, ['1: 1 1 1 1 1 1 1 1 1 1 1 ', '2: 2 2 2 2 2 2 2 2 2 2 2 < ',
       '3: 3 3 3 3 3 3 3 3 3 3 3 < ', '4: 4 4 4 4 4 4 4 4 4 4 4 ',
       '5: 0 5 5 5 5 5 5 5 5 5 5 < ', '6: 1 6 6 6 6 6 6 6 6 6 6 ',
       '7: 2 0 7 7 7 7 7 7 7 7 7 < ', '8: 3 1 8 8 8 8 8 8 8 8 8 ',
       '9: 4 2 9 9 9 9 9 9 9 9 9 ', '10: 0 3 10 10 10 10 10 10 10 10 10 ',
       '11: 1 4 0 11 11 11 11 11 11 11 11 ',
       '12: 2 5 1 12 12 12 12 12 12 12 12 ',
       '13: 3 6 2 0 13 13 13 13 13 13 13 ',
       '14: 4 0 3 1 14 14 14 14 14 14 14 ',
       '15: 0 1 4 2 15 15 15 15 15 15 15 ',
       '16: 1 2 5 3 16 16 16 16 16 16 16 ',
       '17: 2 3 6 4 0 17 17 17 17 17 17 < ',
       '18: 3 4 7 5 1 18 18 18 18 18 18 ',
       '19: 4 5 8 6 2 0 19 19 19 19 19 ',
       '20: 0 6 9 7 3 1 20 20 20 20 20 ',
       '21: 1 0 10 8 4 2 21 21 21 21 21 ',
       '22: 2 1 0 9 5 3 22 22 22 22 22 ',
       '23: 3 2 1 10 6 4 0 23 23 23 23 ',
       '24: 4 3 2 11 7 5 1 24 24 24 24 ',
       '25: 0 4 3 12 8 6 2 0 25 25 25 ', '26: 1 5 4 0 9 7 3 1 26 26 26 ',
       '27: 2 6 5 1 10 8 4 2 27 27 27 ', '28: 3 0 6 2 11 9 5 3 28 28 28 ',
       '29: 4 1 7 3 12 10 6 4 0 29 29 ', '30: 0 2 8 4 13 11 7 5 1 30 30 ',
       '31: 1 3 9 5 14 12 8 6 2 0 31 ', '32: 2 4 10 6 15 13 9 7 3 1 32 ',
       '33: 3 5 0 7 16 14 10 8 4 2 33 ', '34: 4 6 1 8 0 15 11 9 5 3 34 ',
       '35: 0 0 2 9 1 16 12 10 6 4 0 ', '36: 1 1 3 10 2 17 13 11 7 5 1 ',
       '37: 2 2 4 11 3 18 14 12 8 6 2 ', '38: 3 3 5 12 4 0 15 13 9 7 3 ',
       '39: 4 4 6 0 5 1 16 14 10 8 4 ', '40: 0 5 7 1 6 2 17 15 11 9 5 ',
       '41: 1 6 8 2 7 3 18 16 12 10 6 ',
       '42: 2 0 9 3 8 4 19 17 13 11 7 < ',
       '43: 3 1 10 4 9 5 20 18 14 12 8 ',
       '44: 4 2 0 5 10 6 21 19 15 13 9 ',
       '45: 0 3 1 6 11 7 22 20 16 14 10 ',
       '46: 1 4 2 7 12 8 0 21 17 15 11 ',
       '47: 2 5 3 8 13 9 1 22 18 16 12 ',
       '48: 3 6 4 9 14 10 2 23 19 17 13 ',
       '49: 4 0 5 10 15 11 3 24 20 18 14 ',
       '50: 0 1 6 11 16 12 4 0 21 19 15 ',
       '51: 1 2 7 12 0 13 5 1 22 20 16 ',
       '52: 2 3 8 0 1 14 6 2 23 21 17 ', '53: 3 4 9 1 2 15 7 3 24 22 18 ',
       '54: 4 5 10 2 3 16 8 4 25 23 19 ',
       '55: 0 6 0 3 4 17 9 5 26 24 20 ',
       '56: 1 0 1 4 5 18 10 6 27 25 21 ',
       '57: 2 1 2 5 6 0 11 7 28 26 22 ', '58: 3 2 3 6 7 1 12 8 0 27 23 ',
       '59: 4 3 4 7 8 2 13 9 1 28 24 ',
       '60: 0 4 5 8 9 3 14 10 2 29 25 < ',
       '61: 1 5 6 9 10 4 15 11 3 30 26 ',
       '62: 2 6 7 10 11 5 16 12 4 0 27 ',
       '63: 3 0 8 11 12 6 17 13 5 1 28 ',
       '64: 4 1 9 12 13 7 18 14 6 2 29 ',
       '65: 0 2 10 0 14 8 19 15 7 3 30 ',
       '66: 1 3 0 1 15 9 20 16 8 4 31 ',
       '67: 2 4 1 2 16 10 21 17 9 5 32 ',
       '68: 3 5 2 3 0 11 22 18 10 6 33 ',
       '69: 4 6 3 4 1 12 0 19 11 7 34 ', '70: 0 0 4 5 2 13 1 20 12 8 0 ',
       '71: 1 1 5 6 3 14 2 21 13 9 1 ',
       '72: 2 2 6 7 4 15 3 22 14 10 2 < ',
       '73: 3 3 7 8 5 16 4 23 15 11 3 < ',
       '74: 4 4 8 9 6 17 5 24 16 12 4 ', '75: 0 5 9 10 7 18 6 0 17 13 5 ',
       '76: 1 6 10 11 8 0 7 1 18 14 6 ', '77: 2 0 0 12 9 1 8 2 19 15 7 ',
       '78: 3 1 1 0 10 2 9 3 20 16 8 ', '79: 4 2 2 1 11 3 10 4 21 17 9 ',
       '80: 0 3 3 2 12 4 11 5 22 18 10 < ',
       '81: 1 4 4 3 13 5 12 6 23 19 11 ',
       '82: 2 5 5 4 14 6 13 7 24 20 12 < ',
       '83: 3 6 6 5 15 7 14 8 25 21 13 ',
       '84: 4 0 7 6 16 8 15 9 26 22 14 ',
       '85: 0 1 8 7 0 9 16 10 27 23 15 ',
       '86: 1 2 9 8 1 10 17 11 28 24 16 ',
       '87: 2 3 10 9 2 11 18 12 0 25 17 ',
       '88: 3 4 0 10 3 12 19 13 1 26 18 ',
       '89: 4 5 1 11 4 13 20 14 2 27 19 ',
       '90: 0 6 2 12 5 14 21 15 3 28 20 ',
       '91: 1 0 3 0 6 15 22 16 4 29 21 ',
       '92: 2 1 4 1 7 16 0 17 5 30 22 ', '93: 3 2 5 2 8 17 1 18 6 0 23 ',
       '94: 4 3 6 3 9 18 2 19 7 1 24 ', '95: 0 4 7 4 10 0 3 20 8 2 25 < ',
       '96: 1 5 8 5 11 1 4 21 9 3 26 ', '97: 2 6 9 6 12 2 5 22 10 4 27 ',
       '98: 3 0 10 7 13 3 6 23 11 5 28 ',
       '99: 4 1 0 8 14 4 7 24 12 6 29 ', '100: 0 2 1 9 15 5 8 0 13 7 30 ',
       '101: 1 3 2 10 16 6 9 1 14 8 31 ',
       '102: 2 4 3 11 0 7 10 2 15 9 32 < ',
       '103: 3 5 4 12 1 8 11 3 16 10 33 ',
       '104: 4 6 5 0 2 9 12 4 17 11 34 ',
       '105: 0 0 6 1 3 10 13 5 18 12 0 ',
       '106: 1 1 7 2 4 11 14 6 19 13 1 ',
       '107: 2 2 8 3 5 12 15 7 20 14 2 < ',
       '108: 3 3 9 4 6 13 16 8 21 15 3 < ',
       '109: 4 4 10 5 7 14 17 9 22 16 4 ',
       '110: 0 5 0 6 8 15 18 10 23 17 5 < ',
       '111: 1 6 1 7 9 16 19 11 24 18 6 ',
       '112: 2 0 2 8 10 17 20 12 25 19 7 < ',
       '113: 3 1 3 9 11 18 21 13 26 20 8 ',
       '114: 4 2 4 10 12 0 22 14 27 21 9 ',
       '115: 0 3 5 11 13 1 0 15 28 22 10 ',
       '116: 1 4 6 12 14 2 1 16 0 23 11 ',
       '117: 2 5 7 0 15 3 2 17 1 24 12 ',
       '118: 3 6 8 1 16 4 3 18 2 25 13 ',
       '119: 4 0 9 2 0 5 4 19 3 26 14 ',
       '120: 0 1 10 3 1 6 5 20 4 27 15 ',
       '121: 1 2 0 4 2 7 6 21 5 28 16 ', '122: 2 3 1 5 3 8 7 22 6 29 17 ',
       '123: 3 4 2 6 4 9 8 23 7 30 18 ', '124: 4 5 3 7 5 10 9 24 8 0 19 ',
       '125: 0 6 4 8 6 11 10 0 9 1 20 ',
       '126: 1 0 5 9 7 12 11 1 10 2 21 ',
       '127: 2 1 6 10 8 13 12 2 11 3 22 ',
       '128: 3 2 7 11 9 14 13 3 12 4 23 < ',
       '129: 4 3 8 12 10 15 14 4 13 5 24 ',
       '130: 0 4 9 0 11 16 15 5 14 6 25 < ',
       '131: 1 5 10 1 12 17 16 6 15 7 26 ',
       '132: 2 6 0 2 13 18 17 7 16 8 27 ',
       '133: 3 0 1 3 14 0 18 8 17 9 28 ',
       '134: 4 1 2 4 15 1 19 9 18 10 29 ',
       '135: 0 2 3 5 16 2 20 10 19 11 30 ',
       '136: 1 3 4 6 0 3 21 11 20 12 31 ',
       '137: 2 4 5 7 1 4 22 12 21 13 32 ',
       '138: 3 5 6 8 2 5 0 13 22 14 33 < ',
       '139: 4 6 7 9 3 6 1 14 23 15 34 ',
       '140: 0 0 8 10 4 7 2 15 24 16 0 < ',
       '141: 1 1 9 11 5 8 3 16 25 17 1 ',
       '142: 2 2 10 12 6 9 4 17 26 18 2 ',
       '143: 3 3 0 0 7 10 5 18 27 19 3 < ',
       '144: 4 4 1 1 8 11 6 19 28 20 4 ',
       '145: 0 5 2 2 9 12 7 20 0 21 5 < ',
       '146: 1 6 3 3 10 13 8 21 1 22 6 ',
       '147: 2 0 4 4 11 14 9 22 2 23 7 < ',
       '148: 3 1 5 5 12 15 10 23 3 24 8 ',
       '149: 4 2 6 6 13 16 11 24 4 25 9 ',
       '150: 0 3 7 7 14 17 12 0 5 26 10 < ',
       '151: 1 4 8 8 15 18 13 1 6 27 11 ',
       '152: 2 5 9 9 16 0 14 2 7 28 12 ',
       '153: 3 6 10 10 0 1 15 3 8 29 13 ',
       '154: 4 0 0 11 1 2 16 4 9 30 14 ',
       '155: 0 1 1 12 2 3 17 5 10 0 15 ',
       '156: 1 2 2 0 3 4 18 6 11 1 16 ', '157: 2 3 3 1 4 5 19 7 12 2 17 ',
       '158: 3 4 4 2 5 6 20 8 13 3 18 < ',
       '159: 4 5 5 3 6 7 21 9 14 4 19 ',
       '160: 0 6 6 4 7 8 22 10 15 5 20 ',
       '161: 1 0 7 5 8 9 0 11 16 6 21 ',
       '162: 2 1 8 6 9 10 1 12 17 7 22 ',
       '163: 3 2 9 7 10 11 2 13 18 8 23 < ',
       '164: 4 3 10 8 11 12 3 14 19 9 24 ',
       '165: 0 4 0 9 12 13 4 15 20 10 25 < ',
       '166: 1 5 1 10 13 14 5 16 21 11 26 ',
       '167: 2 6 2 11 14 15 6 17 22 12 27 ',
       '168: 3 0 3 12 15 16 7 18 23 13 28 ',
       '169: 4 1 4 0 16 17 8 19 24 14 29 ',
       '170: 0 2 5 1 0 18 9 20 25 15 30 ',
       '171: 1 3 6 2 1 0 10 21 26 16 31 ',
       '172: 2 4 7 3 2 1 11 22 27 17 32 ',
       '173: 3 5 8 4 3 2 12 23 28 18 33 ',
       '174: 4 6 9 5 4 3 13 24 0 19 34 ',
       '175: 0 0 10 6 5 4 14 0 1 20 0 ', '176: 1 1 0 7 6 5 15 1 2 21 1 ',
       '177: 2 2 1 8 7 6 16 2 3 22 2 ', '178: 3 3 2 9 8 7 17 3 4 23 3 < ',
       '179: 4 4 3 10 9 8 18 4 5 24 4 ',
       '180: 0 5 4 11 10 9 19 5 6 25 5 < ',
       '181: 1 6 5 12 11 10 20 6 7 26 6 ',
       '182: 2 0 6 0 12 11 21 7 8 27 7 < ',
       '183: 3 1 7 1 13 12 22 8 9 28 8 ',
       '184: 4 2 8 2 14 13 0 9 10 29 9 ',
       '185: 0 3 9 3 15 14 1 10 11 30 10 ',
       '186: 1 4 10 4 16 15 2 11 12 0 11 ',
       '187: 2 5 0 5 0 16 3 12 13 1 12 ',
       '188: 3 6 1 6 1 17 4 13 14 2 13 ',
       '189: 4 0 2 7 2 18 5 14 15 3 14 ',
       '190: 0 1 3 8 3 0 6 15 16 4 15 ', '191: 1 2 4 9 4 1 7 16 17 5 16 ',
       '192: 2 3 5 10 5 2 8 17 18 6 17 < ',
       '193: 3 4 6 11 6 3 9 18 19 7 18 < ',
       '194: 4 5 7 12 7 4 10 19 20 8 19 ',
       '195: 0 6 8 0 8 5 11 20 21 9 20 ',
       '196: 1 0 9 1 9 6 12 21 22 10 21 ',
       '197: 2 1 10 2 10 7 13 22 23 11 22 ',
       '198: 3 2 0 3 11 8 14 23 24 12 23 < ',
       '199: 4 3 1 4 12 9 15 24 25 13 24 ',
       '200: 0 4 2 5 13 10 16 0 26 14 25 < ',
       '201: 1 5 3 6 14 11 17 1 27 15 26 ',
       '202: 2 6 4 7 15 12 18 2 28 16 27 ',
       '203: 3 0 5 8 16 13 19 3 0 17 28 ',
       '204: 4 1 6 9 0 14 20 4 1 18 29 ',
       '205: 0 2 7 10 1 15 21 5 2 19 30 '])
           
def test_FindAverageGap():
    ntp.GenerateHexas(25)
    assert ntp.FindAverageGap(2) == (35.0, 15.0, 2.3333333333333335)
    assert ntp.FindAverageGap(5) == (85085.0, 22275.0,  3.819753086419753)
    assert ntp.FindAverageGap(25) == (8.011810311763933e+37, 7.650888424384966e+36, 10.47173853199667)

def test_ValidCoordinates():
    combos_list_4= ntp.ValidCoordinates(4)
    combos_list_12 = ntp.ValidCoordinates(12)
    combos_list_9 = ntp.ValidCoordinates(9)
    assert np.array_equal(combos_list_4, ['(2,2)', '(3,4)', '(4,2)'])
    assert np.array_equal(combos_list_12, ['(2,2)', '(3,4)', '(4,2)', '(5,7)', '(6,2)', '(7,4)', '(8,3)', '(9,5)', '(10,2)', '(11,6)', '(12,5)'])
    assert np.array_equal(combos_list_9, ['(2,2)', '(3,4)', '(4,2)', '(5,7)', '(6,2)', '(7,4)', '(8,3)', '(9,5)'] )

def test_WriteValidCoordinates():
    # Run ValidateCoordinates with hexasNum = 10
    hexas_num = 10
    ntp.ValidCoordinates(hexas_num)

    # Test file creation
    file_name = "valid_coordinates.txt"
    path_to_file = os.path.join(os.getcwd(), file_name)
    assert os.path.exists(path_to_file)

    # Test the hexas checked in the file
    with open(path_to_file, "r") as file:
        lines_in_file = file.read().split("\n")
    
    # assert statement
    assert_hexas_checked = "Hexas checked: " + str(hexas_num)
    assert lines_in_file[0] == assert_hexas_checked
   # Test the content of the file with the input hexasNum as the number of hexas checked
    assert_file_content = ["(2,2)", "(3,4)" , "(4,2)", "(5,7)", "(6,2)", "(7,4)", "(8,3)", "(9,5)", "(10,2)"]
    index = 0
    for line in assert_file_content:
        index += 1
        assert line == lines_in_file[index]

def test_GenerateCombos():
    combos_list_3, maxChainLength_3, invalidStart_3 = ntp.GenerateCombos(3)
    assert np.array_equal(combos_list_3, ['3:  3.0 3.0 3.0 <', '5:  0.0 5.0 5.0 <', '7:  2.0 0.0 7.0 <', '10:  0.0 3.0 10.0 <', 
    '12:  2.0 5.0 1.0 <', '17:  2.0 3.0 6.0 <', '18:  3.0 4.0 7.0 <', '23:  3.0 2.0 1.0 <', '25:  0.0 4.0 3.0 <', 
    '28:  3.0 0.0 6.0 <', '30:  0.0 2.0 8.0 <', '32:  2.0 4.0 10.0 <', '33:  3.0 5.0 0.0 <', '37:  2.0 2.0 4.0 <', 
    '38:  3.0 3.0 5.0 <', '40:  0.0 5.0 7.0 <', '45:  0.0 3.0 1.0 <', '47:  2.0 5.0 3.0 <', '52:  2.0 3.0 8.0 <', 
    '58:  3.0 2.0 3.0 <', '60:  0.0 4.0 5.0 <', '63:  3.0 0.0 8.0 <', '65:  0.0 2.0 10.0 <', '67:  2.0 4.0 1.0 <', 
    '70:  0.0 0.0 4.0 <', '72:  2.0 2.0 6.0 <', '73:  3.0 3.0 7.0 <', '77:  2.0 0.0 0.0 <', '80:  0.0 3.0 3.0 <', 
    '82:  2.0 5.0 5.0 <', '87:  2.0 3.0 10.0 <', '88:  3.0 4.0 0.0 <', '93:  3.0 2.0 5.0 <', '95:  0.0 4.0 7.0 <', 
    '98:  3.0 0.0 10.0 <', '100:  0.0 2.0 1.0 <', '102:  2.0 4.0 3.0 <', '103:  3.0 5.0 4.0 <', '105:  0.0 0.0 6.0 <', 
    '107:  2.0 2.0 8.0 <', '110:  0.0 5.0 0.0 <', '115:  0.0 3.0 5.0 <', '117:  2.0 5.0 7.0 <', '122:  2.0 3.0 1.0 <', 
    '128:  3.0 2.0 7.0 <', '133:  3.0 0.0 1.0 <', '135:  0.0 2.0 3.0 <', '137:  2.0 4.0 5.0 <', '138:  3.0 5.0 6.0 <', 
    '140:  0.0 0.0 8.0 <', '142:  2.0 2.0 10.0 <', '143:  3.0 3.0 0.0 <', '147:  2.0 0.0 4.0 <', '150:  0.0 3.0 7.0 <', 
    '157:  2.0 3.0 3.0 <', '158:  3.0 4.0 4.0 <', '165:  0.0 4.0 0.0 <', '168:  3.0 0.0 3.0 <', '170:  0.0 2.0 5.0 <', 
    '172:  2.0 4.0 7.0 <', '173:  3.0 5.0 8.0 <', '175:  0.0 0.0 10.0 <', '177:  2.0 2.0 1.0 <', '180:  0.0 5.0 4.0 <', 
    '182:  2.0 0.0 6.0 <', '187:  2.0 5.0 0.0 <', '192:  2.0 3.0 5.0 <', '193:  3.0 4.0 6.0 <', '198:  3.0 2.0 0.0 <', 
    '203:  3.0 0.0 5.0 <', '205:  0.0 2.0 7.0 <', '208:  3.0 5.0 10.0 <', '210:  0.0 0.0 1.0 <', '212:  2.0 2.0 3.0 <', 
    '213:  3.0 3.0 4.0 <', '215:  0.0 5.0 6.0 <', '217:  2.0 0.0 8.0 <', '220:  0.0 3.0 0.0 <', '227:  2.0 3.0 7.0 <', 
    '228:  3.0 4.0 8.0 <', '235:  0.0 4.0 4.0 <', '238:  3.0 0.0 7.0 <', '242:  2.0 4.0 0.0 <', '243:  3.0 5.0 1.0 <', 
    '245:  0.0 0.0 3.0 <', '247:  2.0 2.0 5.0 <', '248:  3.0 3.0 6.0 <', '250:  0.0 5.0 8.0 <', '252:  2.0 0.0 10.0 <', 
    '257:  2.0 5.0 4.0 <', '263:  3.0 4.0 10.0 <', '268:  3.0 2.0 4.0 <', '270:  0.0 4.0 6.0 <', '275:  0.0 2.0 0.0 <', 
    '278:  3.0 5.0 3.0 <', '280:  0.0 0.0 5.0 <', '282:  2.0 2.0 7.0 <', '283:  3.0 3.0 8.0 <', '285:  0.0 5.0 10.0 <', 
    '287:  2.0 0.0 1.0 <', '290:  0.0 3.0 4.0 <', '292:  2.0 5.0 6.0 <', '297:  2.0 3.0 0.0 <', '298:  3.0 4.0 1.0 <', 
    '303:  3.0 2.0 6.0 <', '305:  0.0 4.0 8.0 <', '308:  3.0 0.0 0.0 <', '312:  2.0 4.0 4.0 <', '313:  3.0 5.0 5.0 <', 
    '315:  0.0 0.0 7.0 <', '318:  3.0 3.0 10.0 <', '320:  0.0 5.0 1.0 <', '322:  2.0 0.0 3.0 <', '325:  0.0 3.0 6.0 <', 
    '327:  2.0 5.0 8.0 <', '333:  3.0 4.0 3.0 <', '338:  3.0 2.0 8.0 <', '340:  0.0 4.0 10.0 <', '345:  0.0 2.0 4.0 <', 
    '347:  2.0 4.0 6.0 <', '348:  3.0 5.0 7.0 <', '352:  2.0 2.0 0.0 <', '353:  3.0 3.0 1.0 <', '355:  0.0 5.0 3.0 <', 
    '357:  2.0 0.0 5.0 <', '360:  0.0 3.0 8.0 <', '362:  2.0 5.0 10.0 <', '367:  2.0 3.0 4.0 <', '368:  3.0 4.0 5.0 <', 
    '373:  3.0 2.0 10.0 <', '375:  0.0 4.0 1.0 <', '378:  3.0 0.0 4.0 <', '380:  0.0 2.0 6.0 <', '382:  2.0 4.0 8.0 <', 
    '385:  0.0 0.0 0.0 <'])

    assert maxChainLength_3 == 6
    assert invalidStart_3 == 151

def test_ValidNumApproximation():
    valid_list, endPoint, prodApprox, prodTrue, error_percentage = ntp.ValidNumApproximation(3)
    assert np.array_equal(valid_list, ['Valid at 2', 'Valid at 3', 'Valid at 5', 'Valid at 7', 'Valid at 8', 'Valid at 10', 'Valid at 12', 'Valid at 17', 'Valid at 18'])
    assert endPoint == 20
    assert prodApprox == 7.012987012987012
    assert prodTrue == 9.0
    assert error_percentage == 22.077922077922086





