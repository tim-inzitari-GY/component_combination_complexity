# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from Plant import Plant

def main():
    myPlants = {}
    myPlants['Lawton'] = Plant(18000000, 'Lawton')
    myPlants['Chile'] = Plant(7000000, "Chile")
    myPlants['Fayetteville'] = Plant(7000000, "Fayetteville")
    myPlants['Napanee'] = Plant(7000000, "Napanee")
    myPlants['SLP'] = Plant(7000000, "SLP")

    print(myPlants)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
