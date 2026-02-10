# Project Memory: 2020 Chevrolet Corvette C8 Stingray (Z51)

This directory contains the specific assets and physics data for the **2020 Chevrolet Corvette C8 Stingray** equipped with the **Z51 Performance Package**.

---

## Vehicle Specifications
* **Chassis:** C8
* **Engine:** LT2 6.2L Naturally Aspirated V8
* **Transmission:** 8-Speed Dual-Clutch (Tremec TR-9080)
* **Drivetrain:** Rear-Wheel Drive (RWD)
* **Layout:** Mid-engine, rear-wheel drive

---

## Z51 Package Specifics
* **Aero:** Front splitter, flat underbody, rear diffuser (~67 kg total downforce at 200 km/h)
* **Suspension:** MagneRide 4.0 adaptive dampers with stiffer springs (226 lb/in front, 263 lb/in rear)
* **Brakes:** Larger rotors (321mm front, 328mm rear)
* **Cooling:** Enhanced cooling for track use
* **Axle Ratio:** 5.17:1 electronic limited-slip differential (eLSD)
* **Tires (OEM):** Michelin Pilot Sport 4S ZP (245/35R19 front, 305/30R20 rear)

---

## Research & Data Integrity
* **Real-World Data Priority:** Always prioritize real-world technical specifications, chassis dyno data, and suspension geometry when making changes to physics files.
* **Web Research Required:** When specific C8 data is unavailable in local documentation, perform web searches for real-world specifications, tire data, and aerodynamic testing before making parameter changes.
* **No Generalizations:** Do not apply generic "Corvette" or "American sports car" assumptions. Every parameter change must be rooted in data specific to the C8 generation with Z51 package.
* **Assumption Protocol:** If specific data is unavailable after research, **do not guess.** Stop and ask for permission before using placeholder values or making engineering assumptions.

---

## Current Physics Status

### Engine (`engine.ini`)
* LT2 6.2L pushrod V8: ~495 hp @ 6,450 rpm, ~637 Nm (470 lb-ft) @ 5,150 rpm
* Natural aspiration with no turbo lag

### Suspension (`suspensions.ini`)
* **Last Updated:** 2026-02-09
* MagneRide 4.0 adaptive dampers with high digressivity (~45-50% fast/slow ratio)
* Progressive bump stops: Front engages at +0.73G, rear at +0.71G
* Spring rates: 39,600 N/m front, 46,000 N/m rear (Z51 spec)
* Ride height: ~105mm front, ~110mm rear
* Camber: -0.5° front/rear (Z51 factory alignment)

### Aerodynamics (`aero.ini`)
* **Last Updated:** 2026-02-09
* Front splitter: ~280 N downforce at 200 km/h
* Rear diffuser: ~420 N downforce at 200 km/h
* Total: ~700 N (~67 kg) at 200 km/h
* Body lift enabled (Cd ≈ 0.362)
* Front/rear aero balance: ~40/60

### Tires (`tyres.ini`)
* **Last Updated:** 2026-02-09
* Ported from BMW M2 G87 tire model
* **Compound 0:** Michelin Pilot Sport 4S (300TW) - street performance
* **Compound 1 (default):** Bridgestone Potenza RE-71RS (200TW) - track-focused
* Staggered setup: 245/35R19 front, 305/30R20 rear
* Optimized for 40/60 weight distribution (3,250 N front, 4,868 N rear corner weights)

---

## Development Guidelines
* **Physics Accuracy:** Ensure power curve reflects the LT2's specific naturally aspirated delivery (~495 hp / 470 lb-ft).
* **Transmission Logic:** Verify that `drivetrain.ini` accounts for dual-clutch shift speed and behavior.
* **MagneRide:** Suspension damping should reflect adaptive damper digressivity and quick response.
* **Weight Distribution:** The C8 is a 40/60 front/rear mid-engine car — physics must reflect this bias.
* **Aerodynamics:** Z51 package provides moderate downforce with diffuser-dominant balance.

---

## Known Real-World Performance Benchmarks
* 0-60 mph: ~2.9 seconds
* Skidpad: ~1.03-1.04g (Z51 on PS4S tires)
* Top speed: ~194 mph (312 km/h)
* Curb weight: ~1,654 kg (3,647 lb) with Z51

---

## Documentation Reference
For technical clarification on parameter syntax or physics engine limitations:

> [!IMPORTANT]
> Consult the **ASSETTO CORSA MODDING MANUAL** located in the repository root for standardized modding protocols and configuration definitions.
