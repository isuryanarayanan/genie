#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import shutil
import sys


def manageConfigurations():
    """ 
    This method will be used to manage configurations for the project.

    The configuration will be specified as environment variables. This method will
    check if the environment variable GENIE_CONFIGURATION_KEY is set. If it is set,
    it will use the value of the environment variable to determine which configuration
    to use. If it is not set, it will use the default configuration. 
    """

    # Check if the environment variable GENIE_CONFIGURATION_KEY is set
    if 'GENIE_CONFIGURATION_KEY' in os.environ:
        configurationKey = os.environ['GENIE_CONFIGURATION_KEY']
    else:
        configurationKey = 'default'

    # If the configurations/ and configurations/genie folder dont exist, create them.
    if not os.path.exists('project/configurations'):
        os.makedirs('project/configurations')
    if not os.path.exists('project/configurations/genie'):
        os.makedirs('project/configurations/genie')

    # If the configurations/<configuration_key> folder does not exist, create it.
    if not os.path.exists('project/configurations/' + configurationKey):
        # Show warning that the environment variable GENIE_CONFIGURATION_KEY is not set.
        print('Warning: GENIE_CONFIGURATION_KEY is not set. Using default configuration.')
        os.makedirs('project/configurations/' + configurationKey)

        # Copy all the files from configurations/genie to configurations/<configuration_key> but
        # swap out all occurrance of the string --configuration-key-- with the value of the
        # environment variable GENIE_CONFIGURATION_KEY.
        for file in os.listdir('project/configurations/genie'):
            if file.endswith('.py'):
                with open('project/configurations/genie/' + file, 'r') as f:
                    filedata = f.read()
                filedata = filedata.replace(
                    '--configuration-key--', configurationKey)
                with open('project/configurations/' + configurationKey + '/' + file, 'w') as f:
                    f.write(filedata)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        manageConfigurations()
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
