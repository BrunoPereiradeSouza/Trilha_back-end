from collections import defaultdict

from django.core.exceptions import ValidationError


class UserValidator:
    def __init__(self, data, errors=None, ErrorClass=None):
        self.errors = defaultdict(list) if errors is None else errors
        self.ErrorClass = ValidationError if ErrorClass is None else ErrorClass
        self.data = data
        self.clean()
    
    def clean(self):
        cleaned_data = self.data

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')

        if first_name is None:
            self.errors['first_name'].append(
                'first_name must not be empty'
            )
        elif len(first_name) < 3:
            self.errors['first_name'].append(
                'first_name must be greather than 2 letters'
            )
        
        if last_name is None:
            self.errors['last_name'].append(
                'last_name must not be empty'
            )
        elif len(last_name) < 3:
            self.errors['last_name'].append(
                'last_name must be greather than 2 letters'
            )

        if email is None:
            self.errors['email'].append(
                'email must not be empty'
            )   

        if self.errors:
            raise self.ErrorClass(self.errors)
