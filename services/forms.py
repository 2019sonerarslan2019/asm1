from .models import RevolvingDoor 
from django import forms



class RevolvingDoorForm(forms.ModelForm):
    delivery_date = forms.DateTimeField(widget = forms.SelectDateWidget,label="Teslim Tarihi")

    class Meta:
        model = RevolvingDoor

     
        fields = [
            'company',
            'adress',
            'delivery_method',
            'delivery_date',
            'dia',
            'trans_height',
            'canopy',
            'wing',
            'fixed_glass',
            'fixed_glass_no',
            'moving_glass',
            'moving_glass_no',
            'color',
            'lighting',
            'broken_wing',
            'ground_circle',
            'night_sensor',
            'heel_sensor',
            'hand_sensor',
            'spot_scan',
            'spain_key',
            'stain_arm',
            'button_pole',
            'notes',
            'drawing',
            'control',
            'manufacturing_chief',
        ]


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=300,label="Başlık")
    to = forms.EmailField(label="Email")
    