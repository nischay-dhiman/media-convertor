
from django.shortcuts import render


from media_convertor.wav2midi import *

def home(request):
    return render(request, 'home.html')


def convert(request):

    # Uploads -> temp file -> DB -> file_path -> CONVERSION PROCESS -> output_path

    input_path = "assets/input.wav"
    output_path = "assets/output.mid"

    run(input_path, output_path)

    url = output_path
    return render(request, 'convert.html')



# OPEN SOURCE CODE
