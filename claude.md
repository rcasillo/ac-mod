# Assetto Corsa Modding Project

This repository contains development files, assets, and configurations for **Assetto Corsa car mods**. It serves as the central hub for managing physics data, visual assets, and performance parameters.

---

## Project Scope
* **Car Configurations:** Comprehensive `.ini` file management for engine, aero, and electronics.
* **Physics Data:** Suspension geometry, drivetrain logic, and tire model definitions.
* **Asset Management:** Integration of 3D models, textures, and CSP (Custom Shaders Patch) features.

---

## Technical Documentation & Guidance
If you require clarification on how specific settings, variables, or physics parameters function within this repository, please consult the primary documentation:

> [!TIP]
> Refer to the **ASSETTO CORSA MODDING MANUAL** located in this repository for a full breakdown of parameters and modding standards.

---

## Development Standards
* **Encoding:** All configuration files must be saved in **UTF-8** (without BOM).
* **Syntax:** Follow standard AC initialization formatting; ensure all brackets `[]` are properly closed.
* **Vehicle Specifications:** When real-world vehicle specifications are discovered (engine specs, transmission details, suspension geometry, tire data, etc.), document them in the car-specific `CLAUDE.md` file within that car's directory. This creates a reference for future development and ensures consistency.

---

## README and Car Metadata Guidelines

**IMPORTANT:** The repository README and release automation depend on concise, consistent car descriptions.

### ui_car.json Description Field
* **Keep descriptions SHORT** - Maximum 10-15 words (one sentence)
* **Focus on key characteristics:** engine type, drivetrain, notable features
* **Good examples:**
  * `"High-performance sports sedan with B58 3.0L turbocharged inline-six and xDrive AWD"`
  * `"Mid-engine American supercar with Z51 package aero parts and Extra A interior dome light"`
* **BAD examples:**
  * Long paragraphs describing history, features, and specifications
  * Multiple sentences with `<br>` tags
  * Marketing copy or flowery language

### README Maintenance (AUTOMATED - DO NOT EDIT MANUALLY)

**CRITICAL:** The README.md car list in the "Available Cars" section is **automatically managed** by GitHub Actions. The workflow:
* Scans all `ui_car.json` files in the `cars/` directory
* Automatically adds any new cars to the README
* **Deduplicates entries** - removes any duplicate cars that may have been manually added
* **Sorts alphabetically** - maintains consistent ordering by year then name
* Runs on every release and can be triggered manually

**DO NOT manually add cars to the README.md "Available Cars" section.** The workflow will:1. Detect the car from `ui_car.json`
2. Add it automatically on the next release
3. Remove any duplicate entries you may have added
4. Re-sort the list alphabetically

**Exception:** If you need to manually edit a car's description in the README, you MUST also update it in the corresponding `ui_car.json` file, otherwise the workflow will overwrite your manual edit on the next run.

### When Adding New Cars
1. Create the car with a SHORT description in `ui_car.json` (10-15 words max)
2. **DO NOT manually add to README.md** - let the automated workflow handle it
3. The workflow will add it on the next release with format: `- **YEAR Name (Variant)** - Description from ui_car.json`
4. If duplicates appear, they will be automatically removed on the next workflow run

---

## Physics & Setup Notes

These notes apply to all Assetto Corsa car configurations:

* **Pickup Ride Height:** This value is only an offset for the car status screen in the setup menu. It does **not** affect physics.
* **Static Camber (`suspensions.ini`):** The `STATIC_CAMBER` setting is a baseline value. The actual static camber is calculated based on suspension geometry and is displayed in the car status window in-game.
* **Build Commands:** Use the `data/` folder for development.
* **Configuration Reference Policy:** Never use another car's configuration in this repository as a reference for "correct" values. All cars are mods in development and may contain errors. Always refer to the **Assetto Corsa Modding Manual** and real-world specifications for authoritative guidance on parameter values and formulas.
