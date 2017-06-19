
******
pyshgp
******

PushGP Genetic Programming in Python


Push Genetic Programming
=========================

Push is programming language that plays nice with evolutionay computing /
genetic programming. It is a stack-based language that features 1 stack per data
type, including code. Programs are represented by lists of instructions, which
modify the values on the stacks. Instuctions are executed in order.

More information about PushGP can be found on
`the Push Redux <https://erp12.github.io/push-redux/>`_ where you can
read about how PushGP works and find listings of other implemenations.


Table Of Contents
==================

.. toctree::
   :maxdepth: 2

   Push_GP
   pyshgp_overview
   api/index
   Instructions
   examples/index
   contributing

Installation
=============

Install from Pip
""""""""""""""""

Coming soon!

Build Frome source
""""""""""""""""""

1. Clone the repo
2. :code:`cd` into the pyshgp repo directory
3. run :code:`pip install . --upgrade`

Thats it! You should be ready to use Pysh.

Examples / Usage
=================

Pysh is compatable with Python 2.7 and Python 3.5.

To run the Pysh examples, simply run one of the problem files in the
``pysh/examples/`` folder.::

   python examples/tutorials/odd.py
   # or
   python examples/tutorials/string_demo.py
   # or
   python examples/software-synthesis/replace_space_with_newline.py

Read more about the pyshgp examples on the `Examples page <Examples.html>`_.


Roadmap
========

Pysh is currently under active development. Feel free to submit a pull request
if you have any additions to make.

To see what features are in development, or planned for the future, check out
the `Github project board <https://github.com/erp12/Pysh/projects/1>`_.

To see Pysh's release notes, check out the
`other Github project board <https://github.com/erp12/Pysh/projects/2>`_.
