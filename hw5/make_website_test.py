import unittest
import os

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    def test_surround_block(self):
        # test text with surrounding h1 tags
        self.assertEqual("<h1>Eagles</h1>", surround_block('h1', 'Eagles'))

        # test text with surrounding h2 tags
        self.assertEqual("<h2>Red Sox</h2>", surround_block('h2', 'Red Sox'))

        # test text with surrounding p tags
        self.assertEqual('<p>Lorem ipsum dolor sit amet, consectetur ' +
                         'adipiscing elit. Sed ac felis sit amet ante porta ' +
                         'hendrerit at at urna.</p>',
                         surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna.'))

    def test_create_email_link(self):

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>',
            create_email_link('lbrandon@wharton.upenn.edu')
        )

        # test email with @ sign
        self.assertEqual(
            '<a href="mailto:krakowsky@outlook.com">krakowsky[aT]outlook.com</a>',
            create_email_link('krakowsky@outlook.com')
        )

        # test email without @ sign
        self.assertEqual(
            '<a href="mailto:lbrandon.at.seas.upenn.edu">lbrandon.at.seas.upenn.edu</a>',
            create_email_link('lbrandon.at.seas.upenn.edu')
        )
    def test_read_file(self):
        # Test reading a valid file
        content = "Sample content of the file."
        file_path = "test_file.txt"
        with open(file_path, "w") as test_file:
            test_file.write(content)
        self.assertEqual(read_file(file_path), [content])
        os.remove(file_path)  # Clean up

    def test_get_name(self):
        # Test a valid name
        valid_name = "Haitham Fawzi"
        valid_resume = [valid_name, "projects: RISC-V, FPGA", "courses: Deep Learning, Economics, Business", "stuff"]
        self.assertEqual(get_name(valid_resume), valid_name)

        # Test an invalid name (lower case)
        invalid_name_resume = ["haitham Fawzi", "Other content"]
        self.assertEqual(get_name(invalid_name_resume), "Invalid Name")

        # Test leading and trailing whitespaces
        invalid_name_resume = ["  Haitham fawzi  ", "Other content"]
        self.assertEqual(get_name(invalid_name_resume), "Haitham fawzi")


    def test_get_email(self):
        # Test a valid email
        valid_email = "hsamir@upenn.edu"
        valid_resume = ["Other content", valid_email, "More content"]
        self.assertEqual(get_email(valid_resume), valid_email)

         # Test a valid email (leading and trailing whitespaces)
        valid_email = "hsamir@upenn.edu"
        valid_resume = ["Other content", "   hsamir@upenn.edu  " , "More content"]
        self.assertEqual(get_email(valid_resume), valid_email)

        # Test an invalid email (capital letter after the @)
        invalid_email_resume = ["Other content", "hsamir@Upenn.edu", "More content"]
        self.assertEqual(get_email(invalid_email_resume), "")
        # Test an invalid email (wrong extension)
        invalid_email_resume = ["Other content", "hsamir@upenn.org", "More content"]
        self.assertEqual(get_email(invalid_email_resume), "")

        # Test an invalid email (digits in email)
        invalid_email_resume = ["Other content", "hsamir3@seas.upenn.edu", "More content"]
        self.assertEqual(get_email(invalid_email_resume), "")

    def test_get_courses(self):
        # Test getting valid courses
        valid_courses_resume = ["name", "projects", "activities", "Courses: Math, Physics, Chemistry"]
        self.assertEqual(get_courses(valid_courses_resume), ["Math", "Physics", "Chemistry"])

        # Test getting no courses (wrong identifier)
        no_courses_resume = ["name", "Projects", "Other content", "no courses"]
        self.assertEqual(get_courses(no_courses_resume), [])

    def test_get_projects(self):
        # Test getting valid projects
        valid_projects_resume = ["Projects", "Project 1", "Project 2", "----------"]
        self.assertEqual(get_projects(valid_projects_resume), ["Project 1", "Project 2"])

        # Test getting no projects (lowercase identifier)
        no_projects_resume =  ["name", "projects", "activities", "Courses: Math, Physics, Chemistry"]
        self.assertEqual(get_projects(no_projects_resume), [])

if __name__ == '__main__':
    unittest.main()
