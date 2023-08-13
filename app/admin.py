# vim: set fileencoding=utf-8 :
from django.contrib import admin

import app.models as models


class FarmerAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'email',
        'owner_name',
        'mobile_number',
        'organization_name',
        'business',
        'detiel',
        'brand_logo',
        'defaultURL',
        'otp',
        'passowrd',
        'ip_address',
        'is_verified',
        'is_founder',
        'is_ceo',
        'is_admin',
        'is_manager',
        'is_head_office',
        'is_hr',
        'is_accountant',
        'is_auditor',
        'is_auditor_manager',
        'is_auditor_head_office',
        'is_employee',
        'is_customer',
        'is_supplier',
        'otp_created_time',
        'password_changes_datatime',
        'login_datetime',
        'logout_datetime',
        'last_activity',
        'created_at',
        'session',
    )
    list_filter = (
        'is_verified',
        'is_founder',
        'is_ceo',
        'is_admin',
        'is_manager',
        'is_head_office',
        'is_hr',
        'is_accountant',
        'is_auditor',
        'is_auditor_manager',
        'is_auditor_head_office',
        'is_employee',
        'is_customer',
        'is_supplier',
        'otp_created_time',
        'password_changes_datatime',
        'login_datetime',
        'logout_datetime',
        'last_activity',
        'created_at',
        'session',
        'id',
        'email',
        'owner_name',
        'mobile_number',
        'organization_name',
        'business',
        'detiel',
        'brand_logo',
        'defaultURL',
        'otp',
        'passowrd',
        'ip_address',
    )
    date_hierarchy = 'created_at'


class FarmAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'village',
        'crop_grown',
        # 'sowing_date',
        'farmer',
        'name',
        'location',
        'description',
        'established_date',
        'latitude',
        'longitude',
    )
    list_filter = (
        # 'sowing_date',
        'farmer',
        'established_date',
        'id',
        'village',
        'crop_grown',
        'name',
        'location',
        'description',
        'latitude',
        'longitude',
    )
    search_fields = ('name',)


class TypeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nutrients',
        'name',
        'type',
        'description',
        'image',
        'price',
        # 'category',
        'origin',
        'created_at',
        'The_highest_appropriate_temperature',
        'effect_of_heat',
        'The_lowest_appropriate_temperature',
        'humidity_soil_highest',
        'humidity_soil_lowest',
        'effect_of_soil_humidity',
        'humidity_weather_highest',
        'humidity_weather_lowest',
        'effect_of_weather_humidity',
        'illumination_highest',
        'illumination_lowest',
        'effect_of_illumination',
        'atmospheric_pressure_highest',
        'atmospheric_pressure_lowest',
        'effect_of_atmospheric_pressure',
    )
    list_filter = (
        'created_at',
        'id',
        'nutrients',
        'name',
        'type',
        'description',
        'image',
        'price',
        # 'category',
        'origin',
        'The_highest_appropriate_temperature',
        'effect_of_heat',
        'The_lowest_appropriate_temperature',
        'humidity_soil_highest',
        'humidity_soil_lowest',
        'effect_of_soil_humidity',
        'humidity_weather_highest',
        'humidity_weather_lowest',
        'effect_of_weather_humidity',
        'illumination_highest',
        'illumination_lowest',
        'effect_of_illumination',
        'atmospheric_pressure_highest',
        'atmospheric_pressure_lowest',
        'effect_of_atmospheric_pressure',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'


class Schedule_detailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        # 'days_after_sowing',f
        # 'Fertiliser',
        # 'quantity',
        # 'quantity_unit',
        'due_date',
        # 'farm',
        # 'name',
        # 'description',
        # 'price',
    )
    list_filter = (
        'due_date',
        'farm',
        # 'id',
        # 'days_after_sowing',
        # 'Fertiliser',
        # 'quantity',
        # 'quantity_unit',
        # 'name',
        # 'description',
        # 'price',
    )
    # raw_id_fields = ('id',)
    # search_fields = ('due_date',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Farmer, FarmerAdmin)
_register(models.Farm, FarmAdmin)
_register(models.Category, TypeAdmin)
_register(models.Schedule_detail, Schedule_detailAdmin)
