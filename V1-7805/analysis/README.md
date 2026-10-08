# Analysis

Script that extracts true peak, valley and ripple from an LTspice export and
compares them with my hand calculations.

- `analyze_simple.py`: the script
- `ltspice_export.txt`: data exported from LTspice (File > Export data as text)
- `ripple_plot_simple.png`: the plot it produces

Run: `python3 analyze_simple.py` (needs numpy and matplotlib).

Note: the output was extracted on 2026-10-08. My 2026-10-07 numbers were read
by hand with cursors, which slightly missed the true peak and valley.
The simulation uses a 2N3055 stand-in for the 7805, so it does not prove
the real regulator's output ripple.
