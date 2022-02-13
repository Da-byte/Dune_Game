
class SpiceHarvester:

    # The spice harvester harvests spice from spice hoards

    def __init__(self, banner, man_power, spice_capacity, speed, armour, attack, position):
        self.banner = banner
        self.man_power = man_power
        self.spice_capacity = spice_capacity
        self.speed = speed
        self.armour = armour
        self.attack = attack
        self.position = position

    def harvest(self, current_energy, hoard_size):
        harvested_spice = hoard_size * 0.2
        hoard_size *= 0.8
        current_energy = current_energy - 5
        return harvested_spice





