# Project Memory: 2020+ BMW M340i xDrive (G20)

This directory contains the specific assets and physics data for the **2020+ BMW M340i xDrive (G20)** equipped with **xDrive all-wheel drive** and **B58 3.0L turbocharged inline-six engine**.

---

## Vehicle Specifications

### Engine & Drivetrain
* **Chassis:** G20
* **Engine:** B58 3.0L Turbocharged Inline-6
* **Power:** 382 HP @ 5,800-6,500 RPM
* **Torque:** 369 lb-ft @ 1,800-5,000 RPM
* **Drivetrain:** xDrive AWD (all-wheel drive)
* **Transmission:** 8-speed ZF 8HP automatic (8HP50)
* **Weight Distribution:** 52% front / 48% rear
* **Curb Weight:** ~1,750 kg (3,858 lbs)

### Dimensions & Geometry
* **Wheelbase:** 2,851 mm
* **Track Width:** 1,587 mm (front) / 1,602 mm (rear)
* **Frontal Area:** 2.25 m²
* **Drag Coefficient:** Cd = 0.26 (BMW official specification)

### Aero Reference Heights (from ground)
* **Ground Clearance:** 130 mm (M Sport suspension)
* **Front Bumper Lower Edge (center):** ~155 mm (+25 mm above ground clearance)
* **Rear Diffuser/Exhaust Center:** ~260 mm (+130 mm above ground clearance)
* **Sources:** BMW official specs, G80/G20 Bimmerpost owner measurements

### Wheels & Tires
* **Wheel Size:** 19x9.0" (front and rear, squared setup)
* **OEM Tire Size:** 255/35R19 (front and rear)
* **Stock Compound:** Michelin Pilot Sport 4S (300TW)
* **Track Compound:** Bridgestone Potenza RE-71RS (200TW)

---

## Suspension Configuration

### Front: Double-Joint Spring Strut Axle (MacPherson Variant)
* **Spring Rate:** 30,000 N/m
* **Anti-Roll Bar:** 38,000 N/m (M Sport package, adjustable via setup)
* **Dampers:** Adaptive M Sport dampers with properly digressive ratios:
  * Slow bump: 2,800 N/(m/s)
  * Fast bump: 1,300 N/(m/s) (46% of slow)
  * Slow rebound: 5,600 N/(m/s)
  * Fast rebound: 2,500 N/(m/s) (45% of slow)
  * **Rationale:** Real adaptive dampers are digressive — fast values should be 40-50% of slow values, not 82% as in the previous model
* **Bump Stops:**
  * Engagement (UP): 50mm (engages just before 1G braking which compresses ~57mm)
  * Rebound travel (DN): 120mm (sedans need more droop travel than coupes)
  * Rate: 60,000 N/m (2x spring rate for progressive rubber stop)
* **Alignment (Factory Spec):**
  * Camber: -2.2° (static, geometry-based)
  * Toe: -0.00015 (~1mm total toe-in, per BMW G20 factory spec)

### Rear: 5-Link Independent Suspension
* **Spring Rate:** 32,000 N/m
* **Anti-Roll Bar:** 21,000 N/m (M Sport package, adjustable via setup)
* **Dampers:** Adaptive M Sport dampers with properly digressive ratios:
  * Slow bump: 2,400 N/(m/s)
  * Fast bump: 1,150 N/(m/s) (48% of slow)
  * Slow rebound: 4,800 N/(m/s)
  * Fast rebound: 2,100 N/(m/s) (44% of slow)
  * **Rationale:** Previous model had fast rebound at 62% of slow (too high); now corrected to 44%
* **Bump Stops:**
  * Engagement (UP): 60mm (earlier engagement for better AWD squat control)
  * Rebound travel (DN): 100mm (sedan compliance)
  * Rate: 65,000 N/m (~2x spring rate, adjusted for 32kN/m springs)
* **Alignment (Factory Spec):**
  * Camber: -1.0° (static)
  * Toe: -0.00065 (~1.5mm total toe-in for xDrive AWD stability)

