from sweet import Sweet

class Candie(Sweet):
    def __init__(self, price= 20, sugar= 10):
        super().__init__(self)
        self._price = price
        self._sugar = sugar

    