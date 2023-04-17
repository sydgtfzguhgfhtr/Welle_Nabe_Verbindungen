# DIN 6885
class Passfeder():
    def __init__(self, dw_von: int, dw_bis: int, b: int, h: int, t1: float, t2: float):
        self.dw_von = dw_von
        self.dw_bis = dw_bis
        self.b = b
        self.h = h
        self.t1 = t1
        self.t2 = t2

# DIN ISO 14
class Keilwelle_leicht():
    def __init__(self, n: int, d: int, D: int, b: int, phi: float):
        self.n = n
        self.d = d
        self.D = D
        self.b = b
        self.phi = phi
        self.dm = (self.D + self.d) / 2
        self.h = (self.D - self.d) / 2

# DIN ISO 14
class Keilwelle_mittel():
    def __init__(self, n: int, d: int, D: int, b: int, phi: float):
        self.n = n
        self.d = d
        self.D = D
        self.b = b
        self.phi = phi
        self.dm = (self.D + self.d) / 2
        self.h = (self.D - self.d) / 2

# DIN 5464
class Keilwelle_schwer():
    def __init__(self, n: int, d: int, D: int, b: int, phi: float):
        self.n = n
        self.d = d
        self.D = D
        self.b = b
        self.phi = phi
        self.dm = (self.D + self.d) / 2
        self.h = (self.D - self.d) / 2

# Abmaße
P_dw_von = [10,12,17,22,30,38,44,50,58,65,75,85,95,110,130,150,170]
P_dw_bis = [12,17,22,30,38,44,50,58,65,75,85,95,110,130,150,170,200]
P_b = [4,5,6,8,10,12,14,16,18,20,22,25,38,32,36,40,45]
P_h = [4,5,6,7,8,8,9,10,11,12,14,14,16,18,20,22,25]
P_t1 = [2.5,3,3.5,4,5,5,5.5,6,7,7.5,9,9,10,11,12,13,15]
P_t2 = [1.8,2.3,2.8,3.3,3.3,3.3,3.8,4.3,4.4,4.9,5.4,5.4,6.4,7.4,8.4,9.4,10.4]

Kl_n = [6,6,6,8,8,8,8,8,8,8,10,10,10,10,10]
Kl_d = [23,26,28,32,36,42,46,52,56,62,72,82,92,102,112]
Kl_D = [26,30,32,36,40,46,50,58,62,68,78,88,98,108,120]
Kl_b = [6,6,7,6,7,8,9,10,10,12,12,12,14,16,18]
Kl_phi = [0.75,0.75,0.75,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9]

Km_n = [6,6,6,6,6,6,6,6,8,8,8,8,8,8,8,10,10,10,10,10]
Km_d = [11,13,16,18,21,23,26,28,32,36,42,46,52,56,62,72,82,92,102,112]
Km_D = [14,16,20,22,25,28,32,34,38,42,48,54,60,65,72,82,92,102,112,125]
Km_b = [3,3.5,4,5,5,6,6,7,6,7,8,9,10,10,12,12,12,14,16,18]
Km_phi = [0.75,0.75,0.75,0.75,0.75,0.75,0.75,0.75,0.75,0.75,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9]

Ks_n = [10,10,10,10,10,10,10,10,10,10,16,16,16,16,20,20,20,20]
Ks_d = [16,18,21,23,26,28,32,36,42,46,52,56,62,72,82,92,102,112]
Ks_D = [20,23,26,29,32,35,40,45,52,56,60,65,72,82,92,102,115,125]
Ks_b = [2.5,3,3,4,4,4,5,5,6,7,5,5,6,7,6,7,8,9]
Ks_phi = [0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9,0.9]

