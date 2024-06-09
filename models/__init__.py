import sqlite3

CONN = sqlite3.connect('/home/manucci/Development/phase-3/Moringa-FT09-phase-3-code-challenge/database/magazine.db')
CURSOR = CONN.cursor()