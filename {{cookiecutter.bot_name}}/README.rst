.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _virtualenv: https://virtualenv.pypa.io/en/stable/
.. _Sanic: https://sanic.readthedocs.io/en/latest/

{{ "=" * cookiecutter.bot_name | length }}
{{cookiecutter.bot_name}}
{{ "=" * cookiecutter.bot_name | length }}

Description
===========
{{cookiecutter.bot_description}}

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

    (.venv) $ MATTERMOST_BOT_TOKEN=... python bot.py

You should have been given the ``MATTERMOST_BOT_TOKEN`` by Mattermost at the
end of your slash command creation process.

Build
=====

Build the Docker image with:

.. code-block:: bash

    $ docker build -t {{cookiecutter.bot_registry_url}} .

You can try the Docker image on your own machine with:

.. code-block:: bash

    $ docker run --rm -i -p 5000:5000 -e MATTERMOST_BOT_TOKEN=... {{cookiecutter.bot_registry_url}}

Deployment
==========

Push your Docker image to the Docker registry with:

.. code-block:: bash

    $ docker push {{cookiecutter.bot_registry_url}}

Create the Kubernetes secret that will contain the Mattermost token:

.. code-block:: bash

    $ kubectl create secret generic {{cookiecutter.bot_name}} --from-literal=mattermost-token=...

Deploy the manifest:

.. code-block:: bash

    $ kubectl apply -f kubernetes.yaml
