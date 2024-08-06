from django.shortcuts import render


def translation(request, *args, **kwargs):
    return render(request,
                  'translation.html')
