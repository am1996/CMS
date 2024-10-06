import os
import uuid

def upload_to(instance: str, filename: str) -> str:
    # Assuming you have a ForeignKey field named 'category' and a custom subfolder name 'documents'
    filename_base, filename_ext = os.path.splitext(filename)
    subfolder_name  = type(instance).__name__
    return f'{instance.product.pk}/{subfolder_name}/{uuid.uuid4()}{filename_ext}'