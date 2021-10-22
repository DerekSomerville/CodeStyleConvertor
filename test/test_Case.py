from unittest import TestCase
from src.Case import *

class Test_Case(TestCase):

    def test_is_pascal_case(self):
        self.assertTrue(is_pascal_case("dataSql")

    def test_is_not_pascal_case(self):
        self.assertTrue(is_pascal_case("datasql")

    def test_is_not_snake_case(self):
        self.assertTrue(is_pascal_case("dataSql")

    def test_is_snake_case(self):
        self.assertTrue(is_pascal_case("data_sql")