from django.conf import settings


def project_name(request):
    return {'PROJECT_NAME': getattr(settings, 'PROJECT_NAME', None)}


def footer_info(request):
    return {'FOOTER_INFO': getattr(settings, 'FOOTER_INFO', None)}
