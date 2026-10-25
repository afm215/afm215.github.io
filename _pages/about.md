---
permalink: /
title: "Alexandre Fournier Montgieux"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% include base_path %}

I am a **Doctoral Researcher in Machine Learning & Computer Vision** at **[Université Paris-Saclay](https://www.universite-paris-saclay.fr/)** and **[CEA LIST (Nano-INNOV)](https://list.cea.fr/en/)** in Palaiseau, France, working with Adrian Popescu, Hervé Le Borgne, and Bertrand Luvison. I hold an **MSc in Mathematics, Vision, and Learning (MVA)** from **ENS Paris-Saclay** (*Très Bien* / Highest Honors) and an **Engineering Degree (Diplôme d'Ingénieur)** from **Télécom Paris** (GPA 4.0/4.0).

My research turns deep generative and representation-learning models into reliable, fair, and reproducible systems for real-world visual and multimodal pipelines. I enjoy the full arc of machine learning research—from mathematical formulation and theoretical guarantees to distributed training at scale on national supercomputers (Jean Zay, Adastra, Factory-IA) and releasing open-source toolkits.

<p>
  <a href="{{ base_path }}/files/CV_Alexandre_Fournier_Montgieux_2p.pdf" class="btn btn--primary"><i class="fa fa-file-pdf" aria-hidden="true"></i> Download CV (2-Page PDF)</a>
  <a href="{{ base_path }}/files/CV_Alexandre_Fournier_Montgieux_1p.pdf" class="btn btn--info"><i class="fa fa-file-alt" aria-hidden="true"></i> Short Resume (1-Page PDF)</a>
  <a href="{{ base_path }}/thesis/" class="btn btn--inverse"><i class="fa fa-graduation-cap" aria-hidden="true"></i> Explore PhD Thesis</a>
</p>

---

## Research Themes

* **Generative & Diffusion Models for Synthetic Data:** Controlled face synthesis via diffusion models and GANs (**FaVGen**, **BALPortraits**), latent trajectory morphing for identity anonymization (DiffMorpher), and continuous flow-matching diffusion models to disentangle common vs. salient visual factors (**Diff-CA**, *NeurIPS 2026 Spotlight*).
* **Statistical & Latent-Space Auditing of AI Fairness:** Moving beyond threshold-fragile scalar fairness metrics by combining logistic/OLS **Average Marginal Effects (AME)**, **SIMEX measurement-error correction**, and **ANOVA on hyperspherical latent spaces** (**FaVFA**, APP-registered software deposit).
* **Reliable & Frugal Demographic Inference:** Theoretical characterization of how annotator noise biases fairness estimators, web-scale dataset curation via **Iterative Proportional Fitting (IPF)** on WebFace42M (**WEG**), and transfer learning on **von Mises-Fisher (vMF)** face representations (**REGI-Face**, integrated in the European Vanguard Project).
* **Cross-Domain Bias & Robustness:** Probing implicit intersectional stereotypes in **16 Vision-Language Models (VLMs)** via indirect casting pretexts (*WACV 2027*), temporal multi-view teacher-student distillation for **weakly supervised 3D object detection** (**MVAT**, *WACV 2026*), and information-theoretic **User Coherence** in large-scale recommender systems (*WWW 2026*).

---

## News & Highlights

* **2026 — WACV 2027 Accepted:** *"Portrait Fitness as a Pretext: Probing Implicit Demographic Bias in VLMs"* (introducing the 9,000-portrait **BALPortraits** benchmark and auditing 16 VLMs).
* **2026 — NeurIPS 2026 Spotlight & Top Reviewer:** *"Diff-CA: Separating Common and Salient Factors with Diffusion Models"* accepted as a **Spotlight** at NeurIPS 2026; recognized as a **NeurIPS 2026 Top Reviewer**.
* **2026 — European Vanguard Integration:** **REGI-Face Toolkit** packaged and integrated into the European Vanguard project for high-throughput, frugal demographic analysis.
* **2026 — WWW 2026 Accepted:** *"Quantifying User Coherence: A Unified Framework for Analyzing Recommender Systems Across Domains"* published in the Proceedings of the ACM Web Conference 2026.
* **2026 — WACV 2026 Accepted:** *"MVAT: Multi-View Aware Teacher for Weakly Supervised 3D Object Detection"* published at IEEE/CVF WACV 2026.
* **2025 — WACV 2025 & APP Deposit:** *"Fairer Analysis and Demographically Balanced Face Generation for Fairer Face Verification"* published at IEEE/CVF WACV 2025; **FaVFA** officially registered with the *Agence pour la Protection des Programmes* (`IDDN.FR.001.160022.000.S.P.2025.000.31235`).

---

## Selected Publications

1. **Portrait Fitness as a Pretext: Probing Implicit Demographic Bias in VLMs**  
   **A. Fournier-Montgieux**, H. Le Borgne, A. Popescu, B. Luvison — *IEEE/CVF WACV 2027*  
   [[PDF]({{ base_path }}/files/BALportrait.pdf)] [[Details]({{ base_path }}/publication/2026-09-01-portrait-fitness-pretext-vlm-bias)]
2. **Diff-CA: Separating Common and Salient Factors with Diffusion Models**  
   M. Soumm, **A. Fournier-Montgieux**, Y. He, P. Gori, A. Newson — *NeurIPS 2026 (Spotlight)*  
   [[arXiv](https://arxiv.org/abs/2606.06120)] [[Details]({{ base_path }}/publication/2026-06-06-diff-ca-diffusion-models)]
3. **Quantifying User Coherence: A Unified Framework for Analyzing Recommender Systems Across Domains**  
   M. Soumm\*, **A. Fournier-Montgieux**\*, A. Popescu, B. Delezoide — *ACM Web Conference (WWW) 2026*  
   [[ACM DOI](https://dl.acm.org/doi/10.1145/3774904.3792563)] [[PDF]({{ base_path }}/files/Quantifying.pdf)] [[Details]({{ base_path }}/publication/2026-04-13-quantifying-user-coherence)]
4. **MVAT: Multi-View Aware Teacher for Weakly Supervised 3D Object Detection**  
   S. Lahlali, **A. Fournier-Montgieux**, N. Granger, H. Le Borgne, Q.-C. Pham — *IEEE/CVF WACV 2026*  
   [[CVF OpenAccess](https://openaccess.thecvf.com/content/WACV2026/papers/Lahlali_MVAT_Multi-View_Aware_Teacher_for_Weakly_Supervised_3D_Object_Detection_WACV_2026_paper.pdf)] [[PDF]({{ base_path }}/files/MVAT.pdf)] [[Details]({{ base_path }}/publication/2026-03-01-mvat-weakly-supervised-3d-detection)]
5. **Reliable and Reproducible Demographic Inference for Fairness in Face Analysis (REDI-Face & REGI-Face)**  
   **A. Fournier-Montgieux**, H. Le Borgne, A. Popescu, B. Luvison — *arXiv 2025 / Under Review*  
   [[arXiv](https://arxiv.org/abs/2510.20482)] [[REDI PDF]({{ base_path }}/files/REDI_FACE.pdf)] [[REGI PDF]({{ base_path }}/files/REGI_Face__WACV_2026.pdf)] [[Details]({{ base_path }}/publication/2025-10-20-redi-face-demographic-inference)]
6. **Fairer Analysis and Demographically Balanced Face Generation for Fairer Face Verification**  
   **A. Fournier-Montgieux**\*, M. Soumm\*, A. Popescu, B. Luvison, H. Le Borgne — *IEEE/CVF WACV 2025*  
   [[CVF OpenAccess](https://openaccess.thecvf.com/content/WACV2025/html/Fournier-Montgieux_Fairer_Analysis_and_Demographically_Balanced_Face_Generation_for_Fairer_Face_WACV_2025_paper.html)] [[PDF]({{ base_path }}/files/fairer_analysis_face.pdf)] [[FaVGen Code](https://github.com/CEA-LIST/FaVGen)] [[FaVFA Code](https://github.com/CEA-LIST/FaVFA)] [[Details]({{ base_path }}/publication/2025-02-28-fairer-analysis-face-verification)]

