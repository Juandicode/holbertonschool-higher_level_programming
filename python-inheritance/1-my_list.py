#!/usr/bin/python3
"""
Muodulo pa clase mylist.
"""


class MyList(list):
    """
   clase mylist hereda d list.
    """

    def print_sorted(self):
        """
        printea la lista en orden ascendente.
        """
        print(sorted(self))
