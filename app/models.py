from django.db import models
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext_lazy as _
from django.contrib.sessions.models import Session
from .manager import UserManager
from django.utils.timezone import now

# Create your models here.
INDUSTRYCHOICES = (
    ("المالك", "المالك"),
    ("تقني", "تقني"),
    ("المدير", "المدير"),
    # ("مسوق", "مسوق"),
    ("مختبر", "مختبر"),
    ("خبير ", "خبير"),
    # ("BUILDING MATERIALS & EQUIPMENT", "BUILDING MATERIALS & EQUIPMENT"),
    # ("CHEMICAL", "CHEMICAL"),
    # ("COMPUTER", "COMPUTER"),
    # ("EDUCATION", "EDUCATION"),
    # ("ELECTRONICS", "ELECTRONICS"),
    # ("ENERGY", "ENERGY"),
    # ("ENTERTAINMENT & LEISURE", "ENTERTAINMENT & LEISURE"),
    # ("FINANCE", "FINANCE"),
    # ("FOOD & BEVERAGE", "FOOD & BEVERAGE"),
    # ("GROCERY", "GROCERY"),
    # ("HEALTHCARE", "HEALTHCARE"),
    # ("INSURANCE", "INSURANCE"),
    # ("LEGAL", "LEGAL"),
    # ("MANUFACTURING", "MANUFACTURING"),
    # ("PUBLISHING", "PUBLISHING"),
    # ("REAL ESTATE", "REAL ESTATE"),
    # ("SERVICE", "SERVICE"),
    # ("SOFTWARE", "SOFTWARE"),
    # ("SPORTS", "SPORTS"),
    # ("TECHNOLOGY", "TECHNOLOGY"),
    # ("TELECOMMUNICATIONS", "TELECOMMUNICATIONS"),
    # ("TELEVISION", "TELEVISION"),
    # ("TRANSPORTATION", "TRANSPORTATION"),
    # ("VENTURE CAPITAL", "VENTURE CAPITAL"),
)


