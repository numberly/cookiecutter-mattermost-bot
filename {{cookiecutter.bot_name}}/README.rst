.. _cookiecutter-mattermost-bot: https://github.com/numberly/cookiecutter-mattermost-bot
.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _virtualenv: https://virtualenv.pypa.io/en/stable/
.. _Sanic: https://sanic.readthedocs.io/en/latest/
.. _slash command creation process: https://docs.mattermost.com/developer/slash-commands.html#custom-slash-command

{{ "=" * cookiecutter.bot_name | length }}
{{cookiecutter.bot_name}}
{{ "=" * cookiecutter.bot_name | length }}

{{cookiecutter.bot_description}}

This repository has been generated with cookiecutter-mattermost-bot_.

Quickstart
==========

To install and run this application locally without Docker, you will need
Python 3.7 and virtualenv_.

Once you have cloned the repository, create and activate a virtualenv_:

.. code-block:: bash

    $ cd {{cookiecutter.bot_name}}
    $ virtualenv -p python3.7 .venv
    $ .venv/bin/activate

Install the application requirements with pip_:

.. code-block:: bash

    (.venv) $ pip install -r requirements.txt

You should now be able to run the bot with:

.. code-block:: bash

    (.venv) $ MATTERMOST_BOT_TOKEN=... python bot.py

The ``MATTERMOST_BOT_TOKEN`` environment variable is required and should have
been given to you by Mattermost at the end of your `slash command creation
process`_.

Docker
======

Build the Docker image with:

.. code-block:: bash

    $ docker build -t {{cookiecutter.bot_image_url}} .

You should now be able to run the bot with:

.. code-block:: bash

    $ docker run --rm -i -p 5000:5000 -e MATTERMOST_BOT_TOKEN=... {{cookiecutter.bot_image_url}}

Kubernetes
==========

Push the Docker image to the Docker registry with:

.. code-block:: bash

    $ docker push {{cookiecutter.bot_image_url}}

Create the Kubernetes secret that will contain the Mattermost token:

.. code-block:: bash

    $ kubectl create secret generic {{cookiecutter.bot_name}} --from-literal=mattermost-token=...

Deploy the manifest:

.. code-block:: bash

    $ kubectl apply -f kubernetes.yaml
