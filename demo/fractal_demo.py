import json, math, time
import numpy as np

def coupling_k(a, d):  # proxy for mutual inductive coupling
    return (a*a)/((a*a + d*d)**1.5)

def phi_stack_k(rings=7, a0=0.35, d0=0.40, phi=1.6180339887):
    ksum, a, d = 0.0, a0, d0
    for _ in range(rings):
        ksum += coupling_k(a, d); a*=phi; d*=phi
    return min(1.0, 0.9*ksum)

def fractal_score(x, scales=(1,2,4,8)):
    scores=[]
    for s in scales:
        block = x.reshape(-1, s).mean(axis=1)
        c = np.corrcoef(block[:-1], block[1:])[0,1]
        scores.append(c)
    return float(np.nanmean(scores))

if __name__ == "__main__":
    t = np.linspace(0, 100, 4096)
    sig = np.sin(2*math.pi*0.07*t) + 0.5*np.sin(2*math.pi*0.14*t) + 0.2*np.random.randn(t.size)
    fs = fractal_score(sig)
    k  = phi_stack_k()
    confidence = min(0.95, 0.5 + 0.4*fs + 0.2*k)
    out = {
        "fractal_score": round(fs,3),
        "coupling_k": round(k,3),
        "confidence": round(confidence,3),
        "provisional": True,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    print(json.dumps(out, indent=2))
