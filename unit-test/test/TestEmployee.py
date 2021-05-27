import unittest
from unittest.mock import patch
from ..app.employee import Employee


class TestEmployee(unittest.TestCase):
    """

    """
    @classmethod
    def setUpClass(cls) -> None:
        print('setup class')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardown class')

    def setUp(self) -> None:
        print('setup')
        self.emp_1 = Employee('Mani', 'Magaji', 10000)
        self.emp_2 = Employee('Teja', 'Mundasad', 20000)

    def tearDown(self) -> None:
        print('teardown')

    def test_email(self):
        print('test_mail')
        self.assertEqual(self.emp_1.email, 'Mani.Magaji@email.com')
        self.assertEqual(self.emp_2.email, 'Teja.Mundasad@email.com')

        self.emp_1.first = 'madhuri'
        self.emp_2.first = 'sanju'

        self.assertEqual(self.emp_1.email, 'madhuri.Magaji@email.com')
        self.assertEqual(self.emp_2.email, 'sanju.Mundasad@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Mani Magaji')
        self.assertEqual(self.emp_2.fullname, 'Teja Mundasad')

        self.emp_1.first = 'madhuri'
        self.emp_2.first = 'sanju'

        self.assertEqual(self.emp_1.fullname, 'madhuri Magaji')
        self.assertEqual(self.emp_2.fullname, 'sanju Mundasad')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 10500)
        self.assertEqual(self.emp_2.pay, 21000)

    def test_monthly_schedule(self):
        with patch('app.employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('company.com/Mani.Magaji@email.com/May')
            self.assertEqual(schedule, 'success')

            mocked_get.return_value.ok = False
            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('company.com/Teja.Mundasad@email.com/June')
            self.assertEqual(schedule, 'Bad Response')


if __name__ == '__main__':
    unittest.main()
