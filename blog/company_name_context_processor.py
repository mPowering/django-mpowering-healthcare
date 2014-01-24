# Django imports
from django.conf import settings


def get_company_name(request):
    return {"company": settings.COMPANY_NAME}
