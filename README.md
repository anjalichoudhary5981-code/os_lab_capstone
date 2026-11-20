# OS Resource Manager

An integrated Python-and-Bash educational simulator for CPU scheduling, memory allocation, deadlock avoidance, disk scheduling, and workload comparison. The application is menu-driven and runs in a terminal; it does not control real operating-system resources.

## Problem and Objectives

Operating-system resource policies are easier to compare when the same workload can be run through multiple algorithms and measured with common metrics. This project provides a modular implementation that:

- Simulates four CPU scheduling policies and reports per-process CT, TAT, and WT.
- Compares First Fit, Best Fit, and Worst Fit memory allocation.
- Computes the Need matrix and safe sequence using Banker's safety algorithm.
- Compares four disk scheduling policies by total and average head movement.
- Exports repeatable CPU, memory, and disk comparisons, with optional graphs.
- Rejects invalid inputs, records activity, and includes automated tests.

## Algorithms and Measures

| Module | Algorithms | Measures |
| --- | --- | --- |
| CPU | FCFS, non-preemptive SJF, Round Robin, non-preemptive Priority | CT, TAT = CT - arrival, WT = TAT - burst, averages, Gantt timeline |
| Memory | First Fit, Best Fit, Worst Fit | Process allocation, remaining/free KB, allocated KB, utilization |
| Deadlock | Banker's safety algorithm | Need = Maximum - Allocation, safe/unsafe state, safe sequence |
| Disk | FCFS, SSTF, SCAN, C-SCAN | Service order, total cylinders moved, average movement per request |

Smaller numeric priority means higher priority. Memory is modeled as variable-size blocks with allocations consuming free space. SCAN and C-SCAN include travel to disk endpoints when their direction requires it. The disk average is total movement divided by request count.

## Requirements and Installation

- Python 3.9 or newer
- Bash for `run.sh` (Linux, macOS, WSL, or Git Bash)
- Matplotlib for graph generation; algorithm execution, CSV, and text reporting use the Python standard library

Install the chart dependency from the project root:

```bash
python -m pip install -r requirements.txt
```

The Python modules and tests can be used without Matplotlib. The report generator still creates CSV and text reports when chart generation is unavailable.

## Run

Linux/macOS/WSL/Git Bash:

```bash
chmod +x run.sh
./run.sh
```

Run the test suite through Bash:

```bash
./run.sh --test
```

Windows PowerShell (from the project directory):

```powershell
py -3 main.py
py -3 -m unittest discover -s tests -v
py -3 -m pip install -r requirements.txt
```

Windows users can also run `./run.sh` from WSL or Git Bash. To generate comparisons, choose **Performance Analysis / Reports** from the main menu.

## Project Structure

```text
main.py                     Integrated terminal menu
run.sh                      Bash launcher, environment check, and test runner
modules/common.py           Shared input, logging, and console helpers
modules/cpu_scheduling.py   CPU schedulers and metrics
modules/memory_management.py Memory allocation strategies
modules/deadlock.py         Banker's safety algorithm
modules/disk_scheduling.py Disk schedulers
modules/reporting.py        Shared-dataset comparisons, CSVs, text report, charts
data/                       Reusable sample datasets
tests/                      unittest coverage
logs/activity.log           Timestamped activity log
reports/                    Generated CSV, text, and PNG artifacts
REPORT.md                   University-level project report
```

## Inputs and Sample Data

Interactive module menus accept process attributes, sizes, vectors/matrices, and disk requests. Times and sizes must be non-negative or positive as appropriate; disk cylinders must be in `[0, disk_size - 1]`. Banker's matrices must have matching dimensions and allocation cannot exceed maximum demand.

The report menu reads `data/process_data.csv`, `data/memory_data.csv`, and `data/disk_data.csv`. It runs every policy in a module against that module's same sample data, so its comparisons are reproducible. The sample CPU workload contains P1 `(arrival=0, burst=5, priority=2)`, P2 `(1,3,1)`, P3 `(2,4,3)`, and P4 `(3,2,2)`.

## Generated Artifacts

The report menu generates:

- `reports/cpu_comparison.csv`, `reports/memory_comparison.csv`, `reports/disk_comparison.csv`
- `reports/performance_report.txt` with workload-specific observations
- With Matplotlib installed: `cpu_comparison.png`, `cpu_gantt.png`, `memory_allocation.png`, `memory_utilization.png`, and `disk_head_movement.png`
- `logs/activity.log` with timestamped application activity

Charts include titles, axes, units, and legends where relevant. Rankings apply only to the sample workloads; a different workload can produce different results.

## Tests

```bash
python -m unittest discover -s tests -v
```

Tests cover valid CPU, memory, Banker, disk, and report comparisons; invalid burst/resource/disk values; unsafe deadlock states; idle CPU intervals; and unallocated memory processes.

## Limitations and Future Scope

This is an instructional simulator, not a live system monitor. SJF and Priority are non-preemptive; memory does not model paging, compaction, or virtual memory; Banker's algorithm checks safety rather than granting live requests; and the terminal interface does not provide a GUI dashboard. Future work could add preemptive schedulers, page replacement, configurable workload editing, and a graphical interface.
