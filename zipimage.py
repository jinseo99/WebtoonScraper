from zipfile import ZipFile
from os import listdir


folder = "delete/1/"
with ZipFile('delete/1.zip', 'w') as zipObj:
    ind = 1
    while True:
        try:
            filename = str(ind) +".jpg"
            filepath = folder+filename
            zipObj.write(filepath, filename)
            ind += 1
        except:
            break
