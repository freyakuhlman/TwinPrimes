import os
os.environ['NUMBA_DISABLE_JIT'] = "1"
os.environ["NUMBA_ENABLE_CUDASIM"] = "1"
import TwinPrimesNumba as tpn
import numpy as np


def test_InitializeArraysNumba():
    size = 100
    hexasArray, sextandsArray, squareSextandsArray = tpn.InitializeArraysNumba(size)
    assert len(hexasArray) == size
    assert len(sextandsArray) == size
    assert len(squareSextandsArray) == size
    
    
def test_GenerateHexasNumba():
    hexas_array, sextands_array, square_sextands_array = tpn.GenerateHexasNumba(25)
        
    assert np.array_equal(hexas_array, [5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49, 53, 55, 59, 61, 65, 67, 71, 73, 77])
    assert np.array_equal(sextands_array, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13])
    assert np.array_equal(square_sextands_array, [4, 8, 20, 28, 48, 60, 88, 104, 140, 160, 204, 228, 280, 308, 368, 400, 468, 504, 580, 620, 704, 748, 840, 888, 988])

def test_FindInvalidChainsNumba():
    max_chain, max_length, critical_zone = tpn.FindInvalidChainsNumba(3)
    assert max_chain == 13
    assert max_length == 4
    assert critical_zone == 12.0

def test_GenerateComboNumba():
    combo = tpn.GenerateComboNumba(2, 2)
    assert combo == '2 2 < '

def test_ViewComboNumba():
    combo_array1 = tpn.ViewComboNumba(3, 3, 3)
    combo_array2 = tpn.ViewComboNumba(3, 4, 5)
    combo_array3 = tpn.ViewComboNumba(3, 6, 10)
    assert np.array_equal(combo_array1, ['3: 3 3 3 < ', '4: 4 4 4 ', '5: 0 5 5 < '])
    assert np.array_equal(combo_array2, ['4: 4 4 4 ', '5: 0 5 5 < ', '6: 1 6 6 ', '7: 2 0 7 < ', '8: 3 1 8 '])
    assert np.array_equal(combo_array2, ['4: 4 4 4 ', '5: 0 5 5 < ', '6: 1 6 6 ', '7: 2 0 7 < ', '8: 3 1 8 '])
    assert np.array_equal(combo_array3, ['6: 1 6 6 ', '7: 2 0 7 < ', '8: 3 1 8 ', '9: 4 2 9 ',
       '10: 0 3 10 ', '11: 1 4 0 ', '12: 2 5 1 ', '13: 3 6 2 ',
       '14: 4 0 3 ', '15: 0 1 4 '])

def test_ViewCritCombosNumba():
    crit_combo1 = tpn.ViewCritCombosNumba(4)
    assert np.array_equal(crit_combo1, ['1: 1 1 1 1 ', '2: 2 2 2 2 < ', '3: 3 3 3 3 < ', '4: 4 4 4 4 ',
       '5: 0 5 5 5 < ', '6: 1 6 6 6 ', '7: 2 0 7 7 < ', '8: 3 1 8 8 ',
       '9: 4 2 9 9 ', '10: 0 3 10 10 ', '11: 1 4 0 11 ', '12: 2 5 1 12 ',
       '13: 3 6 2 0 ', '14: 4 0 3 1 ', '15: 0 1 4 2 ', '16: 1 2 5 3 ',
       '17: 2 3 6 4 < ', '18: 3 4 7 5 < ', '19: 4 5 8 6 ', '20: 0 6 9 7 ',
       '21: 1 0 10 8 ', '22: 2 1 0 9 ', '23: 3 2 1 10 ', '24: 4 3 2 11 ',
       '25: 0 4 3 12 ', '26: 1 5 4 0 ', '27: 2 6 5 1 ', '28: 3 0 6 2 < '])
           
def test_FindAverageGapNumba():
    tpn.GenerateHexasNumba(25)
    assert tpn.FindAverageGapNumba(2) == (35.0, 15.0, 2.3333333333333335)
    assert tpn.FindAverageGapNumba(5) == (85085.0, 22275.0,  3.819753086419753)
    assert tpn.FindAverageGapNumba(25) == (8.011810311763933e+37, 7.650888424384966e+36, 10.47173853199667)

