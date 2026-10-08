# Engineering Notes

Short notes for decisions, mistakes, and fixes that were actually important.

## Entry 1 - 2026-10-07 - V1 - DECISION - SOLVED

**Decision:** Use a 2200 uF / 25 V filter capacitor.

**Why:** I want the 7805 input to stay above about 7 V. If the 9 VAC source is 10% low, it becomes 8.1 VAC.

```text
8.1 * sqrt(2) = 11.46 V peak
11.46 - 1.6 V diode drops = 9.86 V
9.86 - 7.0 = 2.86 V allowable ripple

C >= 0.5 / (2 * 60 * 2.86)
C >= 1459 uF
```

2200 uF is the next value I am using. Even at -20% it would be about 1760 uF, which is still above the calculated minimum.

The 25 V capacitor rating is comfortably above the nominal rectified peak. I am going to measure the real adapter's no-load AC voltage before I treat the hardware voltage margin as verified.

**Result:** Final 1N4007 LTspice run had a rail valley about 9.52 V, which leaves about 2.52 V above the 7 V target (script-extracted, Oct 8).
**What I learned:** Pick the part from the requirement first, then check tolerance and rating instead of just picking a random bigger value.

---

## Entry 2 - 2026-10-07 - V1 - FAILURE - SOLVED

**What happened:** I searched `7805` in LTspice and picked `LTC7805` thinking it was the regulator I needed.

**Cause:** Same numbers, completely different part. I did not check the datasheet first.

**Fix:** I stopped using it and made a temporary 2N3055 emitter-follower stand-in so I could keep working on the front end.

I originally assumed:

```text
VBE ~= 0.8 V
Vout ~= 5.8 - 0.8 = 5.0 V
```

The model gave a smaller VBE at this operating point, so the output was too high. I adjusted the reference to about 5.47 V and got about 5.015 V out.

**What I learned:** Check the exact part number and datasheet before I use something just because the name looks right.

---

## Entry 3 - 2026-10-07 - V1 - FAILURE - SOLVED

**What happened:** LTspice gave me `This model has multiple definitions` after I pasted my own 1N4007 model line.

**Cause:** LTspice already had a built-in 1N4007 model.

**Fix:** Deleted my extra `.model` line and used the built-in `1N4007` part value instead.

**What I learned:** Read the error first. Do not add a model before checking if LTspice already has it.

---

## Entry 4 - 2026-10-07 - V1 - LIMITATION - OPEN

The 2N3055 stand-in is only there so I can keep learning and simulating the front end. It is not a real 7805 model.

It does not have the 7805's real control circuit, dropout behavior, ripple rejection, current limiting, or thermal behavior.

**Plan:** Use the actual L7805CV datasheet for the real design predictions, then prove the important stuff on the physical circuit with the scope and meter.

Things I still want to compare later:

- real 7805 ripple/output behavior
- actual dropout margin
- actual 1N4007 forward drop vs the roughly 0.88 V implied by the final simulation
- regulator temperature under load

---

## Entry 5 - 2026-10-07 - V1 - FAILURE / MODEL CHECK - SOLVED

**What happened:** My earlier LTspice screenshots were from the default/generic diode setup even though I intended to be using 1N4007s.

**What I changed:** Set the Value field of D1-D4 explicitly to `1N4007`, reran the simulation, and saved new cursor screenshots.

**Earlier default-diode run:**

```text
Rail peak   11.068 V
Rail valley  9.626 V
Ripple       1.443 Vpp
Vout         5.015 V
Heat         2.67 W
```

**Final explicit 1N4007 run:**

```text
Rail peak   10.978 V
Rail valley  9.522 V
Ripple       1.456 Vpp
Vout         5.0153 V
Heat         2.66 W
```

These were extracted by script on 2026-10-08. My Oct 7 cursor readings were 10.967 V peak, 9.540 V valley, 1.427 Vpp ripple, and 2.63 W heat.

The final diode drop works out to roughly 0.88 V per conducting diode from the peak result, instead of the roughly 0.83 V I was seeing before.

**What I learned:** A schematic can look basically identical while a different device model changes the numbers. I need to check the actual Value/model field, not just the diode symbol.
