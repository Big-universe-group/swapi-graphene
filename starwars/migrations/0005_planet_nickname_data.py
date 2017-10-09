from django.db import migrations
from django.core.management import call_command


def loadfixture(apps, schema_editor):
    fixtures = 'planets_nickname'.split(' ')
    call_command('loaddata', *fixtures)


class Migration(migrations.Migration):

    dependencies = [
        ('starwars', '0004_planet_nickname'),
    ]

    operations = [
        migrations.RunPython(loadfixture),
    ]
