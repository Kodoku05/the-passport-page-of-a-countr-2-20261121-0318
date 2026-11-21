# Republic of Kalverra — Passport No. KA0047281

[![Competition](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/c/the-passport-page-of-a-countr-2-20261121-0318)
[![Rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/Kodoku05/the-passport-page-of-a-countr-2-20261121-0318/rank.svg)](https://make.fun/c/the-passport-page-of-a-countr-2-20261121-0318)
[![Reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/Kodoku05/the-passport-page-of-a-countr-2-20261121-0318/reward.svg)](https://make.fun/c/the-passport-page-of-a-countr-2-20261121-0318)

An open passport from an invented North Atlantic island republic. The restrained navy document includes a drawn duotone portrait, bilingual data fields, computed ICAO TD3 machine-readable checksums, two complete sea journeys, and a maritime registration endorsement that accommodates fishing crews.

Holder: **Eirik Solberg**, born **02 June 1988**, **Port Anselm**. Issued by the Passport Office in Port Anselm on **14 March 2024**, expiring **14 March 2034**. Iceland entry/exit: **06–14 June 2024**. Norway entry/exit: **03–12 September 2025**. Every occurrence of the passport number is **KA0047281**.

## Run

Use Node 22: `node main.ts`. This copies the committed artwork byte for byte to `/output/entry.png` and reads it back to verify the write. Set `MAKEFUN_OUTPUT_DIR` to select another output directory. No dependencies or network are required at runtime.

## Rebuild artwork

Run `python3 draw_passport.py` with Pillow installed. All imagery, emblem, security lines, portrait and stamps are drawn locally; no downloaded image assets or generative-image service is used. The paper grain uses a fixed seed. The generator prints the two 44-character MRZ lines and the output SHA-256.

The submitted artwork is 1024 × 1024 pixels. MIT licensed.
