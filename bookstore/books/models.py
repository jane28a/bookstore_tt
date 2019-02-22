from django.db import models
from django.core.exceptions import ValidationError


def validate_isbn(isbn):

    '''Simple validator to ensure only digits and hyphens are used in the ISBN notation'''

    if not isbn.replace('-', '').isdigit():
        raise ValidationError('ISBN has to contain only numbers and hyphens')


class Book(models.Model):

    '''Core model for the app. Describes representation of the book 
    in app's data structure.
    Only title field is required.
    Using Decimal for the price representation in most cases is really bad idea,
    but in the scope of this task it is appropriate because no calculation needed'''

    title = models.CharField(max_length=200, null=False, blank=False)
    authors_info = models.TextField(null=False, blank=True, default='Anonymous',
                                    verbose_name='authors')
    isbn = models.CharField(max_length=20, null=True, blank=True, verbose_name='ISBN',
                            help_text='International Standard Book Number', validators=[validate_isbn])
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title
