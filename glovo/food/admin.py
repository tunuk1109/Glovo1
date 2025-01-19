from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

@admin.register(Category, Order)
class AllAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ContactInfoInline(admin.StackedInline, TranslationInlineModelAdmin):
    model = ContactInfo
    extra = 1

class ProductInline(admin.StackedInline, TranslationInlineModelAdmin):
    model = Product
    extra = 1

class ProductComboInline(admin.StackedInline, TranslationInlineModelAdmin):
    model = ProductCombo
    extra = 1

@admin.register(Store)
class StoreAdmin(TranslationAdmin):
    inlines = [ContactInfoInline, ProductInline, ProductComboInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(CarItem)
admin.site.register(Burgers)
admin.site.register(Courier)
admin.site.register(ReviewStore)
admin.site.register(RatingCourier)

