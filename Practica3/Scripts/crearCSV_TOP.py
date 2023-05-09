import pandas as pd


def main():
    CPUus = []
    CPUsy = []
    CPUid = []
    timestamps = []
    i = 1
    with open('CPU.txt', 'r') as fichero:
        for linea in fichero:
            CPUus.append(float(linea[0:4].replace(',', '.')))
            CPUsy.append(float(linea[4:8].replace(',', '.')))
            if (linea[8:13] != "id,") & (linea[8:13] != "id,\n"):
                CPUid.append(
                    round(100 - float(linea[8:13].replace(',', '.')), 1))
            else:
                CPUid.append(100.0)
            timestamps.append(i)
            i = i+1

    data = {'Timestamp': timestamps,
            '% CPU (global)': CPUid, '% CPU (user)': CPUus, '% CPU (system)': CPUsy}

    df = pd.DataFrame(
        data, columns=['Timestamp', '% CPU (global)', '% CPU (user)', '% CPU (system)'])

    df.to_csv('monitorizacionCPU.csv', sep=';', index=False)


if __name__ == '__main__':
    main()
