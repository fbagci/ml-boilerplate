import unittest

from src.project_name.project_name.package.module import Module

class BaseTestFixture(unittest.TestCase):
    # setUp method will work before each test method
    def setUp(self):
        # Initialize module
        self.module = Module()
    # tearDown method will work after each test method
    def tearDown(self):
        pass