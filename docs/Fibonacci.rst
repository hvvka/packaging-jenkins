=========
Fibonacci
=========

Recursive fibonacci.

Quick Start Guide
-----------------

.. code-block:: python

    >>> from lab10.fibonacci import recursion as fib_recursion
    >>> sequence = fib_recursion.get_sequence(10)
    >>> print(sequence)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


Features
--------

* Get the code

.. code-block:: python

    from lab10.fibonacci import recursion as fib_recursion

    code = fib_recursion.get_code()
    print(code)

* To see all the available functions in a module, you can just type ``help()`` with the module name as argument. For example,

.. code-block:: python

    >>> from lab10 import fibonacci
    >>> help(fibonacci)
            Help on package lab10.fibonacci in lab10:

            NAME
                lab10.fibonacci - Collection of fibonacci methods and functions

            PACKAGE CONTENTS
                recursion

            DATA
                __all__ = ['recursion']



Implementations API
-------------------

* Functions and their uses

.. function:: get_sequence(number)

- **number**          : arbitrary integer, that need to be calculated in Fibonacci number type
- **Return Value**    : return Fibonacci value by specified number as integer

.. function:: get_code()

- **Return Value**    : returns the code for the ``get_sequence()`` function
