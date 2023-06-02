import pandas as pd

def main():
    lectura = open("data.txt", mode="r").read().splitlines()
    escritura1 = open("cleanDataP.txt", "w")
    escritura2 = open("cleanDataM.txt", "w")
    escritura3 = open("cleanDataG.txt", "w")
    lectura.pop(0)

    escritura1.write("size,hour,MB/s\n")
    escritura2.write("size,hour,MB/s\n")
    escritura3.write("size,hour,MB/s\n")
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

            if (float(line[0])<963962):
                escritura1.write(f"{line[0]},{line[1]},{line[2]}\n")
            else:
                if (float(line[0])<1927924):
                    escritura2.write(f"{line[0]},{line[1]},{line[2]}\n")
                else:
                    escritura3.write(f"{line[0]},{line[1]},{line[2]}\n")

    dataframe = pd.read_csv("cleanDataP.txt")
    dataframe.to_csv('dataP.csv', index=None)
    dataframe = pd.read_csv("cleanDataM.txt")
    dataframe.to_csv('dataM.csv', index=None)
    dataframe = pd.read_csv("cleanDataG.txt")
    dataframe.to_csv('dataG.csv', index=None)

    lectura1 = open("cleanDataP.txt", mode="r")
    lectura2 = open("cleanDataM.txt", mode="r")
    lectura3 = open("cleanDataG.txt", mode="r")
    escritura1 = open("dataP.arff", "w")
    escritura2 = open("dataM.arff", "w")
    escritura3 = open("dataG.arff", "w")

    line = lectura1.readline()
    escritura1.write("@relation data-server\n\n")
    escritura1.write("@attribute SIZE numeric\n")
    escritura1.write("@attribute HOUR numeric\n")
    escritura1.write("@attribute MBS numeric \n")
    escritura1.write("\n@data\n\n")
    line = lectura1.readline()
    while (line):
        line = line.replace(";",",")
        if(line[len(line)-1]!="," and line[len(line)-2]!=","):
            if(line[len(line)-1]=="."):
                line = line.replace(".","")    
            escritura1.write(line)
        line = lectura1.readline()
    
    line = lectura2.readline()
    escritura2.write("@relation data-server\n\n")
    escritura2.write("@attribute SIZE numeric\n")
    escritura2.write("@attribute HOUR numeric\n")
    escritura2.write("@attribute MBS numeric \n")
    escritura2.write("\n@data\n\n")
    line = lectura2.readline()
    while (line):
        line = line.replace(";",",")
        if(line[len(line)-1]!="," and line[len(line)-2]!=","):
            if(line[len(line)-1]=="."):
                line = line.replace(".","")    
            escritura2.write(line)
        line = lectura2.readline()

    line = lectura3.readline()
    escritura3.write("@relation data-server\n\n")
    escritura3.write("@attribute SIZE numeric\n")
    escritura3.write("@attribute HOUR numeric\n")
    escritura3.write("@attribute MBS numeric \n")
    escritura3.write("\n@data\n\n")
    line = lectura3.readline()
    while (line):
        line = line.replace(";",",")
        if(line[len(line)-1]!="," and line[len(line)-2]!=","):
            if(line[len(line)-1]=="."):
                line = line.replace(".","")    
            escritura3.write(line)
        line = lectura3.readline()

if __name__ == "__main__":
    main()