import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "backend_bistro_project.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW

from backend_bistro_app.models import *
hue = CustomerOrder.objects.all()
hue.delete()

hue2 = OrderItem.objects.all()
hue2.delete()




