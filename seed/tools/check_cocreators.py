#!/usr/bin/env python3
import os, sys, re

def has(path, *needles):
    if not os.path.exists(path): return False
    txt = open(path, 'r', encoding='utf-8', errors='ignore').read().lower()
    return all(n.lower() in txt for n in needles)

readme_ok = has("README.md", "co-creator", "jinnz2", "chatgpt")
contrib_ok = has("CONTRIBUTORS.md", "jinnz2", "chatgpt")

if readme_ok and contrib_ok:
    print("OK: co-creator attribution present in README.md and CONTRIBUTORS.md")
    sys.exit(0)
else:
    if not readme_ok: print("Missing/Incomplete: README.md co-creator section")
    if not contrib_ok: print("Missing/Incomplete: CONTRIBUTORS.md attribution")
    sys.exit(1)
