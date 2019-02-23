from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission, User


class Command(BaseCommand):

    help = 'Create users who managing book data'

    def handle(self, *args, **options):

        '''Define if there are group "managers", if no - creates it and grant permission
        to manage books. Then creates user with given name and password)
        and adds it to the managers group''' 

        managers_group, created = Group.objects.get_or_create(name='managers')
        #If no managers group was created earlier - grant permissions to manage books
        if created:
            managers_group.permissions.add(Permission.objects.get(content_type__app_label='books',
                                                                    codename='add_book'))
            managers_group.permissions.add(Permission.objects.get(content_type__app_label='books',
                                                                    codename='change_book'))
            managers_group.permissions.add(Permission.objects.get(content_type__app_label='books',
                                                                    codename='delete_book'))
            print('Managers group created')
        
        #Create user and add him to the group    
        manager_user = User.objects.create_user(options['name'], password=options['pass'])
        manager_user.is_staff = True
        manager_user.save()
        manager_user.groups.add(managers_group)


    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', 
                            action='store',
                            default='new_manager',
                            help='Username for manager')
        parser.add_argument('-p', '--pass', 
                            action='store',
                            default='not_so_strong_pass',
                            help='Password for the account')
