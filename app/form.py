from django.forms import ModelForm
from django import forms
# from phonenumber_fielfrom phonenumber_field.formfields import PhoneNumberField
# from phonenumber_field.widgets import PhoneNumberPrefixWidget
# from phonenumber_field.modelfields import PhoneNumberField

from .models import Farmer,Farm
from datetime import datetime
from django.utils.translation import gettext_lazy as _


class FarmerForm(ModelForm):
    # notes = forms.TextInput(required=True)
    # notes = forms.CharField(required=True)
    # widget=forms.TextInput(attrs={'placeholder': 'notes'}))
    # close_date = forms.DateTimeField(initial=datetime.now,label=_("close at"), required=False,)
    # open_date = forms.DateTimeField(
        # initial=datetime.now, required=False, label=_("open at"))
    # RegionalPhoneNumberWidget is the default widget.
  

    class Meta:
        model = Farmer
        widgets = {
            
            # widgets = {
                "detiel": forms.Textarea(attrs={ "class": "form-control"}),
                "deactivate": forms.CheckboxInput(attrs={"class": "form-control"}),

        }
        icons = {'passowrd': 'bi bi-pass-fill ',
                #  'active': 'fas fa-lock',
                #  'deactivate': 'bi bi-phone ',
                #  'title': 'bi bi-phone ',
                 'owner_name': 'bi bi-person-circle ',
                 'detiel': 'bi bi-person-circle ',
                 'email': 'bi bi-envelope ',
                 'mobile_number': 'bi bi-phone ',
                 'brand_logo': 'bi bi-card-image ',
                 'business': 'bi bi-building-fill ',
                #  'street': 'bi bi-phone ',
                 'organization_name': 'bi bi-building-add ',
                #  'city': 'bi bi-phone ',
                #  'region': 'bi bi-phone ',
                #  'postcode': 'bi bi-phone ',
                #  'country': 'bi bi-phone ',
                #  'website': 'bi bi-phone ',
                #  'description': 'bi bi-phone ',
                #  'account_name': 'bi bi-phone ',
                #  'opportunity_amount': 'bi bi-phone ',
                #  'is_active': 'bi bi-phone ',
                #  'enquiry_type': 'bi bi-phone ',
                #  'created_from_site': 'bi bi-phone ',
                #  'org': 'bi bi-phone ',
                #  'company': 'bi bi-phone ',
                #  'skype_ID': 'bi bi-phone ',
                #  'industry': 'bi bi-phone ',
                #  'organization': 'bi bi-phone ',
                #  'close_date': 'bi bi-phone ',
                #  'source': 'bi bi-phone ',
                #  'linkedin': 'bi bi-phone ',
                #  'twitter': 'bi bi-phone ',
                #  'spend': 'bi bi-phone ',
                #  'state': 'bi bi-phone ',
                #  'value': 'bi bi-phone ',
                #  'uniqueid': 'bi bi-phone ',
                #  'budget': 'bi bi-phone ',
                #  'open_date':'bi bi-phone ',
                #  'facebook': 'bi bi-phone ',
                #  'priority': 'bi bi-phone ',
                #  'companyemail': 'bi bi-phone ',
                #  'companyindustry': 'bi bi-phone ',
                #  'companyname': 'bi bi-phone ',
                #  'companyphone': 'bi bi-phone ',
                #  'addressline1': 'bi bi-phone ',
                #  'companysize': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 }

        fields = [
            #  'id',
        'owner_name',
        'email',
        'mobile_number',
        'organization_name',
        'business',
        'detiel',
        'brand_logo',
        # 'defaultURL',
        # 'otp',
        'passowrd',
        # 'ip_address',
        # 'is_verified',
        # 'is_founder',
        # 'is_ceo',
        # 'is_admin',
        # 'is_manager',
        # 'is_head_office',
        # 'is_hr',
        # 'is_accountant',
        # 'is_auditor',
        # 'is_auditor_manager',
        # 'is_auditor_head_office',
        # 'is_employee',
        # 'is_customer',
        # 'is_supplier',
        # 'password_changes_datatime',
        # 'login_datetime',
        # 'logout_datetime',
        # 'last_activity',
        # 'session',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', dict())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]

class FarmerLoginForm(ModelForm):
    # notes = forms.TextInput(required=True)
    # notes = forms.CharField(required=True)
    # widget=forms.TextInput(attrs={'placeholder': 'notes'}))
    # close_date = forms.DateTimeField(initial=datetime.now,label=_("close at"), required=False,)
    # open_date = forms.DateTimeField(
        # initial=datetime.now, required=False, label=_("open at"))
    # RegionalPhoneNumberWidget is the default widget.
  

    class Meta:
        model = Farmer
        widgets = {
            
            # widgets = {
                "detiel": forms.Textarea(attrs={ "class": "form-control"}),
                "deactivate": forms.CheckboxInput(attrs={"class": "form-control"}),

        }
        icons = {'passowrd': 'bi bi-pass-fill ',
                #  'active': 'fas fa-lock',
                #  'deactivate': 'bi bi-phone ',
                #  'title': 'bi bi-phone ',
                #  'owner_name': 'bi bi-person-circle ',
                #  'detiel': 'bi bi-person-circle ',
                 'email': 'bi bi-envelope ',
                #  'mobile_number': 'bi bi-phone ',
                #  'brand_logo': 'bi bi-card-image ',
                #  'business': 'bi bi-building-fill ',
                #  'street': 'bi bi-phone ',
                #  'organization_name': 'bi bi-building-add ',
                #  'city': 'bi bi-phone ',
                #  'region': 'bi bi-phone ',
                #  'postcode': 'bi bi-phone ',
                #  'country': 'bi bi-phone ',
                #  'website': 'bi bi-phone ',
                #  'description': 'bi bi-phone ',
                #  'account_name': 'bi bi-phone ',
                #  'opportunity_amount': 'bi bi-phone ',
                #  'is_active': 'bi bi-phone ',
                #  'enquiry_type': 'bi bi-phone ',
                #  'created_from_site': 'bi bi-phone ',
                #  'org': 'bi bi-phone ',
                #  'company': 'bi bi-phone ',
                #  'skype_ID': 'bi bi-phone ',
                #  'industry': 'bi bi-phone ',
                #  'organization': 'bi bi-phone ',
                #  'close_date': 'bi bi-phone ',
                #  'source': 'bi bi-phone ',
                #  'linkedin': 'bi bi-phone ',
                #  'twitter': 'bi bi-phone ',
                #  'spend': 'bi bi-phone ',
                #  'state': 'bi bi-phone ',
                #  'value': 'bi bi-phone ',
                #  'uniqueid': 'bi bi-phone ',
                #  'budget': 'bi bi-phone ',
                #  'open_date':'bi bi-phone ',
                #  'facebook': 'bi bi-phone ',
                #  'priority': 'bi bi-phone ',
                #  'companyemail': 'bi bi-phone ',
                #  'companyindustry': 'bi bi-phone ',
                #  'companyname': 'bi bi-phone ',
                #  'companyphone': 'bi bi-phone ',
                #  'addressline1': 'bi bi-phone ',
                #  'companysize': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 }

        fields = [
            #  'id',
        # 'owner_name',
        'email',
        # 'mobile_number',
        # 'organization_name',
        # 'business',
        # 'detiel',
        # 'brand_logo',
        # 'defaultURL',
        # 'otp',
        'passowrd',
        # 'ip_address',
        # 'is_verified',
        # 'is_founder',
        # 'is_ceo',
        # 'is_admin',
        # 'is_manager',
        # 'is_head_office',
        # 'is_hr',
        # 'is_accountant',
        # 'is_auditor',
        # 'is_auditor_manager',
        # 'is_auditor_head_office',
        # 'is_employee',
        # 'is_customer',
        # 'is_supplier',
        # 'password_changes_datatime',
        # 'login_datetime',
        # 'logout_datetime',
        # 'last_activity',
        # 'session',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', dict())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]




class FarmForm(ModelForm):
    # notes = forms.TextInput(required=True)
    # notes = forms.CharField(required=True)
    # widget=forms.TextInput(attrs={'placeholder': 'notes'}))
    # close_date = forms.DateTimeField(initial=datetime.now,label=_("close at"), required=False,)
    # open_date = forms.DateTimeField(
        # initial=datetime.now, required=False, label=_("open at"))
    # RegionalPhoneNumberWidget is the default widget.
  

    class Meta:
        model = Farm
        # widgets = {
            
        #     # widgets = {
        #         "detiel": forms.Textarea(attrs={ "class": "form-control"}),
        #         "deactivate": forms.CheckboxInput(attrs={"class": "form-control"}),

        # }
        icons = {'passowrd': 'bi bi-pass-fill ',
                #  'active': 'fas fa-lock',
                #  'deactivate': 'bi bi-phone ',
                #  'title': 'bi bi-phone ',
                #  'owner_name': 'bi bi-person-circle ',
                #  'detiel': 'bi bi-person-circle ',
                 'email': 'bi bi-envelope ',
                #  'mobile_number': 'bi bi-phone ',
                #  'brand_logo': 'bi bi-card-image ',
                #  'business': 'bi bi-building-fill ',
                #  'street': 'bi bi-phone ',
                #  'organization_name': 'bi bi-building-add ',
                #  'city': 'bi bi-phone ',
                #  'region': 'bi bi-phone ',
                #  'postcode': 'bi bi-phone ',
                #  'country': 'bi bi-phone ',
                #  'website': 'bi bi-phone ',
                #  'description': 'bi bi-phone ',
                #  'account_name': 'bi bi-phone ',
                #  'opportunity_amount': 'bi bi-phone ',
                #  'is_active': 'bi bi-phone ',
                #  'enquiry_type': 'bi bi-phone ',
                #  'created_from_site': 'bi bi-phone ',
                #  'org': 'bi bi-phone ',
                #  'company': 'bi bi-phone ',
                #  'skype_ID': 'bi bi-phone ',
                #  'industry': 'bi bi-phone ',
                #  'organization': 'bi bi-phone ',
                #  'close_date': 'bi bi-phone ',
                #  'source': 'bi bi-phone ',
                #  'linkedin': 'bi bi-phone ',
                #  'twitter': 'bi bi-phone ',
                #  'spend': 'bi bi-phone ',
                #  'state': 'bi bi-phone ',
                #  'value': 'bi bi-phone ',
                #  'uniqueid': 'bi bi-phone ',
                #  'budget': 'bi bi-phone ',
                #  'open_date':'bi bi-phone ',
                #  'facebook': 'bi bi-phone ',
                #  'priority': 'bi bi-phone ',
                #  'companyemail': 'bi bi-phone ',
                #  'companyindustry': 'bi bi-phone ',
                #  'companyname': 'bi bi-phone ',
                #  'companyphone': 'bi bi-phone ',
                #  'addressline1': 'bi bi-phone ',
                #  'companysize': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 #  'notes': 'bi bi-phone ',
                 }

        fields = [
            #  'id',
        # 'owner_name',
         'village',
        'crop_grown',
        # 'sowing_date',
        # 'farmer',
        'name',
        'location',
        'description',
        # 'established_date',
        'latitude',
        'longitude',
        # 'ip_address',
        # 'is_verified',
        # 'is_founder',
        # 'is_ceo',
        # 'is_admin',
        # 'is_manager',
        # 'is_head_office',
        # 'is_hr',
        # 'is_accountant',
        # 'is_auditor',
        # 'is_auditor_manager',
        # 'is_auditor_head_office',
        # 'is_employee',
        # 'is_customer',
        # 'is_supplier',
        # 'password_changes_datatime',
        # 'login_datetime',
        # 'logout_datetime',
        # 'last_activity',
        # 'session',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icons = getattr(self.Meta, 'icons', dict())
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label
            # field.widget.attrs['maxlength'] = 255
            # add form-control class to all fields
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['style'] = 'display: block !important;'

            # set icon attr on field object
            if field_name in icons:
                field.icon = icons[field_name]
