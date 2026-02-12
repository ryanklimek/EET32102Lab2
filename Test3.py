import pyvisa


supply.write("OUTPut CH1,ON")
time.sleep(2) 
amps = [0.01, 0.1, 1] 
meas_value = [] 
num_wires = 5 
 
supply.write("CH1:VOLT 1") 
for num in range(num_wires): 
    i = 0 
    for run in range(3): 
        string = "CH1:CURRent " + str(amps[i]) 
        supply.write(string) 
        value = dmm.query("MEAS:VOLT:DC?") 
        meas_value.append(value) 
        i +=1 
        time.sleep(120) 
    if num < num_wires: 
        print("Wire Done. Set up next wire.\n") 
        input("Press ENTER when next wire is set up.") 
        time.sleep(5) 
    else: 
        print("All wires complete.\n") 
 
supply.write("OUTPut CH1,OFF") 
