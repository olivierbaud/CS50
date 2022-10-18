from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()
pdf.set_font("helvetica","B", 50)
pdf.cell(w=0,h=40, txt = "CS50 Shirtificate", align = "C")
pdf.image("shirtificate.png",w=pdf.epw , y=60, x = 10)
pdf.set_font("helvetica","B", 20)
pdf.set_text_color(r=255,g=255,b=255)
pdf.cell(w=-190, h=240, txt=(input("Name: "))+" took CS50", align = "C")

pdf.output("shirtificate.pdf")