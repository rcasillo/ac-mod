# Project Memory: 2015 Mitjet LV02

This directory contains the specific assets and physics data for the **2015 Mitjet LV02** silhouette race car.

---

## Reference Car
* **Listing:** [2015 Mitjet LV02 - racecarsforyou.com](https://racecarsforyou.com/listing/2015-mitjet-lv02/)

---

## Important Notes
* **Folder Naming:** The directory is named `mitjet_audi_2l`, but this is a **misnomer** from the original mod creator. The real engine is a **Renault F4R 2.0L**, not an Audi engine.
* **Bodywork:** The fiberglass body is **BMW-style** silhouette, not based on an Audi.

---

## Vehicle Specifications

### Engine & Powertrain
* **Engine:** Renault F4R 2.0L EFI DOHC 16V I4 (RS origin, race-prepped by Oreca)
* **Peak Power:** **230 hp @ 7,500 RPM**
* **Peak Torque:** ~251 Nm @ 5,000-5,500 RPM (estimated from scaling stock F4R 830)
* **Aspiration:** Naturally aspirated
* **Transmission:** SADEV SL75 6-speed sequential, **dogring** engagement, paddle shift
* **Drivetrain:** RWD, locking LSD

### Weight & Balance
* **Dry Weight:** 750 kg (1,653 lbs)
* **With Driver:** ~816 kg (1,800 lbs)

### Suspension
* **Front:** Double wishbone, adjustable coilovers
* **Rear:** Tork Engineering live axle, coilovers (LV02-specific upgrade from earlier swing-axle)

### Brakes
* **Type:** 4-wheel disc
* **Calipers:** **Brembo** 4-piston front, 2-piston rear
* **Rotors:** 328mm ventilated front

### Tires & Wheels
* **Tires:** 255/40/R18 Yokohama Advan (semi-slick)
* **Wheels:** 18"

### Chassis & Body
* **Frame:** FIA-homologated steel tube frame
* **Body:** Fiberglass, **BMW-style** silhouette
* **Dimensions:** 4,100mm L × 1,800mm W × 1,300mm H

### Safety & Electronics
* **Safety:** Containment seat, plumbed fire system, meets modern FIA standards
* **Electronics:** No ABS, no TC, no power steering
* **Fuel Cell:** 19.5 gallon (~74L) for endurance racing

### Performance Benchmarks
* **0-60 mph:** ~4.0 seconds
* **Top Speed:** ~220 km/h

---

## Competition Approvals
Approved for:
* SCCA
* CSRG
* SVRA
* ICSCC
* NASA

---

## Research & Data Integrity
* **Real-World Data Priority:** Always prioritize verified specifications from the listing, race series technical regulations, and multi-source confirmation.
* **Web Research Required:** When specific Mitjet LV02 data is unavailable, search for Renault F4R race engine specs, SADEV SL75 ratios, and FIA silhouette car regulations.
* **No Generalizations:** Do not apply generic "sports car" or "spec racer" assumptions. Every parameter change must be rooted in data specific to the Mitjet LV02 and its Renault F4R/Oreca engine.
* **Assumption Protocol:** If specific data is unavailable after research, **do not guess.** Stop and ask for permission before using placeholder values or making engineering assumptions.

---

## Data Sources
* [2015 Mitjet LV02 Listing - racecarsforyou.com](https://racecarsforyou.com/listing/2015-mitjet-lv02/)
* [RACER: Mitjet 2L Review](https://racer.com/2014/01/21/mitjet-2l-a-real-race-car-for-real-racers/)
* [Road & Track: Mitjet 2L at Barber](https://www.roadandtrack.com/motorsports/a26869/mitjet-2l-silhouette-racer-first-drive/)
* [NASA Speed News: Mitjet 2L Series Tech](https://nasaspeed.news/tech/mitjet-2l-series-technical-and-sporting-regulations-version-20151210/)
* [GoToTheGrid: Mitjet 2L Technical Specs](https://www.gotothegrid.com/technical-specifications-mitjet-2l)
* [EXR Racing: Mitjet Info](https://www.exrracing.com/mitjet)

---

## Known Data Gaps
* **Exact Torque Peak:** Multiple sources confirm 230 hp @ 7,500 RPM, but exact torque peak RPM and value not specified. Current curve scaled from stock Renault F4R 830 (197 hp) by factor of 1.168.
* **Wheelbase:** Not specified in available sources. Dimension data shows overall length/width/height only.
* **Gear Ratios:** SADEV SL75 transmission confirmed with 8×31 (3.875:1) final drive from official SADEV documentation. Individual gear ratios are estimated/rescaled to preserve overall gearing feel while achieving correct top speed.
* **Spring Rates:** Coilovers are adjustable; no factory baseline rates published.
* **Aero Data:** No published downforce or drag coefficient data. Body is basic silhouette with minimal aero devices.

---

## Current Physics Status

### Engine (`engine.ini`)
* **Last Updated:** 2026-02-11
* Renault F4R 2.0L I4: 230 hp @ 7,500 RPM, ~251 Nm @ 5,000-5,500 RPM
* Natural aspiration, no turbo
* Limiter: 7,500 RPM (correct)
* Inertia: 0.13 (reasonable for 2.0L I4)

### Power Curve (`power.lut`)
* **Last Updated:** 2026-02-11
* Scaled from stock Renault F4R 830 curve shape (197 hp @ 7,100 RPM → 230 hp @ 7,500 RPM)
* Scale factor: 1.168 (230/197)
* Peak torque: ~251 Nm @ 5,000-5,500 RPM
* Peak power anchor: 218.4 Nm @ 7,500 RPM (validated: 171.5 kW × 9549 / 7500 = 218.4 Nm)

### Drivetrain (`drivetrain.ini`)
* **Last Updated:** 2026-02-11
* **Final Drive:** 3.875:1 (SADEV SL75 8×31 bevel gear option)
* **Gear Ratios:** Rescaled to preserve overall gearing feel from gears 1-5, with 6th gear increased ~3.7% to achieve 220 km/h top speed
* **Top Speed Calculation:** 7,500 RPM / 3.949 overall (6th) × 2π × 0.307m / 60 = 61.0 m/s = 220 km/h (137 mph)

### Suspension (`suspensions.ini`)
* **Status:** Not yet verified against real specs
* **Known:** Double wishbone front, live axle rear (LV02), coilover dampers
* **Unknown:** Spring rates, damping rates, geometry points

### Aerodynamics (`aero.ini`)
* **Status:** Not yet verified
* **Known:** Basic silhouette body, minimal aero devices
* **Unknown:** Drag coefficient, downforce (if any)

### Tires (`tyres.ini`)
* **Status:** Partially verified
* **Known:** 255/40/R18 Yokohama Advan semi-slick specification
* **Unknown:** Exact compound ratings, thermal properties

---

## Development Guidelines
* **Physics Accuracy:** Power curve must reflect Renault F4R race-prep with 230 hp @ 7,500 RPM.
* **Transmission Logic:** SADEV SL75 sequential with dogring engagement — verify shift logic in `drivetrain.ini`.
* **Live Axle Rear:** The LV02 uses a Tork Engineering live axle (not swing-axle like earlier models). Suspension geometry must reflect solid rear axle behavior.
* **Weight:** Target ~816 kg with driver for physics calculations.
* **No Driver Aids:** Zero ABS, TC, or power steering — ensure electronics.ini reflects this.

---

## Documentation Reference
For technical clarification on parameter syntax or physics engine limitations:

> [!IMPORTANT]
> Consult the **ASSETTO CORSA MODDING MANUAL** located in the repository root for standardized modding protocols and configuration definitions.
