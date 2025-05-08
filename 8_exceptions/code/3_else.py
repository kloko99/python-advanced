# For else
for i in range(3):
    if i == 22:
        print("Zahl gefunen")
        break
else:
    print("Zahl nicht gefunden.")

# Else im Try-except: Wird immer dann ausgeführt,
# wenn keine Excpetion aufgetreten ist, ob abgefangen oder nicht
try:
    p = int("1")
except ValueError as e:
    print("ValueError")
else:
    print("Es ist kein Fehler aufgetreten:", p)
    # hier mit p sauber weiterarbeiten
finally:
    print("wird immer ausgeführt")