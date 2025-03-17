import logging
from Position import Position
from Organisms.Plant import Plant
from Action import Action
from ActionEnum import ActionEnum

class World:

    def __init__(self, worldX, worldY):
        self.__worldX = worldX
        self.__worldY = worldY
        self.__turn = 0
        self.__organisms = []
        self.__newOrganisms = []
        self.__separator = '.'
        self.__isPlagueActive = False
        self.__plagueTurns = 0
        logging.debug("World created with size (%d, %d)", worldX, worldY)

    @property
    def worldX(self):
        return self.__worldX

    @property
    def worldY(self):
        return self.__worldY

    @property
    def turn(self):
        return self.__turn

    @turn.setter
    def turn(self, value):
        self.__turn = value

    @property
    def organisms(self):
        return self.__organisms

    @organisms.setter
    def organisms(self, value):
        self.__organisms = value

    @property
    def newOrganisms(self):
        return self.__newOrganisms

    @newOrganisms.setter
    def newOrganisms(self, value):
        self.__newOrganisms = value

    @property
    def separator(self):
        return self.__separator

    @property
    def isPlagueActive(self):
        return self.__isPlagueActive

    def activatePlague(self):
        if not self.__isPlagueActive:
            logging.info("Plague will start in the next turn.")
            self.__plagueTurns = 2  # Plague will last for 2 turns
            self.__isPlagueActive = True

    def handlePlague(self):
        logging.info("Plague active, %d turns remaining", self.__plagueTurns)
        if self.__plagueTurns == 2:
            print("Plague has started.")
            for org in self.__organisms:
                logging.debug("Halving life length for %s at position %s", org.__class__.__name__, org.position)
                org.liveLength = max(1, org.liveLength // 2)

        self.__plagueTurns -= 1
        if self.__plagueTurns == 0:
            self.__isPlagueActive = False
            logging.info("Plague has ended.")
            print("Plague has ended.")

    def makeTurn(self):
        logging.debug(f"Making turn {self.__turn}")

        if self.__isPlagueActive:
            self.handlePlague()

        actions = []
        for org in self.__organisms:
            if self.positionOnBoard(org.position):
                logging.debug("Processing move for %s at position %s", org.__class__.__name__, org.position)
                actions = org.move()
                for a in actions:
                    self.makeMove(a)
                actions = []
                if self.positionOnBoard(org.position):
                    logging.debug("Processing action for %s at position %s", org.__class__.__name__, org.position)
                    actions = org.action()
                    for a in actions:
                        self.makeMove(a)
                    actions = []

        self.__organisms = [o for o in self.__organisms if self.positionOnBoard(o.position)]
        for o in self.__organisms:
            logging.debug("Updating organism %s at position %s", o.__class__.__name__, o.position)
            o.power += 1
            if not self.__isPlagueActive or self.__plagueTurns != 1:
                o.liveLength -= 1
            if o.liveLength < 1:
                logging.info("%s died of old age at %s", o.__class__.__name__, o.position)
        self.__organisms = [o for o in self.__organisms if o.liveLength > 0]

        self.__newOrganisms = [o for o in self.__newOrganisms if self.positionOnBoard(o.position)]
        self.__organisms.extend(self.__newOrganisms)
        self.__organisms.sort(key=lambda o: o.initiative, reverse=True)
        self.__newOrganisms = []

        self.__turn += 1
        logging.debug(f"Turn {self.__turn} completed")

    def makeMove(self, action):
        logging.debug("Making move: %s", action)
        if action.action == ActionEnum.A_ADD:
            action.organism.world = self  # Upewnij się, że world jest ustawiane
            self.__newOrganisms.append(action.organism)
            logging.debug("Added organism %s at position %s", action.organism.__class__.__name__, action.position)
        elif action.action == ActionEnum.A_INCREASEPOWER:
            action.organism.power += action.value
            logging.debug("Increased power of %s by %d", action.organism.__class__.__name__, action.value)
        elif action.action == ActionEnum.A_MOVE:
            action.organism.position = action.position
            logging.debug("Moved %s to position %s", action.organism.__class__.__name__, action.position)
        elif action.action == ActionEnum.A_REMOVE:
            action.organism.position = Position(xPosition=-1, yPosition=-1)
            logging.debug("Removed %s from position %s", action.organism.__class__.__name__, action.position)

    def addOrganism(self, newOrganism):
        newOrgPosition = Position(xPosition=newOrganism.position.x, yPosition=newOrganism.position.y)
        logging.debug("Trying to add organism %s at position %s", newOrganism.__class__.__name__, newOrgPosition)

        if self.positionOnBoard(newOrgPosition):
            logging.debug("Adding organism: %s at position %s", newOrganism.__class__.__name__, newOrgPosition)
            newOrganism.world = self  # Upewnij się, że world jest ustawiane
            self.__organisms.append(newOrganism)
            self.__organisms.sort(key=lambda org: org.initiative, reverse=True)
            return True
        logging.warning("Failed to add organism: %s at position %s", newOrganism.__class__.__name__, newOrgPosition)
        return False

    def positionOnBoard(self, position):
        result = position.x >= 0 and position.y >= 0 and position.x < self.worldX and position.y < self.worldY
        logging.debug("Position %s on board: %s", position, result)
        return result

    def getOrganismFromPosition(self, position):
        logging.debug("Getting organism from position %s", position)
        pomOrganism = None

        for org in self.__organisms:
            if org.position == position:
                pomOrganism = org
                break
        if pomOrganism is None:
            for org in self.__newOrganisms:
                if org.position == position:
                    pomOrganism = org
                    break
        logging.debug("Organism at position %s: %s", position, pomOrganism.__class__.__name__ if pomOrganism else None)
        return pomOrganism

    def getNeighboringPositions(self, position):
        logging.debug("Getting neighboring positions for %s", position)
        result = []
        pomPosition = None

        for y in range(-1, 2):
            for x in range(-1, 2):
                pomPosition = Position(xPosition=position.x + x, yPosition=position.y + y)
                if self.positionOnBoard(pomPosition) and not (y == 0 and x == 0):
                    result.append(pomPosition)
        logging.debug("Neighboring positions for %s: %s", position, result)
        return result

    def filterFreePositions(self, fields):
        logging.debug("Filtering free positions from %s", fields)
        result = []

        for field in fields:
            if self.getOrganismFromPosition(field) is None:
                result.append(field)
        logging.debug("Free positions: %s", result)
        return result

    def filterPositionsWithoutAnimals(self, fields):
        logging.debug("Filtering positions without animals from %s", fields)
        result = []
        pomOrg = None

        for field in fields:
            pomOrg = self.getOrganismFromPosition(field)
            if pomOrg is None or isinstance(pomOrg, Plant):
                result.append(field)
        logging.debug("Positions without animals: %s", result)
        return result

    def find_nearby(self, position, sign):
        logging.debug("Finding nearby %s from position %s", sign, position)
        for y in range(self.worldY):
            for x in range(self.worldX):
                org = self.getOrganismFromPosition(Position(xPosition=x, yPosition=y))
                if org and org.sign == sign:
                    logging.debug("Found %s at %s", sign, Position(xPosition=x, yPosition=y))
                    return Position(xPosition=x, yPosition=y)
        logging.debug("No nearby %s found", sign)
        return None

    def __str__(self):
        result = '\nturn: ' + str(self.__turn) + '\n'
        for wY in range(0, self.worldY):
            for wX in range(0, self.worldX):
                org = self.getOrganismFromPosition(Position(xPosition=wX, yPosition=wY))
                if org:
                    result += str(org.sign)
                else:
                    result += self.separator
            result += '\n'
        return result
