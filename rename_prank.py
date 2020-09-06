
import os 
#from str import maketrans
def rename_prank():

    transtab = str.maketrans('','',"01234567890")
    for f in os.listdir(r"D:\prank"):
        #result = ''.join([c for c in f if not c.isdigit()])
        result = f.translate(transtab)
        print(result)
        os.rename("D:\\prank\\"+f,"D:\\prank\\"+result)


rename_prank()



