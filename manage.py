#!/usr/bin/env python
import sys
import os

from django.core.management import execute_from_command_line

from tasks import (
    setup_django_environment,
    get_user_config_path
)

if __name__ == "__main__":

    # If user passed the settings flag ignore the default wger settings
    #if not any('--settings' in s for s in sys.argv):
     #   setup_django_environment(get_user_config_path('wger', 'settings.py'))
    if not any('--settings' in s for s in sys.argv):
        config_path = get_user_config_path('wger', 'settings.py')
        print(config_path)
        if not os.path.exists(config_path):
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'wger/settings.py')
        setup_django_environment(config_path)
    # Alternative to above
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    execute_from_command_line(sys.argv)
