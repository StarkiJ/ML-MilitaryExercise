class MilitaryBase():
    def __init__(self, bnum, row, col, fuel_reserve, missile_reserve, defense, military_value):
        self.bnum = bnum
        self.row = row
        self.col = col
        self.fuel_reserve = fuel_reserve
        self.missile_reserve = missile_reserve
        self.defense = defense
        self.military_value = military_value

    def show_info(self):
        print("Military Base: {}".format(self.bnum))
        print("Position: ({}, {})".format(self.row, self.col))
        print("Fuel Reserve: {}".format(self.fuel_reserve))
        print("Missile Reserve: {}".format(self.missile_reserve))
        print("Defense: {}".format(self.defense))
        print("Military Value: {}".format(self.military_value))
        print()


class Fighter():
    def __init__(self, fnum, row, col, max_fuel, max_missile):
        self.fnum = fnum
        self.row = row
        self.col = col
        self.max_fuel = max_fuel
        self.max_missile = max_missile
        self.fuel = max_fuel
        self.missile = max_missile

    def show_info(self):
        print("Fighter: {}".format(self.fnum))
        print("Position: ({}, {})".format(self.row, self.col))
        print("Fuel: {}/{}".format(self.fuel, self.max_fuel))
        print("Missile: {}/{}".format(self.missile, self.max_missile))
        print()
