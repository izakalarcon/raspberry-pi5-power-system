"""
analyze_simple.py - V1 supply: get true peak/valley/ripple from an LTspice export.

Why: reading peak and valley with cursors by hand can miss the real extremes.
Exporting the data as text lets the computer check every sample.
"""
import numpy as np
import matplotlib.pyplot as plt

# ---- settings (change these) ----
FILE = "ltspice_export.txt"   # File > Export data as text in LTspice
WINDOW = 0.1                  # seconds at the end to analyze (ignores start-up)
R_LOAD = 10                   # ohms

# ---- 1. read the file: columns are time, V(in), V(out) ----
data = np.loadtxt(FILE, skiprows=1)      # skip the header row
t, v_in, v_out = data[:, 0], data[:, 1], data[:, 2]

# ---- 2. keep only the last WINDOW seconds, after the circuit settles ----
keep = t >= t[-1] - WINDOW
t, v_in, v_out = t[keep], v_in[keep], v_out[keep]

# ---- 3. measurements ----
peak = v_in.max()                        # highest point of the rail
valley = v_in.min()                      # lowest point of the rail
ripple = peak - valley                   # peak-to-peak ripple
vout = v_out.mean()                      # average output voltage
i_load = vout / R_LOAD                   # Ohm's law
heat = (v_in.mean() - vout) * i_load     # P = (Vin - Vout) * I

# ---- 4. compare with hand calculations: error % = (sim - calc) / calc * 100 ----
calc = {"peak": 11.13, "valley": 9.23, "ripple": 1.89, "vout": 5.00, "heat": 2.59}
sim = {"peak": peak, "valley": valley, "ripple": ripple, "vout": vout, "heat": heat}
for name in calc:
    err = (sim[name] - calc[name]) / calc[name] * 100
    print(f"{name:7s} calc {calc[name]:6.2f}   sim {sim[name]:7.4f}   error {err:+.1f}%")

# ---- 5. plot ----
plt.plot(t * 1000, v_in, label="V(in) rail")
plt.plot(t * 1000, v_out, label="V(out)")
plt.axhline(7, linestyle="--", color="gray", label="7 V minimum")
plt.xlabel("time (ms)"); plt.ylabel("voltage (V)"); plt.legend(); plt.grid(alpha=0.3)
plt.savefig("ripple_plot_simple.png", dpi=150)