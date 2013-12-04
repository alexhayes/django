from django.test import TestCase
from django.core.exceptions import ValidationError
import pickle

class PickableValidationErrorTestCase(TestCase):

    def test_validationerror_is_picklable(self):
        expected = ValidationError(['a', 'b'])
        actual = pickle.loads(pickle.dumps(expected))
        
        self.assertEqual(actual.error_list[0], expected.error_list[0])
        self.assertEqual(actual.error_list[1], expected.error_list[1])
