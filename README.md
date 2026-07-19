# IEEE Nordic Test System

**The IEEE Nordic test system for voltage stability analysis, in RAMSES format.**

This repository holds the Nordic variant detailed in the IEEE PES technical report [PES-TR19, "Test Systems for Voltage Stability Analysis and Security Assessment"](https://resourcecenter.ieee-pes.org/publications/technical-reports/PESTR19.html), prepared for use with the [STEPSS](https://stepss.sps-lab.org/) power system simulation platform (RAMSES dynamic simulator and PyRAMSES Python API).

The system has 74 buses (including 20 generator buses), 20 synchronous machines with detailed dynamic models, and voltage levels of 400/220/130 kV plus generator and distribution buses. It is a well-known benchmark for long-term voltage stability studies and dynamic security assessment.

## Contents

| Path | Description |
|------|-------------|
| `lf_A.dat`, `lf_B.dat` | Load-flow data for operating points A and B |
| `lf_B_plus_*.dat` | Operating point B with total load increased by 25–500 MW |
| `dyn_A.dat`, `dyn_B.dat` | Dynamic data (machines, exciters, governors, PSS, LTCs, OELs) |
| `volt_rat_A.dat`, `volt_rat_B.dat`, `volt_rat_B_plus*.dat` | Power-flow solutions (voltages and transformer ratios) matching each operating point |
| `obs.dat` | Observables selection |
| `settings1.dat` | Solver settings |
| `uvls.dat` | Undervoltage load-shedding (UVLS) controllers |
| `*.dst` | Disturbance scenarios: no-disturbance run, branch/generator trips, LTC changes, Jacobian export for eigenanalysis (`eigen.dst`, `dampJac.dst`) |
| `sim_*.cfg`, `cmd.txt` | Simulation configuration and RAMSES command file |
| `doc/` | Official documentation: IEEE PES-TR19 report, Nordic test system report V6, and operating-point variants description |
| `scripts/` | PyRAMSES, Python, and MATLAB/Simulink usage examples (dynamic security assessment, curve extraction, modal analysis) |
| `jupyterhub-tutorial/` | Self-contained PyRAMSES tutorial notebook used in the [EEN452 course](https://sps-lab.org/courses/een452/) (voltage collapse scenario on operating point B) |

## Quick Start

With [PyRAMSES](https://pyramses.sps-lab.org/):

```python
import pyramses
case = pyramses.cfg()
case.addData('dyn_B.dat')
case.addData('volt_rat_B.dat')
case.addData('settings1.dat')
case.addDst('trip_gen.dst')
case.addObs('obs.dat')
sim = pyramses.sim()
sim.execSim(case)
```

Or run the RAMSES executable directly with one of the `cmd*.txt` command files. Run scripts from the repository root so that relative paths to the data files resolve.

## Documentation

The data formats are documented in the STEPSS user guide at [stepss.sps-lab.org](https://stepss.sps-lab.org/). The test system itself is described in `doc/`:

- **PES-TR19** — the official IEEE PES technical report defining the test system;
- **Nordic_test_system_V6.pdf** — detailed system report (T. Van Cutsem);
- **variants.pdf** — description of the operating-point variants.

## Citation

If you use this test system in your research, please cite the IEEE PES technical report:

> IEEE PES Task Force on Test Systems for Voltage Stability Analysis and Security Assessment, "Test Systems for Voltage Stability Analysis and Security Assessment," Technical Report PES-TR19, Aug. 2015.

## License

This repository is licensed under the [Apache License 2.0](LICENSE). The IEEE PES-TR19 report in `doc/` is redistributed for convenience and remains © IEEE.

## Authors

Developed and maintained by the [Sustainable Power Systems Laboratory (SPS-L)](https://sps-lab.org/) at the Cyprus University of Technology, under the direction of Dr. Petros Aristidou.

Original test system data by Dr. Thierry Van Cutsem (University of Liège) and the IEEE PES Task Force on Test Systems for Voltage Stability Analysis and Security Assessment.
