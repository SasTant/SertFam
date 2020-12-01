#### GrabWin.PY #######
# Grab template
# Versi windows

import tkinter as teka
from docxtpl import DocxTemplate

cen_ut = teka.Tk()
cen_ut.title('Grab Tpl')

# def sal_in(): #salah input
#     ecdis.delete( 0,'end')
#     ecdis.insert(0, 'Masukan 1 atau 2, sesuai tipe ECDIS !!!')

def proses():

    rtgl  = tgl.get()
    rpick = pick.get()
    rbook = book.get()
    rpaid = paid.get()
    rfare = fare.get()
    ropt= opt.get()
    rt_fare = t_fare.get()
    rovo = t_fare.get()
    rpoint = point.get()
    rtrip = trip.get()
    rawal = awal.get()
    rtawl = tawl.get()
    rakhir = akhir.get()
    rtakh = takh.get()

    stgl  = str(rtgl)
    spick = str(rpick)
    sbook = str(rbook)
    spaid = str(rpaid)
    sfare = str(rfare)
    sopt= str(ropt)
    st_fare = str(rt_fare)
    sovo = str(rt_fare)
    spoint = str(rpoint)
    strip = str(rtrip)
    sawal = str(rawal)
    stawl = str(rtawl)
    sakhir = str(rakhir)
    stakh = str(rtakh)

    f = open("semGW.txt","a")
    f.write(stgl+"\n")
    f.write(spick+"\n")
    f.write(sbook+"\n")
    f.write(spaid+"\n")
    f.write(sfare+"\n")
    f.write(sopt+"\n")
    f.write(st_fare+"\n")
    f.write(sovo+"\n")
    f.write(spoint+"\n")
    f.write(strip+"\n")
    f.write(sawal+"\n")
    f.write(stawl+"\n")
    f.write(sakhir+"\n")
    f.write(stakh+"\n")
    f.close()

    # if recdis.isnumeric():
    #     angka_i = int(recdis)
    #     if angka_i < 3 and angka_i > 0:
    #         if angka_i == 1:
    #             recdisr = "FMD - 3300/3200"
    #         elif angka_i==2:
    #             recdisr = "FEA - 2807/2107"
    #     else:
    #         sal_in()
    # else:
    #     sal_in()



    tpl = DocxTemplate('Grab_Tpl.docx')
    context = {1:{  "tgl":"%s" %str(rtgl),
                    "pick":"%s" %str(rpick),
                    "book":"%s" %str(rbook),
                    "paid":"%s" %str(rpaid),
                    "fare":"%s"%str(rfare),
                    "opt": "%s" %str(ropt),
                    "t_fare": "%s" % str(rt_fare),
                    "ovo":"%s" %str(rovo),
                    "point":"%s" %str(rpoint),
                    "trip":"%s" %str(rtrip),
                    "awal":"%s" %str(rawal),
                    "tawl":"%s" %str(rtawl),
                    "akhir":"%s" %str(rakhir),
                    "takh":"%s" %str(rtakh)}
               }


    tpl.render(context[1])
    tpl.save("grab %s.docx" %str(rpick))

    label = teka.Label(cen_ut, text="Grab %s Selesai ! Input Entry lagi / Tutup Program !" %str(rpick))
    label.pack()


ltgl = teka.Label(cen_ut, text="Input Tanggal (Mmm DD, YYYY, TT:MM AM/PM").pack()
tgl = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
tgl.pack()

lpick = teka.Label(cen_ut, text="Input Tanggal jemputan (DD MMMM YYYY").pack()
pick = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
pick.pack()

lbook = teka.Label(cen_ut, text="Input no Booking ID (AAA-XXXX.XXX)").pack()
book = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
book.pack()

lpaid = teka.Label(cen_ut, text="Input paid (Rp NNN.NNNN ").pack()
paid = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
paid.pack()

lfare = teka.Label(cen_ut, text="Input fare (NNN.NNN)").pack()
fare = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
fare.pack()

lopt = teka.Label(cen_ut, text="Input opt in menu (NNN.NNN)").pack()
opt = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
opt.pack()

lt_fare = teka.Label(cen_ut, text="Input Total fare (NNNN.NNN)").pack()
t_fare = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
t_fare.pack()

lpoint = teka.Label(cen_ut, text="Input point ovo (+NNN)").pack()
point = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
point.pack()

ltrip = teka.Label(cen_ut, text="Input trip (XX.XXKm-XXmins)").pack()
trip = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
trip.pack()

lawal = teka.Label(cen_ut, text="Input alamat awal").pack()
awal = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
awal.pack()

ltawl = teka.Label(cen_ut, text="Input waktu awal (TT:MMAM/PM)").pack()
tawl = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
tawl.pack()

lakhir = teka.Label(cen_ut, text="Input alamat akhir").pack()
akhir = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
akhir.pack()

ltakh = teka.Label(cen_ut, text="Input waktu akhir (TT:MMAM/PM)").pack()
takh = teka.Entry(cen_ut, width=70, borderwidth=5, fg='blue')
takh.pack()

tombol9 = teka.Button(cen_ut,text="Proses", command = proses )
tombol9.pack()


cen_ut.mainloop()

