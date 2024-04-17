Setup Guide
===========

This section outlines the steps for setting up the project environment using Pipenv, a tool for managing package dependencies and virtual environments. It assumes that the user has a working installation of pip.

Prerequisites
-------------
- Ensure pip is installed by running ``pip --version`` in your terminal. If pip is not installed, follow the instructions on the `pip installation guide <https://pip.pypa.io/en/stable/installation/>`_.

Installing Pipenv
-----------------
Pipenv can be installed via pip with the following command:

.. code-block:: bash

   pip install --user pipenv

This command installs Pipenv for the current user. The ``--user`` flag ensures that Pipenv is installed in the user's directory and does not require system-wide installation.

Setting Up the Project Environment
----------------------------------
Navigate to the project's root directory, where the ``Pipfile`` and ``Pipfile.lock`` are located, and execute the following command to install dependencies and set up the virtual environment:

.. code-block:: bash

   pipenv install

Activating the Virtual Environment
----------------------------------
Activate the virtual environment created by Pipenv using:

.. code-block:: bash

   pipenv shell

Troubleshooting Python Version Errors
-------------------------------------
If you encounter an error about an unavailable Python version, such as:

.. code-block:: bash

   Error: the specified Python version (3.8) is not available on your system.

It is recommended to use ``pyenv`` to manage multiple Python versions. Installation instructions for ``pyenv`` can be found at the `pyenv GitHub repository <https://github.com/pyenv/pyenv#installation>`_.

After installing ``pyenv``, you may need to restart your shell or terminal to ensure ``pyenv`` and ``pipenv`` are correctly added to your PATH.

When ``pyenv`` is installed, running ``pipenv install`` again will prompt Pipenv to use ``pyenv`` to install the missing Python version. Confirming this allows Pipenv to manage the required Python version for the project automatically.

Conclusion
----------
This guide provided instructions for setting up your project environment with Pipenv, including installing dependencies and resolving Python version issues with ``pyenv``. For additional information, consult the Pipenv documentation or community forums.
