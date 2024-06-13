class MilitaryBase():
    def __init__(self, base_id, row, col, fuel_reserve, missile_reserve, defense, military_value):
        self.base_id= base_id
        self.row = row
        self.col = col
        self.fuel_reserve = fuel_reserve
        self.missile_reserve = missile_reserve
        self.defense = defense
        self.military_value = military_value

    def show_info(self):
        print("Military Base: {}".format(self.base_id))
        print("Position: ({}, {})".format(self.row, self.col))
        print("Fuel Reserve: {}".format(self.fuel_reserve))
        print("Missile Reserve: {}".format(self.missile_reserve))
        print("Defense: {}".format(self.defense))
        print("Military Value: {}".format(self.military_value))
        print()


class Fighter():
    def __init__(self, fid, row, col, max_fuel, max_missile):
        self.fid = fid
        self.row = row
        self.col = col
        self.max_fuel = max_fuel
        self.max_missile = max_missile
        self.fuel = 0  # fuel初始为0
        self.missile = 0  # missile初始为0

    def show_info(self):
        print("Fighter: {}".format(self.fid))
        print("Position: ({}, {})".format(self.row, self.col))
        print("Fuel: {}/{}".format(self.fuel, self.max_fuel))
        print("Missile: {}/{}".format(self.missile, self.max_missile))
        print()


