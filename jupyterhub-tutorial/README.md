# PyRAMSES Tutorials — Nordic Test System

Self-contained tutorial notebooks for learning power system simulation with
[PyRAMSES](https://stepss.sps-lab.org/pyramses/) on the IEEE Nordic test system,
designed for the **Control and Operation of Electric Power Systems (EEN452)**
course at the Cyprus University of Technology (JupyterHub-ready).

## The notebooks

| Notebook | What it teaches |
|----------|-----------------|
| **`Execute.ipynb`** | First contact with RAMSES: configure a case, initialize, trip generator g7 interactively (`addDisturb`), simulate, and plot machine and bus quantities with the extractor. |
| **`PowerFlowToDynamics.ipynb`** | The complete static-to-dynamic workflow of STEPSS: solve the power flow with **HELIOS**, increase every Central-area load by 10 %, re-solve, export the new operating point (static dump + `volt_rat` initial conditions), then simulate the trip of generator g2 with **RAMSES** and compare the frequency and voltage evolution against the original operating point B. |

## Files

| File | Role | Read by |
|------|------|---------|
| `lf_B.dat` | Static network and power-flow data, operating point B | HELIOS |
| `dyn_B.dat` | Dynamic models (machines, AVRs, governors, PSSs, loads, LTC controllers) | RAMSES |
| `volt_rat_B.dat` | Solved operating point B: bus voltages and transformer ratios | RAMSES (initialization) |
| `settings1.dat` | Time-integration and solver settings | RAMSES |
| `obs.dat` | Observables selection (wildcards — record everything) | RAMSES |
| `trip_gen.dst` | Disturbance scenario: trip generator g2 at t = 1 s, stop at t = 120 s | RAMSES |
| `short_trip_branch.dst`, `nothing.dst` | Alternative disturbance scenarios | RAMSES |
| `nordic_oneline.png` | One-line diagram of the Nordic test system | the notebooks |

`PowerFlowToDynamics.ipynb` additionally generates `lf_B_plus10pct.dat` and
`volt_rat_B_plus10pct.dat` (the stressed operating point) plus `*.trace`/`*.trj`
output files when it runs.

## Getting started

On the course JupyterHub simply open a notebook and run the cells in order.
Elsewhere, install first:

```bash
pip install jupyter ipython pyramses
```

On Linux the engine also needs `libopenblas0 libgfortran5 libgomp1`
(see the [installation guide](https://stepss.sps-lab.org/pyramses/installation/)).

## Documentation and references

- [PyRAMSES documentation](https://stepss.sps-lab.org/pyramses/) — API reference and
  [HELIOS power-flow guide](https://stepss.sps-lab.org/pyramses/helios/)
- [STEPSS user guide](https://stepss.sps-lab.org/) — data formats and models
- [EEN452 course page](https://sps-lab.org/courses/een452/)
- The test system: IEEE PES-TR19, *Test Systems for Voltage Stability Analysis and
  Security Assessment*, 2015 (report and variants in `../doc/`)

---

*This material is part of the EEN452 course curriculum at the Cyprus University of
Technology, developed by the [Sustainable Power Systems Lab](https://sps-lab.org/).*
