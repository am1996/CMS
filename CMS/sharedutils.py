import os
import uuid
uuid.uuid4()

def upload_to(instance: str, filename: str,subfolder_name: str) -> str:
    # Assuming you have a ForeignKey field named 'category' and a custom subfolder name 'documents'
    filename_base, filename_ext = os.path.splitext(filename)
    return f'{instance.product.pk}/{subfolder_name}/{uuid.uuid4()}{filename_ext}'