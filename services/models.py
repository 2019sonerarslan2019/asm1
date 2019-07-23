from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

fixed_glass_data = (
    ('4+4 Bombeli Şeffaf Lamine','4+4 Bombeli Şeffaf Lamine'),
    ('5+5 Bombeli Şeffaf Lamine','5+5 Bombeli Şeffaf Lamine'),
    ('6+6 Bombeli Şeffaf Lamine','6+6 Bombeli Şeffaf Lamine'),
    ('4+4 Bombeli Opak Lamine','4+4 Bombeli Opak Lamine'),
    ('5+5 Bombeli Opak Lamine','5+5 Bombeli Opak Lamine'),
    ('6+6 Bombeli Opak Lamine','6+6 Bombeli Opak Lamine'),
)
moving_glass_data = (
    ('8 mm Temperli','8 mm Temperli'),
    ('10 mm Temperli','10 mm Temperli')
)

color_data = (
    ('Ral Boya','Ral Boya'),
    ('Mat Eloksal','Mat Eloksal'),
    ('Renkli Mat Eloksal','Renkli Mat Eloksal'),
    ('304 Kalite Mat','304 Kalite Mat'),
    ('304 Kalite Ayna','304 Kalite Ayna'),
    ('304 Kalite Satina','304 Kalite Satina'),
    ('316 Kalite Mat','316 Kalite Mat'),
    ('316 Kalite Ayna','316 Kalite Ayna'),
    ('316 Kalite Satina','316 Kalite Satina'),

)

lighting_data = (
    ('Halojen Spot Camlı','Halojen Spot Camlı'),
    ('Halojen Spot Camsız','Halojen Spot Camsız'),
    ('Led Spot','Led Spot'),
)

win_data = (
    (3,3),
    (4,4),
)

mr30_type_data = (
    ('OTOMATİK','OTOMATİK'),
    ('MANUEL','MANUEL'),
)

class RevolvingDoor(models.Model):
    
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    company = models.CharField(max_length=300,verbose_name='Firma')
    crm_no = models.IntegerField(default=0,verbose_name="CRM NO")
    adress = models.CharField(max_length=500,verbose_name='Sevk Adresi')
    delivery_date = models.DateTimeField(verbose_name='Teslim Tarihi')
    delivery_method = models.CharField(max_length=100,verbose_name='Teslim Şekli')

    mr30_type = models.CharField(default='OTOMATİK',max_length=30,choices=mr30_type_data,verbose_name='MR30 Kapı Türü')

    dia = models.IntegerField(default=1600, validators=[MinValueValidator(1600), MaxValueValidator(4000)],verbose_name='Çap')
    trans_height = models.IntegerField(default=1900, validators=[MinValueValidator(1900), MaxValueValidator(4000)],verbose_name='Geçiş Yüksekliği')
    canopy = models.IntegerField(default=100, validators=[MinValueValidator(100), MaxValueValidator(1500)],verbose_name='Kanopi')
    wing = models.IntegerField(default=3,choices=win_data,verbose_name='Kanat Sayısı')
    fixed_glass = models.CharField(max_length=100,verbose_name='Sabit Cam',choices=fixed_glass_data,default='4bombeliseffaflamine')
    moving_glass = models.CharField(max_length=100,verbose_name='Hareketli Cam',choices=moving_glass_data,default='8mmtemperli')
    color = models.CharField(max_length=100,verbose_name='Renk',choices=color_data,default='mateloksal')
    ral_color_code = models.CharField(blank=True,null=True,max_length=100,verbose_name='Ral Boya İçin Renk Kodu')
    lighting = models.CharField(max_length=50,verbose_name='Işıklandırma',choices=lighting_data,default='ledspot')
    broken_wing = models.BooleanField(default=False,verbose_name='Kırılan Kanat')
    ground_circle = models.BooleanField(default=False,verbose_name='Yer Çemberi')
    night_sensor =  models.BooleanField(default=False,verbose_name='Gece Kalkanı')  
    heel_sensor = models.BooleanField(default=False,verbose_name='Topuk Sensörü')
    hand_sensor = models.BooleanField(default=False,verbose_name='El Sensörü')
    spot_scan = models.BooleanField(default=False,verbose_name='Spot Scan')
    spain_key = models.BooleanField(default=False,verbose_name='İspanyolet Kilit')
    stain_arm = models.BooleanField(default=False,verbose_name='Paslanmaz Kol')
    button_pole = models.BooleanField(default=False,verbose_name='Buton Direği')

    notes = RichTextField(blank=True,null=True,verbose_name='Notlar')

    drawing = models.CharField(max_length=200,verbose_name='Hazırlayan')
    control = models.CharField(blank=True,max_length=200,verbose_name='Kontrol')
    manufacturing_chief = models.CharField(blank=True,max_length=200,verbose_name='İmalat Şefi')  

    published_date = models.DateTimeField(auto_now_add=True,verbose_name='Oluşturulduğu Tarih')

    def __str__(self):
        return self.company


    class Meta:
        verbose_name_plural = 'MR30/SA DÖNER KAPI'
        ordering = ['-id']




