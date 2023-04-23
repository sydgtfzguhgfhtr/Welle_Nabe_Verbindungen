import math

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

class Einsatzstahl():
    def __init__(self, Bezeichnung: str, Rm_von: int, Rm_bis: int):
        self.Bezeichnung = Bezeichnung
        self.Rm_von = Rm_von
        self.Rm_bis = Rm_bis

class Gusseisen_Lammellengrafit_C():
    def __init__(self, Bezeichnung: str, Rm: int):
        self.Bezeichnung = Bezeichnung
        self.Rm = Rm

class Temperguss_C():
    def __init__(self, Bezeichnung: str, Rm: int):
        self.Bezeichnung = Bezeichnung
        self.Rm = Rm

class Gusseiden_Kugelgrafit_C():
    def __init__(self, Bezeichnung: str, Rm: int):
        self.Bezeichnung = Bezeichnung
        self.Rm = Rm

class Stahlguss_C():
    def __init__(self, Bezeichnung: str, Rm: int):
        self.Bezeichnung = Bezeichnung
        self.Rm = Rm

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

Namen_Einsatzstahl = ["C10E", "C10R", "C15E", "C15R", "17Cr3", "17CrS3", "16MnCr5", "16MnCrS5", "16MnCrB5", "16NiCr4", "16NiCrS4", "18CrMo4", "18CrMoS4", "20MoCr3", "20MoCrS3", "20MoCr4", "20MoCrS4", "17CrNi6-6", "22CrMoS3-3", "15NiCr13", "10NiCr5-4", "20NiCrMo2-2", "20NiCrMoS2-2", "17NiCrMo6-4", "17NiCrMoS6-4", "20NiCrMoS6-4", "20MnCr5", "20MnCrS5", "18NiCr5-4", "14NiCrMo13-4", "20NiCrMo13-4", "18CrNiMo7-6"]
Rm_von_E = [490, 490, 590, 590, 700, 700, 780, 780, 900, 980, 980, 930, 930, 780, 780, 780, 780, 1100, 1000, 920, 900, 800, 800, 1000, 1000, 1100, 980, 980, 1100, 1030, 1400, 1100]
Rm_bis_E = [640, 640, 780, 780, 900, 900, 1080, 1080, 900, 1270, 1270, 1300, 1300, 1080, 1080, 1080, 1080, 1100, 1000, 1230, 900, 800, 800, 1000, 1000, 1100, 1270, 1270, 1100, 1080, 1400, 1100]

Namen_Guss_Lamelle = ["EN-GJL-100","EN-GJL-150","EN-GJL-200","EN-GJL-250","EN-GJL-300","EN-GJL-350"]
Rm_Guss_L = [100, 130, 180, 225, 270, 315]

Namen_Temperguss = ["EN-GJMW-350-4","EN-GJMW-400-5","EN-GJMW-450-7","EN-GJMW-550-4","EN-GJMW-360-12","EN-GJMB-300-6","EN-GJMB-350-10","EN-GJMB-450-6","EN-GJMB-500-5","EN-GJMB-550-4","EN-GJMB-600-3","EN-GJMB-650-2","EN-GJMB-700-2","EN-GJMB-800-1"]
Rm_Temp = [350,400,450,550,360,300,350,450,500,550,600,650,700,800]

Namen_Guss_Kugel = ["EN-GJS-350-22-LT","EN-GJS-350-22-RT","EN-GJS-350-22","EN-GJS-400-18-LT","EN-GJS-400-18-RT","EN-GJS-400-18","EN-GJS-400-15","EN-GJS-450-10","EN-GJS-500-7","EN-GJS-600-3","EN-GJS-700-2","EN-GJS-800-2","EN-GJS-900-2","EN-GJS-450-18","EN-GJS-500-14","EN-GJS-600-10"]
Rm_Kugel = [350,350,350,400,400,400,400,450,500,600,700,800,900,450,500,600]

