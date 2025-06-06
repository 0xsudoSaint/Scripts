#python3 script.py <filename.bin> always use a binary file
#Either use absolute path or just put the bin file and script in the same directory
import sys
import binascii
def main():
    #argument 0 is the module itself
    filename=sys.argv[1]
    file=open(filename,'rb')
    string=""
    #To prevent waste of cpu clock cycles, adding " before the first byte sequence
    byte=file.read(1)
    char=binascii.hexlify(byte).decode()  
    string+="\0 0x"+char
    while True:
        byte=file.read(1)
        char=binascii.hexlify(byte).decode()
        if not byte:
            break
        string+="\0 ,0x"+char
    #string+='"'
    print(string)

if __name__ == "__main__":
    main()