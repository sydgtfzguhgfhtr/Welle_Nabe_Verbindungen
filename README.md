# Welle_Nabe_Verbindungen

## Passfedern berechnen  
### Funktion:  
```
Passfeder(dw, MT, Sf, Werkstoff_Welle, Werkstoff_Nabe, Werkstoff_Passfeder, Anzahl_Passfedern)
```
- dw: Wellendurchmesser  
- MT: zu übertragendes Drehmoment  
- Sf: Sicherheitsfaktor (falls nicht vorhanden Sf=1)  
- Anzahl_Passfedern: 1-3  

### Ausgabe:  
Liste mit folgendem Inhalt:   

0. Breite der Passfeder  
1. Höhe der Passfeder  
2. t1 (Wellennuttiefe) der Passfeder  
3. t2 (Nabennuttiefe) der Passfeder  
4. erforderliche Länge der Passfeder  

$$ \downarrow$$  
```
[b, h, t1, t2, l]
```

## Keilwelle berechnen  
### Funktion:  
```
Keilwelle(dw, MT, Sf, Werkstoff_Welle, Werkstoff_Nabe, Art)
```
- dw: Wellendurchmesser  
- MT: zu übertragendes Drehmoment  
- Sf: Sicherheitsfaktor (falls nicht vorhanden Sf=1)  
- Art: leicht, mittel, schwer (=leichte Reihe...)  

### Ausgabe:  
Liste mit folgendem Inhalt:  

0. Anzahl der Keile  
1. kleiner Durchmesser der Keilwelle  
2. großer Durchmesser der Keilwelle  
3. Breite der Keile  
4. erforderliche Länge der Keilwelle  

$$ \downarrow$$  
```
[n, d, D, b, l]
```
