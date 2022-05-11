from django.contrib import admin
from .models import ExtendUser
from django.apps import apps
from django.contrib.admin import AdminSite


admin.site.register(ExtendUser)

# registers all models from graphql_auth to admin site
app = apps.get_app_config('graphql_auth')

for model_name, model in app.models.items():
    admin.site.register(model)


AdminSite.enable_nav_sidebar = False