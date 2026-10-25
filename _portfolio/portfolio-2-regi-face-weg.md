---
title: "REGI-Face Toolkit & WEG Dataset: Frugal Demographic Inference (European Vanguard Project)"
excerpt: "Modular Python library pairing vMF face recognition backbones with theoretically optimal RBF-SVM heads on the IPF-balanced WEG corpus; integrated into the European Vanguard project.<br/><img src='/images/research/regi_teaser.png' style='max-width: 550px; margin-top: 10px;'>"
collection: portfolio
---

{% include base_path %}

* **REGI-Face Toolkit:** Engineered and packaged a modular, frugal Python library for high-throughput demographic attribute inference (ethnicity & gender) integrated into the **European Vanguard Project** (2026).
* **Theoretical Grounding:** Leverages pretrained angular-margin face recognition encoders whose identity representations follow **von Mises-Fisher (vMF)** distributions on the unit hypersphere, proving that an **RBF-SVM** classification head yields the optimal non-linear decision boundary across demographic mixture components.
* **WEG Dataset & IPF Curation:** Processed and filtered the 42-million-image **WebFace42M** corpus with high-throughput streaming pipelines and **Iterative Proportional Fitting (IPF)** to construct balanced training and evaluation benchmarks.
* **Bias-Corrected Fairness Estimator:** Implements the James–Stein regularized corrected estimator $$\hat{p}^{(\mathrm{corr})}_{\mathrm{reg}}$$ to remove annotator-induced distortion from downstream fairness audits.

![REGI-Face Architecture]({{ base_path }}/images/research/regi_pipeline.png)
