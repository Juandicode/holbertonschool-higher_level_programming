#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        # Create a sorted version of the list and print it
        sorted_list = sorted(self)
        print(sorted_list)