Namen_Stahlguss = ["GE200","GE240","GE300","G17Mn5","G20Mn5","GX4CrNiMo16-5-1","G28Mn6","G10MnMoV6-3","G34CrMo4","G32NiCrMo8-5-4","GX23CrMoV12-1"]
Rm_Stahlguss = [455,525,675,525,550,860,600,675,775,925,810]

Baustaehle = [Baustahl(Namen_Baustahl[i], U_16_Baustahl[i], U_40_Baustahl[i], U_63_Baustahl[i], U_80_Baustahl[i]) for i in range(len(Namen_Baustahl))]
Verguetungsstaehle = [Verguetungsstahl(Namen_Verguetungsstahl[i], U_40_von_V[i], U_40_bis_V[i], Ue_40_von_V[i], Ue_40_bis_V[i]) for i in range(len(Namen_Verguetungsstahl))]
Einsatzstaehle = [Einsatzstahl(Namen_Einsatzstahl[i], Rm_von_E[i], Rm_bis_E[i]) for i in range(len(Namen_Einsatzstahl))]
Gusseisen_Lamellengrafit = [Gusseisen_Lammellengrafit_C(Namen_Guss_Lamelle[i], Rm_Guss_L[i]) for i in range(len(Namen_Guss_Lamelle))]
Temperguss = [Temperguss_C(Namen_Temperguss[i], Rm_Temp[i]) for i in range(len(Namen_Temperguss))]
Gusseisen_Kugelgrafit = [Gusseiden_Kugelgrafit_C(Namen_Guss_Kugel[i], Rm_Kugel[i]) for i in range(len(Namen_Guss_Kugel))]
Stahlguss = [Stahlguss_C(Namen_Stahlguss[i], Rm_Stahlguss[i]) for i in range(len(Namen_Stahlguss))]

def Re_nach_Größe(Werkstoff, d, i):
    if Werkstoff in Namen_Baustahl:
        if d <= 16:
            Re = Baustaehle[i].Re_u_16
        elif d <= 40:
            Re = Baustaehle[i].Re_u_40
        elif d <= 63:
            Re = Baustaehle[i].Re_u_63
        else:
            Re = Baustaehle[i].Re_u_80
    elif Werkstoff in Namen_Verguetungsstahl:
        if d <= 40:
            Re = (Verguetungsstaehle[i].Re_u_40_von + Verguetungsstaehle[i].Re_u_40_bis)/2
        else:
            Re = (Verguetungsstaehle[i].Re_ue_40_von + Verguetungsstaehle[i].Re_ue_40_bis)/2
    elif Werkstoff in Namen_Einsatzstahl:
        Re = (Einsatzstaehle[i].Rm_von + Einsatzstaehle[i].Rm_bis)/2
    elif Werkstoff in Namen_Guss_Lamelle:
        Re = Gusseisen_Lamellengrafit[i].Rm
    elif Werkstoff in Namen_Temperguss:
        Re = Temperguss[i].Rm
    elif Werkstoff in Namen_Guss_Kugel:
        Re = Gusseisen_Kugelgrafit[i].Rm
    elif Werkstoff in Namen_Stahlguss:
        Re = Stahlguss[i].Rm
    else:
        raise ValueError("Werkstoff nicht bekannt")
    
    return Re

