# DIN 6885
class Passfeder():
    def __init__(self, dw_von, dw_bis, b, h, t1, t2):
        self.dw_von = dw_von
        self.dw_bis = dw_bis
        self.b = b
        self.h = h
        self.t1 = t1
        self.t2 = t2

P_dw_von = [10,12,17,22,30,38,44,50,58,65,75,85,95,110,130,150,170]
P_dw_bis = [12,17,22,30,38,44,50,58,65,75,85,95,110,130,150,170,200]
P_b = [4,5,6,8,10,12,14,16,18,20,22,25,38,32,36,40,45]
P_h = [4,5,6,7,8,8,9,10,11,12,14,14,16,18,20,22,25]
P_t1 = [2.5,3,3.5,4,5,5,5.5,6,7,7.5,9,9,10,11,12,13,15]
P_t2 = [1.8,2.3,2.8,3.3,3.3,3.3,3.8,4.3,4.4,4.9,5.4,5.4,6.4,7.4,8.4,9.4,10.4]

Passfeder_Liste = []

for i in range(17):
    Passfeder_Liste.append(Passfeder(P_dw_von[i], P_dw_bis[i], P_b[i], P_h[i], P_t1[i], P_t2[i]))

# DIN ISO 14
class Keilwelle_leicht():
    def __init__(self, n, d, D, b, phi):
        self.n = n
        self.d = d
        self.D = D
        self.b = b
        self.phi = phi
        self.dm = (self.D + self.d) / 2
        self.h = (self.D - self.d) / 2

Kl_n = [6,6,6,8,8,8,8,8,8,8,10,10,10,10,10]
Kl_d = [23,26,28,32,36,42,46,52,56,62,72,82,92,102,112]
Kl_D = [26,30,32,36,40,46,50,58,62,68,78,88,98,108,120]
Kl_b = [6,6,7,6,7,8,9,10,10,12,12,12,14,16,18]
Kl_phi = [0.75,0.75,0.75,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9]

Keilwelle_leicht_Liste = []

for i in range(15):
    Keilwelle_leicht_Liste.append(Keilwelle_leicht(Kl_n[i], Kl_d[i], Kl_D[i], Kl_b[i], Kl_phi[i]))

    