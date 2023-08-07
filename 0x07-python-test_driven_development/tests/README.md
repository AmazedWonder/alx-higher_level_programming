# Python Test Cases __Strong__

Testing is crucial in the software development phase. It helps ensure easy debugging, agile code, and enhanced reusability. Performing tests that cover all use cases helps prevent a codebase from breaking — minimizing exposure to vulnerabilities. Python has two main testing frameworks that developers can use, doctest and unittest.

### What is Doctest?
Doctest is an inbuilt test framework that comes bundled with Python by default. The doctest module searches for code fragments that resemble interactive Python sessions and runs those sessions to confirm they operate as shown.

Developers commonly use doctest to test documentation. The doctest module looks for sequences of prompts in a docstring, re-executes the extracted command, and compares the output with the command’s input given in the docstrings test example.

### What is Unittest?
Unittest test case runners allow more options when running tests, like reporting test statistics such as tests that passed and failed.

The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.



The simplest way to start using doctest (but not necessarily the way you’ll continue to do it) is to end each module M with:

if __name__ == "__main__":
    import doctest
    doctest.testmod()


Another simple application of doctest is testing interactive examples in a text file. This can be done with the testfile() function:

import doctest
doctest.testfile("example.txt")
That short script executes and verifies any interactive Python examples contained in the file example.txt. The file content is treated as if it were a single giant docstring; the file doesn’t need to contain a Python program! For example, perhaps example.txt contains this:

The ``example`` module
======================

Using ``factorial``
-------------------

This is an example text file in reStructuredText format.  First import
``factorial`` from the ``example`` module:

    >>> from example import factorial

Now use it:

    >>> factorial(6)
    120
Running doctest.testfile("example.txt") then finds the error in this documentation:

File "./example.txt", line 14, in example.txt
Failed example:
    factorial(6)
Expected:
    120
Got:
    720
