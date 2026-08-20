# stepss Tutorials: Nordic Test System

Tutorial notebooks for learning power system simulation with
[stepss](https://stepss.sps-lab.org/python/) on the IEEE Nordic test system,
designed for the **Control and Operation of Electric Power Systems (EEN452)**
course at the Cyprus University of Technology (JupyterHub-ready).

## The notebooks

| Notebook | What it teaches |
|----------|-----------------|
| **`Execute.ipynb`** | First contact with RAMSES: configure a case, initialize, trip generator g7 interactively (`addDisturb`), simulate, and plot machine and bus quantities with the extractor. |
| **`PowerFlowToDynamics.ipynb`** | The complete static-to-dynamic workflow of STEPSS: solve the power flow with **HELIOS**, increase every Central-area load by 10 %, re-solve, export the new operating point as one re-loadable data file, then simulate the trip of generator g2 with **RAMSES** and compare the frequency and voltage evolution against the original operating point B. |

## Files

The data lives one directory up and is read from there, so there is one copy of
every file and the notebooks cannot drift from the test system they teach.

| File | Role | Read by |
|------|------|---------|
| `../lf_B.dat` | The network and operating point B: buses, lines, transformers, loads, generation and the solved voltages | HELIOS and RAMSES |
| `../dyn_B.dat` | Dynamic models (machines, AVRs, governors, PSSs, loads, LTC controllers) | RAMSES |
| `../settings1.dat` | Time-integration and solver settings | RAMSES |
| `../obs.dat` | Observables selection (wildcards, record everything) | RAMSES |
| `../trip_gen_long.dst` | Disturbance scenario: trip generator g2 at t = 1 s, stop at t = 120 s | RAMSES |
| `../nothing_long.dst` | Undisturbed 1000 s run | RAMSES |
| `nordic_oneline.png` | One-line diagram of the Nordic test system | the notebooks |

`PowerFlowToDynamics.ipynb` additionally generates `lf_B_plus10pct.dat` and
`volt_rat_B_plus10pct.dat` (the stressed operating point) plus `*.trace`/`*.trj`
output files when it runs. Those stay in this directory: they are run products,
not data.

## Getting started

On the course JupyterHub simply open a notebook and run the cells in order.
Elsewhere, install first:

```bash
pip install jupyter ipython stepss
```

On Linux the engine also needs `libopenblas0 libgfortran5 libgomp1`
(see the [installation guide](https://stepss.sps-lab.org/python/installation/)).

## Documentation and references

- [stepss documentation](https://stepss.sps-lab.org/python/): API reference and
  [HELIOS power-flow guide](https://stepss.sps-lab.org/python/helios/)
- [STEPSS user guide](https://stepss.sps-lab.org/): data formats and models
- [EEN452 course page](https://sps-lab.org/courses/een452/)
- The test system: IEEE PES-TR19, *Test Systems for Voltage Stability Analysis and
  Security Assessment*, 2015 (report and variants in `../doc/`)

---

*This material is part of the EEN452 course curriculum at the Cyprus University of
Technology, developed by the [Sustainable Power Systems Lab](https://sps-lab.org/).*