def test_ValidCoordinatesNumba():
    combos_list_4= tpn.ValidCoordinatesNumba(4)
    combos_list_12 = tpn.ValidCoordinatesNumba(12)
    combos_list_9 = tpn.ValidCoordinatesNumba(9)
    assert np.array_equal(combos_list_4, ['2,2', '3,4', '4,2'])
    assert np.array_equal(combos_list_12, ['2,2', '3,4', '4,2', '5,7', '6,2', '7,4', '8,3', '9,5', '10,2', '11,6', '12,5'])
    assert np.array_equal(combos_list_9, ['2,2', '3,4', '4,2', '5,7', '6,2', '7,4', '8,3', '9,5'] )

def test_WriteValidCoordinatesNumba():
    # Run ValidateCoordinates with hexasNum = 10
    hexas_num = 10
    tpn.ValidCoordinatesNumba(hexas_num)

    # Test file creation
    file_name = "valid_coordinates.txt"
    path_to_file = os.path.join(os.getcwd(), file_name)
    assert os.path.exists(path_to_file)

    # Test the hexas checked in the file
    with open(path_to_file, "r") as file:
        lines_in_file = file.read().split("\n")
    
    # assert statement
    assert_hexas_checked = "Hexas Checked = " + str(hexas_num)
    assert lines_in_file[0] == assert_hexas_checked
   # Test the content of the file with the input hexasNum as the number of hexas checked
    assert_file_content = ["2,2", "3,4" , "4,2", "5,7", "6,2", "7,4", "8,3", "9,5", "10,2"]
    index = 0
    for line in assert_file_content:
        index += 1
        assert line == lines_in_file[index]

