# importing os module
import os
import re
def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

# Function to rename multiple files
def main():
    i = 1
   # dst = "Rizzoli.&.Isles.S01E01.720p.WEB-DL.x264.300MB-Pahe.in.srt"
    dst = "Rizzoli.&.Isles.S03E02.720p.WEB-DL.x264.300MB-Pahe.in.srt"
    lst=sorted_aphanumeric(os.listdir('D:/G'))
    for filename in lst:
        src = filename
        if(i%10==0):
            i=0
            x=chr(ord(dst[20]) + 1)
            dst= dst[:20]+x+'0'+dst[22:]
        dst = dst[:21]+str(i)+dst[22:]
        dst1='D:/G/'+dst
        src='D:/G/'+src
        print(src,"\t",dst1,"\t",)
        os.rename(src, dst1)
        i += 1
    #
# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