def Grösseneinflussfaktor_Kt(Werkstoff, d):
    if Werkstoff in Namen_Baustahl:
        Kt = 1-0.23*math.log10(d/32)
        if Kt < 0.89: Kt = 0.89
        if Kt >= 1: Kt = 1
    elif Werkstoff in Namen_Verguetungsstahl:
        Kt = 1-0.26*math.log10(d/16)
        if Kt < 0.67: Kt = 0.67
        if Kt >= 1: Kt = 1
    elif Werkstoff in Namen_Einsatzstahl:
        Kt = 1-0.41*math.log10(d/11)
        if Kt < 0.41: Kt = 0.41
        if Kt >= 1: Kt = 1
    elif Werkstoff in Namen_Guss_Lamelle:
        Kt = -0.3760574852272785 * math.log10( d ) + 1.5082467648888314
        if Kt < 0.56: Kt = 0.56
        if Kt >= 1.2: Kt = 1.2
    elif Werkstoff in Namen_Temperguss:
        Kt = -0.11985755012367008 * math.log10(d) + 1.1412951447553383
        if Kt < 0.825: Kt = 0.825
        if Kt >= 1: Kt = 1
    elif Werkstoff in Namen_Guss_Kugel:
        Kt = -0.13359602848294613*math.log10(d)+1.2386319918784392
        if Kt < 0.89: Kt = 0.89
        if Kt > 1: Kt = 1
    elif Werkstoff in Namen_Stahlguss:
        Kt = -0.12471967507884896*math.log10(d)+1.2493459085173144
        if Kt < 0.925: Kt = 0.925
        if Kt > 1: Kt = 1
    else:
        raise ValueError("Werkstoff nicht bekannt")    
    return Kt

def Nummer(Werkstoff):
    i = 0
    if Werkstoff in Namen_Baustahl:
        for i in range(len(Namen_Baustahl)):
            if Werkstoff == Namen_Baustahl[i]:
                return i
    elif Werkstoff in Namen_Verguetungsstahl:
        for i in range(len(Namen_Verguetungsstahl)):
            if Werkstoff == Namen_Verguetungsstahl[i]:
                return i
    elif Werkstoff in Namen_Einsatzstahl:
        for i in range(len(Namen_Einsatzstahl)):
            if Werkstoff == Namen_Einsatzstahl[i]:
                return i
    elif Werkstoff in Namen_Guss_Lamelle:
        for i in range(len(Namen_Guss_Lamelle)):
            if Werkstoff == Namen_Guss_Lamelle[i]:
                return i
    elif Werkstoff in Namen_Temperguss:
        for i in range(len(Namen_Temperguss)):
            if Werkstoff == Namen_Temperguss[i]:
                return i
    elif Werkstoff in Namen_Guss_Kugel:
        for i in range(len(Namen_Guss_Kugel)):
            if Werkstoff == Namen_Guss_Kugel[i]:
                return i
    elif Werkstoff in Namen_Stahlguss:
        for i in range(len(Namen_Stahlguss)):
            if Werkstoff == Namen_Stahlguss[i]:
                return i
    else:
        raise ValueError("Werkstoff nicht bekannt")

def P_ZUL(Werkstoff: str, d: float, Sf: float):
    Re = Re_nach_Größe(Werkstoff, d, Nummer(Werkstoff))
    Kt = Grösseneinflussfaktor_Kt(Werkstoff, d)
    p = (Re*Kt)/Sf
    return p