# Listen mit Objekten erstellen
Passfeder_Liste = [Passfeder(P_dw_von[i], P_dw_bis[i], P_b[i], P_h[i], P_t1[i], P_t2[i]) for i in range(len(P_b))]
Keilwelle_leicht_Liste = [Keilwelle_leicht(Kl_n[i], Kl_d[i], Kl_D[i], Kl_b[i], Kl_phi[i]) for i in range(len(Kl_n))]
Keilwelle_mittel_Liste = [Keilwelle_mittel(Km_n[i], Km_d[i], Km_D[i], Km_b[i], Km_phi[i]) for i in range(len(Km_n))]
Keilwelle_schwer_Liste = [Keilwelle_schwer(Ks_n[i], Ks_d[i], Ks_D[i], Ks_b[i], Ks_phi[i]) for i in range(len(Ks_n))]

# Werkstoffe
class Baustahl():
    def __init__(self, Bezeichnung: str, Re_u_16: int, Re_u_40: int, Re_u_63: int, Re_u_80: int):
        self.Bezeichunung = Bezeichnung
        self.Re_u_16 = Re_u_16
        self.Re_u_40 = Re_u_40
        self.Re_u_63 = Re_u_63
        self.Re_u_80 = Re_u_80

class Verguetungsstahl():
    def __init__(self, Bezeichnung: str, Re_u_40_von: int, Re_u_40_bis: int, Re_ue_40_von: int, Re_ue_40_bis: int):
        self.Bezeichnung = Bezeichnung
        self.Re_u_40_von = Re_u_40_von
        self.Re_u_40_bis = Re_u_40_bis
        self.Re_ue_40_von = Re_ue_40_von
        self.Re_ue_40_bis = Re_ue_40_bis
        
Namen_Baustahl = ["S185", "S235", "S275", "S355", "S450"]
U_16_Baustahl = [185, 235, 275, 355, 450]
U_40_Baustahl = [175, 225, 265, 345, 430]
U_63_Baustahl = [175, 215, 255, 335, 410]
U_80_Baustahl = [175, 215, 245, 325, 390]

Namen_Verguetungsstahl = ["C22E", "C35", "C35E", "C45", "C45E", "C55", "C55E", "C60", "C60E", "28Mn6", "38Cr2", "46Cr2", "34Cr4", "37Cr4", "25CrMo4", "25CrMoS4", "41Cr4", "41CrS4", "34CrMo4", "34CrMoS4", "42CrMo4", "42CrMoS4", "50CrMo4", "51CrV4", "30NiCrMo16-6", "34CrNiMo6", "36NiCrMo16", "30CrNiMo8", "20MnB5", "30MnB5", "27MnCrB5-2", "39MnCrB6-2"]
U_40_von_V = [410, 520, 600, 580, 650, 640, 750, 670, 800, 600, 700, 800, 800, 850, 800, 800, 900, 900, 900, 900, 1000, 1000, 1000, 1000, 1080, 1100, 1250, 1250, 750, 800, 900, 1050]
U_40_bis_V = [410, 520, 750, 580, 800, 640, 900, 670, 950, 600, 850, 950, 950, 1000, 950, 950, 1100, 1100, 1100, 1100, 1200, 1200, 1200, 1200, 1230, 1300, 1450, 1450, 900, 950, 1150, 1250]
Ue_40_von_V = [410, 520, 550, 580, 630, 640, 700, 670, 750, 600, 600, 650, 700, 750, 700, 700, 800, 800, 800, 800, 900, 900, 900, 900, 1080, 1000, 1100, 1100, 750, 800, 800, 1000]
Ue_40_bis_V = [410, 520, 700, 580, 780, 640, 850, 670, 900, 600, 750, 800, 850, 900, 850, 850, 950, 950, 950, 950, 1100, 1100, 1100, 1100, 1230, 1200, 1300, 1300, 900, 950, 1000, 1200]

Baustaehle = [Baustahl(Namen_Baustahl[i], U_16_Baustahl[i], U_40_Baustahl[i], U_63_Baustahl[i], U_80_Baustahl[i]) for i in range(len(Namen_Baustahl))]
Verguetungsstaehle = [Verguetungsstahl(Namen_Verguetungsstahl[i], U_40_von_V[i], U_40_bis_V[i], Ue_40_von_V[i], Ue_40_bis_V[i]) for i in range(len(Namen_Verguetungsstahl))]
