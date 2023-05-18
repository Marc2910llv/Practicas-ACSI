import pandas as pd

def main():
    lectura = open("data.txt", mode="r").read().splitlines()
    escritura = open("cleanData.txt", "w")
    lectura.pop(0)

    escritura.write("size,hour,MB/s\n")
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

            escritura.write(f"{line[0]},{line[1]},{line[2]}\n")

    dataframe = pd.read_csv("cleanData.txt")
    dataframe.to_csv('data.csv', index=None)

    lectura = open("cleanData.txt", mode="r")
    escritura = open("data.arff", "w")
    line = lectura.readline()
    escritura.write("@relation data-server\n\n")
    escritura.write("@attribute SIZE numeric\n")
    escritura.write("@attribute HOUR numeric\n")
    escritura.write("@attribute MBS numeric \n")
    escritura.write("\n@data\n\n")
    line = lectura.readline()
    while (line):
        line = line.replace(";",",")
        if(line[len(line)-1]!="," and line[len(line)-2]!=","):
            if(line[len(line)-1]=="."):
                line = line.replace(".","")    
            escritura.write(line)
        line = lectura.readline()

if __name__ == "__main__":
    main()