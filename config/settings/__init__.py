import os
import glob
from split_settings.tools import include

ENV = os.environ.get('PROJECT_ENV') or 'development'
print('****Running on %s settings****' % ENV)

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
SECRET_KEY = '8q2%@g(#mnf3#41_6961&05shtb1mv*$gu(i-30*5s_m=0364)'

COMPONENT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'components'
)
COMPONENTS = [
    'components/{}'.format(os.path.basename(component)) for component 
    in glob.glob(os.path.join(COMPONENT_DIR, '*.py'))
]
SETTINGS = COMPONENTS + ['environments/%s.py' % ENV]

include(*SETTINGS)
