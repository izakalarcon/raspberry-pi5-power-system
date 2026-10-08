# Session Log

**Date:** 2026-10-07  
**Revision:** V1 - 7805 linear supply  
**Phase:** Simulation

## Goal

Simulate the V1 front end in LTspice and compare it to my hand calculations before I build it.

## What I expected

**CALCULATED:**

- rectified peak: 11.13 V
- ripple: 1.89 Vpp at 500 mA
- rail valley: 9.23 V
- regulator heat: 2.59 W

I did not really have my own expectation before the very first run because I was still learning what peak, RMS, ripple, and dropout meant. For the transistor stand-in, I expected `Vout = Vref - VBE = 5.8 - 0.8 = about 5.0 V`.

## What I did

- Worked through `DeltaV = I / (2fC)` and got a minimum capacitor around 1459 uF, so I chose 2200 uF / 25 V.
- Built the bridge rectifier, capacitor, and load in LTspice.
- Used a 12.73 V peak, 60 Hz sine to represent 9 VAC RMS.
- Found out that `LTC7805` is not the 7805 linear regulator I need.
- Used a 2N3055 emitter follower as a temporary stand-in.
- Adjusted the reference to 5.47 V so the output was close to 5 V.
- Used LTspice cursors to read the rail and output.
- Caught that my first 20 ohm load was on the wrong node and moved the load to the 5 V output, where 10 ohm gives about 500 mA.
- Reran the final schematic with D1-D4 explicitly set to `1N4007`.

## Test conditions - SIMULATED

- Load: 10 ohm, about 500 mA
- Input: 12.73 V peak sine, 60 Hz
- Bridge: D1-D4 Value = `1N4007`
- Filter cap: 2200 uF
- Regulator stand-in: 2N3055
- IN node: rectifier/filter output
- OUT node: stand-in regulator output
- Simulation: `.tran 0.3`

## Final results - 1N4007 run

| Item | Calculated | LTspice | Measured | Difference vs calculated |
|---|---:|---:|---:|---:|
| Rail peak | 11.13 V | 10.978 V | not yet | -1.4% |
| Rail valley | 9.23 V | 9.522 V | not yet | +3.2% |
| Ripple | 1.89 Vpp | 1.456 Vpp | not yet | -23.0% |
| Vout | 5.00 V | 5.0153 V | not yet | +0.3% |
| Regulator heat | 2.59 W | 2.66 W | not yet | +2.6% |

2026-10-08: Re-extracted the numbers with a script from the LTspice export. The Oct 7 values were read by hand with cursors.


## Earlier default-diode run

Before explicitly setting D1-D4 to `1N4007`, the earlier run gave roughly:

- rail peak: 11.068 V
- rail valley: 9.626 V
- ripple: 1.443 Vpp
- Vout: 5.015 V
- regulator heat: 2.67 W

I kept those screenshots but labeled them `DEFAULT_DIODE` so I do not mix them up with the final run.

## Problem / lesson

The hardest part today was honestly the vocabulary and getting LTspice set up correctly. I have not learned most of this in class yet.

Ripple makes a lot more sense now. The capacitor charges near the peaks, then feeds the load until the rectified voltage rises high enough to charge it again.

The simple ripple equation is a first-order estimate. In this simulation it came out higher than LTspice because the capacitor started recharging before a full half-cycle had passed.

I also learned that model choice matters. The default diode setup and explicit `1N4007` run were close, but not identical.

## Next action

When the adapter arrives, measure its no-load AC voltage with the multimeter before connecting it to the circuit.

## Saved

- [x] verified LTspice source (`V1_front_end.asc`)
- [x] final 1N4007 screenshots
- [x] earlier/default-diode screenshots labeled clearly
- [x] handwritten notes PDF
- [x] typed notebook transcription
- [ ] physical photos
- [ ] git commit

