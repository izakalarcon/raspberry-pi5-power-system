# Raspberry Pi 5 Power System

I am building a custom power system for a Raspberry Pi 5 and using it as a way to learn power electronics hands-on.

I could just buy a 5 V module and be done, but that would miss the whole point of the project. I want to be able to predict what should happen, simulate it, build it, measure it, and explain why the real result is different.

The project starts with a basic 7805 linear supply so I can learn the fundamentals, then moves into testing and characterization, a custom buck converter PCB, and eventually the full Raspberry Pi power system.

I am an electrical engineering student interested in power electronics and power systems. My goal with this project is to get experience outside of class with circuit analysis, simulation, hardware, measurements, troubleshooting, and PCB design.

## How I work

For every major revision I follow the same general process:

1. Define what the circuit needs to do.
2. Do the hand calculations.
3. Simulate it in LTspice.
4. Build it.
5. Measure it on the bench.
6. Compare the calculated, simulated, and measured results.
7. Figure out why they are different and document what I changed.

I label results as **CALCULATED**, **SIMULATED**, or **MEASURED** so it is clear where every number came from.

I also keep mistakes and failed attempts in the project instead of hiding them. Most of the useful stuff I learn comes from figuring out why something did not work the way I expected.

## Roadmap

| Version | What I am doing | Status |
|---|---|---|
| **V1** | 9 VAC adapter → bridge rectifier → 2200 uF filter → 7805 regulator → 5 V output | Calculations and LTspice simulation done. Hardware build and measurements next. |
| **V2** | Characterize V1: ripple, load regulation, efficiency, heat, and real-vs-simulated behavior | Planned |
| **V3** | Design, simulate, lay out, and test a higher-current buck converter PCB | Planned |
| **V4** | Integrate the power system with the Raspberry Pi 5 and add power monitoring/data logging | Planned |

The later versions are still planned, not finished designs. I will update them as the project develops.

## V1 requirements

| Parameter | Target |
|---|---|
| Output voltage | 5.0 V +/- 2% (4.90 to 5.10 V) |
| Load range | 0 to 500 mA |
| Output ripple | < 50 mV peak-to-peak at 500 mA |
| Regulator input | Stay above about 7 V |
| Regulator temperature | Stay below thermal shutdown |

## V1 status

**As of 2026-10-07**

| Item | CALCULATED | SIMULATED | MEASURED |
|---|---:|---:|---:|
| Rail peak | 11.13 V | 10.978 V | not yet |
| Rail valley | 9.23 V | 9.522 V | not yet |
| Rail ripple | 1.89 Vpp | 1.456 Vpp | not yet |
| Vout | 5.00 V | 5.0153 V | not yet |
| Regulator heat | 2.59 W | 2.66 W | not yet |

For the current LTspice work I used a 2N3055 emitter-follower as a temporary stand-in for the 7805. My LTspice setup did not have the 7805 model I was looking for, and searching `7805` brought up the LTC7805, which is a completely different switching controller.

Because of that, I am not treating the simulated 5 V output as proof that the real 7805 will meet the final ripple or regulation requirements. That has to be proven with the actual circuit and bench measurements.

## Repository

Detailed work for each revision is kept in its own folder.

```text
V1-7805/
├── README.md
├── V1_front_end.asc
├── session-log.md
├── engineering-notes.md
├── handwritten-notes-transcription.md
├── images/
└── source/
```

Start here:

[`V1-7805/README.md`](V1-7805/README.md)

That folder has the calculations, LTspice results, screenshots, mistakes I caught, engineering notes, and the next steps for the physical build.

## Tools

Tools I am using across the project include:

- LTspice
- Rigol DS1054Z oscilloscope
- Digital multimeter
- Soldering equipment
- Power resistors / dummy loads
- KiCad
- Python
- Raspberry Pi 5

## Where this is going

The 7805 supply is not meant to be the final Raspberry Pi power supply. It is the starting point.

The main goal is to work my way from a simple linear regulator circuit into a higher-current switching supply that I designed, simulated, laid out, built, tested, and eventually use to power the Raspberry Pi 5.

By the end I want the project to show the entire process, not just a finished board:

**requirements → calculations → simulation → hardware → measurements → troubleshooting → redesign → PCB → Raspberry Pi integration**

## Author

**Izak Alarcon**

Electrical engineering student interested in power electronics and power systems.

Currently seeking electrical engineering internship opportunities.
