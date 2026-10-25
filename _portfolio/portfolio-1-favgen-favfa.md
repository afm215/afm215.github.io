---
title: "FaVGen & FaVFA: Controlled Synthetic Face Generation & Statistical Fairness Auditing"
excerpt: "Open-source diffusion control pipeline for generating over 1M balanced synthetic face images (FaVGen) and APP-registered statistical bias auditing framework (FaVFA).<br/><img src='/images/research/favgen_pipeline.png' style='max-width: 550px; margin-top: 10px;'>"
collection: portfolio
---

{% include base_path %}

* **FaVGen ([GitHub: CEA-LIST/FaVGen](https://github.com/CEA-LIST/FaVGen)):** Controlled diffusion-based generation framework built atop DCFace to synthesize over 1 million demographically balanced face verification training images ($$\text{DCFace}+\text{C}_{ge}$$ and $$\text{DCFace}+\text{C}_{all}$$), jointly balancing identity-level demographics and image-level age and head pose.
* **FaVFA ([GitHub: CEA-LIST/FaVFA](https://github.com/CEA-LIST/FaVFA)):** End-to-end statistical bias decomposition toolkit combining logistic regression **Average Marginal Effects (AME)** and **ANOVA on latent-space cosine distances** (WACV 2025).
* **Software Protection Registration:** Formally registered with the *Agence pour la Protection des Programmes* (**APP Deposit N° `IDDN.FR.001.160022.000.S.P.2025.000.31235`**).

![UMAP Representation & Latent Space Analysis]({{ base_path }}/images/research/favfa_umap.png)
