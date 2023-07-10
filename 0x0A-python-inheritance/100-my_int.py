#!/usr/bin/python3
"""Reimplementing equality and non equality in int"""


class MyInt(int):
    """MyInt class setup"""

    def __eq__(self, other):
        """Redefinition of the int equality method"""

        return super().__ne__(other)

    def __ne__(self, other):
        """Redefinition of the int non equality method"""

        return super().__eq__(other)
