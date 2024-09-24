Pydxdiag - Python Parser & ORMs for dxdiag
==========================================

Pydxdiag is a ``praser`` and ``ORMs`` for ``dxdiag.exe`` on Windows.
Meaning you can access dxdiag information in your Python programs.

To install
~~~~~~~~~~

type below command in your favorite terminal.

.. code:: bash

   pip install pydxdiag

or

.. code:: bash

   pip install git+https://github.com/ElinLiu0/pydxdiag

Quick Start
~~~~~~~~~~~

Here you need to initialize a ``DxDiagparser()`` object like below.

.. code:: python

   from pydxdiag.DxdiagParser import DxdiagParser
   parser = DxdiagParser()

This will call a subprocess to run below command in background:

.. code:: powershell

   dxdiag.exe -w output.xml

..

   Since dxdiag doesn’t support directly output into terminal,so that we
   can only export it into xml format.

Once parser object has been initalized,you can try calling this code as
below:

.. code:: python

   parser.GetOSInformation()

If you get this:

.. code:: python

   OSInformation(Name='Windows 11 专业版 64-bit (10.0, Build 22631) (22621.ni_release.220506-1250)', Version=11, Bit=64, BuildId=22631, ReleaseId='22621.ni_release.220506-1250', Language='Chinese (Simplified) (Regional Setting: Chinese (Simplified))')

That means all things is get ready for you,GLHF : )
