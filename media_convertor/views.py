import os
import mimetypes
import codecs
import time
import requests

from django.http import HttpResponse
from django.shortcuts import render, redirect

from media_convertor.forms import DocumentForm
from media_convertor.wav2midi import *
from media_convertor.models import Document

def home(request):
    message = ''
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if ("mediafile" in request.FILES):
            inputFile = Document(mediaFile=request.FILES['mediafile'])
            inputFile.save()

            timestr = time.strftime("%Y%m%d-%H%M%S")
            output_filename = f"output_{timestr}.mid"
            output_dir = "/media/"

            input_path = inputFile.mediaFile.path
            output_path = f"{output_dir}{output_filename}"
            if input_path.endswith('.wav'):
                run(input_path, output_path)

                midFile = open(output_path, 'rb')
                response = HttpResponse(midFile, content_type='audio/mid')

                response['Content-Disposition'] = "attachment; filename=%s" % output_filename
                return response
            else:
                message = 'Invalid File Format!'

        elif (form.data['mediaUrl'] != ''): #form.has_media_url():
            url = form.data['mediaUrl']

            timestr = time.strftime("%Y%m%d-%H%M%S")

            input_filename = f"input_{timestr}.wav"
            input_path = f"/media/{input_filename}"

            file_response = requests.get(url)
            if (url.endswith('.wav') and file_response.status_code == 200):
                open(input_path, "wb").write(file_response.content)

                output_filename = f"output_{timestr}.mid"
                output_dir = "/media/"

                output_path = f"{output_dir}{output_filename}"
                run(input_path, output_path)

                midFile = open(output_path, 'rb')
                response = HttpResponse(midFile, content_type='audio/mid')

                response['Content-Disposition'] = "attachment; filename=%s" % output_filename
                return response
            else:
                message = 'Invalid Url!'
                # form = DocumentForm()
        else:
            message = 'Invalid form!'
            # form = DocumentForm()
    else:
        form = DocumentForm()

        # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'home.html', context)