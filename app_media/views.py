from django.http import HttpResponse
from django.shortcuts import render, redirect

from app_media.forms import UploadFileForm, DocumentForm, MultiUploadFileForm
from app_media.models import File


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


def upload_files(request):

    if request.method == 'POST':
        form = MultiUploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('file_field')

            for file in files:
                instance = File(file=file)
                instance.save()
            return redirect('/')
    else:
        form = MultiUploadFileForm()

    return render(request,
                  'media/upload_files.html',
                  {'form': form})
