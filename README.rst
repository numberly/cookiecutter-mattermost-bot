cookiecutter-mattermost-bot
===========================

Reference template from which you can generate a boilerplate bot for Mattermost.

Usage
-----

Install dependencies:

.. code-block:: bash

   $ pip install --user -r requirements.txt

Generate a new bot:

.. code-block:: bash

   $ cookiecutter https://github.com/numberly/cookiecutter-mattermost-bot

To create the project, you will need:

- a token that you will get at the end of the creation process of a Mattermost slash command
- a Git repository URL you will get after creating a Git repository

Once all questions have been answered, check the ``README.rst`` file of your newly generated application to learn how to run it.
