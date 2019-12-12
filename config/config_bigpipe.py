import os
from django.conf import settings

parent_dir = os.path.abspath(os.pardir)

client_base_path = os.path.join(parent_dir, 'client')
rendered_output_path = os.path.join(parent_dir, 'public')

CLIENT_BASE_PATH = [client_base_path]
RENDERED_OUTPUT_PATH = rendered_output_path
STATIC_URI = settings.STATIC_URL
IS_PRODUCTION_MODE = not settings.DEBUG
