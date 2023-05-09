import pandas as pd


def main():
    timestamps = []
    with open('timestamp.txt', 'r') as fichero:
        for linea in fichero:
            timestamps.append(linea[6:14])

    CPUus = []
    CPUsy = []
    CPUid = []
    with open('CPU.txt', 'r') as fichero:
        for linea in fichero:
            CPUus.append(float(linea[9:13].replace(',', '.')))
            CPUsy.append(float(linea[18:22].replace(',', '.')))
            CPUid.append(round(100 - float(linea[36:40].replace(',', '.')),1))

    data = {'Timestamp': timestamps,
            '% CPU (global)': CPUid, '% CPU (user)': CPUus, '% CPU (system)': CPUsy}

    df = pd.DataFrame(
        data, columns=['Timestamp', '% CPU (global)', '% CPU (user)', '% CPU (system)'])

    df.to_csv('monitorizacionCPU.csv', sep=';', index=False)


if __name__ == '__main__':
    main()
