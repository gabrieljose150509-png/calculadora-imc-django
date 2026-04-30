from django.shortcuts import render

def index(request):
    resultado = None
    frase = ""
    
    if request.method == "POST":
        frase = request.POST.get('frase', '')
        # Conta apenas letras, ignorando espaços
        resultado = len(frase.replace(" ", ""))
        
    return render(request, 'contletras/index.html', {
        'resultado': resultado, 
        'frase': frase
    })

    