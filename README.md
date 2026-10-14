# Gammafunktion
Eulers Gammafunktion und die Fakultaet um deren Zusammenhang besser zu verstehen. Dazu verwendet dieses Python
Programm die Gammafunktion aus `math` und eine Näherung nach der von Leonhard Euler entdeckten Formel für die Gammafunktion mit wählbarer Iterationszahl.

![Gammafunktion und Fakultätskurve](kurven.jpg)

## Verwendung

Die Fakultät kann mit einer Zahl als Kommandozeilenparameter berechnet werden:

```sh
python gammafunktion.py 5
```

Die Iterationszahl kann als zweiter Parameter angegeben werden:

```sh
python gammafunktion.py 5 50
python gammafunktion.py k 100
```

Fehlt der zweite Parameter, fragt das Programm immer nach der Iterationszahl,
auch beim Aufruf mit `k`. Sie muss eine positive ganze Zahl sein und gilt
für beide selbstgemachten Berechnungen bzw. Kurven.
Die Produktformel verwendet genau die angegebene Anzahl von Faktoren.
Alle vier numerischen Ergebnisse werden mit genau drei Nachkommastellen
ausgegeben. Die Berechnungen selbst behalten ihre volle Genauigkeit.

Ohne Parameter fragt das Programm nach einer Zahl (oder `k`) und anschließend
nach der Iterationszahl:

```sh
python gammafunktion.py
```

Mit dem Parameter `k` werden die Gammafunktion, die selbstgemachte Gammafunktion
und die Fakultätskurve
von -6 bis 6 in einem eigenen Fenster angezeigt.
Die Zeichenfläche startet mit 800 × 800 Pixeln (8 × 8 Zoll bei 100 dpi);
Fensterrahmen, Werkzeugleiste und Bildschirm-Skalierung können die äußere
Fenstergröße beeinflussen.
Der sichtbare y-Bereich ist ebenfalls auf -6 bis 6 begrenzt.
Beide Achsen haben denselben Maßstab; die Koordinatenachsen bei x = 0
und y = 0 sind hervorgehoben.

```sh
python -m pip install -r requirements.txt
python gammafunktion.py k
```

Der Graph zeigt Gamma(x) in Blau und x! = Gamma(x + 1) in Grün.
Die selbstgemachte Euler-Produktnäherung `gammafunktionSelbstGemacht(x)`
wird in Rot angezeigt, die entsprechende Fakultätsnäherung in Oliv.
Die gewählte Iterationszahl steht in der Legende. Mit steigender
Iterationszahl nähern sich die selbstgemachten Werte den Referenzwerten an.
Die Gammafunktion erweitert dabei die Fakultät
auch auf nicht ganzzahlige Werte. An den Polstellen werden die Kurven
unterbrochen: Gamma(x) ist bei 0, -1, -2, ... nicht definiert,
Gamma(x + 1) bei -1, -2, ... . Werte außerhalb des sichtbaren
y-Bereichs werden nicht angezeigt, aber nicht verändert.

Negative nicht ganzzahlige Werte können ebenfalls eingegeben werden;
an den Polstellen ist die Berechnung nicht definiert.
