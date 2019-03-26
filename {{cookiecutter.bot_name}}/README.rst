.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _virtualenv: https://virtualenv.pypa.io/en/stable/
.. _Sanic: https://sanic.readthedocs.io/en/latest/
.. _Docker installation guide: https://docs.docker.com/install/

{{ "=" * cookiecutter.bot_name | length }}
{{cookiecutter.bot_name}}
{{ "=" * cookiecutter.bot_name | length }}

Description
===========
{{cookiecutter.app_description}}

This project leverages the Sanic_ asynchronous framework in a Mattermost bot context.

Prerequisites
=============

- Python 3.7

Installation
============

To install this application, you have to:

1. clone this repository
2. create and activate a virtualenv_

.. code-block:: bash

    $ virtualenv -p python3.7 .venv
    $ .venv/bin/activate

3. install the application requirements with pip_

.. code-block:: bash

    (.venv) $ pip install -r requirements.txt

You should now be able to run it with:

.. code-block:: bash

    (.venv) $ python run.py

Docker
======

This project can be run in a Docker container using the provided dockerfile.
To run it, Docker Engine is required.
Procedure to install Docker can be found here: `Docker installation guide`_.
