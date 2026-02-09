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
* **Vehicle Specifications:** When real-world vehicle specifications are discovered (engine specs, transmission details, suspension geometry, tire data, etc.), document them in the car-specific `claude.md` file within that car's directory. This creates a reference for future development and ensures consistency.

---

## Physics & Setup Notes

These notes apply to all Assetto Corsa car configurations:

* **Pickup Ride Height:** This value is only an offset for the car status screen in the setup menu. It does **not** affect physics.
* **Static Camber (`suspensions.ini`):** The `STATIC_CAMBER` setting is a baseline value. The actual static camber is calculated based on suspension geometry and is displayed in the car status window in-game.
* **Build Commands:** Use the `data/` folder for development; pack to `data.acd` only for release.
