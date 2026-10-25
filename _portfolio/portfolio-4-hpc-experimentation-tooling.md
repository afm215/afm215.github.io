---
title: "HPC Experimentation Tooling: Slurm Job Generation, Multi-Node Optuna Search & Scratch Management"
excerpt: "Python libraries for large-scale experimentation on Jean Zay (Nvidia A100/V100), Adastra (AMD ROCm MI250X), and Factory-IA: config-driven Slurm job generation with resource validation, multi-node Optuna search with marginal-effect analysis of hyperparameters, and coordinated node-local scratch management.<br/><img src='/images/research/hpc_tooling_teaser.png' style='max-width: 550px; margin-top: 10px;'>"
collection: portfolio
---

{% include base_path %}

![Slurm job generation, multi-node Optuna search with hyperparameter marginal effects, and coordinated scratch management]({{ base_path }}/images/research/hpc_tooling_teaser.png)

* **Slurm Job Generator (2024–2026):** Packaged as a Python library, `create_slurm_generator.py` turns a declarative `.conf` file into ready-to-submit Slurm `sbatch` scripts. Requested resources (partitions, GPUs, CPUs, memory, wall time) are checked against the configurations each cluster actually offers before anything is submitted, and a single configuration can expand into hundreds of independent jobs. Used across heterogeneous national supercomputers (**Jean Zay** Nvidia A100/V100, **Adastra** AMD ROCm MI250X, and **Factory-IA**).
* **Multi-Node Hyperparameter Search & Analysis:**
  * A set of **Optuna** helper functions, predating Optuna's journal-file storage, that let independent Slurm jobs running on different nodes share and contribute to the same hyperparameter study.
  * A companion library that extracts the **marginal effect of each hyperparameter on every available metric**, together with the associated **p-values**, to identify which hyperparameters significantly influence each metric.
* **Scratch Management Library:** Coordinates node-local scratch storage across independent multi-node processes. At job start, the dataset is extracted once per node rather than once per process, so co-located processes do not waste bandwidth on redundant transfers; at the end of the run, results saving is coordinated across nodes.
