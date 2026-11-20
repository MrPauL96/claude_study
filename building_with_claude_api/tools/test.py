"""
Test suite for the pi calculation module.
"""

import unittest
import math
from main import calculate_pi, get_pi_to_5th_digit


class TestPiCalculation(unittest.TestCase):
    """Test cases for pi calculation functions."""
    
    def test_pi_to_5th_digit(self):
        """Test that pi is calculated correctly to the 5th decimal digit."""
        result = get_pi_to_5th_digit()
        expected = 3.14159
        self.assertAlmostEqual(result, expected, places=5,
                              msg=f"Expected {expected}, got {result}")
    
    def test_pi_accuracy(self):
        """Test that the calculated value is close to math.pi."""
        result = get_pi_to_5th_digit()
        self.assertAlmostEqual(result, math.pi, places=5,
                              msg=f"Calculated pi {result} differs from math.pi {math.pi}")
    
    def test_pi_different_precisions(self):
        """Test pi calculation with different precision levels."""
        # Test 2 decimal places
        pi_2 = calculate_pi(2)
        self.assertAlmostEqual(pi_2, 3.14, places=2)
        
        # Test 3 decimal places
        pi_3 = calculate_pi(3)
        self.assertAlmostEqual(pi_3, 3.142, places=3)
        
        # Test 5 decimal places
        pi_5 = calculate_pi(5)
        self.assertAlmostEqual(pi_5, 3.14159, places=5)
        
        # Test 10 decimal places
        pi_10 = calculate_pi(10)
        self.assertAlmostEqual(pi_10, 3.1415926536, places=10)
    
    def test_return_type(self):
        """Test that the function returns a float."""
        result = get_pi_to_5th_digit()
        self.assertIsInstance(result, float,
                            msg=f"Expected float, got {type(result)}")
    
    def test_pi_range(self):
        """Test that pi is within the expected range."""
        result = get_pi_to_5th_digit()
        self.assertGreater(result, 3.14, msg="Pi should be greater than 3.14")
        self.assertLess(result, 3.15, msg="Pi should be less than 3.15")
    
    def test_pi_exact_value(self):
        """Test that pi matches the exact expected value to 5 digits."""
        result = get_pi_to_5th_digit()
        # Pi to 5 decimal places is 3.14159
        self.assertEqual(result, 3.14159,
                        msg=f"Expected exactly 3.14159, got {result}")


def run_tests():
    """Run all tests and display results."""
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPiCalculation)
    
    # Run the tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
