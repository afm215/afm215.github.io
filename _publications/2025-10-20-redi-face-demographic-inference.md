---
title: "Reliable and Reproducible Demographic Inference for Fairness in Face Analysis"
collection: publications
category: manuscripts
permalink: /publication/2025-10-20-redi-face-demographic-inference
excerpt: "Theoretical proof of how demographic annotator error biases fairness audits, coupled with the IPF-balanced WEG dataset and REGI-Face (vMF + RBF-SVM transfer learning annotator)."
date: 2025-10-20
venue: "arXiv preprint arXiv:2510.20482 (and companion paper Reliable Face Ethnicity and Gender Inference)"
paperurl: "/files/REDI_FACE.pdf"
bibtexurl: "/files/publications.bib"
citation: "Fournier-Montgieux, A., Le Borgne, H., Popescu, A., &amp; Luvison, B. (2025). &quot;Reliable and Reproducible Demographic Inference for Fairness in Face Analysis.&quot; <i>arXiv:2510.20482</i>."
---

{% include base_path %}

**Authors:** Alexandre Fournier-Montgieux, Hervé Le Borgne, Adrian Popescu, Bertrand Luvison  
**Preprint & Companion Manuscript:** `arXiv:2510.20482` (*REDI-Face*) & *Reliable Face Ethnicity and Gender Inference* (*REGI-Face*)  

<p>
  <a href="https://arxiv.org/abs/2510.20482" class="btn btn--primary">arXiv:2510.20482</a>
  <a href="{{ base_path }}/files/REDI_FACE.pdf" class="btn btn--info">Download REDI-Face PDF</a>
  <a href="{{ base_path }}/files/REGI_Face__WACV_2026.pdf" class="btn btn--info">Download REGI-Face PDF</a>
</p>

## Abstract

Fairness evaluation in face analysis systems (FAS) uses automatic demographic attribute inference (DAI), which in turn relies on predefined demographic segmentation. However, the validity of fairness auditing hinges on the reliability of the DAI process, a dependency we prove theoretically—and assert empirically—by showing that improved DAI reliability leads to less biased, lower-variance estimates of FAS fairness. We revisit DAI by proposing **REDI-Face** / **REGI-Face**, a fully reproducible ethnicity and gender prediction pipeline that combines curated, diversified training and test datasets (**WEG**, built via Iterative Proportional Fitting on WebFace42M) with a transfer-learning architecture pairing pretrained face recognition encoders and theoretically motivated **RBF-SVM** classification heads over **von Mises-Fisher (vMF)** hyperspherical embeddings. We audit this pipeline across three dimensions: accuracy, fairness, and intra-identity robustness (**HomE**, **MiMA**, **MaMA**), outperforming seven competitive baselines (including FairFace and generalist VLMs) by 7 to 10 accuracy points on ethnicity while at least doubling fairness and robustness.

![REGI-Face Architecture and Evaluation]({{ base_path }}/images/research/regi_pipeline.png)
