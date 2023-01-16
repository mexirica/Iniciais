
def most_frequent_chars(filename: str) -> str:
    arquivos=[]
#quantidade arquivos
    while (filename not in arquivos) :
        arquivos.append(filename)
        f = open(filename, "r")
        filename=f.readline().rstrip( '\n' )
        f = open(filename, "r")
        filename=f.readline().rstrip( '\n' )
# juntando elementos
    mylist=[]
    for i in arquivos:
        with open(i) as teste:
            for x in teste:
                if x.strip():
                    mylist.append(x.strip())
#removendo arquivos de texto
    for x in mylist:
        if x.endswith('.txt'):
            mylist.remove(x)

    counter=0
    num=[]
    for i in mylist:
        if len(i)>counter:
            counter=len(i)
    i=0
    dic= {}
    palavra=[]
    bosta={}
    while(i<counter):
        for l in mylist:
            if((len(l)) > i):
                if dic.get(l[i]):
                    dic[l[i]]+=1
                else:
                    dic[l[i]]=1
            else:
                pass
        for k,v in dic.items():
            if bosta=={}:
                bosta[k]=v
                maior=v
            elif v>maior:
                bosta={k:v}
                maior=v
            elif v==maior:
                bosta[k]=v
        y=sorted(bosta)
        palavra.append(y[0])
        i+=1
        dic.clear()
        bosta.clear()
    result = [' '.join(palavra)]
    result=str(result)
    result=result.replace(" ","")
    result=result.strip('"[' )
    result=result.strip('"]' )
    result=result.strip("'")
    return result

most_frequent_chars('test02/bullfight.txt')