def Passfeder(dw: int, MT: float, Sf: float, Werkstoff_Welle: str, Werkstoff_Nabe: str, Werkstoff_Passfeder: str, Anzahl_Passfedern: int):
    """Berechnung Passfeder

    Args:
        dw (int): Durchmesser der Welle in mm
        MT (float): wirkendes Drehmoment in Nm
        Sf (float): Sicherheitsfaktor
        Werkstoff_Welle (str): Werkstoff der Welle
        Werkstoff_Nabe (str): Werkstoff der Nabe
        Werkstoff_Passfeder (str): Werkstoff der Passfedern
        Anzahl_Passfedern (int): Anzahl der Passfedern (1-3)
    return Liste:
        [Breite, Höhe, t1, t2, Länge] in mm
    """
    MT = MT*1000
    for Passfeder_Nummer in range(len(Passfeder_Liste)):
        if Passfeder_Liste[Passfeder_Nummer].dw_von <= dw and Passfeder_Liste[Passfeder_Nummer].dw_bis > dw:
            break

    p_Welle = P_ZUL(Werkstoff_Welle, dw, Sf)
    p_Nabe = P_ZUL(Werkstoff_Nabe, dw*2.2, Sf)
    p_Passfeder = P_ZUL(Werkstoff_Passfeder, Passfeder_Liste[Passfeder_Nummer].b, Sf)

    pzul = min(p_Welle, p_Nabe, p_Passfeder)

    l1 = (2*MT)/(dw*pzul*(Passfeder_Liste[Passfeder_Nummer].h-Passfeder_Liste[Passfeder_Nummer].t1))+Passfeder_Liste[Passfeder_Nummer].b
    l2 = (2*MT)/(dw*pzul*(Passfeder_Liste[Passfeder_Nummer].h-Passfeder_Liste[Passfeder_Nummer].t1)*2*0.75)+Passfeder_Liste[Passfeder_Nummer].b
    l3 = (2*MT)/(dw*pzul*(Passfeder_Liste[Passfeder_Nummer].h-Passfeder_Liste[Passfeder_Nummer].t1)*3*0.75)+Passfeder_Liste[Passfeder_Nummer].b

    mögl_Längen = [8, 10, 12, 14, 16, 18, 20, 22, 25, 28, 32, 36, 40, 45, 50, 56, 63, 70, 80, 90, 100, 110, 125, 140, 160, 180, 200, 220, 250, 280, 320, 360, 400]

    for i in range(len(mögl_Längen)):
        if l1 <= mögl_Längen[i]:
            l1 = mögl_Längen[i]
            break

    for i in range(len(mögl_Längen)):
        if l2 <= mögl_Längen[i]:
            l2 = mögl_Längen[i]
            break

    for i in range(len(mögl_Längen)):
        if l3 <= mögl_Längen[i]:
            l3 = mögl_Längen[i]
            break
        
    if Anzahl_Passfedern == 1:
        l = l1
    elif Anzahl_Passfedern == 2:
        l = l2
    elif Anzahl_Passfedern == 3:
        l = l3
    else:
        raise ValueError("nur 1, 2 oder 3 Passfedern möglich")
        
    return[Passfeder_Liste[Passfeder_Nummer].b, Passfeder_Liste[Passfeder_Nummer].h, Passfeder_Liste[Passfeder_Nummer].t1, Passfeder_Liste[Passfeder_Nummer].t2, l]

def Keilwelle(dw: int, MT: float, Sf: float, Werkstoff_Welle: str, Werkstoff_Nabe: str, Art: str):
    """Berechnung Keilwelle

    Args:
        dw (int): Durchmesser der Welle in mm
        MT (float): Drehmoment in Nm
        Sf (float): Sicherheitsfaktor
        Werkstoff_Welle (str): Werkstoff der Welle
        Werkstoff_Nabe (str): Werkstoff der Nabe
        Art (str): leicht, mittel, schwer
    Returns:
        Liste[
        n...Anzahl der Keile,
        d...kleiner Durchmesser,
        D...großer Durchmesser,
        b...Breite der Keile,
        l...erforderliche Länge der Keilwell
        ]
    """
    if Art == "leicht":
        Keilwelle = Keilwelle_leicht_Liste
    elif Art == "mittel":
        Keilwelle = Keilwelle_mittel_Liste
    elif Art == "schwer":
        Keilwelle = Keilwelle_schwer_Liste
    else:
        raise ValueError("nur leicht, mittel oder schwer möglich")

    MT = 1000*MT

    for k in range(len(Keilwelle)):
        if Keilwelle[k].d >= dw:
            nr = k
            break

    p_Welle = P_ZUL(Werkstoff_Welle, dw, Sf)
    p_Nabe = P_ZUL(Werkstoff_Nabe, 2*dw, Sf)

    p_zul = min(p_Welle, p_Nabe)

    i = 1

    while True:
        p = (2*MT)/(Keilwelle[k].dm*Keilwelle[k].h*i*Keilwelle[k].n*Keilwelle[k].phi)
        if p >= 0 and p <= p_zul:
            break
        i += 1

    Maße = [Keilwelle[k].n, Keilwelle[k].d, Keilwelle[k].D, Keilwelle[k].b, i]
    return Maße

