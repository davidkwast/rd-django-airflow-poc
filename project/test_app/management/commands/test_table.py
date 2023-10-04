from django.core.management.base import BaseCommand, CommandError

from ... import models


class Command(BaseCommand):


    def add_arguments(self, parser):
        pass


    def handle(self, *args, **options):
        # print(options)
        run(**options)



def run(**kwargs):

    models.Test_Table.objects.create(text='cli test')
