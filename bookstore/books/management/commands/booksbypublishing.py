from django.core.management import BaseCommand

from books.models import Book


class Command(BaseCommand):

    help = 'Books ordering by publish date ("-a" for ascending\
        or "-d" for descending direction)'

    def handle(self, *args, **options):

        '''Prints the list of all books objects from the database,
        oredered by 'publish_date' field.  Direction of ordering (ascending/descending)
        is defined by options'''

        #Define if only one option was given
        if options['ascending'] ^ options['descending']:
            if options['ascending']:
                direction = 'publish_date'
            else:
                direction = '-publish_date'
            books_list = Book.objects.order_by(direction)
            for book in books_list:
                print('"{}" by {} was published on {}'.format(book.title,
                                                            book.authors_info,
                                                            book.publish_date))
        #If no ordering option provided or both of them were given
        else:
            print('Please, choose direction of ordering')


    def add_arguments(self, parser):
        parser.add_argument('-a', '--ascending', 
                            action='store_true',
                            default=False,
                            help='Earlier first')
        parser.add_argument('-d', '--descending', 
                            action='store_true',
                            default=False,
                            help='Later first')
