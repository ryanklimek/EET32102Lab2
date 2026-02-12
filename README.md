EET32102Lab2

Objective:
The objective of this lab is to compare methods for accurately measuring small resistances below 1 Ohm using a Siglent SDM3055 digital multimeter (DMM). You will test various measurement techniques and analyze the results to determine the most accurate method.

Equipment:
- Siglent SDM3055 digital multimeter 
- 5 lengths of 12-inch 22 AWG wire
- Banana plug to alligator clip leads
- Optional: Siglent SPD3303X-E DC power supply for alternate 4-wire method

Alternate 4-Wire Method
- Use an external DC power supply instead of the DMM's internal source
- Force different test currents (10 mA, 100 mA, 1A) and measure voltage drop to calculate resistance per Ohm's Law
- Allow wires to settle for 2 minutes between tests as temperature may increase resistance
- Create a Python script to automatically set the test current from the power supply, make the voltage drop measurement with the DMM, and calculate the resistance.  Have the script write these values to a spreadsheet or database. The program should include the 2 minute wait time between each current setting and measurement.
