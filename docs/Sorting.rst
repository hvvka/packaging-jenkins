=======
Sorting
=======

Just sort the way you want.

Quick Start Guide
-----------------

.. code-block:: python

    # import the required sort
    >>> from lab10.sorting import bubble_sort

    >>> my_list = [12, 4, 2, 14, 3, 7, 5]

    # to sort the _list
    >>> sorted_list = bubble_sort.sort(my_list)

Features
--------

* To see all the available functions in a module, you can just type ``help()`` with the module name as argument. For example,

.. code-block:: python

    >>> from lab10 import sorting
    >>> help(sorting)
    Help on package lab10.sorting in lab10:

    NAME
        lab10.sorting - Collection of sorting methods

    PACKAGE CONTENTS
         bubble_sort

* For sorting:
  Remember ``sort()`` function takes its parameter as a _list only.

.. code-block:: python

    # import the required sort
    >>> from lab10.sorting import bubble_sort

    >>> my_list = [12, 4, 2, 14, 3, 7, 5]

    # to sort the _list
    >>> sorted_list = bubble_sort.sort(my_list)

* Get time complexities of all the sorting algorithms

.. code-block:: python

    >>> from lab10.sorting import bubble_sort

    # for printing time complexities of bubble_sort
    >>> print(bubble_sort.time_complexities())

* Get the code used for any of the algorithm

.. code-block:: python

    >>> from lab10.sorting import bubble_sort

    # for printing the source code of bubble_sort
    >>> print(bubble_sort.get_code())


Bubble Sort
-----------

* Functions and their uses

.. function:: bubble_sort.sort(_list)

- **_list**           : `list` or `array` to be sorted
- **Return Value**    : returns the sorted `list`

.. function:: bubble_sort.time_complexities()

- **Return Value**    : returns time complexities (Best, Average, Worst)

.. function:: bubble_sort.get_code()

- **Return Value**    : returns the code for the ``bubble_sort.sort()`` function

* For improved Bubble sort

.. function:: bubble_sort.improved_sort(_list)

- **_list**           : `list` or `array` to be sorted
- **Return Value**    : returns the sorted `list`


