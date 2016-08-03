from django.shortcuts import render

# Create your views here.
#from nandoodonto.report import write_to_pdf

'''def projeto2pdf(request, slug=None):
    projeto = get_object_or_404(Projeto, slug=slug)
    response = write_to_pdf('template_pdf.html', {'projeto': projeto}, projeto.slug)
    return response
from reportlab.pdfgen import canvas
from django.http import HttpResponse'''

def some_view(request):
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    p = canvas.Canvas(response)

    # Desenhe coisas no PDF. Aqui é onde a geração do PDF acontece.
    # Veja a documentação do ReportLab para a lista completa de
    # funcionalidades.
    p.drawString(100, 100, "Hello world.")

    # Feche o objeto PDF, e está feito.
    p.showPage()
    p.save()
    return response