import microBit
from time import sleep


class Microbit:
    def __init__(self, blockUntilConnect=True, showProgress=True):
        self.uBit = microBit.Microbit()
        print("Trying to connect...")
        if blockUntilConnect:
            while not self.uBit.isConnected():
#                if showProgress:                               <<<< uncomment this to add in details about connection
#                    msg = self.uBit.dequeueStatusMessage()
#                    if len(msg) > 0:
#                        print(msg)
                continue
            self.name = self.uBit.getName()
        if showProgress:
            print("Buttons wired up.")
            print("Magnetometer has detected magnetic field.")
            print("Accelerometer is ready to go.")
            print("Thermometer thermometering.")
            print("Successfully connected")
            print("Houston, I'm ready to run code.")
            print("- - - - - - - - - - - - - - - - - - - - - - - - -")

    def setText(self, text):                    # scrolls the text across the screen
        self.uBit.setText(text)

    def print(self, text):                      # scrolls the text across the screen
        self.uBit.setText(text)

    def getButtonA(self):                       # return 0 if not pressed, 1 if pressed
        return self.uBit.getButtonA()

    def getButtonB(self):                       # return 0 if not pressed, 1 if pressed
        return self.uBit.getButtonB()

    def getButtons(self):                       # returns a list of [button A, button B]
        buttonAState = self.uBit.getButtonA()
        buttonBState = self.uBit.getButtonB()

        return buttonAState, buttonBState

    def waitForButtonA(self):                   # waits for button A to be released, then pressed
        # wait for release first
        while self.uBit.getButtonA() != 0:
            continue
        # pressed
        while self.uBit.getButtonA() == 0:
            continue

    def waitForButtonB(self):                   # waits for button B to be released, then pressed
        # wait for release first
        while self.uBit.getButtonB() != 0:
            continue
        while self.uBit.getButtonB() == 0:
            continue

    def waitForButtonPress(self):               # waits for any button to be released, then pressed
        buttonAState = self.uBit.getButtonA()
        buttonBState = self.uBit.getButtonB()

        while buttonAState == 0 and buttonBState == 0:
            buttonAState = self.uBit.getButtonA()
            buttonBState = self.uBit.getButtonB()

        sleep(0.5)
        return buttonAState, buttonBState

    def getTemperature(self):                   # returns integer of temp reading
        return self.uBit.getTemperature()

    def getBearing(self):                       # returns number between 0 and 360 
        return self.uBit.getBearing()

    def getMagnetometer(self):                  # returns a list of massive neg/pos values (X, Y, Z) --> we need to return value between 0 and 360
        return (self.uBit.getMagnetometerX(), self.uBit.getMagnetometerY(), self.uBit.getMagnetometerZ())

    def getAccelerometer(self):                 # returns acceleration in [X, Y, Z] 
        return [self.uBit.getAccelerometerX(), self.uBit.getAccelerometerY(), self.uBit.getAccelerometerZ()] 

    def getAccelerometerX(self):                # returns acceleration in X 
        return self.uBit.getAccelerometerX() 

    def getAccelerometerY(self):                # returns acceleration in Y 
        return self.uBit.getAccelerometerY()

    def getAccelerometerZ(self):                # returns acceleration in Z 
        return self.uBit.getAccelerometerZ() 

    def startRecordData(self, interval):
        self.uBit.recordData(interval * 1000)
        while not self.uBit.isRecording():
            continue
        return

    def set(self, col, row, value):             # True: turns LED on, False: turns LED off
        self.uBit.updatePixel(4 - row, col, value)
        sleep(0.05)

    def setLED(self, col, row, value):          # True: turns LED on, False: turns LED off
        self.uBit.updatePixel(4 - row, col, value)
        sleep(0.05)

    def clear(self):                            # Turns off LEDs
        self.uBit.clearLED()
        sleep(0.05)

    def fill(self):                             # Turns on all LEDs
        self.uBit.fillLED()
        sleep(0.05)

    def stopRecordData(self):
        return self.uBit.stopRecordData()
    
    def getCompass(self, bearing):
        if bearing > 22 and bearing <= 67:
            facing = "NE"
        elif bearing > 67 and bearing <= 112:
            facing = "E"
        elif bearing > 112 and bearing <= 157:
            facing = "SE"
        elif bearing > 157 and bearing <= 202:
            facing = "S"
        elif bearing > 202 and bearing <= 247:
            facing = "SW"
        elif bearing > 247 and bearing <= 292:
            facing = "W"
        elif bearing > 292 and bearing <= 337:
            facing = "NW"
        elif bearing > 337 and bearing <= 359 or bearing >= 0 and bearing <= 22:
            facing = "NW"
        else:
            facing = "Number out of range 0 to 359"
        return facing