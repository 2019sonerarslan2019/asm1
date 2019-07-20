from .models import RevolvingDoor 
from django import forms



class RevolvingDoorForm(forms.ModelForm):
    delivery_date = forms.DateTimeField(widget = forms.SelectDateWidget,label="Teslim Tarihi")

    class Meta:
        model = RevolvingDoor

        fields = [
            'company',
            'crm_no',
            'adress',
            'delivery_method',
            'delivery_date',
            'mr30_type',
            'dia',
            'trans_height',
            'canopy',
            'wing',
            'fixed_glass',
            'moving_glass',
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

