import pandas as pd


def main():
    total = 11301176
    timestamp = []
    time = 1
    mem = []
    memused = []
    mempercent = []
    with open('MEM.txt', 'r') as fichero:
        linea = fichero.readline()
        linea = fichero.readline()
        linea = fichero.readline()
        while (linea != ""):
            mem.append(int(linea))
            memused.append(int(total-int(linea)))
            mempercent.append(float(((total-int(linea))*100)/total))
            timestamp.append(time)
            time += 1
            linea = fichero.readline()

    data = {'Timestamp': timestamp,
            'Capacidad disponible': mem, 'Capacidad utilizada': memused, '% Memoria utilizada': mempercent}

    df = pd.DataFrame(
        data, columns=['Timestamp', 'Capacidad disponible', 'Capacidad utilizada', '% Memoria utilizada'])

    df.to_csv('monitorizacionMEM.csv', sep=';', index=False)


if __name__ == '__main__':
    main()
