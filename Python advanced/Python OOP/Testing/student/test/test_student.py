from project.student import Student
import unittest


class StudentTests(unittest.TestCase):

    def setUp(self):
        self.niki = Student('Niki')
        self.nikiJS = Student('Niki', {'JS': ['async']})

    def test_init(self):
        self.assertEqual('Niki', self.niki.name)
        self.assertEqual({}, self.niki.courses)
        self.assertEqual('Niki', self.nikiJS.name)
        self.assertEqual({'JS': ['async']}, self.nikiJS.courses)

    def test_enroll_course_already_added(self):
        self.assertEqual('Course already added. Notes have been updated.', self.nikiJS.enroll('JS', ['a', 'b']))
        self.assertEqual({'JS': ['async', 'a', 'b']}, self.nikiJS.courses)
        self.assertEqual(['async', 'a', 'b'], self.nikiJS.courses['JS'])
        self.assertEqual('async', self.nikiJS.courses['JS'][0])
        self.assertEqual('a', self.nikiJS.courses['JS'][1])
        self.assertEqual('b', self.nikiJS.courses['JS'][2])
        self.assertEqual(3, len(self.nikiJS.courses['JS']))

    def test_enroll_course_already_added_with_third_param(self):
        self.assertEqual('Course already added. Notes have been updated.', self.nikiJS.enroll('JS', ['a', 'b'], 'das'))
        self.assertEqual({'JS': ['async', 'a', 'b']}, self.nikiJS.courses)
        self.assertEqual(['async', 'a', 'b'], self.nikiJS.courses['JS'])
        self.assertEqual('async', self.nikiJS.courses['JS'][0])
        self.assertEqual('a', self.nikiJS.courses['JS'][1])
        self.assertEqual('b', self.nikiJS.courses['JS'][2])
        self.assertEqual(3, len(self.nikiJS.courses['JS']))

    def test_enroll_course_already_added_with_third_param_on_non_empty(self):
        self.assertEqual('Course and course notes have been added.', self.nikiJS.enroll('Python', ['a', 'b'], 'Y'))
        self.assertEqual({'JS': ['async'], 'Python': ['a', 'b']}, self.nikiJS.courses)
        self.assertEqual(['async'], self.nikiJS.courses['JS'])
        self.assertEqual('async', self.nikiJS.courses['JS'][0])
        self.assertEqual(1, len(self.nikiJS.courses['JS']))

    def test_enroll_course_already_added_without_third(self):
        self.assertEqual('Course and course notes have been added.', self.nikiJS.enroll('Python', ['a', 'b'], ''))
        self.assertEqual({'JS': ['async'], 'Python': ['a', 'b']}, self.nikiJS.courses)
        self.assertEqual(['async'], self.nikiJS.courses['JS'])
        self.assertEqual('async', self.nikiJS.courses['JS'][0])
        self.assertEqual(1, len(self.nikiJS.courses['JS']))

    def test_enroll_course_and_course_notes(self):
        self.assertEqual('Course and course notes have been added.', self.niki.enroll('Python', ['1', '2'], 'Y'))
        self.assertEqual({'Python': ['1', '2']}, self.niki.courses)
        self.assertEqual(['1', '2'], self.niki.courses['Python'])

    def test_enroll_course_and_course_notes_without_third_param(self):
        self.assertEqual('Course and course notes have been added.', self.niki.enroll('Python', ['1', '2']))
        self.assertEqual({'Python': ['1', '2']}, self.niki.courses)
        self.assertEqual(['1', '2'], self.niki.courses['Python'])

    def test_enroll_course_and_course_notes_with_empty_str(self):
        self.assertEqual('Course and course notes have been added.', self.niki.enroll('Python', ['1', '2'], ''))
        self.assertEqual({'Python': ['1', '2']}, self.niki.courses)

    def test_enroll_course_added(self):
        self.assertEqual('Course has been added.', self.niki.enroll('JS', [], 'N'))
        self.assertEqual({'JS': []}, self.niki.courses)
        self.assertEqual([], self.niki.courses['JS'])

    def test_add_note(self):
        self.assertEqual('Notes have been updated', self.nikiJS.add_notes('JS', 'a'))
        self.assertEqual({'JS': ['async', 'a']}, self.nikiJS.courses)
        self.assertEqual(['async', 'a'], self.nikiJS.courses['JS'])

    def test_add_note_exception(self):
        with self.assertRaises(Exception) as ex:
            self.niki.add_notes('das', 'das')
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_leave_course(self):
        self.assertEqual('Course has been removed', self.nikiJS.leave_course('JS'))
        self.assertEqual({}, self.nikiJS.courses)

    def test_leave_course_exception(self):
        with self.assertRaises(Exception) as ex:
            self.niki.leave_course('das')
        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))


if __name__ == '__main__':
    unittest.main()