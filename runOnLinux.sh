#!/usr/bin/env bash
set -e  # Beendet das Skript sofort, falls ein Schritt fehlschlägt

# 1. Sicherstellen, dass python3-venv (und python3-tk für den Plot) unter Ubuntu installiert sind
if ! python3 -c "import venv, tkinter" >/dev/null 2>&1; then
    echo "Fehlende Systempakete werden installiert (Passwort erforderlich)..."
    sudo apt-get update && sudo apt-get install -y python3-venv python3-tk
fi

# 2. Virtuelle Umgebung erstellen, falls noch nicht vorhanden
if [ ! -d ".venv" ]; then
    echo "Erstelle virtuelle Umgebung (.venv)..."
    python3 -m venv .venv
fi

# 3. Virtuelle Umgebung für dieses Skript aktivieren
source .venv/bin/activate

# 4. Requirements installieren / abgleichen
echo "Prüfe und installiere Abhängigkeiten..."
python -m pip install --upgrade pip -q
python -m pip install -r requirements.txt -q

# 5. Python-Skript starten und alle übergebenen Parameter ("$@") durchreichen
echo "Starte gammafunktion.py..."
python gammafunktion.py "$@"

# 6. Deaktivieren (geschieht beim Skript-Ende auch automatisch)
deactivate
