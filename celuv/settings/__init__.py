import os
from .base import *  # NOQA

if 'RDS_DB_NAME' in os.environ:
    from .production import *  # NOQA
else:
    # from .development import *  # NOQA
    from .production import *  # NOQA
