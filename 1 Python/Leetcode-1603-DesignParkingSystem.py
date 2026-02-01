class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.L = [big,medium,small] #because this is order in which inputs are given
    def addCar(self, carType: int) -> bool:
        self.L[carType-1] -=1
        return self.L[carType-1]>=0 #whether space is available after allocation

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
