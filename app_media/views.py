from django.http import HttpResponse
from django.shortcuts import render

from app_media.forms import UploadFileForm


def upload_file(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=file.name, status=200)
    else:
        form = UploadFileForm()

    return render(request,
                  'media/upload_file.html',
                  {'form': form})
