from datetime import datetime

from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.formats import date_format


def translation(request, *args, **kwargs):
    return render(request,
                  'translation.html')


def greetings_page(request, *args, **kwargs):
    greetings_message = _('Привет! Сегодня %(date)s %(time)s') % {
        'date': date_format(datetime.now().date(), format='SHORT_DATE_FORMAT', use_l10n=True),
        'time': datetime.now().time()
    }

    return render(request,
                  'greetings.html',
                  context={
                      'greetings_message': greetings_message
                  })


def welcome(request, *args, **kwargs):
    return render(request, 'welcome.html')


def main(request, *args, **kwargs):
    return render(request, 'main.html')
