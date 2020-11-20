import tkinter as teka

from docxtpl import DocxTemplate
from docx2pdf import convert

cen_ut = teka.Tk()
cen_ut.title('Sertifikat Familiarisasi')

def proses():
    s=1

    rasma = asma.get()
    rref = ref.get()
    rttl = ttl.get()
    rttt= ttt.get()
    rprau = prau.get()

    tpl = DocxTemplate('Python.docx')
    context = {s:{  "nama":"%s" %str(rasma),
                    "TTL":"%s" %str(rttl),
                    "ref":"Ref: CPA-2020-FTR-%s"%str(rref),
                    "TTT": "%s" %str(rttt),
                    "ship":"Onboard %s" %str(rprau)}
               }

    tpl.render(context[s])
    tpl.save("cpa ref-%s.docx" %str(rasma))

    convert("cpa ref-%s.docx" %str(rasma), "cpa ref-%s.pdf" %str(rasma))

    label = teka.Label(cen_ut, text="Input Entry lagi / Tutup Program")
    label.pack()



asma = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
asma.pack()
lasma = teka.Label(cen_ut, text="Input Entry Nama lengkap").pack()

ttl = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
ttl.pack()
lttl = teka.Label(cen_ut, text="Input Entry Tanggal Lahir").pack()

ref = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
ref.pack()
lref = teka.Label(cen_ut, text="Input Entry No Sertifikat").pack()

ttt = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
ttt.pack()
lttt = teka.Label(cen_ut, text="Input Entry Tempat Tanggal Training").pack()

prau = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
prau.pack()
lprau = teka.Label(cen_ut, text="Input Entry Nama Kapal").pack()

tombol9 = teka.Button(cen_ut,text="Proses", command = proses )
tombol9.pack()


cen_ut.mainloop()
