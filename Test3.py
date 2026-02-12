import PCT_EET320 as pct
import time

def four_wire(amps):
    pct.supply.write("OUTPut CH1,OFF")
    
    pct.supply.write("CH1:VOLTage 5")
    pct.supply.write(f"CH1:CURR {amps:.2f}")
    
    time.sleep(2)
    pct.supply.write("OUTPut CH1,ON")
    time.sleep(2)
    
    volts = float(pct.dmm.query("MEAS:VOLT:DC?"))
    pct.supply.write("OUTPut CH1,OFF")
    
    resistance = abs(volts/amps)
    
    print(f"\n\nApplied current: {pct.eng_note(amps, 5)}A\nMeasured voltage: {pct.eng_note(volts, 5)}V\nCalculated resistance: {pct.eng_note(resistance, 4)}Ω")
    
    return resistance
    
    
    
    
    
if __name__ == '__main__':
    
    pct.addr_assign()
    current_vals = [.01, .1, 1]
    measure = []
    
    for I in current_vals:
        resistance = four_wire(I)
        measure.append(f"{I:f},{resistance:f}\n")
        
    #Save results to a text file.
    file = open(f'results_amps_{int(time.time()):d}.csv','w')
    file.write("AMPS,OHMS\n")
    for value in measure:
        file.write(value)
    file.close()
    print("Wrote to 'results.csv'")
        
        
