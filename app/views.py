from django.shortcuts import render
from fpdf import FPDF
from django.http import FileResponse

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context=context)

# Generate certificate
def certificate(request):
    pdf = FPDF('L', 'mm', 'A4')
    pdf.set_title('Certificate Of Completion')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'Certificate Of Completion',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)
    for line in sales:
        pdf.cell(200, 8, f"{line['item'].ljust(30)} {line['amount'].rjust(20)}", 0, 1)

    pdf.output('cert.pdf', 'F')
    return FileResponse(open('cert.pdf', 'rb'), as_attachment=True, content_type='application/pdf')