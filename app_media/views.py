from django.http import HttpResponse
from django.shortcuts import render, redirect

from app_media.forms import UploadFileForm, DocumentForm


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


def model_form_upload(request):

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()

    return render(request,
                  'media/file_form_upload.html',
                  {'form': form})
