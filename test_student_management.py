import unittest
from student_management import add_student, get_all_students


class TestStudentManagement(unittest.TestCase):

    def test_add_student(self):
        student = add_student(100, "Test")
        self.assertEqual(student["roll_no"], 100)
        self.assertEqual(student["name"], "Test")

    def test_student_in_list(self):
        add_student(101, "Test2")
        self.assertIn({"roll_no": 101, "name": "Test2"}, get_all_students())


if __name__ == "__main__":
    unittest.main()
