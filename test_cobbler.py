#!/usr/bin/python
"""cobbler sample test against portal"""

import sys
from portal.cobbler import Cobbler
from django.core.management import setup_environ
import nuages.settings
setup_environ(nuages.settings)
from portal.models import *

profile = 'basic6'

profile = Profile.objects.get(name=profile)
cobblerprovider = profile.cobblerprovider
cobblerhost, cobbleruser, cobblerpassword = cobblerprovider.host, cobblerprovider.user, cobblerprovider.password
c = Cobbler(cobblerhost,cobbleruser, cobblerpassword)
#print c.checkprofile(profile)
print c.removemac(['00:1a:4a:a8:01:3a'])
#print c.classes()
sys.exit(0)
