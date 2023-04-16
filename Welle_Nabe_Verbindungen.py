class Passfeder():
    def __init__(self, dw_von, dw_bis, b, h, t1, t2):
        self.dw_von = dw_von
        self.dw_bis = dw_bis
        self.b = b
        self.h = h
        self.t1 = t1
        self.t2 = t2

dw_von = [10,12,17,22,30,38,44,50,58,65,75,85,95,110,130,150,170]
dw_bis = [12,17,22,30,38,44,50,58,65,75,85,95,110,130,150,170,200]
b = [4,5,6,8,10,12,14,16,18,20,22,25,38,32,36,40,45]
h = [4,5,6,7,8,8,9,10,11,12,14,14,16,18,20,22,25]
t1 = [2.5,3,3.5,4,5,5,5.5,6,7,7.5,9,9,10,11,12,13,15]
t2 = [1.8,2.3,2.8,3.3,3.3,3.3,3.8,4.3,4.4,4.9,5.4,5.4,6.4,7.4,8.4,9.4,10.4]

Passfeder_Liste = []

for i in range(17):
    Passfeder_Liste.append(Passfeder(dw_von[i], dw_bis[i], b[i], h[i], t1[i], t2[i]))

