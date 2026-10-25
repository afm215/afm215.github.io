---
title: "Fairer Analysis and Demographically Balanced Face Generation for Fairer Face Verification"
collection: publications
category: conferences
permalink: /publication/2025-02-28-fairer-analysis-face-verification
excerpt: "Controlled diffusion-based face generation pipeline (FaVGen) and statistical bias decomposition framework (FaVFA) using logistic regression marginal effects and latent-space ANOVA."
date: 2025-02-28
venue: "Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2025)"
paperurl: "/files/fairer_analysis_face.pdf"
bibtexurl: "/files/publications.bib"
citation: "Fournier-Montgieux, A., Soumm, M., Popescu, A., Luvison, B., &amp; Le Borgne, H. (2025). &quot;Fairer Analysis and Demographically Balanced Face Generation for Fairer Face Verification.&quot; <i>IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)</i>."
---

{% include base_path %}

**Authors:** Alexandre Fournier-Montgieux\*, Michaël Soumm\*, Adrian Popescu, Bertrand Luvison, Hervé Le Borgne (*equal contribution*)  
**Venue:** IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2025)  

<p>
  <a href="https://openaccess.thecvf.com/content/WACV2025/html/Fournier-Montgieux_Fairer_Analysis_and_Demographically_Balanced_Face_Generation_for_Fairer_Face_WACV_2025_paper.html" class="btn btn--primary">CVF OpenAccess</a>
  <a href="{{ base_path }}/files/fairer_analysis_face.pdf" class="btn btn--info">Download PDF</a>
  <a href="https://github.com/CEA-LIST/FaVGen" class="btn btn--inverse">FaVGen Code &amp; Data</a>
  <a href="https://github.com/CEA-LIST/FaVFA" class="btn btn--inverse">FaVFA Auditing Toolkit</a>
</p>

## Abstract

Face recognition and verification are two computer vision tasks whose performances have advanced with the introduction of deep representations. However, ethical, legal, and technical challenges due to the sensitive nature of face data and biases in real-world training datasets hinder their development. Generative AI addresses privacy by creating fictitious identities, but fairness problems remain. Using the existing DCFace SOTA framework, we introduce a new controlled generation pipeline that improves fairness. Through classical fairness metrics and a proposed in-depth statistical analysis based on logit models and ANOVA, we show that our generation pipeline improves fairness more than other bias mitigation approaches while slightly improving raw performance.

![Controlled Synthetic Generation Pipeline (FaVGen)]({{ base_path }}/images/research/favgen_pipeline.png)

## Key Contributions

* **Controlled Synthetic Generation (`FaVGen`):** Filters identity collisions and visual artifacts in diffusion-generated ID images, balances demographic segments ($$\text{DCFace}+\text{C}_{ge}$$), and diversifies age and head pose through style-bank selection ($$\text{DCFace}+\text{C}_{all}$$).
* **Statistical Bias Decomposition (`FaVFA`):** Introduces logistic regression with Average Marginal Effects (AME) and latent-space ANOVA on pairwise embedding distances to disentangle direct demographic bias from confounding covariates (pose, age). Officially registered with the *Agence pour la Protection des Programmes* (APP Deposit `IDDN.FR.001.160022.000.S.P.2025.000.31235`).
