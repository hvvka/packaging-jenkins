lab10-lib-0
===========

| 0.0.1 version of lab10 library


Features
~~~~~~~~

* Fine version of library – everything works as expected
* Library made of few modules and packages implementing simple data transformations and calculations
* Main goal is practising package management


Installation
~~~~~~~~~~~~

* Type in the following command in your terminal:

::

    pip install lab10


::

    python setup.py install


Publishing
~~~~~~~~~~

1. Create a source distribution

Make sure the ``setup.py`` and ``MANIFEST.in`` files appear in the top-level directory of your package.
Once you have done this, you should be able to make a source distribution by typing a command such as this:

::

    python setup.py sdist


This will create a file such as ``lab10-0.0.1.zip`` or ``lab10-0.0.1.tar.gz`` (depending on the platform) in ``dist`` directory.
If it all works, this file is suitable for giving to others or uploading to the Python Package Index (https://pypi.org/).

2a. Upload that file to PyPI with Twine

::

    python3 -m pip install --user --upgrade twine
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*


2b. Or to Gitlab

::

    git init
    source venv/bin/activate
    git remote add origin git@git.e-science.pl:hgrodzicka226154/lab10-lib.git
    git add . && git commit -m "Version 0.0.1"
    git push --set-upstream git@git.e-science.pl:hgrodzicka226154/lab10-lib.git master


Quick Start Guide
~~~~~~~~~~~~~~~~~

* To sort your list

.. code-block:: python

    >>> from lab10.sorting import bubble_sort
    >>> my_list = [12, 4, 3, 5, 13, 1, 17, 19, 15]
    >>> sorted_list = bubble_sort.sort(my_list)
    >>> print(sorted_list)
    >>> [1, 3, 4, 5, 12, 13, 15, 17, 19]


* To get the code for function used

.. code-block:: python

    >>> from lab10.sorting import bubble_sort
    >>> code = bubble_sort.get_code()
    >>> print(code)


* To get the time complexity of an algorithm

.. code-block:: python

    >>> from lab10.sorting import bubble_sort
    >>> time_complexity = bubble_sort.time_complexities()
    >>> print(time_complexity)

* To see all the available functions in a module, you can just type ``help()`` with the module name as argument. For example,

.. code-block:: python

    >>> from lab10 import sorting
    >>> help(sorting)
        Help on package lab10.sorting in lab10:

        NAME
            lab10.sorting - Collection of sorting methods

        PACKAGE CONTENTS
            bubble_sort

    
Tests
~~~~~

* Type in the following command to run the tests

::

    python3 -m unittest

* This will run all the tests defined in the files of the ``tests/`` directory

