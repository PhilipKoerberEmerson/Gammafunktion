# Gammafunktion
Eulers Gammafunktion und die Fakultaet um deren Zusammenhang besser zu verstehen. Dazu verwendet dieses Python
Programm seine eigene Gamma-Funtion aus Math und eine Näherung nach der von Leonhard Euler entdeckten Formel für die Gammafunktion mit 50 Iterationen.

## Verwendung

Die Fakultät kann mit einer Zahl als Kommandozeilenparameter berechnet werden:

```sh
python gammafunktion.py 5
```

Ohne Parameter fragt das Programm nach einer Zahl:

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

Frühere Darstellung mit dem y-Bereich von -25 bis 25:

![Frühere Darstellung der Gammafunktion und Fakultätskurve](kurven.jpg)

```sh
python -m pip install -r requirements.txt
python gammafunktion.py k
```

Der Graph zeigt Gamma(x) als durchgezogene Kurve und x! = Gamma(x + 1)
als gestrichelte Kurve. Die selbstgemachte Lanczos-Näherung
`gammafunktionSelbstGemacht(x)` wird als gelbe, gepunktete dritte Kurve angezeigt.
Sie liegt aufgrund der hohen Genauigkeit nahezu auf der Gamma(x)-Kurve.
Die Gammafunktion erweitert dabei die Fakultät
auch auf nicht ganzzahlige Werte. An den Polstellen werden die Kurven
unterbrochen: Gamma(x) ist bei 0, -1, -2, ... nicht definiert,
Gamma(x + 1) bei -1, -2, ... . Werte außerhalb des sichtbaren
y-Bereichs werden nicht angezeigt, aber nicht verändert.

Die numerische Eingabe akzeptiert weiterhin nur positive Zahlen.
