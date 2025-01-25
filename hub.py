import math

class Hub:
    
    def __init__(self, LFO, RFO, OLD, DL, DR, SHD, OSB):
        # LFO = left flange offset. Distance from the lock nut 
        #     to the centre of the left flange.
        # RFO = right flange offset. Distance from the lock nut 
        #     to the centre of the right flange.
        # OLD = measurement from lock nut to lock nut
        # DL = spoke circle diameter non-drive side
        # DR = spoke circle diameter drive side
        # SHD = spoke hole diameter. The diameter of the spoke hole in the flange. 
        #     Normally in that range of 2mm to 2.5mm.
        # OSB = The distance from the centre of the spoke hole to the centre of the rim. 

        self.LFO = LFO
        self.RFO = RFO
        self.OLD = OLD
        self.DL = DL
        self.DR = DR
        self.SHD = SHD
        self.OSB = OSB

    def __repr__(self):
        
        return f"Hub({self.LFO}, {self.RFO}, {self.OLD}, {self.DL}, {self.DR}, {self.SHD})"

class Rim:
    
    def __init__(self, ERD, num_spokes, num_crosses):
        self.ERD = ERD
        self.num_spokes = num_spokes
        self.num_crosses = num_crosses

    def __repr__(self):
        
        return f"Wheel({self.ERD}, {self.num_crosses}, {self.num_crosses})"


class Calculator:

    def __init__(self, hub, rim):
        self.hub = hub
        self.rim = rim

    def make_calc(self):

        R = self.rim.ERD / 2
        LH = self.hub.DL / 2
        LF = self.hub.LFO
        R = self.rim.ERD / 2
        RH = self.hub.DR / 2
        RF = self.hub.RFO
        h = self.rim.num_spokes

        ML = 2 * R * LH * math.cos((4 * math.pi * self.rim.num_crosses) / h )
        left_length = round((math.sqrt(R**2 + LH**2 + LF**2 - ML)) - self.hub.SHD / 2, 1)
        
        MR = 2 * R * RH * math.cos((4 * math.pi * self.rim.num_crosses) / h )
        right_length = round((math.sqrt(R**2 + RH**2 + RF**2 - MR)) - self.hub.SHD / 2, 1)

        return {'right':right_length, 'left':left_length}


            
        




