from django.apps import AppConfig
import products.signals as s

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        import products.templatetags.sharedutils
        s.ready()