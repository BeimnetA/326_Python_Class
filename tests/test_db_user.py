import unittest
from db_user import create_user, get_user, log_workout, log_nutrition, create_tables
from progress import get_progress

class TestDBUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize the database and create tables
        create_tables()
    
    def test_create_user(self):
        create_user('Test User', 25, 70, 175, 'Lose weight')
        user = get_user('Test User')
        self.assertIsNotNone(user)
        self.assertEqual(user[1], 'Test User')
        self.assertEqual(user[2], 25)
        self.assertEqual(user[3], 70)
        self.assertEqual(user[4], 175)
        self.assertEqual(user[5], 'Lose weight')

    def test_log_workout(self):
        user = get_user('Test User')
        user_id = user[0]
        log_workout(user_id, '2024-08-14', 'Running', 30, 'Moderate', 300)
        workouts, _ = get_progress(user_id)
        self.assertTrue(len(workouts) > 0)

    def test_log_nutrition(self):
        user = get_user('Test User')
        user_id = user[0]
        log_nutrition(user_id, '2024-08-14', 'Breakfast', 500, 50, 20, 15)
        _, nutrition = get_progress(user_id)
        self.assertTrue(len(nutrition) > 0)

if __name__ == '__main__':
    unittest.main()