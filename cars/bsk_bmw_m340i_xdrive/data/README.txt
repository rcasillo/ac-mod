================================================================================
BMW 340i xDrive G20 - Assetto Corsa Configuration v6
================================================================================
Realistic physics based on actual dyno data and tire specifications

================================================================================
VERSION 6 MAJOR CHANGES
================================================================================

1. POWER CURVE - BASED ON ACTUAL B58 DYNO DATA
   - Peak torque: 443 Nm base × 1.13 turbo = 500 Nm (matches BMW spec!)
   - Flat torque plateau from 1850-4900 RPM (per real dyno)
   - Torque builds rapidly from 1500 RPM (turbo spool)
   - Smooth dropoff from 5000 RPM to redline
   - 7000 RPM shows ~172 Nm (realistic high-RPM torque)

2. ADJUSTABLE ANTI-ROLL BARS (IN-GAME!)
   - ARB_RATE added to suspensions.ini for both axles
   - setup.ini [ARB] section controls adjustment
   - Base: Front=38000 N/m, Rear=21000 N/m
   - Adjust via Content Manager or in-game setup screen

3. COMPLETELY REVISED TIRE MODEL

   MICHELIN PILOT SPORT 4S (Compound 0):
   - Optimal temp: 60-85°C (WIDE operating window)
   - Cold pressure: 25 PSI → Hot optimal: 34 PSI
   - Grip: DY_REF 1.18 front, 1.25 rear (scaled for width)
   - Thermal: Slow to heat/cool, very stable
   - Forgiving breakaway, good in all conditions
   - Low grain/blister tendency

   BRIDGESTONE POTENZA RE-71RS (Compound 1):
   - Optimal temp: 70-100°C (NARROW window - needs heat!)
   - Cold pressure: 25 PSI → Hot optimal: 32 PSI
   - Grip: DY_REF 1.32 front, 1.42 rear (higher peak grip)
   - Thermal: Fast response, cools quickly
   - Sharp breakaway, requires precise driving
   - Grains when cold, blisters when hot

4. INCREASED DRAG FOR CORRECT TOP SPEED
   - Body CD increased to 0.35 at 0 AOA
   - Balances higher power for realistic top speed

================================================================================
TIRE COMPARISON TABLE
================================================================================

                    | PS4S (Compound 0)  | RE-71RS (Compound 1)
--------------------|--------------------|-----------------------
Optimal Temp        | 60-85°C            | 70-100°C
Cold PSI            | 25                 | 25
Hot Optimal PSI     | 34                 | 32
Front Grip (DY_REF) | 1.18               | 1.32
Rear Grip (DY_REF)  | 1.25               | 1.42
Thermal Response    | Slow/Stable        | Fast/Sensitive
Falloff Character   | Gradual/Forgiving  | Sharp/Demanding
Best For            | Street/All-around  | Track/Autocross

================================================================================
ANTI-ROLL BAR ADJUSTMENT
================================================================================

In Content Manager or AC setup screen:

FRONT ARB:
- Base value: 38,000 N/m
- Softer (-): More front grip, more understeer resistance
- Stiffer (+): Sharper turn-in, less body roll

REAR ARB:
- Base value: 21,000 N/m  
- Softer (-): More rear grip, more oversteer tendency
- Stiffer (+): More stability, less rotation

Recommended starting points:
- Street: Front 0, Rear 0 (base values)
- Spirited: Front +3000, Rear +1500
- Track: Front +5000, Rear +3000

================================================================================
POWER CURVE DETAILS
================================================================================

Based on actual B58 340i dyno results:

RPM     | Base Torque | With Turbo (×1.13)
--------|-------------|--------------------
1500    | 305 Nm      | 345 Nm (spool)
1850    | 443 Nm      | 500 Nm (peak)
2000-4900| 443 Nm     | 500 Nm (plateau)
5000    | 438 Nm      | 495 Nm
5500    | 378 Nm      | 427 Nm
6000    | 288 Nm      | 325 Nm
6500    | 210 Nm      | 237 Nm
7000    | 152 Nm      | 172 Nm

Peak power occurs around 5800-6000 RPM where torque × RPM is maximized.

================================================================================
SETUP RECOMMENDATIONS
================================================================================

STREET DRIVING (PS4S):
- Tire pressure: 25 PSI cold (will reach 32-35 hot)
- Camber: -1.2° front, -1.0° rear
- ARB: Base values (0/0)
- TC: Level 5-7

SPIRITED DRIVING (PS4S):
- Tire pressure: 26-27 PSI cold
- Camber: -1.5° front, -1.2° rear
- ARB: +3000/+1500
- TC: Level 7-9

TRACK DAY (RE-71RS):
- Tire pressure: 25 PSI cold (will reach 30-32 hot)
- Camber: -2.0° front, -1.5° rear
- ARB: +5000/+3000
- TC: Level 9 or OFF
- Note: Warm up tires before pushing! RE-71RS needs heat.

================================================================================
KNOWN ISSUES
================================================================================

AUDIO: If engine sound cuts out after shifting, the issue is in the 
sound bank files (sfx folder), not the configuration. The sound bank 
may have limited RPM coverage. Try a different sound mod.

================================================================================
FILES MODIFIED IN V6
================================================================================

- power.lut: Realistic B58 dyno curve
- tyres.ini: Complete PS4S and RE-71RS remodel
- suspensions.ini: Adjustable ARB support
- setup.ini: ARB adjustment, 25 PSI cold pressure
- __cm_tyre_perfcurve_*.lut: Thermal performance curves
- wing_body_AOA_CD.lut: Increased drag for top speed balance

================================================================================
