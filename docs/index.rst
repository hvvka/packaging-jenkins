=====
lab10
=====

Introduction
------------

``lab10``

* Stwórz w języku python bibliotekę składającą się z pakietów i modułów. Kilka wersji biblioteki zamieść na gitlabie (niech w tych bibliotekach niektóre z metod będą miały inne działanie lub też różne sygnatury).
* Biblioteka może zawierać zbiór klas/funkcji jak w projekcie "doradca". Można też stworzyć całkiem nową bibliotekę.
* Stwórz nowy projekt, w którym zostanie wykorzystana biblioteka. Sprawdź, czy po pobraniu nowego projektu z gitlaba da się go uruchomić (chodzi o zapewnienie zgodności wersji użytych bibliotek)
* Proszę w celu zapoznania się z obsługą pakietów zadeklarować przynajmniej dwa pakiety i kilka modułów.
* Proszę zapoznać się z opisem podobnego zadania umieszczonym pod adresem: https://github.com/BillMills/pythonPackageLesson

Structure
-----------

.. toctree::
:maxdepth: 2
       :caption: Documentation:

           Fibonacci
           Math
           Sorting
           Strings

Quick Start Guide
-----------------

* Import the required file

.. code-block:: python

    from lab10.sorting import bubble_sort

    # This will print the code for bubble sort
    print(bubble_sort.get_code())

    my_list = [12, 4, 2, 14, 3, 7, 5]

    # to sort the list
    sorted_list = bubble_sort.sort(my_list)


Getting Started
---------------

* Download the package using Python package manager

::

    pip3 install lab10


::

    python setup.py install
