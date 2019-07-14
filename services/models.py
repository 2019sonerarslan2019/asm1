from django.db import models
from ckeditor.fields import RichTextField


fixed_glass_data = (
    ('4bombeliseffaflamine','4+4 Bombeli Şeffaf Lamine'),
    ('4bombeliseffaflamine','5+5 Bombeli Şeffaf Lamine'),
    ('4bombeliseffaflamine','6+6 Bombeli Şeffaf Lamine'),
    ('4bombeliopaklamine','4+4 Bombeli Opak Lamine'),
    ('4bombeliopaklamine','5+5 Bombeli Opak Lamine'),
    ('4bombeliopaklamine','6+6 Bombeli Opak Lamine'),
)
moving_glass_data = (
    ('8mmtemperli','8 mm Temperli'),
    ('10mmtemperli','10 mm Temperli')
)

color_data = (
    ('ralboya','Ral Boya'),
    ('mateloksal','Mat Eloksal'),
    ('renklimateloksal','Renkli Mat Eloksal'),
    ('304kalitemat','304 Kalite Mat'),
    ('304kaliteayna','304 Kalite Ayna'),
    ('304kalitesatina','304 Kalite Satina'),
    ('316kalitemat','316 Kalite Mat'),
    ('316kaliteayna','316 Kalite Ayna'),
    ('316kalitesatina','316 Kalite Satina'),

)

lighting_data = (
    ('halojenspotcamli','Halojen Spot Camlı'),
    ('halojenspotcamsiz','Halojen Spot Camsız'),
    ('ledspot','Led Spot'),
)

class RevolvingDoor(models.Model):

    company = models.CharField(max_length=300,verbose_name='Firma')
    adress = RichTextField(verbose_name='Sevk Adresi')
    delivery_date = models.DateTimeField(verbose_name='Teslim Tarihi')
    delivery_method = models.CharField(max_length=100,verbose_name='Teslim Şekli')

    dia = models.IntegerField(default=0,verbose_name='Çap')
    trans_height = models.IntegerField(default=0,verbose_name='Geçiş Yüksekliği')
    canopy = models.IntegerField(default=0,verbose_name='Kanopi')
    wing = models.IntegerField(default=0,verbose_name='Kanat Sayısı')
    fixed_glass = models.CharField(max_length=100,verbose_name='Sabit Cam',choices=fixed_glass_data,default='4bombeliseffaflamine')
    moving_glass = models.CharField(max_length=100,verbose_name='Hareketli Cam',choices=moving_glass_data,default='8mmtemperli')
    fixed_glass_no = models.IntegerField(default=0,verbose_name='Sabit Cam Sayısı')
    moving_glass_no = models.IntegerField(default=0,verbose_name='Hareketli Cam Sayısı')
    color = models.CharField(max_length=100,verbose_name='Renk',choices=color_data,default='mateloksal')
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
    

    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = 'MR30/SA OTOMATİK DÖNER KAPI'
        ordering = ['-id']