class Farmer(models.Model):
    """ Customize default User model """
    email = models.EmailField(unique=True)
    owner_name = models.CharField(
        verbose_name=_('Owner Name'),
        max_length=50,
    )
    # phone_regex = RegexValidator(regex=r'^(?:\+88|88|+967|967)?(70[3-9]\d{8}|71[3-9]\d{8}|73[3-9]\d{8}|77[3-9]\d{8}|01[3-9]\d{8})$', message="Phone number must be entered in the format: '+9677XXXXXX'. Up to 14 digits allowed.")
    mobile_number = models.CharField(max_length=20, unique=False)
    organization_name = models.CharField(
        verbose_name=_("Farm Name"),
        max_length=50
    )
    business = models.CharField(
        verbose_name=_("Business"),
        max_length=50,
        choices=INDUSTRYCHOICES,
        help_text=_("Select your business type:"),
        null=True, blank=True,
    )
    detiel = models.TextField(
        verbose_name=_('detiel'),
        # max_length=50,
        null=True, blank=True
    )
    # FIXME: dEFAUTL brand logo not showing in UI throughing error inside view.
    brand_logo = CloudinaryField('Brand Logo', null=True, blank=True)

    defaultURL = models.URLField(null=True, blank=True)

    otp = models.SmallIntegerField(
        help_text='One Time Password',
        null=True, blank=True
    )
    passowrd = models.CharField(
        verbose_name=_('passowrd'),
        max_length=100,
        unique=True,
        null=True, blank=True, 
        help_text='passowrd for authentication'
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_('IP Address'),
        help_text='IP Address',
        blank=True, null=True
    )
    is_verified = models.BooleanField(
        _('verified'),
        default=False,
        help_text=_(
            'Designates whether this user has been verified.'
            'Un-verified users cannot log in.'
        ),
    )
    is_founder = models.BooleanField(
        _('founder'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as founder.'
        ),
    )
    is_ceo = models.BooleanField(
        _('ceo'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as CEO.'
        ),
    )
    is_admin = models.BooleanField(
        _('admin'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as admin.'
        ),
    )
    is_manager = models.BooleanField(
        _('manager'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as manager.'
        ),
    )
    is_head_office = models.BooleanField(
        _('head office'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as head office.'
        ),
    )
    is_hr = models.BooleanField(
        _('hr'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as Human resources (HR).'
        ),
    )
    is_accountant = models.BooleanField(
        _('accountant'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as accountant.'
        ),
    )
    is_auditor = models.BooleanField(
        _('auditor'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as auditor.'
        ),

    )
    is_auditor_manager = models.BooleanField(
        _('auditor manager'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as auditor manager.'
        ),
    )
    is_auditor_head_office = models.BooleanField(
        _('auditor head office'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as auditor head office.'
        ),
    )
    is_employee = models.BooleanField(
        _('employee'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as employee.'
        ),
    )
    is_customer = models.BooleanField(
        _('customer'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as customer.'
        ),
    )
    is_supplier = models.BooleanField(
        _('supplier'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as supplier.'
        ),
    )

    # Timestamps fields
    otp_created_time = models.DateTimeField(
        default=now,
        verbose_name=_('OTP created time'),
        editable=False,
    )
    password_changes_datatime = models.DateTimeField(
        verbose_name=_('Password changes datatime'),
        blank=True,
        null=True,
    )
    login_datetime = models.DateTimeField(
        verbose_name=_('Login datetime'),
        blank=True,
        null=True,
    )
    logout_datetime = models.DateTimeField(
        verbose_name=_('Logout datetime'),
        blank=True,
        null=True,
    )
    last_activity = models.DateTimeField(
        verbose_name=_('Last activity'),
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(default=now, editable=False)

    session = models.OneToOneField(Session, on_delete=models.CASCADE, blank=True, null=True)

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_number']

    objects = UserManager()


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Farmer'
        verbose_name_plural = 'Farmers'

class Farm(models.Model):
    # area = models.FloatField(blank=False)  # size
    village = models.CharField(blank=True,null=True, max_length=255)
    crop_grown = models.CharField(blank=True,null=True, max_length=255)
    # sowing_date = models.DateTimeField(auto_now_add=False)
    farmer = models.ForeignKey(Farmer, on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    established_date = models.DateField(auto_now_add=True,blank=True,null=True)
    latitude = models.DecimalField(blank=True,null=True,max_digits=9, decimal_places=9)
    longitude = models.DecimalField(blank=True,null=True,max_digits=9, decimal_places=6)


    def __str__(self):
        return self.name
UNIT_CHOICES = (
    ('ton', 'Ton'),
    ('kg', 'Kilograms'),
    ('g', 'grams'),
    ('L', 'litres'),
    ('mL', 'millitres'),
)
TYPE_CHOICES = (
    ('Fruits', 'Fruits'),
    ('Veggies', 'Veggies'),
    
)

class Category(models.Model):
    name = models.CharField(max_length=100)
        # name = models.CharField(max_length=100)
    type = models.CharField(
        verbose_name=_("Type"),
        max_length=50,
        choices=TYPE_CHOICES,
        help_text=_("Select type:"),
        null=True, blank=True,
    )
    description = models.TextField()
    image = models.ImageField(upload_to='produce_images/')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    # category = models.CharField(max_length=100)
    origin = models.CharField(blank=True, null=True,max_length=100)
    nutrients = models.TextField(blank=True, null=True,auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    The_highest_appropriate_temperature = models.DecimalField(null=True,max_digits=9, decimal_places=2)
    effect_of_heat = models.TextField(blank=True, null=True)
    The_lowest_appropriate_temperature = models.DecimalField(null=True,max_digits=9, decimal_places=2)
    # temperature_range = models.CharField(max_length=100)
    humidity_soil_highest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    humidity_soil_lowest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    effect_of_soil_humidity = models.TextField(blank=True, null=True)
    humidity_weather_highest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    humidity_weather_lowest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    effect_of_weather_humidity = models.TextField(blank=True, null=True)
    illumination_highest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    illumination_lowest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    effect_of_illumination = models.TextField(blank=True, null=True)
    atmospheric_pressure_highest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    atmospheric_pressure_lowest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    effect_of_atmospheric_pressure = models.TextField(blank=True, null=True)
    water_tomperatatur_ighest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    water_tomperatatur_lowest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    effect_water_tomperatatur = models.TextField(blank=True, null=True)

    # illumination = models.CharField(max_length=100)
    # effect = models.TextField()

    def __str__(self):
        return self.name
class Schedule_detail(models.Model):
    days_after_sowing = models.IntegerField(blank=False)
    # Fertiliser = models.CharField(blank=True, max_length=255)
    # quantity = models.IntegerField(blank=False)
    # quantity_unit = models.CharField(choices=UNIT_CHOICES, max_length=10)
    # price = models.FloatField(blank=False, default=0)
    
    # The_highest_appropriate_temperature = models.DecimalField(null=True,max_digits=9, decimal_places=2)
    # effect_of_heat = models.TextField(blank=True, null=True)
    The_appropriate_temperature = models.DecimalField(null=True,max_digits=9, decimal_places=2)
    # temperature_range = models.CharField(max_length=100)
    humidity_soil = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    water_tomperatatur = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    # humidity_soil_lowest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    # effect_of_soil_humidity = models.TextField(blank=True, null=True)
    humidity_weather = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    # humidity_weather_lowest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    # effect_of_weather_humidity = models.TextField(blank=True, null=True)
    illumination = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    # illumination_lowest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    # effect_of_illumination = models.TextField(blank=True, null=True)
    atmospheric_pressure = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    # atmospheric_pressure_lowest = models.DecimalField(blank=True, null=True,max_digits=9,decimal_places=2)
    # effect_of_atmospheric_pressure = models.TextField(blank=True, null=True)

    due_date = models.DateTimeField(auto_now_add=False, null=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, null=True,blank=True)
    # name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return str(Schedule_detail.id)