#!/usr/bin/env python
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_django.settings')
django.setup()

from django.contrib.auth import authenticate
from accounts.models import CustomUser

# Test authentication
user = authenticate(username='testuser', password='testpass123')
print(f'Authentication successful: {user is not None}')
if user:
    print(f'User: {user.username}, Email: {user.email}')
else:
    print('Authentication failed')
