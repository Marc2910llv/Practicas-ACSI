# Variables
Rn = [0]
Xn = [0]
R1n = [0]
N1n = [0]
X1n = [0]
U1n = [0]
R2n = [0]
N2n = [0]
X2n = [0]
U2n = [0]
# Constantes
Scpu = 0.03
Sdisco = 0.1
Vdisco = 7
Vcpu = Vdisco + 1
z = 8
print("Trabajos |   Rcpu     Rdisco    |       R        Xo       |     Ncpu      Ndisco\n")
for i in range(10):
    n = i+1
    R1n.append((N1n[n-1]+1)*Scpu)
    R2n.append((N2n[n-1]+1)*Sdisco)
    Rn.append((Vcpu*R1n[n])+(Vdisco*R2n[n]))
    Xn.append((n)/(z+Rn[n]))
    N1n.append(Xn[n]*Vcpu*R1n[n])
    N2n.append(Xn[n]*Vdisco*R2n[n])
    X1n.append(Xn[n]*Vcpu)
    X2n.append(Xn[n]*Vdisco)
    U1n.append(Xn[n]*Vcpu*Scpu)
    U2n.append(Xn[n]*Vdisco*Sdisco)
    print(n, "      |   ", "{:.4f}".format(R1n[n]), "  ", "{:.4f}".format(R2n[n]), "  |   ",
          "{:.4f}".format(Rn[n]), "   ", "{:.4f}".format(Xn[n]), "   |   ", "{:.4f}".format(N1n[n]), "  ", "{:.4f}".format(N2n[n]), "\n")
