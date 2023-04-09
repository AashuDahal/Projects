import string
letters=string.ascii_letters
key=3
encoding_dict={}
for i in range(len(letters)):
    encoding_dict[letters[i]]=letters[(i+key)%len(letters)]
    encoding_dict[" "]=""
    decoding_dict={value:key for (key,value) in encoding_dict.items()}
    decoding_dict[" "]=""

def get_user_input():
    while True:
        encode_or_decode=input("Enter (e) to encrypt a password, and (d) to decrypt: ")
        if (encode_or_decode=="e" or encode_or_decode=="d"):
            break
        else:
            print("invalid mode")
    
    if (encode_or_decode=="e"):
        f=open("123.txt")
        f0=f.read()
        f.close()
        x1=encode(f0)
        f1=open("encrypted_hello.txt","w")
        f1.write(x1)
        f1.close()
        print("Output written to: encrypted_hello.txt")

    if (encode_or_decode=="d"):
        f=open("123.txt")
        y0=f.read()
        f.close()
        y1=decode(y0)
        f1=open("decrypted_hello.txt","w")
        f1.write(y1)
        f1.close()
        print("Output written to: decrypted_hello.txt")

    while True:
        re_input=input("Would you like to encode or decode again? (y/n)")
        if (re_input=="y" or re_input=="n"):
            break
        else:
            pass

    if re_input=="y":
        get_user_input()
    elif (re_input=="n"):
        print("Thank you for using this program")
    

def encode(message):
    l1=[]
    for i in message:
        for j in i:
            encoded_message=encoding_dict[j]
            l1.append(encoded_message)
    stringg=""
    for i in l1:
        if (i!=""):
            stringg=stringg+i
        if (i==""):
            stringg=stringg+" "

    return stringg

def decode(message):
    m1=[]
    for i in message:
        for j in i:
            decoded_message=decoding_dict[j]
            m1.append(decoded_message)
    stringg=""
    for i in m1:
        if (i!=""):
            stringg=stringg+i
        if (i==""):
            stringg=stringg+" "
            
    return stringg
get_user_input()