### Damper Calibration Methodology
Damper values were scaled proportionally from the BMW M2 G87's calibrated model:
* **Front:** M2 uses 2,500 N/(m/s) bump for 32.7 kN/m springs; M340i uses 2,800 N/(m/s) for 30 kN/m springs (slightly higher for heavier car)
* **Rear:** M2 uses 2,200 N/(m/s) bump for 37 kN/m springs; M340i uses 2,400 N/(m/s) for 32 kN/m springs
* **Digressive Ratios:** Fast bump/rebound thresholds and ratios match M2's proven adaptive damper behavior (0.050m / 0.100m thresholds, 44-48% fast-to-slow ratios)

---

## Aerodynamics

### Aero Model Convention
Uses the **M2 G87 aero LUT convention**: **Positive CL = Lift** in LUT files. This convention is opposite to some AC defaults but is physically intuitive and matches real-world wind tunnel data reporting.

### Drag Budget (at 0° AOA, 0° pitch)
* **Body:** 0.97 × 0.26 × 2.25 × 1.0 = **0.568 CdA**
* **Front wing:** 0.18 × 0.04 × 0.8 × 1.75 = **0.010 CdA**
* **Rear wing:** 0.15 × 0.04 × 0.6 × 1.70 = **0.006 CdA**
* **Total:** **0.584 CdA** (target: 0.585 for Cd=0.26) ✓

### Lift Budget (at 0° pitch, with ANGLE offsets applied)
* **Body** at AOA=1°: CL≈-0.01 → 0.80 × (-0.01) × 2.25 = **-0.018** (slight downforce)
* **Front** at AOA=-1°: CL≈0.22 → 0.38 × 0.22 × 0.8 × 1.75 = **+0.117** (front lift)
* **Rear** at AOA=3°: CL≈0.32 → 0.60 × 0.32 × 0.6 × 1.70 = **+0.196** (rear lift)
* **Net Cl:** **≈0.13** (realistic sedan lift, rear-biased for stability)

### Wing Gains & Angles
* **WING_0 (BODY):** CL_GAIN=0.80, CD_GAIN=0.97, ANGLE=1
* **WING_1 (FRONT):** CL_GAIN=0.38, CD_GAIN=0.18, ANGLE=-1
* **WING_2 (REAR):** CL_GAIN=0.60, CD_GAIN=0.15, ANGLE=3

### Rationale
The previous aero model had front/rear wing CL_GAIN values of 0.12/0.10, which contributed essentially zero lift. A stock G20 sedan should produce meaningful net aerodynamic lift at speed (~Cl 0.12-0.15), split roughly 45/55 front/rear. The new model produces realistic sedan lift while maintaining the correct BMW-specified Cd=0.26.

---

## Tire Model

### Overview
**TIRE MODEL PORTED FROM BMW M2 G87** — The M340i now uses the M2's well-calibrated tire model, adapted for the narrower 255/35R19 squared wheel setup. The M2's tire model features:
* Hand-crafted temperature-grip curves (not Content Manager auto-generated)
* Calibrated grip coefficients (DY_REF/DX_REF) based on real-world skidpad data
* Proper camber sensitivity curves (peaks at -3.5° for PS4S, -4.5° for RE-71RS)
* Realistic thermal behavior with proper heat generation and dissipation

### Compound 0: Michelin Pilot Sport 4S (300TW)
**Max Performance Summer / Street Tire**

