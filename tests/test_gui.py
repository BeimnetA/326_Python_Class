import unittest
from tkinter import Tk
from gui import create_gui

class TestGUI(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.gui = create_gui(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_gui_creation(self):
        # Test if the main window is created
        self.assertIsNotNone(self.root)

    def test_widgets_creation(self):
        # Basic test to check if widgets are created
        self.assertTrue(hasattr(self.gui, 'title'))
        self.assertTrue(hasattr(self.gui, 'button_create_user'))
        self.assertTrue(hasattr(self.gui, 'button_log_workout'))
        self.assertTrue(hasattr(self.gui, 'button_log_nutrition'))

if __name__ == '__main__':
    unittest.main()