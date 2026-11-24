# IdCard

Personal data cards from a records search (検索結果:個人情報). Cards stack as results come in, and the newest one is still loading its photo.

**Theme:** Clock (frame 41).

**Card anatomy:**
- **Frame:** a 3px `color-border-accent` border with 10px rounded corners and a strong amber bloom. A thinner inner frame sits around the content, above the footer.
- **Photo:** a 196px square with a 2px frame on a pale grey ground. The preview draws a neutral silhouette; put an `<img>` inside for a real photo.
- **Name:** Japanese name in `display` 900 at 40px with heavy bloom, and the romanised name under it at 19px (`TAKANASHI,rin`).
- **Fields:** bilingual. Each Japanese label and value is followed by its English version: 学籍 / School, 住所 / Home Address, 性別 / Sex, 血液型 / Blood Type. 11.5px bold with bloom.
- **Barcode row:** a full-width barcode under the photo, generated from the ID number so the same number always gives the same bars. Under it are the number in `mono` 22px and a small secondary bar block.
- **Footer:** two solid amber blocks either side of `検索結果:個人情報 / Search Results : Personal Data`.

**Stacking:** results overlap, each offset down and to the right of the one before, with the newest on top.

**States** (newest card):
- **Searching** (`#searching`): the photo box is empty and dark, a bright bar scans down it, and `SEARCHING` sits in the middle. The card's label says it is loading.
- **Found** (`#found`): the photo resolves in three steps, the scan bar and status go away, and the label gives the full record.

The preview searches for 2.4 seconds in every 9.

**Motion and accessibility:** under `prefers-reduced-motion` the newest card shows as found, with no scan. Each card is an `<article>` whose `aria-label` carries the record.

**Consumer provides:** per card the photo, both name forms, the field pairs and the ID number; and the loading state of the newest card.

**Privacy:** the names and records in the preview are invented. Don't use real people's data in examples.
