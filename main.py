from tkinter import *
import tkinter as teka
from docxtpl import DocxTemplate
from docx2pdf import convert

cen_ut = teka.Tk()
cen_ut.title('Sertifikat Familiarisasi')


def sel():
    if var.get() == 1:
        teka.Label(cen_ut, text="Tipe ECDIS FMD - 3200/3300 ").pack(anchor = S )
    elif var.get() == 2:
        teka.Label(cen_ut, text="Tipe ECDIS FEA - 2107/2807 ").pack(anchor = S )


def selhas():
    if var.get() == 1:
        recdisr = "FMD - 3300/3200"
    elif var.get() == 2:
        recdisr = "FEA - 2107/2807"
    return recdisr

var = IntVar()


def proses():

    rasma = asma.get()
    rref = ref.get()
    rttl = ttl.get()
    rttt= ttt.get()
    rprau = prau.get()
    rdowo = dowo.get()
    recdis=str(selhas())

    tpl = DocxTemplate('Python.docx')
    context = {1:{  "nama":"%s" %str(rasma),
                    "TTL":"%s" %str(rttl),
                    "ref":"Ref: CPA-2021-FTR-%s"%str(rref),
                    "TTT": "%s" %str(rttt),
                    "ecdis": "ECDIS Model %s" % str(recdis),
                    "ship":"Onboard %s" %str(rprau),
                    "dura": "%s" % str(rdowo)}
                }

    sref= str(rref)
    sasma = str(rasma)
    sprau = str(rprau)
    jenber = " "+ sref + " "+ sasma + " " + sprau

    tpl.render(context[1])
    tpl.save("CPA2021FTR%s.docx" %jenber)

    convert("CPA2021FTR%s.docx" %jenber, "C:/Users/QylaMeisya/Documents/Sertifikat Training Familiarrisasi ECDIS Photosop/sertfampy" )

    label = teka.Label(cen_ut, text="Sert. %s Selesai ! Input Entry lagi / Tutup Program !" %str(rasma))
    label.pack()


lasma = teka.Label(cen_ut, text="Input Entry Nama lengkap").pack()
asma = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
asma.pack()

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

teka.Label(cen_ut, text="Input Entry Durasi Training").pack()
dowo = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
dowo.pack()

R1 = Radiobutton(cen_ut, text="ECDIS FMD-3200/3300", variable=var, value=1, command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(cen_ut, text="ECDIS FEA-2107/2807", variable=var, value=2, command=sel)
R2.pack( anchor = W )

tombol9 = teka.Button(cen_ut,text="Proses", command = proses )
tombol9.pack()


cen_ut.mainloop()

