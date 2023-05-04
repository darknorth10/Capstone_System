from django.shortcuts import render
from django.http import JsonResponse
from .models import Transaction, Item

from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib import fonts, pagesizes
from reportlab.lib.units import inch, mm
import io

# Create your views here.
 
def sales_transaction(request):
  transactions = Transaction.objects.all().order_by('-transaction_no')
  payments = Transaction.objects.all()

  if request.method == 'POST':
    return JsonResponse({'success': True}, status=200)
  # transaction_no = 0
  context = {'transactions': transactions, 'payments': payments}

  return render(request, 'UserInterface/transactions/sales_transaction.html', context)

#receipt table
def view_detailed(request, id):
  item = Item.objects.filter(transaction_no=id)
  return render(request, 'UserInterface/transactions/detailed_transaction.html', context = {'items': item})

def payment_info(request):
  payment = Transaction.objects.all().order_by('-transaction_no')
  installment = Transaction.objects.filter(installment='true').order_by('-transaction_no')
  return render(request, 'UserInterface/transactions/payment_info.html', context = {'payment': payment, 'installment': installment,})


def generate_receipt_pdf(request, transaction_no):

  items = Item.objects.filter(transaction_no=transaction_no)
  trans = Transaction.objects.get(transaction_no=transaction_no)
  buf = io.BytesIO()

  #pdf object
  p = canvas.Canvas(buf, pagesize=(176, 400), bottomup=0)
  
  #draw to canvas
  txtobj = p.beginText()
  txtobj.setTextOrigin(15, 20)
  txtobj.setFont('Courier', 7)

  txtobj.textLine('Receipt : Transaction # ' + str(transaction_no))
  p.drawText(txtobj)

  txtobj = p.beginText()
  txtobj.setTextOrigin(15, 40)
  txtobj.setFont('Courier', 5)
  

  lines = [
    "-------------------------------------------------",
  ]
  txtobj.setFont('Courier', 5)
  for item in items:
    lines.append(" ")

    lines.append(f"Product Name :         { item.name }")
    lines.append(f"Product Size :         { str(item.size) }")
    lines.append(f"Quantity :             { str(item.pieces) }")
    lines.append(f"Subtotal :             { str(item.total) }")

    lines.append(" ")

  for line in lines:
    txtobj.textLine(line)
  
  txtobj.textLine("-------------------------------------------------")

  #close and save
  p.drawText(txtobj)

  txtobj.setFont('Courier', 6)

  if trans.installment == "false":
    txtobj.textLine("Date                     " + str(trans.date_of_purchace.date() ))
    txtobj.textLine("Total                    " + str(trans.total_price))
    txtobj.textLine("Cash Paid                " + str(trans.amount ))
    txtobj.textLine("Change                   " + str(trans.change ))
    p.drawText(txtobj)
  else:
    txtobj.textLine("Date:                  " + str(trans.date_of_purchace.date() ))
    txtobj.textLine("Total:                 " + str(trans.total_price))
    txtobj.textLine("Downpayment:           " + str(trans.amount ))
    txtobj.textLine("Balance:               " + str(trans.total_price - trans.amount ))
    p.drawText(txtobj)

  p.showPage()
  p.save()

  # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
  buf.seek(0)

  return FileResponse(buf, as_attachment=True, filename=f'receipt#{trans.transaction_no }.pdf')