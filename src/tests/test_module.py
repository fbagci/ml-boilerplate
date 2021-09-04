import unittest

from src.tests.test_base import BaseTestFixture
from src.project_name.core.package.module import module

class test_module1(BaseTestFixture):
    def test_module(self):
        print("Test: Module")
        result = self.module.run_module()
        expected = True
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main(argv=["ignored", "-v"], exit=False)