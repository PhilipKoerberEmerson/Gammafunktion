import sys


def fakultaet(zahl: int) -> int:
    if zahl < 0:
        raise ValueError("Die Zahl muss nichtnegativ sein.")

    ergebnis = 1
    for faktor in range(2, zahl + 1):
        ergebnis *= faktor
    return ergebnis


def main() -> int:
    try:
        zahl = int(input("Nichtnegative ganze Zahl eingeben: "))
        ergebnis = fakultaet(zahl)
    except (ValueError, EOFError):
        print("Fehler: Bitte eine nichtnegative ganze Zahl eingeben.", file=sys.stderr)
        return 1

    # Auch sehr große Ergebnisse vollständig als Dezimalzahl ausgeben.
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    print(f"{zahl}! = {ergebnis}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
