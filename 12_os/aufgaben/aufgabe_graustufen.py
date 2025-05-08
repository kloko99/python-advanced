"""
Aufgabe: Bild in Graustufen konvertieren mit Multiprocessing
Schreibe ein Programm, das ein großes Farbbild (z. B. .jpg)
in Graustufen umwandelt – und zwar blockweise parallel mit multiprocessing.

Anforderungen:
Lade ein Bild mit Pillow (from PIL import Image).
Installieren mit: pip install pillow

Teile es in z.B. 100×100-Pixel-Blöcke auf.

Verwandle jeden Block parallel in Graustufen mit multiprocessing.Pool.

Füge das Ergebnis wieder zum Gesamtbild zusammen.

Speichere das fertige Graustufenbild ab.

Hinweise:
Jede Worker-Funktion bekommt ein Bildsegment und gibt den umgewandelten
Block + Position zurück.

Nutze Pool.map

"""

from multiprocessing import Pool, cpu_count
from typing import TypeAlias
from PIL import Image, ImageOps
from pathlib import Path

# Bildpfad und Blockgröße (ggf. anpassen)
DATA_PATH = Path(__file__).resolve().parent
image_path = DATA_PATH / "testbild.jpg"
block_size = 100

# Bild laden (bleibt so)
image = Image.open(image_path)
width, height = image.size

# Type Aliases zur besseren Lesbarkeit
# Ein Rechteck: (x0, y0, x1, y1)
Box: TypeAlias = tuple[int, int, int, int]
Block: TypeAlias = tuple[Box, Image.Image]  # Ein Farbbild-Block
GrayBlock: TypeAlias = tuple[Box, Image.Image]  # Ein Graustufenblock


def get_blocks(img: Image.Image, block_size: int) -> list[Block]:
    """
    Zerteilt ein Bild in rechteckige Blöcke fester Größe.

    Aufgabe: Bild in gleich große Blöcke (z. B. 100x100 Pixel) zerlegen.
    Jeder Block wird als Tupel (Position, Bildbereich) zurückgegeben.

    Verwendet img.crop(box), um Teilbereiche auszuschneiden. Am Bildrand
    können Blöcke kleiner sein, falls Breite oder Höhe nicht durch
    block_size teilbar sind – dies wird mit min(x + block_size, width)
    bzw. min(y + block_size, height) berücksichtigt.
    """
    blocks: list[Block] = []

    # Originalbild Größe
    width, height = img.size

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            pass
            # 1) Rechteck-Koordinaten berechnen, ohne über das Bild hinauszugehen
            # x, y = linke obere Ecke, x2, y2 = rechte untere Ecke
            # Achtung: x2 und y2 dürfen nicht über den Bildrand hinausgehen.
            # Verwende:
            # x2 = min(x + block_size, width) bzw.
            # y2 = min(y + block_size, height),
            # um übergroße Blöcke am Rand zu vermeiden.

            # box = (x, y, x2, y2)  # Box-tupel mit den Koordinaten

            # 2) Schneide ein Bildblock aus, indem
            # der box-tupel an crop() übergeben wird
            #
            # block_img = img.crop(?)
            #
            # 3) füge zu der blocks-Liste einen Tupel bestehend aus Position (box)
            # und block_img zu:
            # blocks.append(?)  # Tuple(Position, Bildausschnitt)

    return blocks


def convert_to_grayscale(data: Block) -> GrayBlock:
    """
    Aufgabe: Einen Farbblock (PIL.Image) in Graustufen umwandeln.
    Nutzt: ImageOps.grayscale(block)
    Rückgabe: gleicher Block, aber als Graustufenbild.
    """
    box, block = data
    gray_block = ImageOps.grayscale(block)
    return (box, gray_block)


def process_image_multiprocessing(
    image: Image.Image, block_size: int, output_path: str | Path
) -> Path:
    """
    Aufgabe: Bild blockweise in Graustufen umwandeln,
    alle Blöcke zusammenfügen und das Ergebnis speichern.

    1. Bild in Blöcke zerlegen (get_blocks aufrufen)
    2. Blöcke parallel in Graustufen konvertieren (Pool.map)
    3. Neues Graustufenbild zusammensetzen (Image.new + paste)
    4. Als JPG speichern
    """

    # 1) blocks = get_blocks(?)  # Eine Liste aus Tupeln, die die Position
    # und den Bildblock beinhalten

    # 2) mit pool.map die Funktion convert_to_grayscale für die
    # blocks aufrufen
    # erzeugt eine Liste von Tupeln mit Größe, Graustufenbild
    # with Pool(?Anzahl Prozesse) as pool:
    # results = pool.map(? )

    # 3) Leeres, neues Graustufenbild in der Originalgröße erstellen
    # width, height = image.size
    # new_image = Image.new("L", (width, height))  # "L" = Graustufenmodus

    # jetzt an den Positionen (box) die blöcke einfügen
    # for box, gray_block in results:
    #    new_image.paste(gray_block, box)  # Block wieder einfügen

    # output_path = Path(output_path)
    # new_image.save(output_path)
    return output_path'


# Aufruf der Verarbeitung (kann so bleiben)
output_path = process_image_multiprocessing(
    image, block_size, DATA_PATH / "graustufen.jpg"
)

print(f"Graustufenbild gespeichert unter: {output_path}")

