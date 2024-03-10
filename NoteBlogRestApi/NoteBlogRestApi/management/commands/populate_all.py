# main_app/management/commands/populate_all.py
from django.core.management.base import BaseCommand, call_command

class Command(BaseCommand):
    help = 'Runs all populate commands in a specified order'

    def handle(self, *args, **kwargs):
        # Call each command in the desired order
        call_command('populate_categories_and_tags')
        # Add more commands as needed, for example:
        #call_command('populate_other_data', arg1, arg2)
        # ...
        self.stdout.write(self.style.SUCCESS('All data has been populated.'))