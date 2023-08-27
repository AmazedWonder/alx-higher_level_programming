#!/usr/bin/python3
"""Defines a class MyInt that inherits from int.

defines a class MyInt that inherits from the built-in int class.
The purpose of MyInt class is to invert behavior of the equality
operators == and != when comparing MyInt objects with other values.

The MyInt class overrides the __eq__ method to change the behavior
of the == operator. In the overridden __eq__ method, it compares
the real part of the MyInt object with the given value using the
!= operator. This means that when you use == to compare a MyInt
object with another value, it will perform a "not equal" comparison.

The MyInt class also overrides the __ne__ method to change the
behavior of the != operator. In the overridden __ne__ method,
it compares the real part of the MyInt object with the given
value using the == operator. This means that when you use !=
to compare a MyInt object with another value, it will perform
an "equal" comparison.

"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
