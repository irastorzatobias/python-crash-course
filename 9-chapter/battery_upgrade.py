from inheritance import ElectricCar, Battery

tesla = ElectricCar('Tesla', 'Vergamota', 2020, 75)


print(tesla.battery.upgrade_battery())
tesla.get_descriptive_name()
print(tesla.battery.get_range())
print(tesla.battery.describe_battery())