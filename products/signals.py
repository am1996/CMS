from django.apps import apps
from django.db.models.signals import post_delete
import os
from django.dispatch import receiver
import importlib
import inspect
from django.db import models

@receiver(post_delete)
def _post_save_receiver(sender, instance,**kwargs):
    if hasattr(instance,"attachment"):
        if os.path.isfile(instance.attachment.path):
            os.remove(instance.attachment.path)


def connect_post_delete_signal_to_all_models():
    # Get all installed apps
    for app_config in apps.get_app_configs():
        # Import the models module dynamically from each app
        try:
            models_module = importlib.import_module(f'{app_config.name}.models')
        except ModuleNotFoundError:
            continue  # If app doesn't have a models module, continue to the next

        # Use inspect.getmembers() to get all model classes
        for name, obj in inspect.getmembers(models_module):
            # Check if the object is a subclass of Django's Model (but not the base Model itself)
            if inspect.isclass(obj) and issubclass(obj, models.Model):
                # Connect the post_delete signal to the model
                post_delete.connect(_post_save_receiver, sender=obj)

def ready():
    connect_post_delete_signal_to_all_models()