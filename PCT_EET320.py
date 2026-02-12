'''
MIT License

Copyright (c) 2026 Jacob Smithmyer, Pennsylvania College of Technology

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sys 
import subprocess

global oscope
global supply
global fungen
global dmm


def addr_assign():  # Automatically locates and assigns addresses for benchtop equipment.
    
    # IMPORT PACKAGE
    try:
        import pyvisa
        print("\033[1;32;40mImported pyvisa successfully.\033[0m")
    except ModuleNotFoundError:
        print("\033[1;31;40mERROR: PyVISA module not installed.\033[0m")
        ans = input("\033[1;33;40mWould you like to install the PyVISA module? (Y/N)\n> \033[0m")
    
        match ans.upper():
            case 'Y':
                subprocess.check_call([sys.executable, "-m", "pip", "install", "pyvisa"])
                import pyvisa
                print("\033[1;32;40mImported pyvisa successfully.\033[0m")
            case _:
                print("\033[1;31;40m\nPlease install PyVISA to proceed.\n\nUse the terminal command \"py -m pip install -U pyvisa\" to install using the Python package manager.\033[0m") 
                input("\n\033[1;37;40mPress [ENTER] to close terminal.\033[38;5;0m\033[?25l")
                print("\033[0m\033[?25h")
                sys.exit(1)
                
    rm = pyvisa.ResourceManager()
    resources = rm.list_resources()
    num_devices = len(resources) - 1
    print("\033[1;33;40mDevices found:\t" + str(num_devices) + "\033[0m")
    for device in resources:
        match device[23:25]:
            case "DS":
                global oscope 
                oscope = rm.open_resource(device)
                print("\033[1;33;40mOpened Oscilloscope.\033[0m")
            case "PD":
                global supply 
                supply = rm.open_resource(device)
                print("\033[1;33;40mOpened Power Supply.\033[0m")
            case "DG":
                global fungen 
                fungen = rm.open_resource(device)
                print("\033[1;33;40mOpened Function Generator.\033[0m")
            case "DM":
                global dmm 
                dmm = rm.open_resource(device)
                print("\033[1;33;40mOpened Multimeter.\033[0m")
                
               
               
def eng_note(inputValue, numSigFigs =0):    # Formats value in engineering notation to be displayed in a terminal.
    exponent = 0
    newVal = float(inputValue)
    while (abs(newVal) >= 1000) and exponent <= 24:
        exponent += 3
        newVal = float(inputValue) / 10**exponent
    while (abs(newVal) < 1.0 )  and exponent >= -24:
        exponent -= 3
        newVal = float(inputValue) / 10**exponent
     
    if numSigFigs == 0:
        returnVal = str(newVal)
    else:
        if abs(newVal) < 10:
            numsAfterDecimal = numSigFigs - 1
        elif abs(newVal) < 100:
            numsAfterDecimal = numSigFigs - 2
        else:
            numsAfterDecimal = numSigFigs - 3
            
        formatStr = '{: ' + str(numSigFigs) + '.' + str(numsAfterDecimal) + 'f}'
        returnVal = formatStr.format(newVal)

    if abs(exponent) > 24:
        if numSigFigs == 0:
            returnVal = '{:e}'.format(float(inputValue))
        else:
            formatStr = '{: ' + str(numSigFigs) + '.' + str(numSigFigs-1) + 'e}'
            returnVal = formatStr.format(float(inputValue))
    
    match exponent:
        case 24:
            returnVal += 'Y'
        case 21:
            returnVal += 'Z'
        case 18:
            returnVal += 'E'
        case 15:
            returnVal += 'P'
        case 12: 
            returnVal += 'T'
        case 9: 
            returnVal += 'G'
        case 6: 
            returnVal += 'M'
        case 3:
            returnVal += 'k'
        case -3:
            returnVal += 'm'
        case -6:
            returnVal += 'u'
        case -9:
            returnVal += 'n'
        case -12:
            returnVal += 'p'
        case -15:
            returnVal += 'f'
        case -18:
            returnVal += 'a'
        case -21:
            returnVal += 'z'
        case -24:
            returnVal += 'y'
        case _:
            returnVal += ' '
            
    return returnVal
    



