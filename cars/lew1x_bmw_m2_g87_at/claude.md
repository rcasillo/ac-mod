# Project Memory: 2023 BMW M2 (Automatic)

This directory contains the specific assets and physics data for the **2023 BMW M2 (G87)** equipped with an **8-speed automatic transmission**.

---

## Vehicle Specifications
* **Chassis:** G87
* **Engine:** S58 3.0L Twin-Turbo Inline-6
* **Transmission:** 8-Speed Automatic (ZF 8HP76)
* **Drivetrain:** Rear-Wheel Drive (RWD)

---

## Research & Data Integrity
* **Real-World Data Priority:** Always prioritize real-world technical specifications, dyno graphs, and suspension geometry data when making changes to physics files.
* **Web Research Required:** When specific G87 M2 data is unavailable in local documentation, perform web searches for real-world specifications, tire data, and suspension geometry before making parameter changes.
* **No Generalizations:** Do not apply generic "M-car" or "Modern BMW" assumptions. Every parameter change must be rooted in data specific to the G87 M2.
* **Assumption Protocol:** If specific data is unavailable after research, **do not guess.** Stop and ask for permission before using placeholder values or making engineering assumptions.

---

## Development Guidelines
* **Physics Accuracy:** Ensure the power curve reflects the S58's specific delivery (approx. 453 hp / 406 lb-ft).
* **Automatic Transmission Logic:** Verify that `drivetrain.ini` accounts for automatic shift timing, torque converter behavior, and shift patterns. The ZF 8HP76 should reflect realistic shift speeds and torque multiplication characteristics.
* **Electronics:** Configuration should include BMW M-specific Traction Control (10-stage) and MDM (M Dynamic Mode) via CSP scripts.

---

## Documentation Reference
For technical clarification on parameter syntax or physics engine limitations:

> [!IMPORTANT]
> Consult the **ASSETTO CORSA MODDING MANUAL** located in the repository root for standardized modding protocols and configuration definitions.
