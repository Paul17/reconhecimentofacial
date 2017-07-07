from django.shortcuts import render
from .forms import UploadImageForm
from django.http import HttpResponse
from .Imagem import Imagem
from PIL import Image

# Create your views here.

def salvarFoto(foto):
    path = 'home/projetoreconhecimentofacial/reconhecimentofacial/modelo/static/uploads/upload.jpg'
    with open(path, 'wb+') as wfoto:
        for chunk in foto.chunks():
            wfoto.write(chunk)
    img = Imagem('modelo/static/uploads/upload.jpg')
    img.marcarFace()
    img.SalvarImagem(path)
    return path



def index(request):
    data={}
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            foto = request.FILES['arquivo']
            data['path'] = salvarFoto(foto)
            return render(request, 'views/principal.html',data)
    else:
        form = UploadImageForm()
    data['form'] = form
    data['path'] = None
    return render(request, 'views/principal.html',data)

