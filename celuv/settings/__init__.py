import os
from .base import *  # NOQA

if os.environ.get('PROJECT_ENV') == 'production':
    from .production import *  # NOQA
else:
    from .development import *  # NOQA
    # from .production import *  # NOQA
