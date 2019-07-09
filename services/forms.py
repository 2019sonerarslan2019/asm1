from .models import RevolvingDoor 
from django import forms


class RevolvingDoorForm(forms.ModelForm):
    
    class Meta:
        model = RevolvingDoor

     
        fields = [
            'company',
            'crm_no',
            'adress',
            'delivery_method',
            'dia',
            'trans_height',
            'canopy',
            'total_height',
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
        ]
