# Import Kivy dependencies
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition

# Create a gloabl ScreenManager object with desired transitions
screenManager = ScreenManager(transition=NoTransition())

# Custom object to support swithcing between screens
class SwitchingScreen(Screen):

    # Returns the global ScreenManager object used for the application
    @staticmethod
    def getScreenManager():
        return screenManager

    # Switch to another screen using the the SwitchingScreen's "name" field
    @staticmethod
    def switchScreen(screen):
        screenManager.current = screen  # "screen" is the "name" field of the screen
