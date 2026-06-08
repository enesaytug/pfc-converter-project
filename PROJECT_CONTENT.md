# PFC Converter — Project Content (source of truth for the website)

This file contains all verified content extracted from the ELK453E term project
report. Use it as the text/data source when building the website. Do not invent
numbers — everything below is taken from the report.

---

## Project identity

- **Title:** 500 W, 400 V, 50 kHz Single-Phase Boost PFC Converter
- **Subtitle:** Design, Component Sizing, Control and Model-Based Verification (MIL / SIL / PIL)
- **Course:** ELK 453E — Industrial Applications of Power Electronics
- **Authors:** Enes Aytuğ Kır (040240785), Ufuk Barın (040240791)
- **Course Coordinator:** Prof. Dr. S. Barış Öztürk
- **Institution:** Istanbul Technical University (İTÜ)

## Design specifications (Table 1)

| Symbol | Description | Value |
|---|---|---|
| Vin | RMS line voltage | 240 Vrms |
| f_line | Line frequency | 50 Hz |
| Vo | Regulated DC output voltage | 400 V |
| Po | Rated output power | 500 W |
| fs | Switching frequency | 50 kHz |
| ΔVo/Vo | Max output voltage ripple | < 1 % |
| V̂p | PWM sawtooth carrier peak | 3 V |

---

## SECTION: What is PFC and why we use it

- A diode bridge with a bulk capacitor pulls current only near the voltage peaks, so the
  line current is spiky and non-sinusoidal.
- This lowers the power factor and injects significant current harmonics into the grid.
- A boost PFC stage forces the input current to be sinusoidal and in phase with the voltage,
  so the power factor approaches unity.
- Benefits: compliance with harmonic standards (e.g. IEC 61000-3-2), lower RMS current,
  better utilisation of the supply.
- Real-world uses: server / PC power supplies, LED drivers, EV chargers, appliance motor drives.

## SECTION: Converter topology and control structure

- AC mains → EMI filter → full-wave diode-bridge rectifier producing v_rect(t) = Vin,pk·|sin(ωt)|.
- Boost stage: inductor L, MOSFET S, ultrafast diode D, bulk output capacitor Co feeding load R = Vo²/Po.
- Dual-loop cascaded average current-mode control: fast inner current loop (Gci), slow outer voltage loop (Gcv).
- Multiplier/divider builds the current reference i_ref = (v_ea · v_rect)/Vrms².
- PWM modulator with 3 V sawtooth carrier. Scheme follows TI SPRA902A.
- FIGURE: (block diagram — from report Figure 1; not yet exported, see note at bottom)

## SECTION: Mathematical component sizing

- Operating point: Vin,pk = √2·240 = 339.41 V; Iin = 500/240 = 2.083 Arms; Iin,pk = 2.946 A;
  Io = 1.25 A; R = 320 Ω.
- Duty range: d = 1 − Vin,pk·|sin|/Vo → d_min = 0.1515 at the line peak; clamped to d ≤ 0.95 near zero-crossings.
- Boost inductor: CCM ripple rule with k = 0.4 gives L ≥ 0.872 mH. Chosen L = 12 mH for low
  ripple (ΔiL,pk ≈ 0.0857 A, ~2.9% of Iin,pk) and robust CCM.
- Output capacitor: 2nd-harmonic ripple equation, 1% limit needs Co ≥ 994.7 µF. Chosen Co = 1500 µF
  → ΔVo,pp = 2.65 V → 0.66% < 1%.
- Semiconductors: MOSFET 600 V / 10 A (IS,pk = 3.29 A); boost diode 600 V / 5 A; diode bridge 600 V / 6 A.
- Every value traces back to a closed-form equation in the report — not a trial number.

## SECTION: Average model of the converter

- Switched state equations written for MOSFET-on and MOSFET-off subintervals.
- Moving-average operator over one switching period removes the switching-frequency ripple.
- Result is a bilinear large-signal averaged state-space model (duty ratio multiplies the states).
- Quasi steady-state argument recovers the DC conversion ratio ⟨vo⟩ = ⟨v_rect⟩/(1−d) and a
  sinusoidal inductor-current envelope ⟨iL⟩ = Iin,pk·|sin(ωt)|.
- Open-loop simulation confirms the power stage sits in the right operating region (Vo ≈ 400 V).
- FIGURES: openloop-vout-il.png (DC-side Vout & IL), openloop-vin-iin.png (input side)

## SECTION: Small-signal plants and Bode analysis

- Linearised around the rated operating point.
- Current plant: Gid(s) = Vo(1+sRCo) / (s²LRCo + sL + R), duty → inductor current. LC resonance ≈ 37.5 Hz.
  At target current crossover 5 kHz: |Gid| = 0.515 dB, phase ≈ −90°.
- Voltage plant: Gvi(s) = R/(1+sRCo), inductor current → output voltage. Output pole ≈ 0.332 Hz.
  At target voltage crossover 2.5 Hz: |Gvi| = 32.48 dB, phase ≈ −82.45°.
- FIGURE: plant-bode.png

## SECTION: PI controller design and re-tuning (the key story)

