from .models import Category, Store, ContactInfo, Product, ProductCombo, Order
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )


@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('description', 'address' )


@register(ContactInfo)
class ContactInfoTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')


@register(ProductCombo)
class ProductComboTranslationOptions(TranslationOptions):
    fields = ('description', )


@register(Order)
class OrderTranslationOptions(TranslationOptions):
    fields = ('delivery_address', )



















