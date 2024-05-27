from django import forms
from .models import Customer, User

class CustomerForm(forms.ModelForm):

    czech_alphabet = "abcdefghijklmnopqrstuvwxyzáčďéěíňóřšťúůýž"

    class Meta:
        model = Customer
        fields = ["given_name","surname","age","contact"]

    def __init__(self, *args, **kwargs):
        
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields["given_name"].label = "Krestni jmeno"
        self.fields["surname"].label = "Prijmeni"
        self.fields["age"].label = "Vek"
        self.fields["contact"].label = "Telefon"
        #self.fields["insurance_type"].label = "Pojistna udalost"
    
    def clean_insurance_type(self):
        data = self.cleaned_data.get("insurance_type")
    
    def clean_given_name(self):
        """
        This violates DRY and I am sure it is possible to
        store validation into a function like in console app, somehow,
        but I don't have time to find out how.
        """
        data = self.cleaned_data.get("given_name")
        
        for letter in data:
            if letter.lower() not in self.czech_alphabet:
                raise forms.ValidationError("Vsechny znaky musi byt soucasti ceske abecedy.")
        if not data[0].isupper():
            raise forms.ValidationError("Prvni pismeno musi byt velke.")
        return data
    
    def clean_surname(self):
        data = self.cleaned_data.get("surname")
        
        for letter in data:
            if letter.lower() not in self.czech_alphabet:
                raise forms.ValidationError("Vsechny znaky musi byt soucasti ceske abecedy.")
        if not data[0].isupper():
            raise forms.ValidationError("Prvni pismeno musi byt velke.")
        
        return data
      
    def clean_contact(self):
        data = self.cleaned_data.get("contact")
        
        try:
            int(data)
        except ValueError:
            raise forms.ValidationError("telefonni cislo musi obsahovat pouze cislice bez mezer.")             
        if len(data) != 9:
            raise forms.ValidationError("Je treba 9 cislic.")
        return data
    

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "password"]

    
class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ["email", "password"]
