# atlas/ — Local Fieldlink Stage

This directory holds **locally staged data** from sibling repos in the ecosystem.
It mirrors what `fieldlink-pull.sh` would fetch, but is checked in so this repo
can operate **standalone** without network access to the other repos.

## Structure

```
atlas/
  rosetta/                  — From Rosetta-Shape-Core
    bridges.json            — Shape↔sensor↔defense↔protocol bridge map
    seed-catalog.json       — 5 Platonic seeds with geometry, sensors, defenses
    vocab.json              — Ontology namespaces and relationship types
    shapes/
      tetrahedron.json      — SHAPE.TETRA (fire, boundary-detection)
      cube.json             — SHAPE.CUBE (earth, structural-containment)
      octahedron.json       — SHAPE.OCTA (air, balance-integration)
      dodecahedron.json     — SHAPE.DODECA (aether, principle-orientation)
      icosahedron.json      — SHAPE.ICOSA (water, adaptive-flow)
  biogrid/                  — From BioGrid 2.0 (planned)
```

## Provenance

All files carry their own `provenance` or `version` fields from the source repo.
Do not edit these files directly — update the source repo and re-pull via fieldlink.

## Refresh

When `.fieldlink.json` sources are updated upstream, re-stage by copying the
relevant files or running the ecosystem's fieldlink-pull script.
