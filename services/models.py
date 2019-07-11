from django.db import models
from ckeditor.fields import RichTextField


class RevolvingDoor(models.Model):

    company = models.CharField(max_length=300,verbose_name='Firma')
    crm_no = models.CharField(max_length=50,verbose_name='CRM No')
    adress = RichTextField(verbose_name='Sevk Adresi')
    delivery_date = models.DateTimeField(verbose_name='Teslim Tarihi')
    delivery_method = models.CharField(max_length=100,verbose_name='Teslim Şekli')

    dia = models.IntegerField(default=0,verbose_name='Çap')
    trans_height = models.IntegerField(default=0,verbose_name='Geçiş Yüksekliği')
    canopy = models.IntegerField(default=0,verbose_name='Kanopi')
    total_height = models.IntegerField(default=0,verbose_name='Toplam Yükseklik')
    wing = models.IntegerField(default=0,verbose_name='Kanat Sayısı')
    fixed_glass = models.CharField(max_length=100,verbose_name='Sabit Cam')
    moving_glass = models.CharField(max_length=100,verbose_name='Hareketli Cam')
    fixed_glass_no = models.IntegerField(default=0,verbose_name='Sabit Cam Sayısı')
    moving_glass_no = models.IntegerField(default=0,verbose_name='Hareketli Cam Sayısı')
    color = models.CharField(max_length=100,verbose_name='Renk')
    lighting = models.CharField(max_length=50,verbose_name='Işıklandırma')
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
        return self.color

    class Meta:
        verbose_name_plural = 'MR30/SA OTOMATİK DÖNER KAPI'
        ordering = ['-id']