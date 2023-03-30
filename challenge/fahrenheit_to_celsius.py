"""Fahrenheit to Celsius Converter."""

import os

__all__ = ['fahrenheit_to_celsius']

min_f = 32
max_f = 212


class FahrenheitError(Exception):
    """Exception for invalid Fahrenheit degrees."""

    def __init__(self, f: float, *args) -> None:
        """Initialize the exception with the Fahrenheit degrees that cause it."""
        super().__init__(*args)
        self.f = f

    def __str__(self) -> str:
        return f'{self.f}°F is not in a valid range ({min_f}°F, {max_f}°F)'


def fahrenheit_to_celsius(farheit: float):
    """Return the Celsius degree of the Fahrenheit degrees."""
    if not min_f <= farheit <= max_f:
        raise FahrenheitError(farheit)

    return (farheit - 32) * (5 / 9)


if __name__ == '__main__':
    import argparse

    base = os.path.basename(__file__)
    parser = argparse.ArgumentParser(os.path.splitext(base)[0])
    parser.add_argument('fahrenheit',
                        help='An Fahrenheit degrees to convert to Celsius.')
    args = parser.parse_args()
    fahrenheit = args.fahrenheit

    try:
        fahrenheit = float(fahrenheit)
    except ValueError as err:
        print(err)
    else:
        try:
            celsius = fahrenheit_to_celsius(fahrenheit)
        except FahrenheitError as err:
            print(err)
        else:
            print(f'{fahrenheit:.2f}°F = {celsius:.2f}°C')
