class Bicycle:
    def __init__(self, bike: dict):
        self.idClient = bike.get('idClient')
        self.type = bike.get('type')
        self.serialNumber = bike.get('serialNumber')
        self.brand = bike.get('brand')
        self.model = bike.get('model')
        self.price = bike.get('price')
        self.age = bike.get('age')
        self.isElectric = bike.get('isElectric')
        self.category = bike.get('category')
        self.powerInWatts = bike.get('powerInWatts')
