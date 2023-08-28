#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file.

A script that uses the save_to_json_file and load_from_json_file
functions to manage a list of items stored in a JSON file.

What the code does:

The sys module is imported to access command-line arguments.

The script checks if it is being run as the main module by using
the __name__ == "__main__" condition. This allows the code within
the conditional block to execute when the script is executed
directly, but not when it is imported as a module.

The __import__ function is used to dynamically import the
save_to_json_file and load_from_json_file functions from
the respective modules. This is an older way of importing modules
and functions dynamically. In modern Python, it is recommended
to use the import statement instead.

The script attempts to load the contents of the "add_item.json"
file using the load_from_json_file function. If the file is not
found (raises a FileNotFoundError), an empty list is assigned
to the items variable.

The command-line arguments (sys.argv[1:]) are added to the items
list using the extend method. sys.argv[1:] represents all the
command-line arguments passed to the script, excluding the script
name itself.

The updated items list is saved back to the "add_item.json" file
using the save_to_json_file function.

Overall, this script allows you to add new items to the list stored
in the "add_item.json" file by passing them as command-line arguments
when executing the script.

"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
