# test_bridgesync.py
"""
Tests for BridgeSync module.
"""

import unittest
from bridgesync import BridgeSync

class TestBridgeSync(unittest.TestCase):
    """Test cases for BridgeSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BridgeSync()
        self.assertIsInstance(instance, BridgeSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BridgeSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
