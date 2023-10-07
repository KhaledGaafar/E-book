from django import forms

from .models import book


class productModelForm(forms.ModelForm):
    class Meta:
        model = book
        fields= '__all__'


    def clean_name(self):
        name = self.cleaned_data['name']
        if book.objects.filter(name=name).exists():
            raise forms.ValidationError("This products already exists")

        return name
    


#class borrowbookform(forms.ModelForm):
    #class Meta:
        model = borrowbook
        fields = ['name']