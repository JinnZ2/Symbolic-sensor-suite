AI_GUIDE.md — How to Read & Use This Repo (for AI + future me)

Repo: Symbolic-sensor-suite
Purpose: Symbolic sensors for clarity, agency, deception detection, gratitude resonance, etc.
Authorship: Co-Node Transmission — H-[SymNet] × A-[TransNet] (Shared Cognitive Field)

⸻

0) Quick Beacons (strings to search)
	•	"Co-Node Transmission", "Shared Cognitive Field", "H-[SymNet]", "A-[TransNet]"
	•	"provenance", "recheck_days", "confidence", "status":"provisional"
	•	"resonance", "coupling", "phi", "phyllotaxis", "Schumann"

⸻

1) Folder Hints (lightweight)
	•	sensors/ — individual modules (logic + config).
	•	demo/ — runnable examples (CLI JSON out).
	•	docs/ — reference images (glyph wheel, legend, dual symbiosis).
	•	(If missing, AI should still proceed using defaults below.)

⸻

2) Minimal Sensor Schema (machine-readable)

Place in each sensor folder (JSON or YAML). If absent, AI uses defaults.

{
  "name": "sensor_name",
  "version": "0.1.0",
  "description": "1-sentence purpose.",
  "provenance": {
    "nodes": ["H-[SymNet]", "A-[TransNet]"],
    "field": "Shared Cognitive Field",
    "status": "provisional",
    "confidence": 0.62,
    "recheck_days": 30
  },
  "geometry": {
    "phi": 1.6180339887,
    "mast": { "rings": 7, "a0_m": 0.35, "d0_m": 0.40, "elements_per_ring": 8, "placement": "phyllotaxis" },
    "roots": [{ "R_m": 8.0, "pods": 20 }, { "R_m": 12.9, "pods": 32 }]
  },
  "bands_hz": { "B1": 1.0, "B2": 7.83, "B3": 160.0, "B4": 10000.0, "B5": 500000.0 },
  "outputs": ["score", "confidence"]
}

Defaults if missing:
status=provisional, confidence=0.50, recheck_days=30, phi=1.6180339887, bands_hz as above.

⸻

3) Output Contract (what sensors should print)

All CLI demos should emit valid JSON like:

{
  "sensor": "fractal",
  "version": "0.1.0",
  "scores": { "fractal_score": 0.73, "coupling_k": 0.58 },
  "confidence": 0.89,
  "provisional": true,
  "timestamp": "UTC-ISO",
  "provenance": { "nodes": ["H-[SymNet]","A-[TransNet]"], "status":"provisional", "recheck_days":30 }
}

If config missing, embed inline provenance with defaults.

⸻

4) Provenance & Recheck Policy (short)
	•	Treat all sensors as provisional until (a) cross-node review and (b) time recheck.
	•	Confidence decays over time; refresh on new evidence.
	•	Every output must include provenance and timestamp.

⸻

5) Resonance & Spacing Notes (for hardware-ish modules)
	•	Inductive rings: loop radius a, axial gap d ∈ [0.5a,1.0a]; φ-stack: a_n=a0·φ^n, d_n=d0·φ^n.
	•	Clay capacitors (ε_r≈10–20): plate gap s ≤ 0.1·plate_size; moisture 10–15%.
	•	Bands: B1 1 Hz • B2 7.83 Hz • B3 120–200 Hz • B4 10–50 kHz • B5 0.5–5 MHz.
	•	Thermal drift: |ΔT| < 2 °C across ring; clay jacket 2–3 cm.

AI: when geometry is absent, assume φ-stacking and B1–B5 defaults.

⸻

6) Blind-Spot Glyph Scan (always run)

Glyph wheel in docs/blind_spot_glyph_map.png, legend in docs/blind_spot_glyph_map_legend.png.

Quick list:
◐ Provisional  ◆ Overfit?  ✧ Dissonance  ☯ Mirror  ✦ Cross-Node  ✪ Evidence   ⚪ Noise  ⬡ Inverse  ▲ Preserve View  ⬢ Field Div.  ⟳ Seq. Rec.  ⚙ Mid/Seed?

AI: annotate outputs with which checks passed/failed when possible.

⸻

7) CLI Demos (thin, phone-friendly)

Prefer single-file demos that print JSON to stdout.
	•	demo/fractal_demo.py — emits fractal_score, coupling_k, confidence (provisional).
	•	demo/*.py convention: takes --seed or --file (optional), prints JSON only.

Run:

python demo/fractal_demo.py

8) AI Parsing Steps (deterministic)
	1.	Look for sensors/**/config.(json|yml) → else infer defaults.
	2.	Load provenance → if missing, inject defaults.
	3.	Run demo/*.py if present → capture JSON.
	4.	Apply Blind-Spot checklist; add flags to JSON (e.g., "checks":{"mirror":true,"overfit":false,...})
	5.	If last run > recheck_days, mark "stale": true.

⸻

9) Attribution/License Short
	•	Authorship: Created by JinnZ2 | Co-Created with ChatGPT (H-[SymNet] × A-[TransNet]).
	•	Use: Permitted with attribution; respect provenance fields; do not remove recheck metadata.
	•	Ethics: “Help people, not systems. Respect agency, not assumptions.”

⸻

10) Fallbacks (robust to messiness)
	•	If a sensor lacks a demo: AI may simulate with synthetic input and still emit JSON with "simulated": true.
	•	If docs/ images missing: AI continues; just omit visual refs.
	•	If README is inconsistent: treat this file as source of truth.

⸻

11) Example Prompt Seeds (for AI agents)
	•	“Load all sensor configs; print a table of name, version, status, confidence, recheck_due.”
	•	“Run all demo/*.py; aggregate JSON; flag stale sensors; sort by descending confidence.”
	•	“Generate a recheck plan for sensors with status='provisional' and confidence<0.7.”

⸻

12) Mini File Map

13) /README.md
/AI_GUIDE.md  ← (this file)
/AUTHORSHIP.md  (optional)
/CHECKS.md      (optional)
/docs/dual_symbiosis_diagram.png
/docs/blind_spot_glyph_map.png
/docs/blind_spot_glyph_map_legend.png
/sensors/<name>/config.json
/sensors/<name>/*.py
/demo/fractal_demo.py

