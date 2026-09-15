# Reviews QR

QR para negocios que dirige al cliente directo a la puntuación/reseñas de Google, evitando el trámite de buscar el negocio a mano.

## La idea en una frase (esto es lo único que se vende)
> Escaneas, puntúas. Si vas bien, te lleva a Google. Si vas mal, le llega un email directo al negocio. El negocio no tiene que hacer nada más.

## Estado actual: MVP — Capa 1 únicamente
Construimos solo lo mínimo vendible. Todo lo demás es fase 2 y NO se toca ni se menciona en la venta todavía.

**Incluido en el MVP:**
- Landing de valoración (`landing/template-base.html`) con flujo de estrellas
- 4-5★ → prioriza botón a reseña de Google (sin ocultar el enlace nunca, por política de Google — nada de "review gating")
- 1-3★ → prioriza feedback privado por email al dueño
- Alta de negocio simple (enlace de Google + email + nombre)

**Explícitamente fuera del MVP (fase 2, después de tener clientes reales):**
- Plantillas de diseño distintas por categoría de negocio (vía Google Places API)
- Descuentos por valorar (requiere código de un solo uso + atado a compra en persona, para evitar abuso)
- Panel de seguimiento/analíticas para el negocio
- Web pública de pedido online con productos físicos (tarjeta, tótem de madera...)

Razón: cada función de fase 2 pide al negocio aprender algo o cambiar un hábito. Eso agobia en la venta inicial — se ofrece más adelante, cuando el negocio ya confía en el producto.

## Estructura del repo
- `landing/` — **esta carpeta entera es lo que subes al hosting** (GitHub Pages, Netlify...):
  - `landing.html` — la landing de valoración. Es ÚNICA para todos los negocios, no se duplica.
  - `negocios.json` — la base de datos de todos los negocios (nombre, emoji, enlace de Google, email del dueño). El QR de cada negocio apunta a `landing.html?n=<slug>`, y la página busca ese slug en este JSON.
- `onboarding/anadir_negocio.py` — añade un negocio nuevo a `negocios.json` sin riesgo de romper el JSON a mano
- `docs/` — pitch, pricing, decisiones
- `website/` — vacío por ahora (fase 2)
- `clients/` — notas internas privadas (no se despliega, no va en el JSON público)

**Nota de privacidad**: `negocios.json` se despliega público (lo carga el navegador del cliente). Contiene el email de cada negocio. Es una contrapartida asumida por simplicidad — revisar si se vuelve un problema real con más volumen de negocios.

## Próximos pasos
1. Subir `landing/` a un hosting (GitHub Pages) para tener una URL real
2. Generar el QR de prueba con esa URL + `?n=cafe-lantana`
3. Primeros 10-15 negocios probados en persona
