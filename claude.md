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

### README Maintenance
* **NEVER manually add duplicate entries** - Always check if a car already exists in the Available Cars section before adding
* **Check for base model variants** - Cars like "M2 G87 (AT)" and "M2 G87 (MT)" share a base model; don't duplicate the base entry
* **Match the description** from `ui_car.json` exactly when adding cars manually
* **Automated workflow handles updates** - The GitHub Actions workflow automatically adds new cars from `ui_car.json`, so manual updates should be minimal

### When Adding New Cars
1. Create a SHORT description in `ui_car.json` (10-15 words max)
2. Verify the car doesn't already exist in README.md
3. If manually adding to README, use alphabetical order by year then name
4. Use the format: `- **YEAR Name (Variant)** - Short description from ui_car.json`

---

## Physics & Setup Notes

These notes apply to all Assetto Corsa car configurations:

* **Pickup Ride Height:** This value is only an offset for the car status screen in the setup menu. It does **not** affect physics.
* **Static Camber (`suspensions.ini`):** The `STATIC_CAMBER` setting is a baseline value. The actual static camber is calculated based on suspension geometry and is displayed in the car status window in-game.
* **Build Commands:** Use the `data/` folder for development.
