"""
Añade un negocio nuevo a landing/negocios.json de forma segura
(evita errores de sintaxis al editar el JSON a mano).

Uso:
    python3 anadir_negocio.py cafe-lantana "Café Lantana" "☕" hosteleria "https://g.page/r/XXXX/review" "dueño@ejemplo.com"

El primer argumento es el slug: el identificador corto que irá en el QR
(https://tudominio.com/landing.html?n=cafe-lantana), sin espacios ni tildes.

La categoría debe coincidir con una de las que existen en comentarios.json
(por ahora: hosteleria, automocion, generico). Si pones una que no existe,
la landing usará "generico" automáticamente como respaldo.
"""

import json
import sys
from pathlib import Path

NEGOCIOS_PATH = Path(__file__).resolve().parent.parent / "docs" / "negocios.json"


def anadir(slug, business_name, emoji, category, google_review_url, owner_email):
    negocios = json.loads(NEGOCIOS_PATH.read_text(encoding="utf-8"))

    if slug in negocios:
        print(f"Aviso: '{slug}' ya existía, se ha sobrescrito.")

    negocios[slug] = {
        "business_name": business_name,
        "emoji": emoji,
        "category": category,
        "google_review_url": google_review_url,
        "owner_email": owner_email,
    }

    NEGOCIOS_PATH.write_text(
        json.dumps(negocios, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Añadido '{slug}'. El QR de este negocio debe apuntar a:")
    print(f"  https://TUDOMINIO/landing.html?n={slug}")


if __name__ == "__main__":
    if len(sys.argv) != 7:
        sys.exit(
            "Uso: python3 anadir_negocio.py <slug> <nombre> <emoji> <categoria> <enlace_google> <email_dueño>"
        )
    anadir(*sys.argv[1:])