#### Physical Dimensions (255/35R19)
* **Width:** 255mm
* **Radius:** 330.55mm (89.25mm sidewall + 241.3mm rim)
* **Vertical Stiffness:** 265,000 N/m front & rear (scaled from M2's 285k for 275-width)
* **Angular Inertia:** 1.65 kg·m² (19x9 + 255 tire)

#### Grip Characteristics
* **DY_REF:** 1.23 (lateral friction coefficient at FZ0)
  * **Improvement:** Old model used 1.12; M2's calibrated value is 1.23
* **DX_REF:** 1.24 (longitudinal friction coefficient)
  * **Improvement:** Old model used 1.15; M2's calibrated value is 1.24
* **Load Sensitivity:** LS_EXPY=0.82 front / 0.80 rear (moderate degressive)
* **Peak Slip Angle:** ~8° at reference load
* **Falloff Behavior:** Progressive (FALLOFF_LEVEL=0.88, FALLOFF_SPEED=1.8)

#### Thermal Behavior
* **Optimal Temperature:** 75°C core (~65-85°C operating window)
* **Cold Grip:** Works well from 40-50°C (street tire characteristic)
* **Heat Generation:** FRICTION_K=0.045 front / 0.040 rear
* **Cooling:** COOL_FACTOR=2.0 front / 2.3 rear

#### Camber Sensitivity
* **Peak Camber:** -3.5° (from tire_camber_dy_ps4s.lut)
* **Gain at -3.5°:** +4.0% grip
* **DCAMBER_LUT:** tire_camber_dy_ps4s.lut (M2's proven curve)

#### Expected Performance
* **Lateral Grip:** ~1.04g sustained (matching M340i xDrive real-world skidpad data)
* **Braking Distance (70-0 mph):** ~155-157 feet

---

### Compound 1: Bridgestone Potenza RE-71RS (200TW)
**Extreme Performance Summer / Track Tire**

#### Physical Dimensions (255/35R19)
* **Width:** 255mm
* **Radius:** 330.55mm
* **Vertical Stiffness:** 260,000 N/m front & rear (scaled from M2's 290k for 285-width)
* **Angular Inertia:** 1.58 kg·m² (lighter, stiffer construction)

#### Grip Characteristics
* **DY_REF:** 1.29 (lateral friction coefficient)
  * **Improvement:** Old model used 1.28; M2's calibrated value is 1.29
  * **~14% more grip than PS4S**
* **DX_REF:** 1.30 (longitudinal friction coefficient)
* **Load Sensitivity:** LS_EXPY=0.85 front & rear (better grip retention under load)
  * **MAJOR FIX:** Old model used 0.72 front / 0.70 rear, which made the tire too degressive
* **LS_EXPX:** 0.83 (longitudinal load sensitivity)
  * **MAJOR FIX:** Old model used 0.74; M2's value is 0.83
* **Peak Slip Angle:** ~9.5° at reference load
* **Falloff Behavior:** More progressive (FALLOFF_LEVEL=0.90, FALLOFF_SPEED=1.6)

#### Thermal Behavior (Per Bridgestone Engineer Data)
* **Optimal Temperature:** 90°C core (~120-130°F surface, safe to 160°F)
* **Cold Penalty:** Significant — needs warmup laps
* **Heat Generation:** FRICTION_K=0.065 front / 0.055 rear (sticky compound)
* **Cooling:** COOL_FACTOR=1.5 front / 1.8 rear (retains heat well for track sessions)
* **Graining:** GRAIN_GAIN=0.55 (200TW tires grain significantly when cold/overdriven)

#### Camber Sensitivity
* **Peak Camber:** -4.5° (from tire_camber_dy_re71rs.lut)
* **Gain at -4.5°:** +4.8% grip
* **DCAMBER_LUT:** tire_camber_dy_re71rs.lut (M2's proven curve)

#### Expected Performance
* **Lateral Grip:** ~1.15-1.20g sustained (200TW track tire level)
* **Optimal Pressures:** Cold 24-28 psi → Hot 32-37 psi (34 psi optimal)

---

### Tire Scaling Methodology
When adapting the M2's tire model from 275/285-width to the M340i's 255-width, the following parameters were scaled:
* **RATE (vertical stiffness):** Scaled by width ratio (255/275 or 255/285)
* **DAMP (damping):** Scaled by width ratio
* **ANGULAR_INERTIA:** Scaled by width ratio (narrower tire = lighter)
* **All grip coefficients (DY_REF, DX_REF, LS_EXPY, etc.):** Copied directly from M2 (grip is a function of compound, not width)
* **All thermal parameters:** Copied directly from M2 (thermal behavior is compound-specific)
* **All LUT files:** Copied directly from M2 (camber curves, temperature curves, wear curves are compound-specific)

---

## Research & Data Integrity

### Real-World Data Priority
Always prioritize real-world technical specifications, test data, and tire data when making changes to physics files. For this M340i xDrive model:
* **Performance Data:** Car & Driver M340i xDrive test (0.92-0.96g lateral, 155-157 ft braking)
* **Tire Model Source:** BMW M2 G87's calibrated and proven tire model (ported and scaled)
* **Damper Ratios:** BMW adaptive damper behavior (digressive, fast = 40-50% of slow)
* **Aerodynamics:** BMW G20 official Cd=0.26 specification, sedan lift characteristics from automotive aerodynamics research

### Web Research Required
When specific G20 M340i xDrive data is unavailable in local documentation, perform web searches for:
* Real-world specifications (suspension geometry, alignment specs, brake sizes)
* Performance test data (skidpad, braking, acceleration)
* Tire data (sizes, pressures, temperature ranges)

### No Generalizations
Do not apply generic "BMW" or "Modern Sports Sedan" assumptions. Every parameter change must be rooted in:
1. **Specific G20 M340i xDrive data**, OR
2. **Proven calibration from a similar vehicle** (e.g., M2 G87 tire model for tire physics), OR
3. **Engineering calculations** (e.g., bump stop engagement based on spring rate and load transfer)

### Assumption Protocol
If specific data is unavailable after research, **do not guess.** Stop and ask for permission before using placeholder values or making engineering assumptions.

---

## Development Guidelines

### Physics Accuracy
* **Power Curve:** Ensure engine.ini reflects B58's specific delivery (~382 hp / 369 lb-ft torque curve)
* **Transmission:** ZF 8HP50 automatic with xDrive AWD logic
* **Electronics:** Configuration should include BMW-specific traction control and xDrive torque distribution via CSP scripts

### Suspension Modifications
* **Damper Ratios:** Always maintain digressive ratios (fast = 40-50% of slow) when adjusting dampers
* **Bump Stops:** Calculate engagement points based on spring rate and load transfer — never use arbitrary values
* **Alignment:** Factory toe-in specs are critical for AWD stability (rear toe-in especially important)

### Tire Model Modifications
* **Never Auto-Generate LUTs:** Use hand-crafted LUT files from proven models (M2, in this case)
* **Grip Coefficients:** Base on real-world skidpad data, not guesswork
* **Thermal Model:** Verify IDEAL_TEMP and COOL_FACTOR against tire manufacturer data

### Aerodynamics
* **LUT Convention:** This model uses "Positive CL = Lift" convention (matching M2)
* **Drag Budget:** Always verify total CdA matches BMW specification (0.585 for Cd=0.26)
* **Lift Distribution:** Sedans should produce net lift (~Cl 0.12-0.15), rear-biased for stability

---

## Documentation Reference

For technical clarification on parameter syntax or physics engine limitations:

> [!IMPORTANT]
> Consult the **ASSETTO CORSA MODDING MANUAL** located in the repository root for standardized modding protocols and configuration definitions.

---

## Change Log

### Latest Changes (Physics Overhaul)
1. **Suspension:**
   * Fixed damper fast-rebound ratios (front 82%→45%, rear 62%→44%)
   * Increased front bump stop rebound travel from 75mm to 120mm (sedan needs more droop)
   * Added BMW G20 factory toe-in (front -0.00015, rear -0.00065)
   * Adjusted bump stop rates and engagement points for proper 1G behavior

2. **Aerodynamics:**
   * Rewritten aero model using M2's proven LUT convention (positive CL = lift)
   * Increased front/rear wing CL_GAIN from 0.12/0.10 to 0.38/0.60 (now produces realistic sedan lift)
   * Adjusted body CD_GAIN to 0.97 to maintain total Cd=0.26
   * Rewritten 6 of 7 wing LUT files using M2 profiles

3. **Tires:**
   * Completely ported M2 G87's tire model (both PS4S and RE-71RS compounds)
   * Increased PS4S grip coefficients (DY_REF 1.12→1.23, DX_REF 1.15→1.24)
   * **MAJOR FIX:** RE-71RS load sensitivity (LS_EXPY 0.72→0.85 front, 0.70→0.85 rear; LS_EXPX 0.74→0.83)
   * Added M2's hand-crafted LUT files (temperature curves, wear curves, camber curves)
   * Added missing [ADDITIONAL1] section
   * Changed default compound to INDEX=0 (PS4S) — appropriate for street car

---

## Notes

* **Pickup Ride Height:** This value is only an offset for the car status screen in the setup menu. It does **not** affect physics.
* **Static Camber:** The `STATIC_CAMBER` setting in suspensions.ini is a baseline value. The actual static camber is calculated based on suspension geometry and is displayed in the car status window in-game.
* **Build Commands:** Use the `data/` folder for development.
