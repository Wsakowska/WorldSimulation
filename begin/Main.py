from World import World
from Position import Position
from Organisms.Lynx import Lynx
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Antelope import Antelope
import os
import logging

if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    pyWorld = World(10, 10)

    # Dodanie przykładowych organizmów na start
    newOrg = Lynx(position=Position(xPosition=5, yPosition=5), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Grass(position=Position(xPosition=9, yPosition=9), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Grass(position=Position(xPosition=1, yPosition=1), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Sheep(position=Position(xPosition=2, yPosition=2), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    newOrg = Antelope(position=Position(xPosition=7, yPosition=7), world=pyWorld)
    pyWorld.addOrganism(newOrg)

    print(pyWorld)

    while True:
        user_input = input('Press Enter to continue, type "1" to activate plague, type "2" to add organism, or type "3" to exit: ')
        if user_input == '1':
            pyWorld.activatePlague()
        elif user_input == '2':
            org_type = input('Choose organism to add (R: Lynx, S: Sheep, G: Grass, A: Antelope): ')
            x = input('Enter x position: ')
            y = input('Enter y position: ')
            try:
                x = int(x)
                y = int(y)
                if x < 0 or x >= pyWorld.worldX or y < 0 or y >= pyWorld.worldY:
                    raise ValueError("Position out of bounds.")
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue

            if org_type == 'R':
                newOrg = Lynx(position=Position(xPosition=x, yPosition=y), world=pyWorld)
            elif org_type == 'S':
                newOrg = Sheep(position=Position(xPosition=x, yPosition=y), world=pyWorld)
            elif org_type == 'G':
                newOrg = Grass(position=Position(xPosition=x, yPosition=y), world=pyWorld)
            elif org_type == 'A':
                newOrg = Antelope(position=Position(xPosition=x, yPosition=y), world=pyWorld)
            else:
                print("Unknown organism type!")
                continue
            
            if pyWorld.addOrganism(newOrg):
                print("Organism added successfully.")
            else:
                print("Failed to add organism. Position might be occupied or invalid.")
            
            print(pyWorld)  # Wyświetl planszę po dodaniu organizmu
            continue
        elif user_input == '3':
            break

        os.system('clear')
        pyWorld.makeTurn()
        print(pyWorld)