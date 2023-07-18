from tkinter import *
def contentToDictionaryConverter(contents):
    charDictionary={}
    for character in contents:
        if character in charDictionary:
            charDictionary[character]+=1
        elif character not in charDictionary:
            charDictionary[character]=1
    return charDictionary
def TreeCreator(dictionary):
    tree={}
    lst_of_nodes=[]
    for key in dictionary:
        lst_of_nodes.append([key,dictionary[key]])
    while len(lst_of_nodes)>1:
        small1=lst_of_nodes[0]
        for i in range(1,len(lst_of_nodes)):
            if lst_of_nodes[i][1]<small1[1]:
                small1=lst_of_nodes[i]
        lst_of_nodes.remove(small1)
        small2=lst_of_nodes[0]
        for i in range(1,len(lst_of_nodes)):
            if lst_of_nodes[i][1]<small2[1]:
                small2=lst_of_nodes[i]
        lst_of_nodes.remove(small2)
        small1.append(0)
        small2.append(1)
        tup=[small1[0]+small2[0],small1[1]+small2[1]]
        tree[tup[0]]=[small1,small2]
        lst_of_nodes.append(tup)
    tree["start"]=lst_of_nodes[0][0]
    return tree
def BinaryDictionaryCreater(dictionary,tree):
    BinaryDictionary={}
    for character in dictionary:
        found=False
        start=tree["start"]
        code=""
        while found!=True:
            if character in tree[start][0][0]:
                digit=tree[start][0][2]
                if character == tree[start][0][0]:
                    found=True
                else:
                    start=tree[start][0][0]
            elif character in tree[start][1][0]:
                digit=tree[start][1][2]
                if character == tree[start][1][0]:
                    found=True
                else:
                    start=tree[start][1][0]
            code=code+str(digit)
        BinaryDictionary[character]=code
    return (BinaryDictionary)
def ContentToBinary(contents,BinaryDictionary):
    BinaryContent=""
    for character in contents:
        BinaryContent+=BinaryDictionary[character]
    return BinaryContent
def binToChr(msg):
    binary = []
    asc = []
    char = ''
    y = 0
    #seperating the binary for characters; start
    while y != len(msg):
        temp = ''
        while len(temp) != 7:
            temp += msg[y]
            y+=1
        binary.append(temp)
    #seperating the binary for characters; end
    #converting binary to decimal; start
    for x in binary:
        decimal, i =  0, 0
        x = int(x)
        
        while x != 0:
            dec = x % 10
            decimal = decimal + dec * (2**i)
            x = x // 10
            i += 1
        asc.append(decimal)
    #converting binary to decimal; end
    #translating ascii to character; start
    for z in asc:
        char += chr(z)
    #translating ascii to character; end
    return(char)
def binary_converter(num):
    result=[]
    while num>1:
        result.append(str(num%2))
        num=num//2
    result.append(str("1"))
    result=result[::-1]
    result="".join(result)
    if len(result)<7:
        result=("0"*(7-len(result)))+result
    return result
def string_to_binary(txt):
    l= [ord(items) for items in txt]
    result=""
    for i in l:
        result+=binary_converter(i)
    return result
def coded_are_keys(diction):
    k=diction.keys()
    result={}
    for i in k:
        result[diction[i]]=i
    return result
def coded_to_uncoded(diction,content):
    result=''
    count=0
    code=''
    while count< len(content):
        found= False
        code=content[count]
        while found== False:
            first=count
            if code in diction.keys():

                found=True
                result+= diction[code]
                count+=1
            else:
                
                count+=1
                code+=content[first+1:count+1]  
    return result
def CompressionAlgorithm():
    file_name=txt.get()
    file1=open(file_name,"r")
    contents=file1.read()
    file_size_Original=len(contents)*8
    charDictionary=contentToDictionaryConverter(contents)
    tree=TreeCreator(charDictionary)
    BinaryDictionary=BinaryDictionaryCreater(charDictionary,tree)
    BinaryContent=ContentToBinary(contents,BinaryDictionary)
    Binarylength=len(BinaryContent)
    if Binarylength%7!=0:
        BinaryContent+=("0"*(7-(Binarylength%7)))
    message=binToChr(BinaryContent)
    file1.close()
    file_name=file_name[0:len(file_name)-4]+"compressed"+file_name[len(file_name)-4:len(file_name)]
    file2=open(file_name,"w")
    file_size_compressed=8
    for character in charDictionary:
        content=character+str(charDictionary[character])+"\n"
        file_size_compressed+=(len(content)*8)
        file2.write(content)
    file2.write("End\n")
    file2.write(str(Binarylength)+"\n")
    file_size_compressed+=len(str(Binarylength))*8+8
    for i in message:
        file2.write(i)
    file_size_compressed+=len(message)*8
    file2.close()
    Window=Tk()
    Window.geometry('480x240')
    Window.title("Welcome to File compression algorithm")
    lbl = Label(Window, text="File Compression successful. Congrats",font=("Arial Bold", 15))
    lb2 = Label(Window, text="Total file zize before conversion: "+str(file_size_Original//8)+" Bytes",font=("Arial Bold", 15))
    lb3 = Label(Window, text="Total file zize after conversion: "+str(file_size_compressed//8)+" Bytes",font=("Arial Bold", 15))
    lbl.grid(column=0, row=0)
    lb2.grid(column=0, row=1)
    lb3.grid(column=0, row=2)

def DeCompressionAlgorithm():
    skip=False
    end=False
    file_name=txt.get()
    file1=open(file_name,"r")
    contents=file1.readlines()
    CharDictionary={}
    i=0
    while end==False:
        if "End" in contents[i]:
            i+=1
            end=True
            break
        if skip!=True:
            if len(contents[i])<=1:
                skip=True
                CharDictionary[contents[i]]=0
            else:
                CharDictionary[contents[i][0]]=int(contents[i][1:len(contents[i])])
        elif skip==True:
            CharDictionary[contents[i-1]]=int(contents[i])
            skip=False
        i+=1
    Binarylength=int(contents[i])
    contents=contents[i+1:len(contents)]
    contents="".join(contents)
    contents=string_to_binary(contents)
    contents=contents[0:Binarylength]
    tree=TreeCreator(CharDictionary)
    BinaryDictionary=BinaryDictionaryCreater(CharDictionary,tree)
    BinaryDictionary=coded_are_keys(BinaryDictionary)
    message=coded_to_uncoded(BinaryDictionary,contents)
    file2=open("DecompressedFile.txt","w")
    file2.write(message)
    file2.close()
    Window=Tk()
    Window.geometry('480x240')
    Window.title("Welcome to File compression algorithm")
    lbl = Label(Window, text="File DeCompression successful. Congrats",font=("Arial Bold", 15))
    lbl.grid(column=0, row=0)


Window=Tk()
Window.geometry('360x240')
Window.title("Welcome to File compression algorithm")
lbl = Label(Window, text="Hello. Enter the file name.",font=("Arial Bold", 15))
lbl.grid(column=0, row=0)
txt = Entry(Window,width=40)
txt.grid(column=0,row=1)
filename=txt.get()
compressbtn = Button(Window, text="Compress",command=CompressionAlgorithm)
compressbtn.grid(column=0, row=3)
decompressbtn=Button(Window, text="DeCompress",command=DeCompressionAlgorithm)
decompressbtn.grid(column=1, row=3)
Window.mainloop()