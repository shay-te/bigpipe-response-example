import os
from django.conf import settings

parent_dir = os.path.abspath(os.pardir)

source_base_path = os.path.join(parent_dir, 'client')
rendered_output_path = os.path.join(parent_dir, 'public')

JS_SOURCE_PATH = [source_base_path]
CSS_SOURCE_PATH = [source_base_path]
RENDERED_OUTPUT_PATH = rendered_output_path
STATIC_URI = settings.STATIC_URL
IS_PRODUCTION_MODE = not settings.DEBUG
