from django.shortcuts import render

def calcular_imc(request):
    resultado = None
    classificacao = ""
    
    if request.method == 'POST':
        peso = float(request.POST.get('peso'))
        altura = float(request.POST.get('altura'))
        try:
            
            imc = peso / (altura ** 2)

        except ZeroDivisionError:
            return render(request, 'calculadora/index.html',
                {
                    'resultado' : 'ERRO',
                    'classificação' : 'A altura nao pode ser 0'
                }
            )
            
        resultado = round(imc, 2)
        
        # Lógica de Classificação
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc >= 18.5 and imc < 24.9:
            classificacao = "Peso normal"
        elif imc >= 25.0 and imc < 29.9:
            classificacao = "Sobrepeso"
        elif imc >= 30.0 and imc < 34.9:
            classificacao = "Obesidade Grau I"
        elif imc >= 35.0 and imc < 39.9:
            classificacao = "Obesidade Grau II"
        else:
            classificacao = "Obesidade Grau III (Mórbida)"
    
    return render(request, 'calculadora/index.html', 
	    {
        'resultado': resultado, 
        'classificacao': classificacao
	    }
    )
def pagina1(x=None):
    return render(x, 'calculadora/index2.html')

def pagina3(x=None):
    return render(x, 'calculadora/index3.html')

def conversor_graus_kelvin(request):
    result = None
    if request.method == 'POST':
        graus = float(request.POST.get('graus'))

        kelvin = graus +  273.15

        result = round(kelvin, 2)
    return  render(request, 'calculadora/index4.html',
        {
            'result' : result
        }               
    )


# conversor_graus_kelvin(100)