- Started from textbook PI gains aimed exactly at the 5 kHz / 2.5 Hz crossover targets.
- Those gains kept input-current THD stuck above the 5% limit no matter how they were adjusted.
- Spent hours iterating PI gains AND passive values together.
- Passive redesign: L changed from 1 mH → 12 mH; Co changed from 4500 µF → 1500 µF. This cut the
  ripple far more effectively than forcing the PI to hit crossover targets.
- Final continuous gains:
  - Current PI: Kp = 2.8, Ki = 17600
  - Voltage PI: Kp = 0.055, Ki = 0.2
- Discrete form: Ts = 20 µs → Ki,i,d = 0.352, Ki,v,d = 4.0e−6 (Kp unchanged).
- Selection rule became "best measured THD and PF", not exact crossover matching.
- FIGURES: closedloop-vout.png (Vout settles ~400 V), closedloop-vin-iin.png, inductor-current.png

## SECTION: Loop-gain stability margins

- Current loop actual crossover: 14.89 kHz (≈ 3× the 5 kHz target). PM ≈ 86.2°.
- Voltage loop actual crossover: 5.85 Hz (≈ 2.3× the 2.5 Hz target). PM ≈ 87.6°.
- Gain margin: infinite (no finite phase crossing) for both loops → stable.
- Higher-than-target bandwidth accepted as a deliberate practical compromise for better harmonics.
- FIGURES: openloop-margins.png, closedloop-bode.png

## SECTION: THD and power factor — what the system does WELL

- Output voltage regulated, settles near 400 V after the startup transient.
- Input current shaped to follow the line-voltage envelope.
- Power factor ≈ 0.99 (nearly in phase with the voltage).
- Representative input-current THD ≈ 4.48% — below the 5% target.
- Dual-loop control stable with very large phase margins (> 86°).
- FIGURE: thd-pf-model.png (Simulink view: PF 0.9999, THD 0.0448)

## SECTION: Limitations — what the system does NOT do well (be honest)

- The good THD holds in the chosen steady-state window but can spike up to ~12% in other windows.
- High current-loop bandwidth (14.89 kHz) is the likely cause of this window sensitivity.
- The voltage loop is faster than its target too, though still slow enough not to distort the reference.
- PIL hardware verification link was never closed (no physical C2000 board) → on-target numerics
  and timing remain unverified.
- Summary: regulation and PF are solid; harmonic robustness is the weak point.

## SECTION: MIL / SIL / PIL verification chain

- MIL (Model-in-the-Loop): controller runs as a model inside the closed-loop reference simulation. (Part f/g)
- SIL (Software-in-the-Loop): controller compiled to C code and run on the host computer. (Part h)
  Built on macOS with Xcode Clang (macOS x64); moving to Windows can raise compiler/path/toolchain errors.
- PIL (Processor-in-the-Loop): same code cross-compiled and run on the real target MCU
  (TI C2000, LAUNCHXL-F28379D Delfino). Adds target numerics, bit-accurate behavior, and
  execution-timing checks (must fit within the 20 µs sample period).
- MIL and SIL were completed; PIL documented conceptually (hardware not available).
- Comparison: Part f THD ≈ 4.48% / PF ≈ 0.99 (cleanest reference); Part g (MIL) THD ≈ 4.92%;
  Part h (SIL) software-level execution verified with stronger startup transient.
- FIGURES: mil-waveform.png, mil-thd-view.png, sil-waveform.png

## SECTION: Conclusion

- Carried the design from spec-based component sizing all the way to model-based verification.
- The passive redesign was the key move that brought THD under 5% while keeping PF near 0.99.
- Dual-loop average current-mode control gave stable, well-damped regulation.
- MIL and SIL confirmed the controller survives the move into generated code.
- Future work: close the PIL loop on real hardware; reduce the THD window sensitivity.

## References

1. R. W. Erickson and D. Maksimović, *Fundamentals of Power Electronics*, 3rd ed., Springer, 2020.
2. D. W. Hart, *Power Electronics*, McGraw-Hill, 2011.
3. N. Mohan, T. M. Undeland, W. P. Robbins, *Power Electronics: Converters, Applications, and Design*, 3rd ed., Wiley, 2003.
4. S. Choudhury, "Average Current Mode Controlled PFC Converter using TMS320LF2407A," TI Application Report SPRA902A, Jul. 2005.

---

## Figure inventory (in ./figures/)

| File | Use on site |
|---|---|
| openloop-vout-il.png | Average model — open-loop DC-side Vout & IL |
| openloop-vin-iin.png | Average model — open-loop input side |
| plant-bode.png | Small-signal — plant Bode (Gid, Gvi) |
| openloop-margins.png | Stability — open-loop margins |
| closedloop-bode.png | Stability — closed-loop Bode |
| closedloop-vout.png | PI design — closed-loop Vout response |
| closedloop-vin-iin.png | PI design — closed-loop input current/voltage |
| inductor-current.png | PI design — zoomed inductor current |
| thd-pf-model.png | Performance — Simulink THD 0.0448 / PF 0.9999 |
| mil-waveform.png | MIL — waveform set |
| mil-thd-view.png | MIL — THD measurement view |
| sil-waveform.png | SIL — waveform result |

NOTE: The clean converter block diagram (report Figure 1) is NOT in this folder yet.
If you want it on the Topology section, export page 6 of the report PDF or recreate it as SVG.
