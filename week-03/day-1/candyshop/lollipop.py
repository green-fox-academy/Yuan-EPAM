from lollipop import Lollipop

class Lollipop(Sweet):
    def __init__(self, price= 10, sugar= 5):
        super().__init__(self)
        self._price = price
        self._sugar = sugar
    
    