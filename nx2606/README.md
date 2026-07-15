# NX 2606 Manual Runtime Probes

These probes are generated and statically checked by `nx-cad`, but only the
user may execute them manually inside Siemens NX through:

```text
File -> Execute -> NX Open
```

Do not ask an agent, MCP server, shell command, batch file, or GUI automation
to start NX or execute these journals.

Copy this entire directory to the NX machine because the numbered probes use
the sibling `_probe_support.py` module. Run one probe at a time in numeric
order and return the generated `.nxreport.json` after each run.

Current probes:

| Probe | Purpose | Recipe status |
| --- | --- | --- |
| `01_create_part.py` | work-part creation/load-status handling | verified by manual NX 2606 run |
| `02_closed_polyline_section.py` | closed Section and curve rules | verified by manual NX 2606 run |
| `03_closed_spline_section.py` | periodic StudioSplineBuilderEx curve | verified by manual NX 2606 run |
| `04_through_curves_solid.py` | two-section solid loft | verified by manual NX 2606 run |
| `08_boolean_unite.py` | overlapping-body boolean unite | verified by manual NX 2606 run |
| `09_edge_blend.py` | collector + AddChainset edge blend | verified by manual NX 2606 run |
| `10_step_ap242.py` | generic StepCreator native save and solid STEP export | experimental; 004 manual rerun required after enabling `ObjectTypes.Solids` |

Reserved probes `05` through `07` cover fixed-orientation, tapered, and
angular-law sweep configurations. They are intentionally not generated from
memory. The attempted NX 2606 angular-law and section-string configurations
already have user-reported failures. New sweep probes require exact API review
and a conservative recipe before handoff.

Validate a returned result locally without starting NX:

```bash
skills/nx-cad/scripts/check-runtime-report \
  models/nx_runtime_probes/nx2606/04_through_curves_solid.nxreport.json \
  --expected-bodies 1
```

Successful manual runtime evidence may promote the matching recipe from
`experimental` to `verified`. Static checks alone cannot do so.
