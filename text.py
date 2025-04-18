import pymupdf 
import os


doc = pymupdf.open('K:/WORK/saurabh/SSC CGL/App_/book.pdf')

#print(doc.metadata)

page = doc[8]

text = page.get_text()

#print(text)

blocks = page.get_text("blocks", sort=True)

for block in blocks:
    #print("block #", block[5])
    #print(block, "\n")
    pgdict = page.get_text("dict", sort= True)
    for block in pgdict['blocks']:

        if(block['type'] == 0):
            #print("block #", block['number'])
            for line in block['lines']:
                #print("line dir : ", line['dir'],"wmode: " ,line['wmode'], "\n")
                for span in line['spans']:
                    print("size: " ,span['size'], "font: " ,span['font'], "color: ", span['color'], "\n")
                    print("\t", span['text'], "\n")

#for selecting a perticular area from page 
#                    cropstart = page.search_for("Meaning")
#
#                    for rect in cropstart:
#                        print(rect)
#
#                        cropend = page.search_for("Outputs: SNo, Word, Meaning, Hindi, #A ")
#
#                        for rect in cropend:
#                            print(rect)
#
#
#                        rx0 = cropstart[0].x0+200
#                        ry0 = cropstart[0].y0
#
#                        rx1 = cropend[0].x1
#                        ry1 = cropend[0].y1
#
#                        cr = pymupdf.Rect(rx0, ry0, rx1, ry1)
#                        print(cr)
#
