def move(kilometres, direction, current_position, current_energy):
    current_position[direction] += kilometres
    current_energy -= kilometres * 0.5


def recharge(current_energy, energy_to_charge, spice_wealth, price):
    current_energy += energy_to_charge
    spice_wealth -= price


def return_to_base(current_positon, current_energy):
    kilometres_to_travel = 0
    for km in current_positon:
        kilometres_to_travel += km

    if current_energy - kilometres_to_travel < 0:
        print("There is not enough energy to return by land. Consider sending an helicopter")


