# Next Session

## Main goal

Measure the real 9 VAC adapter before I connect it to anything else.

## Do this first

- [ ] Make sure the meter leads are in the correct jacks.
- [ ] Set the multimeter to AC volts.
- [ ] Plug in the adapter by itself.
- [ ] Measure the no-load output.
- [ ] Record the value as **MEASURED**.

```text
Nameplate: 9 VAC
Measured no-load: ______ VAC
```

## After that

Use the real measured AC voltage to update the expected peak voltage before testing the bridge rectifier.

Then build/test one stage at a time:

```text
adapter
-> bridge
-> bridge + capacitor
-> 7805
-> load
```

## GitHub

Today's LTspice file has been rerun with D1-D4 explicitly set to `1N4007`, and the final cursor screenshots are saved.

- [x] verify `V1_front_end.asc` runs
- [x] save final Vout screenshot
- [x] save final rail peak screenshot
- [x] save final rail valley screenshot
- [x] label earlier screenshots as default-diode/early-run where needed
- [ ] commit to GitHub
