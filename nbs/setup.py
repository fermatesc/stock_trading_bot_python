import os
import sys
import pathlib


NBS_DIR = pathlib.Path(__file__).parent
REPO_DIR = NBS_DIR.parent
DJANGO_BASE_DIR = REPO_DIR / 'src'
DJANGO_SETTINGS_MODULE = 'cfehome'

def init_django(project_name: str= 'cfehome'):
    """Run administrative tasks."""
    os.chdir(DJANGO_BASE_DIR)
    sys.path.insert(0, DJANGO_BASE_DIR)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{project_name}.settings')
    os.environ.setdefault('DJANGO_ALLOW_ASYNC_UNSAFE', 'true')
    import django
    django.setup()
