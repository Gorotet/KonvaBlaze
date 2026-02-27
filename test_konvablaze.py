# test_konvablaze.py
"""
Tests for KonvaBlaze module.
"""

import unittest
from konvablaze import KonvaBlaze

class TestKonvaBlaze(unittest.TestCase):
    """Test cases for KonvaBlaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = KonvaBlaze()
        self.assertIsInstance(instance, KonvaBlaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = KonvaBlaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
