from hub import Hub, Rim, Calculator

hub = Hub(LFO = 30, RFO = 16.99, OLD = 100, DL = 57, DR = 57, SHD = 2.6, OSB = 0)
rim = Rim(ERD = 599, num_spokes = 32, num_crosses = 3)

calculator = Calculator(hub, rim)
print(calculator.make_calc())
