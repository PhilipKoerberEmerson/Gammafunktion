import math
import argparse


def gammafunktion(zahl: float) -> float:
	"""Berechnet die Fakultät einer positiven Zahl mithilfe der Gammafunktion."""
	if zahl <= 0:
		raise ValueError("Die Zahl muss positiv sein.")
	return math.gamma(zahl)


def zeichne_gammafunktion() -> None:
	import matplotlib.pyplot as plt

	x_werte = [0.1 + (5.0 - 0.1) * i / 490 for i in range(491)]
	y_werte = [math.gamma(x) for x in x_werte]
	fakultaets_x_werte = [0.1 + (4.0 - 0.1) * i / 390 for i in range(391)]
	fakultaetswerte = [math.gamma(x + 1) for x in fakultaets_x_werte]
	fig, ax = plt.subplots()
	ax.plot(x_werte, y_werte, label="Gamma(x)")
	ax.plot(fakultaets_x_werte, fakultaetswerte, linestyle="--", label="x! = Gamma(x + 1)")
	ax.set_xlim(0.1, 5.0)
	ax.set_xlabel("x")
	ax.set_ylabel("Funktionswert")
	ax.set_title("Gammafunktion bis 5 und Fakultät bis 4")
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
		fakultaet = gammafunktion(zahl + 1)
		
	except ValueError as error:
		parser.error(str(error))

	print(f"Gamma({zahl}) = {ergebnis}")
	print(f"      {zahl}! = {fakultaet}")

if __name__ == "__main__":
	main()
