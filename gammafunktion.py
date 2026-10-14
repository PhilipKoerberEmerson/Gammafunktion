import math
import argparse


def gammafunktionSelbstGemacht(zahl: float) -> float:
	"""Berechnet die Fakultät einer positiven Zahl mithilfe der Gammafunktion (selbstgemacht)."""
	if zahl < 0 and zahl % 1 == 0:
		raise ValueError("Die Zahl darf nicht negativ UND ganzzahlig gerade sein.")
	# Näherung der Gammafunktion nach Lanczos
	p = [
		676.5203681218851,
		-1259.1392167224028,
		771.32342877765313,
		-176.61502916214059,
		12.507343278686905,
		-0.13857109526572012,
		9.9843695780195716e-6,
		1.5056327351493116e-7,
	]
	if zahl < 0.5:
		return math.pi / (math.sin(math.pi * zahl) * gammafunktionSelbstGemacht(1 - zahl))
	zahl -= 1
	x = 0.99999999999980993
	for i, pval in enumerate(p):
		x += pval / (zahl + i + 1)
	t = zahl + len(p) - 0.5
	return math.sqrt(2 * math.pi) * t**(zahl + 0.5) * math.exp(-t) * x

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
	y_werte = [
		math.nan if x <= 0 and x.is_integer() else math.gamma(x)
		for x in x_werte
	]
	selbstgemachte_werte = [
		math.nan if x <= 0 and x.is_integer() else gammafunktionSelbstGemacht(x)
		for x in x_werte
	]
	fakultaetswerte = [
		math.nan if x <= -1 and x.is_integer() else math.gamma(x + 1)
		for x in x_werte
	]
	fig, ax = plt.subplots()
	ax.plot(x_werte, y_werte, label="Gamma(x)")
	ax.plot(x_werte, fakultaetswerte, linestyle="--", label="x! = Gamma(x + 1)")
	ax.plot(
		x_werte, selbstgemachte_werte,
		linestyle=":", linewidth=2, label="Gamma(x) selbstgemacht (Lanczos)",
	)
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
