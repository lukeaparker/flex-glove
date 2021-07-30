import time
import board
from analogio import AnalogIn

class Hand():

    def __init__(self):
        self.pinkie_finger = {
            'pin': AnalogIn(board.A0),
            'vmin': 0.42,
            'vmax': 0.73,
            'dmin': 0,
            'dmax': 180,
        }
        self.index_finger = {
            'pin': AnalogIn(board.A1),
            'vmin': 0.7,
            'vmax': 1.3,
            'dmin': 0,
            'dmax': 180,
        }
        self.middle_finger = {
            'pin': AnalogIn(board.A2),
            'vmin': 0.82,
            'vmax': 1.3,
            'dmin': 0,
            'dmax': 180,
        }
        self.pointer_finger = {
            'pin': AnalogIn(board.A3),
            'vmin': 1,
            'vmax': 1.3,
            'dmin': 0,
            'dmax': 180,
        }
        self.thumb_finger = {
            'pin': AnalogIn(board.A4),
            'vmin': 0.45,
            'vmax': 0.75,
            'dmin': 0,
            'dmax': 180,
        }
    
    def get_voltage(self, pin):
        return (pin.value * 3.3) / 65536
    
    def get_angle(self, finger):
        angle = ( (hand.get_voltage(finger['pin']) - finger['vmin']) / (finger['vmax'] - finger['vmin']) ) * (finger['dmax'] - finger['dmin']) + finger['dmin']
        if angle > 180:
            angle = 180
        elif angle < 0:
            angle = 0
        return angle
    
    def read(self): 
        while True:
            print(f'pinkie: {hand.get_angle(hand.pinkie_finger)} | index: {hand.get_angle(hand.index_finger)} | middle: {hand.get_angle(hand.middle_finger)} | pointer: {hand.get_angle(hand.pointer_finger)} | thumb: {hand.get_angle(hand.thumb_finger)}')

hand = Hand()
hand.read()



# pinkie_finger = AnalogIn(board.A0)
# index_finger = AnalogIn(board.A1)
# middle_finger = AnalogIn(board.A2)
# pointer_finger = AnalogIn(board.A3)
# thumb = AnalogIn(board.A4)

# def get_voltage(pin):
#     return (pin.value * 3.3) / 65536

# def get_pinkie_angle():
#     voltage = get_voltage(pinkie_finger)
#     vmin = 0.42
#     vmax = 0.73
#     dmin = 0
#     dmax = 180
#     angle = ( (voltage - vmin) / (vmax - vmin) ) * (dmax - dmin) + dmin
#     if angle > 180:
#         angle = 180
#     elif angle < 0:
#         angle = 0
#     return angle

# def get_index_angle():
#     voltage = get_voltage(index_finger)
#     vmin = 0.7
#     vmax = 1.3
#     dmin = 0
#     dmax = 180
#     angle = ( (voltage - vmin) / (vmax - vmin) ) * (dmax - dmin) + dmin
#     if angle > 180:
#         angle = 180
#     elif angle < 0:
#         angle = 0
#     return angle

# def get_middle_angle():
#     voltage = get_voltage(middle_finger)
#     vmin = 0.82
#     vmax = 1.3
#     dmin = 0
#     dmax = 180
#     angle = ( (voltage - vmin) / (vmax - vmin) ) * (dmax - dmin) + dmin
#     if angle > 180:
#         angle = 180
#     elif angle < 0:
#         angle = 0
#     return angle

# def get_pointer_angle():
#     voltage = get_voltage(pointer_finger)
#     vmin = 1
#     vmax = 1.3
#     dmin = 0
#     dmax = 180
#     angle = ( (voltage - vmin) / (vmax - vmin) ) * (dmax - dmin) + dmin
#     if angle > 180:
#         angle = 180
#     elif angle < 0:
#         angle = 0
#     return angle

# def get_thumb_angle():
#     voltage = get_voltage(thumb)
#     vmin = 0.45
#     vmax = 0.75
#     dmin = 0
#     dmax = 180
#     angle = ( (voltage - vmin) / (vmax - vmin) ) * (dmax - dmin) + dmin
#     if angle > 180:
#         angle = 180
#     elif angle < 0:
#         angle = 0
#     return angle


# while True:
#     # get_thumb_angle()
#     print(f'pinkie: {get_pinkie_angle()} | index: {get_index_angle()} | middle: {get_middle_angle()} | pointer {get_pointer_angle()} | thumb: {get_thumb_angle()}')
