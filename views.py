from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .forms import QRCodeForm
import qrcode
import os
import qrcode.image.svg


def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurent_name']
            url = form.cleaned_data['url']

            # Here you would generate the QR code and save it to a file
            qr=qrcode.make(url) 
            file_name = res_name.replace(" ", "_").lower() + '_menu.png'

            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)

            qr_url = os.path.join(settings.MEDIA_URL, file_name)
            context = {
                'res_name': res_name,
                'qr_url': qr_url,
                'file_name': file_name,
            }
            return render(request,'qr_result.html',context)
           
    else:
        form = QRCodeForm()
        context = {
            'form': form,
        }
        return render(request, 'generate_qr_code.html', context)
   