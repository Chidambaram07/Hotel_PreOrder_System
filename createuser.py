import os
import django

# Ensure the correct settings module is set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HotelPreorderproj.settings')

# Initialize Django
django.setup()

from django.contrib.auth.models import User

# The desired admin password
admin_password = 'admin17935@dj'

try:
    # Try to get the admin user
    user = User.objects.get(username='admin')
    # If user exists, update the password
    user.set_password(admin_password)
    user.save()
    print(f'Admin user exists. Password updated.')
except User.DoesNotExist:
    # Create the admin user if it doesn't exist
    user = User.objects.create_superuser(username='admin', email='admin@dj.com', password=admin_password)
    print(f'Admin user created with password: {admin_password}')
