import tkinter as teka
from docxtpl import DocxTemplate
from docx2pdf import convert

cen_ut = teka.Tk()
cen_ut.title('Sertifikat Familiarisasi')

def sal_in(): #salah input
    ecdis.delete( 0,'end')
    ecdis.insert(0, 'Masukan 1 atau 2, sesuai tipe ECDIS !!!')

def proses():

    rasma = asma.get()
    rref = ref.get()
    rttl = ttl.get()
    rttt= ttt.get()
    rprau = prau.get()
    recdis = ecdis.get()

    if recdis.isnumeric():
        angka_i = int(recdis)
        if angka_i < 3 and angka_i > 0:
            if angka_i == 1:
                recdisr = "FMD - 3300/3200"
            elif angka_i==2:
                recdisr = "FEA - 2807/2107"
        else:
            sal_in()
    else:
        sal_in()

    tpl = DocxTemplate('Python.docx')
    context = {1:{  "nama":"%s" %str(rasma),
                    "TTL":"%s" %str(rttl),
                    "ref":"Ref: CPA-2020-FTR-%s"%str(rref),
                    "TTT": "%s" %str(rttt),
                    "ecdis": "ECDIS Model %s" % str(recdisr),
                    "ship":"Onboard %s" %str(rprau)}
               }

    tpl.render(context[1])
    tpl.save("cpa ref-%s.docx" %str(rasma))

    convert("cpa ref-%s.docx" %str(rasma), "cpa ref-%s.pdf" %str(rasma))

    label = teka.Label(cen_ut, text="Sert. %s Selesai ! Input Entry lagi / Tutup Program !" %str(rasma))
    label.pack()


lasma = teka.Label(cen_ut, text="Input Entry Nama lengkap").pack()
asma = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
asma.pack()

# ecdis = teka.Checkbutton(cen_ut, text="ECDIS FMD-3200/3300", variable = ecd ) # width=70, borderwidth=5, fg='blue')
# ecdis.pack()
# lecdis = teka.Label(cen_ut, text="Input Entry Tipe ECDIS").pack()

lecdis = teka.Label(cen_ut, text="Input angka 1 / 2 untuk Tipe ECDIS ( 1 : FMD 3300/3200 | 2 : FEA 2807/2107) ").pack()
ecdis = teka.Entry(cen_ut, width=35, borderwidth=5, fg='blue')
ecdis.pack()

lttl = teka.Label(cen_ut, text="Input Entry Tanggal Lahir").pack()
ttl = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
ttl.pack()

lref = teka.Label(cen_ut, text="Input Entry No Sertifikat").pack()
ref = teka.Entry(cen_ut, width=5, borderwidth=5, fg='blue')
ref.pack()

lttt = teka.Label(cen_ut, text="Input Entry Tempat Tanggal Training").pack()
ttt = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
ttt.pack()

lprau = teka.Label(cen_ut, text="Input Entry Nama Kapal").pack()
prau = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
prau.pack()

tombol9 = teka.Button(cen_ut,text="Proses", command = proses )
tombol9.pack()


cen_ut.mainloop()

