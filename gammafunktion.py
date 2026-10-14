import math
import argparse

iterationen = 50

def gammafunktionSelbstGemacht(zahl: float) -> float:
	"""Berechnet die Fakultät einer positiven Zahl mithilfe der Gammafunktion (selbstgemacht)."""
	if zahl < 0 and zahl % 1 == 0:
		raise ValueError("Die Zahl darf nicht negativ UND ganzzahlig gerade sein.")
	# Näherung nach der von Leonhard Euler entdeckten Formel für die Gammafunktion
	selbstBerechntesProdukt = 1
	for n in range(1, iterationen):
		selbstBerechnterWert = (1 + 1/n) ** (zahl - 1) * (1 + (zahl - 1) / n) ** -1
		selbstBerechntesProdukt = selbstBerechnterWert * selbstBerechntesProdukt
	return selbstBerechntesProdukt

def gammafunktion(zahl: float) -> float:
	"""Berechnet die Fakultät einer positiven Zahl mithilfe der Gammafunktion."""
	#if zahl <= 0:
	#	raise ValueError("Die Zahl muss positiv sein.")
	if zahl < 0 and zahl % 1 == 0:
		raise ValueError("Die Zahl darf nicht negativ UND ganzzahlig gerade sein.")
	return math.gamma(zahl)


def zeichne_gammafunktion() -> None:
	import matplotlib.pyplot as plt

	x_werte = [i / 100 for i in range(-600, 601)]
	# NaN unterbricht die Kurven an Polstellen, statt sie dort zu verbinden.
	gammawerte = [
		math.nan if x <= 0 and x.is_integer() else math.gamma(x)
		for x in x_werte
	]
	gammawerte_selbstgemacht = [
		math.nan if x <= 0 and x.is_integer() else gammafunktionSelbstGemacht(x)
		for x in x_werte
	]
	fakultaetswerte = [
		math.nan if x <= -1 and x.is_integer() else math.gamma(x + 1)
		for x in x_werte
	]
	fakultaetswerte_selbstgemacht = [
		math.nan if x <= -1 and x.is_integer() else gammafunktionSelbstGemacht(x + 1)
		for x in x_werte
	]
	fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
	ax.plot(x_werte, gammawerte, color="blue", label="Gamma(x)")
	ax.plot(x_werte, fakultaetswerte, color="green", label="x! = Gamma(x + 1)")
	ax.plot(x_werte, gammawerte_selbstgemacht, color="red", linewidth=1, label=f"Gamma(x) ({iterationen} Iterationen)")
	ax.plot(x_werte, fakultaetswerte_selbstgemacht, color="olive", linewidth=1, label=f"x! ({iterationen} Iterationen)")
	ax.set_xlim(-6.0, 6.0)
	ax.set_ylim(-6.0, 6.0)
	ax.set_aspect("equal", adjustable="box")
	ax.set_xticks(range(-6, 7))
	ax.set_yticks(range(-6, 7))
	ax.axhline(0, color="black", linewidth=0.8)
	ax.axvline(0, color="black", linewidth=0.8)
	ax.set_xlabel("x")
	ax.set_ylabel("Funktionswert")
	ax.set_title("Gammafunktion und Fakultät")
	ax.grid(True)
	ax.legend()
	fig.tight_layout()
	plt.show()


def main() -> None:
	parser = argparse.ArgumentParser(
		description="Berechnet eine Fakultät oder zeichnet mit 'k' die Gammafunktion."
	)
	parser.add_argument(
		"zahl",
		nargs="?",
		help="Zahl, deren Fakultät berechnet werden soll, oder 'k' für den Graphen",
	)
	args = parser.parse_args()

	if args.zahl == "k":
		zeichne_gammafunktion()
		return

	try:
		zahl = args.zahl
		if zahl is None:
			zahl = input("Bitte gib eine positive Zahl ein, oder k für den Graphen: ")
		if zahl == "k":
			zeichne_gammafunktion()
			return
		zahl = float(zahl)
		ergebnis = gammafunktion(zahl)
		selbstgemacht = gammafunktionSelbstGemacht(zahl)
		fakultaet = gammafunktion(zahl + 1)
		fakultaetSelbstgemacht = gammafunktionSelbstGemacht(zahl + 1)
		
	except ValueError as error:
		parser.error(str(error))

	print(f"Gamma({zahl}) = {ergebnis}")
	print(f"Gamma({zahl}) = {selbstgemacht} (selbstgemacht)")
	print(f"      {zahl}! = {fakultaet}")
	print(f"      {zahl}! = {fakultaetSelbstgemacht} (selbstgemacht)")
	

if __name__ == "__main__":
	main()
