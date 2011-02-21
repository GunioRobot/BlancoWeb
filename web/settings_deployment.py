# Django settings for blanco project.
import os.path

BASE_PATH = os.path.realpath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SERVER_EMAIL = 'jcorderomartinez@gmail.com'

ADMINS = (
    (u'Javier Cordero Martinez', 'jcorderomartinez@gmail.com'),
)

MANAGERS = ADMINS + (
	(u'Javier Cordero Martinez' 'jcorderomartinez@gmail.com'),
)

EMAIL_SUBJECT_PREFIX = '[BLANCO] '

DATABASE_ENGINE = 'postgresql_psycopg2'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'jneight_blanco'             # Or path to database file if using sqlite3.
DATABASE_USER = 'jneight'             # Not used with sqlite3.
DATABASE_PASSWORD = 'uTkJVvUx'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es-es'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = BASE_PATH+'/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '8o@1v%1aggsql9-%fu&db*3@60b5wefndm@9=i!e*yh^s2t70a'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.csrf.middleware.CsrfMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'blanco.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_PATH+'/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.markup',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'blanco.web.templatetags.tags',
    'django.contrib.flatpages',
    'blanco.compress',
    'blanco.web',
)

DATE_FORMAT="d/m/Y"
TIME_FORMAT="H:i"

# Override the server-derived value of SCRIPT_NAME 
# See http://code.djangoproject.com/wiki/BackwardsIncompatibleChanges#lighttpdfastcgiandothers
FORCE_SCRIPT_NAME = ''

# DJANGO-COMPRESS

COMPRESS = True  
COMPRESS_AUTO = True  
COMPRESS_VERSION = True  
   
COMPRESS_CSS = {  
     'compressed_css': {  
         'source_filenames': ('css/estructura.css','css/base.css','css/estilos.css',),  
         'output_filename': 'all.r?.css',  
         'extra_context': {  
             'media': 'screen,projection',  
         },  
     },  
     'compressed_blueprint': {
         'source_filenames': ('css/blueprint/screen.css','css/blueprint/plugins/fancy-type/screen.css'),
         'output_filename': 'blue.r?.css',
         'extra_context': {
             'media': 'screen,projection',
         },
     },
     'compressed_blueprintP': {
         'source_filenames': ('css/blueprint/print.css',),
         'output_filename': 'blueP.r?.css',
         'extra_context': {
             'media': 'print',
         },
     },
}  
   
COMPRESS_JS = {  
     'group_js': {  
         'source_filenames': ('js/mootools-1.2.4-core-yc.js',),  
         'output_filename': 'js/all.r?.js',
      },
      'ie_js': {
                'source_filenames':('js/ie/IE8.js',),
                'output_filename': 'js/ie.r?.js',
    },
}

IMAGENES_DIR = MEDIA_ROOT+'/imagenes'
IMAGENES_URL = MEDIA_URL+'/imagenes/'
