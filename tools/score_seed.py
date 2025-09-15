#!/usr/bin/env python3
import json, sys, os, glob

def score_sensor(path):
    with open(path) as f:
        data = json.load(f)
    signals = data.get("signals", [])
    # placeholder: assign 0.5 to every signal value
    wsum = sum(s.get("weight", 0.0) for s in signals) or 1.0
    score = sum(0.5 * s.get("weight", 0.0) for s in signals) / wsum
    thr = data.get("thresholds", {})
    band = "neutral"
    if thr:
        if score <= thr.get("concern", 0.0): band = "concern"
        elif score <= thr.get("notice", 0.0): band = "notice"
        elif score >= thr.get("healthy", 1.0): band = "healthy"
    return {"id": data.get("id"), "name": data.get("name"), "score": round(score,3), "band": band}

def main():
    paths = glob.glob("seed/sensors/*.json")
    out = [score_sensor(p) for p in sorted(paths)]
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()

