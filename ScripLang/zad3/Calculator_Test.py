from Calculator import Calculator
import unittest


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_default_display_0(self):
        self.assertEqual("0", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_0_represented_as_0(self):
        self.calc.Press("0")
        self.calc.Press("0")
        self.calc.Press("0")
        self.calc.Press("0")

        self.assertEqual("0", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_intger_Number(self):
        self.calc.Press("1")
        self.calc.Press("2")
        self.calc.Press("3")
        self.calc.Press("4")
        self.calc.Press("5")
        self.calc.Press("6")
        self.calc.Press("7")
        self.calc.Press("8")
        self.calc.Press("9")
        self.calc.Press("0")

        self.assertEqual("1234567890", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_decimal_Number_1(self):
        self.calc.Press(".")
        self.calc.Press("0")
        self.calc.Press("0")
        self.calc.Press("3")
        self.calc.Press("4")
        self.calc.Press("5")
        self.calc.Press("6")
        self.calc.Press("7")
        self.calc.Press("8")
        self.calc.Press("9")

        self.assertEqual("0.003456789", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_decimal_Number_2(self):
        self.calc.Press("4")
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("0")
        self.calc.Press("4")
        self.calc.Press("2")

        self.assertEqual("42.042", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_sum_Input_first_value(self):
        self.calc.Press("1")
        self.calc.Press("2")
        self.calc.Press("+")
        self.assertEqual("12", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_sum_Input_second_value(self):
        self.calc.Press("1")
        self.calc.Press("2")
        self.calc.Press("+")
        self.calc.Press("2")
        self.assertEqual("2", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_sum_two_values_with_addiction_sign(self):
        self.calc.Press("1")
        self.calc.Press("2")
        self.calc.Press("+")
        self.calc.Press("2")
        self.calc.Press("+")
        self.assertEqual("14", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_sum_input_third_value(self):
        self.calc.Press("1")
        self.calc.Press("2")
        self.calc.Press("+")
        self.calc.Press("2")
        self.calc.Press("+")
        self.calc.Press("5")
        self.assertEqual("5", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_sum_three_values_with_equal_sign(self):
        self.calc.Press("1")
        self.calc.Press("2")
        self.calc.Press("+")
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("+")
        self.calc.Press("5")
        self.calc.Press("=")
        self.assertEqual("19.5", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_substract_input_two_values(self):
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("-")
        self.calc.Press("5")
        self.assertEqual("5", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_substract_two_values_with_substract_sign(self):
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("-")
        self.calc.Press("5")
        self.calc.Press("-")
        self.assertEqual("2.5", self.calc.Display)
        self.assertTrue(self.calc.IsNegative)

    def test_substract_three_values_with_equal_sign(self):
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("-")
        self.calc.Press("5")
        self.calc.Press("-")
        self.calc.Press("2")
        self.calc.Press("=")
        self.assertEqual("4.5", self.calc.Display)
        self.assertTrue(self.calc.IsNegative)

    def test_multiply_input_two_values(self):
        self.calc.Press("2")
        self.calc.Press("x")
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.assertEqual("2.5", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_multiply_two_values_with_multiply_sign(self):
        self.calc.Press("2")
        self.calc.Press("x")
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("x")
        self.assertEqual("5", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_multiply_three_values_with_equal_sign(self):
        self.calc.Press("2")
        self.calc.Press("x")
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("x")
        self.calc.Press("2")
        self.calc.Press("=")
        self.assertEqual("10", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_divide_input_two_values(self):
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("/")
        self.calc.Press("5")
        self.assertEqual("5", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_divide_two_values_with_divide_sign(self):
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("/")
        self.calc.Press("5")
        self.calc.Press("/")
        self.assertEqual("0.5", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_divide_three_values_with_equal_sign(self):
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("/")
        self.calc.Press("5")
        self.calc.Press("/")
        self.calc.Press("2")
        self.calc.Press("=")
        self.assertEqual("0.25", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_sum_and_multiply(self):
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("+")
        self.calc.Press("5")
        self.calc.Press("x")
        self.calc.Press("2")
        self.calc.Press("=")
        self.assertEqual("15", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_divide_and_substract(self):
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("/")
        self.calc.Press("5")
        self.calc.Press("-")
        self.calc.Press("1")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("=")

        self.assertEqual("1", self.calc.Display)
        self.assertTrue(self.calc.IsNegative)

    def test_sum_and_equal_many_times(self):
        self.calc.Press("2")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("+")
        self.calc.Press("5")
        self.calc.Press(".")
        self.calc.Press("1")
        self.calc.Press("=")
        self.calc.Press("=")
        self.calc.Press("=")
        self.assertEqual("7.6", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_multiple_many_times(self):
        self.calc.Press("-")
        self.calc.Press("2")
        self.calc.Press("x")
        self.calc.Press("x")
        self.calc.Press("x")
        self.calc.Press("2")
        self.calc.Press("=")
        self.assertEqual("4", self.calc.Display)
        self.assertTrue(self.calc.IsNegative)

    def test_negative_values_equatation(self):
        self.calc.Press("-")
        self.calc.Press("4")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("+")
        self.calc.Press("2")
        self.calc.Press("=")
        self.assertEqual("2.5", self.calc.Display)
        self.assertTrue(self.calc.IsNegative)

    def test_negative_values_equatation2(self):
        self.calc.Press("-")
        self.calc.Press("4")
        self.calc.Press("x")
        self.calc.Press("-")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("=")
        self.assertEqual("2", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_fraction_short(self):
        self.calc.Press(".")
        self.calc.Press("4")
        self.assertEqual("0.4", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_fraction_short_second_value(self):
        self.calc.Press("5")
        self.calc.Press("+")
        self.calc.Press(".")
        self.calc.Press("4")
        self.assertEqual("0.4", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_Clear(self):
        self.calc.Press("-")
        self.calc.Press("5")
        self.calc.Press("C/CE")
        self.assertEqual("0", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_input_after_Clear(self):
        self.calc.Press("-")
        self.calc.Press("5")
        self.calc.Press("C/CE")
        self.calc.Press("-")
        self.calc.Press(".")
        self.calc.Press("5")
        self.assertEqual("0.5", self.calc.Display)
        self.assertTrue(self.calc.IsNegative)

    def test_equatation_after_Clear(self):
        self.calc.Press("-")
        self.calc.Press("5")
        self.calc.Press("C/CE")
        self.calc.Press("-")
        self.calc.Press(".")
        self.calc.Press("5")
        self.calc.Press("x")
        self.calc.Press("5")
        self.calc.Press("=")
        self.assertEqual("2.5", self.calc.Display)
        self.assertTrue(self.calc.IsNegative)

    def test_negative_multiply(self):
        self.calc.Press("-")
        self.calc.Press("5")
        self.calc.Press("x")
        self.calc.Press("-")
        self.calc.Press("6")
        self.calc.Press("=")
        self.assertEqual("30", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_M_plus_value(self):
        self.calc.Press("5")
        self.calc.Press("4")
        self.calc.Press("M+")
        self.assertTrue(self.calc.IsMemorized)

    def test_M_plus_value2(self):
        self.calc.Press("5")
        self.calc.Press("4")
        self.calc.Press("M+")
        self.calc.Press("5")
        self.assertEqual("5", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_MRC_value(self):
        self.calc.Press("4")
        self.calc.Press("M+")
        self.calc.Press("-")
        self.calc.Press("5")
        self.calc.Press("M+")
        self.calc.Press("MRC")
        self.assertEqual("1", self.calc.Display)
        self.assertTrue(self.calc.IsNegative)

    def test_MRC_value2(self):
        self.calc.Press("4")
        self.calc.Press("M+")
        self.calc.Press("-")
        self.calc.Press("5")
        self.calc.Press("M-")
        self.calc.Press("MRC")
        self.assertEqual("9", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_value_after_MRC(self):
        self.calc.Press("4")
        self.calc.Press("M+")
        self.calc.Press("-")
        self.calc.Press("5")
        self.calc.Press("M+")
        self.calc.Press("MRC")
        self.calc.Press("3")
        self.assertEqual("3", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_sqrt(self):
        self.calc.Press("4")
        self.calc.Press("sqrt")
        self.assertEqual("2", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_sqrt_error(self):
        self.calc.Press("-")
        self.calc.Press("4")
        self.calc.Press("sqrt")
        self.assertEqual("0", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)
        self.assertTrue(self.calc.Error)

    def test_percent_multiply(self):
        self.calc.Press("1")
        self.calc.Press("0")
        self.calc.Press("0")
        self.calc.Press("x")
        self.calc.Press("2")
        self.calc.Press("p")
        self.assertEqual("2", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)

    def test_percent_Divide(self):
        self.calc.Press("1")
        self.calc.Press("0")
        self.calc.Press("0")
        self.calc.Press("/")
        self.calc.Press("2")
        self.calc.Press("p")
        self.assertEqual("5000", self.calc.Display)
        self.assertFalse(self.calc.IsNegative)


if __name__ == '__main__':
    unittest.main()