def test_GenerateCombosNumba():
    combos_list_3, maxChainLength_3, invalidStart_3 = tpn.GenerateCombosNumba(3)
    assert np.array_equal(combos_list_3, ['3:  3.0 3.0 3.0 <', '5:  0.0 5.0 5.0 <', '7:  2.0 0.0 7.0 <', '10:  0.0 3.0 10.0 <', '12:  2.0 5.0 1.0 <', 
    '17:  2.0 3.0 6.0 <', '18:  3.0 4.0 7.0 <', '23:  3.0 2.0 1.0 <', '25:  0.0 4.0 3.0 <', '28:  3.0 0.0 6.0 <', '30:  0.0 2.0 8.0 <', 
    '32:  2.0 4.0 10.0 <', '33:  3.0 5.0 0.0 <', '37:  2.0 2.0 4.0 <', '38:  3.0 3.0 5.0 <', '40:  0.0 5.0 7.0 <', '45:  0.0 3.0 1.0 <', 
    '47:  2.0 5.0 3.0 <', '52:  2.0 3.0 8.0 <', '58:  3.0 2.0 3.0 <', '60:  0.0 4.0 5.0 <', '63:  3.0 0.0 8.0 <', '65:  0.0 2.0 10.0 <', 
    '67:  2.0 4.0 1.0 <', '70:  0.0 0.0 4.0 <', '72:  2.0 2.0 6.0 <', '73:  3.0 3.0 7.0 <', '77:  2.0 0.0 0.0 <', '80:  0.0 3.0 3.0 <', 
    '82:  2.0 5.0 5.0 <', '87:  2.0 3.0 10.0 <', '88:  3.0 4.0 0.0 <', '93:  3.0 2.0 5.0 <', '95:  0.0 4.0 7.0 <', '98:  3.0 0.0 10.0 <', 
    '100:  0.0 2.0 1.0 <', '102:  2.0 4.0 3.0 <', '103:  3.0 5.0 4.0 <', '105:  0.0 0.0 6.0 <', '107:  2.0 2.0 8.0 <', '110:  0.0 5.0 0.0 <', 
    '115:  0.0 3.0 5.0 <', '117:  2.0 5.0 7.0 <', '122:  2.0 3.0 1.0 <', '128:  3.0 2.0 7.0 <', '133:  3.0 0.0 1.0 <', '135:  0.0 2.0 3.0 <', 
    '137:  2.0 4.0 5.0 <', '138:  3.0 5.0 6.0 <', '140:  0.0 0.0 8.0 <', '142:  2.0 2.0 10.0 <', '143:  3.0 3.0 0.0 <', '147:  2.0 0.0 4.0 <', 
    '150:  0.0 3.0 7.0 <', '157:  2.0 3.0 3.0 <', '158:  3.0 4.0 4.0 <', '165:  0.0 4.0 0.0 <', '168:  3.0 0.0 3.0 <', '170:  0.0 2.0 5.0 <', 
    '172:  2.0 4.0 7.0 <', '173:  3.0 5.0 8.0 <', '175:  0.0 0.0 10.0 <', '177:  2.0 2.0 1.0 <', '180:  0.0 5.0 4.0 <', '182:  2.0 0.0 6.0 <', 
    '187:  2.0 5.0 0.0 <', '192:  2.0 3.0 5.0 <', '193:  3.0 4.0 6.0 <', '198:  3.0 2.0 0.0 <', '203:  3.0 0.0 5.0 <', '205:  0.0 2.0 7.0 <', 
    '208:  3.0 5.0 10.0 <', '210:  0.0 0.0 1.0 <', '212:  2.0 2.0 3.0 <', '213:  3.0 3.0 4.0 <', '215:  0.0 5.0 6.0 <', '217:  2.0 0.0 8.0 <',
     '220:  0.0 3.0 0.0 <', '227:  2.0 3.0 7.0 <', '228:  3.0 4.0 8.0 <', '235:  0.0 4.0 4.0 <', '238:  3.0 0.0 7.0 <', '242:  2.0 4.0 0.0 <', 
     '243:  3.0 5.0 1.0 <', '245:  0.0 0.0 3.0 <', '247:  2.0 2.0 5.0 <', '248:  3.0 3.0 6.0 <', '250:  0.0 5.0 8.0 <', '252:  2.0 0.0 10.0 <', 
     '257:  2.0 5.0 4.0 <', '263:  3.0 4.0 10.0 <', '268:  3.0 2.0 4.0 <', '270:  0.0 4.0 6.0 <', '275:  0.0 2.0 0.0 <', '278:  3.0 5.0 3.0 <', 
     '280:  0.0 0.0 5.0 <', '282:  2.0 2.0 7.0 <', '283:  3.0 3.0 8.0 <', '285:  0.0 5.0 10.0 <', '287:  2.0 0.0 1.0 <', '290:  0.0 3.0 4.0 <', 
     '292:  2.0 5.0 6.0 <', '297:  2.0 3.0 0.0 <', '298:  3.0 4.0 1.0 <', '303:  3.0 2.0 6.0 <', '305:  0.0 4.0 8.0 <', '308:  3.0 0.0 0.0 <', 
     '312:  2.0 4.0 4.0 <', '313:  3.0 5.0 5.0 <', '315:  0.0 0.0 7.0 <', '318:  3.0 3.0 10.0 <', '320:  0.0 5.0 1.0 <', '322:  2.0 0.0 3.0 <', 
     '325:  0.0 3.0 6.0 <', '327:  2.0 5.0 8.0 <', '333:  3.0 4.0 3.0 <', '338:  3.0 2.0 8.0 <', '340:  0.0 4.0 10.0 <', '345:  0.0 2.0 4.0 <', 
     '347:  2.0 4.0 6.0 <', '348:  3.0 5.0 7.0 <', '352:  2.0 2.0 0.0 <', '353:  3.0 3.0 1.0 <', '355:  0.0 5.0 3.0 <', '357:  2.0 0.0 5.0 <', 
     '360:  0.0 3.0 8.0 <', '362:  2.0 5.0 10.0 <', '367:  2.0 3.0 4.0 <', '368:  3.0 4.0 5.0 <', '373:  3.0 2.0 10.0 <', '375:  0.0 4.0 1.0 <', 
     '378:  3.0 0.0 4.0 <', '380:  0.0 2.0 6.0 <', '382:  2.0 4.0 8.0 <', '385:  0.0 0.0 0.0 <'])

    assert maxChainLength_3 == 6
    assert invalidStart_3 == 151

def test_ValidNumApproximationNumba():
    validList, endPoint, prodApprox, prodTrue, errorPercentage = tpn.ValidNumApproximationNumba(1)
    assert np.array_equal(validList, ['Valid at 0', 'Valid at 1', 'Valid at 2', 'Valid at 3'])
    assert endPoint == 4
    assert prodApprox == 2.4
    assert prodTrue == 4.0
    assert errorPercentage == 40.0






