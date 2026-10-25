---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<p>
  <a href="{{ base_path }}/files/CV_Alexandre_Fournier_Montgieux_2p.pdf" class="btn btn--primary"><i class="fa fa-file-pdf" aria-hidden="true"></i> Download Full CV (2-Page PDF)</a>
  <a href="{{ base_path }}/files/CV_Alexandre_Fournier_Montgieux_1p.pdf" class="btn btn--info"><i class="fa fa-file-alt" aria-hidden="true"></i> Download Short Resume (1-Page PDF)</a>
</p>

## Experience

* **Doctoral Researcher in Machine Learning & Computer Vision** — *CEA LIST (Nano-INNOV) & Université Paris-Saclay*, Palaiseau, France *(Nov. 2023 – Nov. 2026)*
  * **Distributed Vision Training at Scale:** Trained deep representation backbones (iResNet-50, ResNet-101, ViT-S; 50M–100M parameters) on 2M+ image datasets using PyTorch Lightning across multi-GPU national supercomputers (Jean Zay / Nvidia A100 & V100, Adastra / AMD ROCm MI250X, Factory-IA).
  * **Synthetic Training Set Generation for Face Recognition:** Generated over 1M diverse synthetic face images using GAN and Diffusion models ([FaVGen, WACV 2025](https://github.com/CEA-LIST/FaVGen)), improving downstream verification fairness without sacrificing accuracy.
  * **Identity Anonymization & VLM Bias Auditing:** Scaled diffusion-based latent trajectory morphing (DiffMorpher) and text-driven synthesis to build **BALPortraits** (9,000 anonymized portraits across 24 demographic segments) and audit 16 Vision-Language Models (*WACV 2027*).
  * **Continuous Generative Modeling:** Co-developed **Diff-CA** (*NeurIPS 2026 Spotlight*), training continuous flow-matching diffusion models to separate shared visual factors from salient characteristics.
  * **Web-Scale Data Curation & Demographic Inference:** Filtered WebFace42M (42M images) via Iterative Proportional Fitting (IPF) to construct the **WEG** benchmark and **REGI-Face** transfer-learning annotator.
  * **Teacher-Student 3D Perception:** Co-developed **MVAT**, a weakly supervised multi-view teacher-student distillation framework for 3D object detection on nuScenes and Waymo (*WACV 2026*).
  * **Multi-Node Hyperparameter & Contrastive Pre-Training:** Orchestrated distributed multi-node Optuna hyperparameter searches and SimCLR contrastive pre-training pipelines.

* **Referent Teacher — Advanced Deep Learning (Master BDMA, M2)** — *CentraleSupélec*, Gif-sur-Yvette, France *(2024 – 2026)*
  * Designed and delivered M2 coursework covering deep computer vision architectures, optimization methods, object detection/segmentation, and fairness auditing methodologies.

* **Practical Training Supervisor — Fairness in AI** — *Université Paris-Saclay*, Orsay, France *(Feb. 2024)*
  * Led hands-on lab sessions on statistical bias detection and mitigation in machine learning models.

* **Research Intern — Generative Modeling with GANs** — *CEA LIST (Nano-INNOV)*, Palaiseau, France *(Apr. 2023 – Sep. 2023)*
  * Engineered controlled generation pipelines with StyleGAN and HyperStyleGAN to synthesize demographically balanced training sets for face recognition.

* **Computer Vision Intern — Automated Lithology Characterization** — *Schlumberger (SLB)*, Clamart, France *(Feb. 2022 – Aug. 2022)*
  * Developed segmentation pipelines and frugal deep classification/regression models to estimate rock grain size from high-resolution 2D microscopic imagery.

* **Front-End & Platform Developer — BackOffice Team** — *Stockly*, Paris, France *(Aug. 2021 – Feb. 2022)*
  * Contributed to the production BackOffice logistics platform in **Rust** and **Angular**, unifying order and supplier management workflows.

---

## Education

* **Ph.D. in Machine Learning & Computer Vision** — *Université Paris-Saclay & CEA LIST*, Palaiseau, France *(2023 – 2026)*
* **MSc in Mathematics, Vision, and Learning (MVA)** — *ENS Paris-Saclay*, Cachan, France *(2022 – 2023)*
  * **Mention: Très Bien (Highest Honors)**.
  * Coursework & projects: Denoising Diffusion Probabilistic Models (DDPM) for image restoration, Plug-and-Play (PnP) proximal optimization (ADMM/PGD), and multilingual Named Entity Recognition on low-resource African languages (MasakhaNER with LLaMA/XLM-RoBERTa).
* **Engineering Degree (Diplôme d'Ingénieur) in Computer Science & Machine Learning** — *Télécom Paris*, Palaiseau/Paris, France *(2019 – 2023)*
  * **GPA: 4.0 / 4.0**.
  * Specialization in Image Processing, 3D Graphics & Interactive Systems, and Deep Learning (OpenCL GPU-accelerated Bayesian Fourier super-resolution, particle fluid simulation).
* **Classes Préparatoires aux Grandes Écoles (MPSI / MP\*)** — *Lycée Janson de Sailly*, Paris, France *(2017 – 2019)*

---

## Software, Awards & Research Projects

* **NeurIPS 2026 Top Reviewer** *(2026)*
* **REGI-Face Toolkit** — Modular Python library for frugal, high-throughput facial demographic inference; integrated into the **European Vanguard Project** *(2026)*.
* **[FaVFA (Fairness in Face Verification Analysis)](https://github.com/CEA-LIST/FaVFA)** — Open-source statistical bias auditing framework registered with the *Agence pour la Protection des Programmes* (APP Deposit `N° IDDN.FR.001.160022.000.S.P.2025.000.31235`, *2025*).
* **SHARP Project (French PEPR AI Program)** — Cross-lab collaboration on frugal and trustworthy machine learning *(2023 – 2026)*.
* **International Research Visit** — Embedded 1-month research collaboration at **CERTH** (Centre for Research and Technology Hellas), Thessaloniki, Greece *(April – May 2024)*.

---

## Technical Skills & Languages

* **Core Languages:** Python, C++, Rust, C, SQL, OCaml, Java, JavaScript/TypeScript, GLSL, OpenCL/OpenGL, Bash
* **Deep Learning & ML:** PyTorch, PyTorch Lightning, Hugging Face, TorchVision, TensorFlow, Optuna, Scikit-learn, SciPy, NumPy
* **Architectures & Paradigms:** Diffusion Models (DDPM, DDIM, Latent Diffusion), Flow Matching, GANs (StyleGAN, DCFace), Vision Transformers (ViT, DINOv2), iResNet/ResNet, Contrastive & Self-Supervised Learning, vMF Representations, 3D Point-Cloud Detection
* **HPC & Infrastructure:** SLURM Workload Manager, Jean Zay (Nvidia A100/V100), Adastra (AMD ROCm MI250X), Factory-IA, Linux/Ubuntu, Git, LaTeX
* **Human Languages:** French (Native), English (C1 / Fluent), German (B2–C1 / Working Proficiency)
* **Interests:** Karate, Tennis, Swimming, Choir Singer, Soloist & Choir Director

---

## Publications

<ul>{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

## Teaching

<ul>{% for post in site.teaching reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

## Talks & Research Visits

<ul>{% for post in site.talks reversed %}
  {% include archive-single-talk-cv.html %}
{% endfor %}</ul>

