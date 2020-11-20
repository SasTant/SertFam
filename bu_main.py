from docxtpl import DocxTemplate


def proses(s):
    tpl = DocxTemplate('Python.docx')
    context = {1:{  "nama":"Hadi Merdianto",
                    "TTL":"Cilacap, 18 juli 2000",
                    "ref":"Ref: CPA-2020-FTR-%s"%str(s),
                    "TTT": "JKT,skrg",
                    "ship":"Onboard ARIMBI "},
              2: {  "nama":"Dodik ManhgkuBoto Mekarsari",
                    "TTL":"Cilacap, 18 juli 2000",
                    "ref":"Ref: CPA-2020-FTR-%s"%str(s+2),
                    "TTT": "JKT,20 November 2020",
                    "ship":"Onboard GAMKONORA "}
               }
    tpl.render(context[s])
    tpl.save("cpa ref-%s.docx" %str(s))

for s in range(1,3):
    proses(s)

