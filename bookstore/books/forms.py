from django import forms

from .models import Book


class BookForm(forms.ModelForm):

    '''Form for manipulating the Book instances.
    Some attributes added to default widgets for customization with MetroUI'''

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title' : forms.widgets.TextInput(attrs={'data-role':'input'}),
            'authors_info' : forms.widgets.Textarea(attrs={'data-role':'textarea',
                                                            'data-auto-size':'true',
                                                            'data-max-height': '100'}),
            'isbn' : forms.widgets.TextInput(attrs={'data-role':'input'}),
            'price': forms.widgets.TextInput(attrs={'data-role': 'spinner',
                                                    'data-step': '.01',
                                                    'data-fixed': '2'}),
        }

    def clean_isbn(self):
        
        '''Basic validation of ISBN input - only digits and hyphens are allowed'''

        isbn = self.cleaned_data['isbn']
        if isbn and not isbn.replace('-', '').isdigit():
            raise forms.ValidationError('Only digits and hyphens are allowed')
        return isbn

