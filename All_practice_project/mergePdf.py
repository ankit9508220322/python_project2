from PyPDF2 import PdfWriter

merge = PdfWriter()
pdfs = []
n =int(input("how to murze pdf do want to \n"));

for i in range(0 , n):
    name  = input(f"enter the name of pdf {i + 1}:")
    pdfs.append(name)

for pdf in pdfs:
    merge.append(pdf)
merge.write("merge-pdf.pdf")
merge.close()

# ///////////////////////////////////////////////////////////////
from PyPDF2 import PdfWriter

merge = PdfWriter()
n = int(input("how many pdf do you want to merge?\n"))

for i in range(n):
    name = input(f"enter the name of pdf {i+1}: ")
    merge.append(name)   # Directly add PDF
                         # No need to store in list

merge.write("merge-pdf.pdf")
merge.close()
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

from PyPDF2 import PdfWriter

try:
    addPdf = PdfWriter()
    n = int(input("How many PDFs do you want to merge? "))

    for i in range(n):
        name = input(f"Enter the name of PDF {i+1}: ")
        addPdf.append(name)

    addPdf.write("newPDF.pdf")
    addPdf.close()
    print("PDF merged successfully!")

except FileNotFoundError:
    print("Error  Check the fil pdf name.")

except Exception as e:
    print("An unexpected error occurred:", e)
