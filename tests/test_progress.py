import unittest
from progress import get_progress, plot_progress
from db_user import create_user, log_workout, log_nutrition, get_user

class TestProgress(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        create_user('Progress Test', 30, 80, 180, 'Gain muscle')
        user = get_user('Progress Test')
        user_id = user[0]
        log_workout(user_id, '2024-08-14', 'Cycling', 60, 'High', 600)
        log_nutrition(user_id, '2024-08-14', 'Lunch', 700, 60, 30, 20)

    def test_get_progress(self):
        user = get_user('Progress Test')
        user_id = user[0]
        workouts, nutrition = get_progress(user_id)
        self.assertTrue(len(workouts) > 0)
        self.assertTrue(len(nutrition) > 0)

    def test_plot_progress(self):
        user = get_user('Progress Test')
        user_id = user[0]
        workouts, nutrition = get_progress(user_id)
        try:
            plot_progress(workouts, nutrition)
            result = True
        except:
            result = False
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()