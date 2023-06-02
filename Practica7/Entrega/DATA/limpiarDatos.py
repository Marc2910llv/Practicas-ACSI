import pandas as pd

def main():
    lectura = open("data.txt", mode="r").read().splitlines()
    escritura = open("cleanData.txt", "w")
    lectura.pop(0)

    hora = -1
    size=[]
    mbs=[]
    n = 0
    escritura.write("size;hour;MB/s\n")
    for line in lectura:
        if (line[0] != "-"):
            line = line.split(",")

            try:
                line.pop(2)
            except:
                pass

            try:
                temp = line[1].split("\t")
            except:
                print(line)
            line[1] = temp[0]

            x = temp[1].split(".")
            if len(x) == 3:
                temp[1] = f"{x[0]}{x[1]}.{x[2]}"
            line.append(temp[1])

            if(line[1]!=hora):
                if(hora != -1):
                    ssum=0
                    nsum=0
                    for i in range(n):
                        ssum+=float(size[i])
                        nsum+=float(mbs[i])
                    msize=ssum/n
                    mmbs=nsum/n
                    escritura.write(f"{msize};{hora};{mmbs}\n")
                hora=line[1]
                size=[line[0]]
                mbs=[line[2]]
                n = 1
            else:
                size.append(line[0])
                mbs.append(line[2])
                n=n+1

    ssum=0
    nsum=0
    for i in range(n):
        ssum+=float(size[i])
        nsum+=float(mbs[i])
    msize=ssum/n
    mmbs=nsum/n
    escritura.write(f"{msize},{hora},{mmbs}\n")

    dataframe = pd.read_csv("cleanData.txt")
    dataframe.to_csv('data.csv', index=None)

if __name__ == "__main__":
    main()