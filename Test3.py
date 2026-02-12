import time
import csv


try:
    import pyvisa
    print("\033[1;32;40mImported pyvisa successfully.\033[0m")
except ModuleNotFoundError:
    print("\033[1;31;40m" + "ERROR: PyVISA python module required for PCTspice calculations.\nPlease install PyVISA to proceed.\n\nUse the terminal command \"py -m pip install -U pyvisa\" to install using the Python package manager." + "\033[0m")
    print("\n\033[1;37;40mPress [ENTER] to close terminal.\033[38;5;0m\033[?25l")
    input()
    print("\033[0m\033[?25h")
    exit()

rm = pyvisa.ResourceManager()
resources = rm.list_resources()
num_devices = len(resources) - 1

print("\033[1;33;40mDevices found:\t" + str(num_devices) + "\033[0m")
for device in resources:
    match device[23:25]:
        case "DS":
            oscope = rm.open_resource(device)
            print("\033[1;33;40mOpened Oscilloscope.\033[0m")
        case "PD":
            supply = rm.open_resource(device)
            print("\033[1;33;40mOpened Power Supply.\033[0m")
        case "DG":
            fungen = rm.open_resource(device)
            print("\033[1;33;40mOpened Function Generator.\033[0m")
        case "DM":
            dmm = rm.open_resource(device)
            print("\033[1;33;40mOpened Multimeter.\033[0m")


supply.write("OUTPut CH1,ON")
time.sleep(2) 
amps = [0.01, 0.1, 1] 
meas_res = []
num_wires = 5 
 
supply.write("CH1:VOLT 1") 
for num in range(num_wires): 
    i = 0 
    for run in range(3): 
        string = "CH1:CURRent " + str(amps[i]) 
        supply.write(string)
        cur = float(supply.query("CH1:CURR?"))
        print(cur)
        time.sleep(1)
        volt = float(dmm.query("MEAS:VOLT:DC?"))
        time.sleep(1)
        print(volt)
        res = volt/cur
        meas_res.append(res)
        i+=1
        time.sleep(120)
    meas_value.append('\n')
    if num < num_wires: 
        print("Wire Done. Set up next wire.\n") 
        input("Press ENTER when next wire is set up.") 
        time.sleep(5) 
    else: 
        print("All wires complete.\n") 
 
supply.write("OUTPut CH1,OFF") 

with open('Gabloff_EET321_Lab3_Test3.txt', 'a') as results:
    results.write('Detected Waveforms:\n')
    for value in meas_value:
        results.write(value)
    results.write('\n\n')