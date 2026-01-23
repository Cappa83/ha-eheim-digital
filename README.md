# EHEIM Professional 5e – Home Assistant Integration

Diese Integration ist ein Grundgerüst für den EHEIM Professional 5e Filter. Sie ist als **benutzerdefiniertes Repository** (HACS Custom Repository) vorbereitet und kann direkt in Home Assistant eingebunden werden.

## Installation (HACS Custom Repository)

1. Öffne **HACS → Integrationen → ⋮ → Benutzerdefiniertes Repository**.
2. Füge die URL dieses Repositories hinzu und wähle als Kategorie **Integration**.
3. Installiere die Integration über HACS.
4. Starte Home Assistant neu.

## Installation (manuell)

1. Kopiere den Ordner `custom_components/eheim_professional_5e` in dein Home-Assistant-`config/custom_components` Verzeichnis.
2. Starte Home Assistant neu.

## Konfiguration

Die Konfiguration erfolgt ausschließlich über die UI und benötigt **nur die IP-Adresse** des Filters.

## API-Abfrage (erste Version)

Die Integration ruft den Filter über eine einfache HTTP-GET-Abfrage ab:

```
http://<IP>/api?to=
```

Der Query-Parameter `to` ist optional und kann die Ziel-MAC-Adresse enthalten. In dieser ersten Version bleibt er leer.

### Beispiel-Antwort (Auszug)

Wichtige Felder, die als Sensoren abgebildet werden:

- `filterActive` (1 = aktiv, 0 = inaktiv)
- `freq` / `freqSoll` (aktuelle / Ziel-Frequenz)
- `rotSpeed` (Rotor-Drehzahl in Hz, Wert wird durch 100 geteilt)
- `runTime` (Laufzeit in Minuten)
- `serviceHour` (Service-Intervall in Stunden)
- `version` (Hardware-Version)

### Flow-Rate-Tabellen

**Liter (EU-Modelle)**

| flowRate | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filter 350 | 400 | 440 | 480 | 515 | 550 | 585 | 620 | 650 | 680 | 710 | 740 | 770 | 800 | 830 | 860 |
| Filter 450 | 400 | 460 | 515 | 565 | 610 | 650 | 690 | 730 | 770 | 805 | 840 | 875 | 910 | 945 | 980 |
| Filter 600T & 700 | 400 | 470 | 540 | 600 | 650 | 700 | 745 | 785 | 825 | 865 | 905 | 945 | 985 | 1025 | 1065 |

**Gallonen (US-Markt)**

| flowRate | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Filter 350 | 110 | 120 | 130 | 140 | 145 | 155 | 165 | 175 | 180 | 190 | 195 | 205 | 215 | 220 | 230 |
| Filter 450 | 110 | 125 | 140 | 150 | 165 | 175 | 185 | 195 | 205 | 215 | 225 | 235 | 240 | 250 | 260 |
| Filter 600T & 700 | 110 | 125 | 145 | 165 | 175 | 185 | 200 | 210 | 220 | 230 | 240 | 250 | 260 | 275 | 285 |
