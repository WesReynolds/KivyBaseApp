# Import Kivy dependencies 
from kivy.app import App
from kivy.uix.widget import Widget

# Import custom SwitchingScreen object
from switchingScreen import SwitchingScreen

# Instantiate a global ScreenManager
screenManager = SwitchingScreen.getScreenManager()

# Definition of a Start Screen
class StartScreen(SwitchingScreen):
    def __init__(self, **kw):
        super(StartScreen, self).__init__(**kw) # Inherit __init__ of parent class


# Definition of a Second Screen
class SecondScreen(SwitchingScreen):
    def __init__(self, **kw):
        super(SecondScreen, self).__init__(**kw)    # Inherit __init__ of parent class


# Application class
class MyApp(App):
    def __init__(self):
        super(MyApp, self).__init__() # Inherit __init__ of parent class
        # Define each screen to be used in the application
        self.startScreen = None
        self.secondScreen = None

    # Method used to build the application
    def build(self):
        # Define the screens to be used
        self.startScreen = StartScreen(name="start")    # "name" field is used to identify unique instances of SwithcingScreens
        self.secondScreen = SecondScreen(name="second")

        # Add the used screens to the screen manager
        screenManager.add_widget(self.startScreen)
        screenManager.add_widget(self.secondScreen)

        return screenManager


# Method to initialize the application
def main():
    MyApp().run()

if __name__ == "__main__":
    main()
