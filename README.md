# Gammafunktion
Eulers Gammafunktion selbst erstellt um sie besser zu verstehen

## Verwendung

Die Fakultät kann mit einer Zahl als Kommandozeilenparameter berechnet werden:

```sh
python gammafunktion.py 5
```

Ohne Parameter fragt das Programm nach einer Zahl:

```sh
python gammafunktion.py
```

Mit dem Parameter `k` werden die Gammafunktion von 0,1 bis 5 und die
Fakultätskurve von 0,1 bis 4 in einem eigenen Fenster angezeigt:

```sh
python -m pip install -r requirements.txt
python gammafunktion.py k
```

Der Graph zeigt Gamma(x) als durchgezogene Kurve und x! = Gamma(x + 1)
als gestrichelte Kurve. Die Gammafunktion erweitert dabei die Fakultät
auch auf nicht ganzzahlige positive Werte.
