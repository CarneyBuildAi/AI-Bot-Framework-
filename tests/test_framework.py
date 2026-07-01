"""Tests for AI Bot Framework"""
import unittest
import os
from dotenv import load_dotenv

class TestFrameworkConfiguration(unittest.TestCase):
    """Test framework configuration"""
    
    def setUp(self):
        """Set up test fixtures"""
        load_dotenv()
    
    def test_environment_variables(self):
        """Test environment variables are accessible"""
        bot_name = os.getenv('BOT_NAME', 'AI Bot')
        self.assertIsNotNone(bot_name)
        self.assertEqual(bot_name, 'AI Bot')
    
    def test_framework_initialization(self):
        """Test framework can initialize"""
        from main import AIBot
        bot = AIBot()
        self.assertIsNotNone(bot)
    
    def test_bot_run(self):
        """Test bot can run"""
        from main import AIBot
        bot = AIBot()
        result = bot.run()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()