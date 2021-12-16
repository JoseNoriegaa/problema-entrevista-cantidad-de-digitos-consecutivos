"""
Problem:
    Se necesita saber el conteo de cuántos dígitos sucesivos contiene
    un número de modo que el 7 se compone de 7 dígitos mientras que
    el 10 se compone de 11, programar la solución que permita saber
    la cantidad de dígitos de cualquier número.

Example:
    `Secuencia
    1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 1 - 0
    Cantidad
    1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - 11`
"""

def count_consecutive_digits(num: int) -> int:
    """
    Count the consecutive digits from 1 to the given number.

    Time complexity: O(n * m) where n is the given number and m is the number of digits of the given number.

    Args:
        num: Number to count the consecutive digits.

    Returns:
        The number of consecutive digits.
    """

    assert type(num) == int, "The number must be an integer."

    normalized_number = abs(num)

    if normalized_number < 10:
        return normalized_number

    count = 0

    for i in range(normalized_number):
        # count digits
        number_digits = len(str(i + 1))
        count += number_digits

    return count


if __name__ == '__main__':
    import unittest
    from ddt import ddt
    from ddt import data
    from ddt import unpack

    @ddt
    class CountConsecutiveDigitsTestCase(unittest.TestCase):
        """Test cases for the count_consecutive_numbers function."""

        @data(
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10 ,11),
            (11 ,13),
            (100 ,192),
        )
        @unpack
        def test_count_consecutive_digits(self, number: int, expected_value: int):
            """Test the count_consecutive_digits function."""
            self.assertEqual(count_consecutive_digits(number), expected_value)

    unittest.main(verbosity=2)
