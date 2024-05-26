from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ["name","age","contact"]
    
    def clean_name(self):
        data = self.cleaned_data.get("name")
    
    def clean_contact(self):
        data = self.cleaned_data.get("contact")
        
        try:
            int(data)
        except ValueError:
            raise forms.ValidationError("telefonni cislo musi obsahovat pouze cislice bez mezer")
            
        
        if len(data) != 9:
            raise forms.ValidationError("Je treba 9 cislic")
        return data
