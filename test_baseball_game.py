# -*- coding: utf8 -*-

import unittest
import baseball_game as bg

from mock import patch
from io import StringIO


class TestBaseballGame(unittest.TestCase):

    def test_is_digit(self):
        self.assertEqual(True, bg.is_digit("3232"))
        self.assertEqual(False, bg.is_digit("32.2"))
        self.assertEqual(False, bg.is_digit("15.4"))
        self.assertEqual(True, bg.is_digit("323"))

    def test_is_between_100_and_999(self):
        self.assertEqual(True, bg.is_between_100_and_999("100"))
        self.assertEqual(False, bg.is_between_100_and_999("5"))
        self.assertEqual(False, bg.is_between_100_and_999("4934"))
        self.assertEqual(True, bg.is_between_100_and_999("503"))
        for i in range(1, 99):
            self.assertEqual(False, bg.is_between_100_and_999(str(i)))
        for i in range(100, 999):
            self.assertEqual(True, bg.is_between_100_and_999(str(i)))
        for i in range(1000, 100000):
            self.assertEqual(False, bg.is_between_100_and_999(str(i)))

    def test_is_duplicated_number(self):
        self.assertEqual(True, bg.is_duplicated_number("100"))
        self.assertEqual(True, bg.is_duplicated_number("110"))
        self.assertEqual(True, bg.is_duplicated_number("111"))
        self.assertEqual(True, bg.is_duplicated_number("220"))
        self.assertEqual(False, bg.is_duplicated_number("312"))
        self.assertEqual(False, bg.is_duplicated_number("542"))
        for i in range(100, 999):
            id_duplicated = bg.is_duplicated_number(str(i))
            self.assertEqual(id_duplicated, bg.is_duplicated_number(str(i)))

    def test_is_validated_number(self):
        self.assertEqual(False, bg.is_validated_number("100"))
        self.assertEqual(False, bg.is_validated_number("99999"))
        self.assertEqual(False, bg.is_validated_number("efkqk"))
        self.assertEqual(False, bg.is_validated_number("19"))
        self.assertEqual(True, bg.is_validated_number("567"))
        self.assertEqual(True, bg.is_validated_number("154"))
        self.assertEqual(True, bg.is_validated_number("437"))
        self.assertEqual(False, bg.is_validated_number("110"))
        self.assertEqual(False, bg.is_validated_number("111"))


    def test_get_not_duplicated_three_digit_number(self):
        for i in range(5000):
            is_duplicated = self.is_duplicated_number(
                str(bg.get_not_duplicated_three_digit_number()))
            self.assertEqual(False, is_duplicated)

    def test_get_strikes_or_ball(self):
        strikes, balls = bg.get_strikes_or_ball("123", "123")
        self.assertEqual(3, strikes)
        self.assertEqual(0, balls)

        strikes, balls = bg.get_strikes_or_ball("456", "123")
        self.assertEqual(0, strikes)
        self.assertEqual(0, balls)

        strikes, balls = bg.get_strikes_or_ball("312", "123")
        self.assertEqual(0, strikes)
        self.assertEqual(3, balls)

        strikes, balls = bg.get_strikes_or_ball("472", "764")
        self.assertEqual(0, strikes)
        self.assertEqual(2, balls)

        strikes, balls = bg.get_strikes_or_ball("174", "175")
        self.assertEqual(2, strikes)
        self.assertEqual(0, balls)

    def test_is_yes(self):
        self.assertEqual(True, bg.is_yes("yEs"))
        self.assertEqual(True, bg.is_yes("yES"))
        self.assertEqual(True, bg.is_yes("Y"))
        self.assertEqual(True, bg.is_yes("y"))
        self.assertEqual(True, bg.is_yes("yes"))
        self.assertEqual(True, bg.is_yes("YES"))

        self.assertEqual(False, bg.is_yes("n01"))
        self.assertEqual(False, bg.is_yes("n3493"))
        self.assertEqual(False, bg.is_yes("no"))
        self.assertEqual(False, bg.is_yes("yyyyyyy"))
        self.assertEqual(False, bg.is_yes("yesyesyes"))

    def test_is_no(self):
        self.assertEqual(True, bg.is_no("no"))
        self.assertEqual(True, bg.is_no("NO"))
        self.assertEqual(True, bg.is_no("No"))
        self.assertEqual(True, bg.is_no("nO"))
        self.assertEqual(True, bg.is_no("n"))
        self.assertEqual(True, bg.is_no("N"))

        self.assertEqual(False, bg.is_no("n01"))
        self.assertEqual(False, bg.is_no("non"))
        self.assertEqual(False, bg.is_no("nnnnnnn"))
        self.assertEqual(False, bg.is_no("nonono"))

        self.assertEqual(False, bg.is_no("YES"))


    def is_no(self, one_more_input):
        if one_more_input.upper() == 'NO':
            return True
        if one_more_input.upper() == 'N':
            return True
        return False


    def is_duplicated_number(self, three_digit):
        for number in three_digit:
            if three_digit.count(number) > 1:
                return True
        return False

    def get_strikes_or_ball(self, user_input_number, random_number):
        result = []
        if random_number == user_input_number:
            result = [3, 0]

        strikes = 0
        ball = 0

        for number in user_input_number:
            if (number in random_number):
                if user_input_number.index(number) is random_number.index(number):
                    strikes += 1
                else:
                    ball += 1
        result = [strikes, ball]
        return result
if __name__ == '__main__':
    unittest.main()