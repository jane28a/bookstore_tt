from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType

from books.models import Book


class Command(BaseCommand):

    help = 'Create users who managing book data'

    def handle(self, *args, **options):

        '''Define if there are group "managers", if no - creates it and grant permission
        to manage books. Then creates user with given name (but without password)
        and adds it to the managers group''' 

        managers_group, created = Group.objects.get_or_create(name='managers')
        #If no managers group was created earlier - grant permissions to manage books
        if created:
            ct = ContentType.objects.get_for_model(Book)
            manager_permission = Permission.objects.create(codename='can_manage_books',
                                                        name='Can manage books',
                                                        content_type=ct)
            managers_group.permissions.add(manager_permission)
            print('Managers group created')
        
        #Create user and add him to the group    
        manager_user = User.objects.create_user(options['name'])
        manager_user.groups.add(managers_group)


    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', 
                            action='store',
                            default='new_manager',
                            help='Username for manager')
