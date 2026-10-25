---
layout: single
title: "PhD Thesis: Auditing and Mitigating Demographic Bias in Face Analysis & Vision-Language Systems"
permalink: /thesis/
author_profile: true
---

{% include base_path %}

![Auditing and Mitigating Demographic Bias in Face Images — Université Paris-Saclay & CEA]({{ base_path }}/images/research/thesis_banner.png)

<p>
  {% comment %} TEMPORARY: manuscript not yet officially validated. Restore this link once publication is approved:
  <a href="{{ base_path }}/files/PhD_Thesis_Alexandre_Fournier_Montgieux.pdf" class="btn btn--primary"><i class="fa fa-file-pdf" aria-hidden="true"></i> Download PhD Manuscript (PDF)</a>
  {% endcomment %}
  <span class="btn btn--primary btn--disabled" aria-disabled="true" title="The manuscript is pending official validation for publication"><i class="fa fa-file-pdf" aria-hidden="true"></i> PhD Manuscript (PDF) — Coming Soon</span>
  <a href="{{ base_path }}/files/publications.bib" class="btn btn--inverse"><i class="fa fa-book" aria-hidden="true"></i> Download BibTeX</a>
</p>

**Coming soon:** the manuscript has not yet been officially validated for publication. The PDF will be made available here once it is approved.
{: .notice--info}

**Institution:** Université Paris-Saclay & CEA LIST (Nano-INNOV, Palaiseau, France)  
**Period:** November 2023 – November 2026  
**Supervision & Collaborators:** Hervé Le Borgne, Adrian Popescu, Bertrand Luvison  

---

## Abstract

Deep face recognition (FR) systems owe their accuracy to ever larger models and training corpora, and therefore inherit the structure and imbalance of these corpora. Their error rates differ systematically across gender, ethnicity, and age, with documented consequences ranging from authentication failures to wrongful arrests, while data-protection regulation increasingly restricts access to the real face data needed to study and correct these disparities. This thesis treats demographic bias primarily as a property of the data and addresses three questions: can training-data composition be modified to reduce bias without degrading accuracy, how far do imperfect demographic labels distort a fairness audit, and do these conclusions transfer beyond face verification?

We first assemble a statistical toolbox for face verification audits that complements classical fairness metrics, which saturate at strict operating thresholds and become unstable on small cohorts, with an ANOVA decomposition of embedding distances and a regression-based marginal-effect analysis. Applied to models trained on real corpora, it shows that demographically balancing the training data improves fairness at the cost of raw accuracy on standard benchmarks. We then compare loss weighting, re-sampling, and a controlled diffusion-based generation pipeline that balances identity demographics while diversifying pose and age: controlled generation yields the largest reduction of ethnicity-related bias without degrading accuracy relative to uncontrolled synthetic data, although a gap with real-data training remains.

Because every audit depends on demographic labels, we next study the annotators themselves. We prove that plug-in disparity estimators are biased by annotator errors, propose a corrected estimator, and show that widely used annotators are inaccurate, fragile, and difficult to reproduce. We address this gap with WEG, a diversified dataset sampled from WebFace42M, and REGI, an annotator combining a frozen FR backbone with an RBF-SVM head motivated by the von Mises–Fisher geometry of angular-margin embeddings, which improves accuracy, fairness, and robustness over seven baselines. Moving beyond verification, we introduce BALPortraits, 9,000 anonymised portraits balanced over 24 ethnicity–gender–age segments, and audit 16 vision-language models on an indirect casting task: biases are intersectional and context-dependent, and omitting appearance controls can invert the sign of demographic effects. Finally, by contrasting 3D object detection and recommender systems, we place demographic bias in faces on a spectrum of group definability, between classes given by the task and groups that must be constructed from behaviour.

Together, these contributions argue that a credible fairness audit requires controlled data, explicit statistical control of confounders, and an audit of the annotator itself.

![Face Recognition & Fairness Pipeline]({{ base_path }}/images/research/fr_banner.png)

---

## Manuscript Structure & Roadmap

![PhD Manuscript Structure & Workflow Across Chapters]({{ base_path }}/images/research/thesis_roadmap.png)

### Chapter-by-Chapter Breakdown

#### Chapters 1 & 2 — Introduction, Regulatory Context & Technical Background
- Reviews documented demographic disparities in commercial and academic face analysis alongside legal frameworks (**GDPR Article 9**, **EU AI Act**, **Illinois BIPA**) and the retraction of unconsented web-scraped benchmarks (MS-Celeb-1M, MegaFace).
- Connects **neural scaling laws** and over-parameterized convergence under the **Polyak–Łojasiewicz ($$\mathrm{PL}^\star$$) condition** to demographic bias: high-capacity models interpolating imbalanced web corpora inevitably inherit and amplify majority-group representations.
- Surveys hyperspherical face recognition losses (CosFace, ArcFace, AdaFace), evaluation datasets, classical fairness metrics, demographic attribute inference (DAI), and synthetic face generators.

#### Chapter 3 — Statistical Tools for Demographic Bias Analysis in Face Verification
- Establishes an **information-theoretic lower bound** showing how test-set characteristics impose a structural floor on classical fairness metrics.
- Formulates **ANOVA on pairwise cosine distances** in the hyperspherical representation space to measure how demographic attributes structure latent geometry independently of any operating threshold.
- Introduces **Average Marginal Effects (AME)** via logistic and OLS regression with **SIMEX** measurement-error correction to decorrelate gender, ethnicity, age, and head-pose effects on verification outcomes.

#### Chapter 4 — Mitigating Demographic Bias in Face Recognition Training Data *(WACV 2025)*
- Benchmarks loss reweighting and resampling on real corpora (CASIA-WebFace, BUPT-Balancedface) against synthetic training sets (DigiFace, DCFace).
- Introduces **FaVGen** ($$\text{DCFace}+\text{C}_{ge}$$ and $$\text{DCFace}+\text{C}_{all}$$), filtering identity collisions and jointly balancing demographic segments, age, and head pose via style-bank matching.
- Demonstrates through classical metrics, AME, and latent-space ANOVA that controlled synthetic generation improves fairness more effectively than post-hoc reweighting while preserving or improving verification accuracy.

#### Chapter 5 — Why Annotator Reliability Matters: A Diagnostic Framework *(arXiv 2025 / REDI)*
- Introduces taxonomy-agnostic intra-identity consistency metrics (**HomE**, **MiMA**, **MaMA**) to evaluate demographic annotator robustness across varying pose, lighting, and expression.
- Proves **Proposition 1 (Bias of the Plug-In Fairness Estimator)**: relates the expected error of downstream fairness metrics (DoB, DPD/DPR, EOD/EOR) directly to the annotator's confusion matrix $$C$$.
- Exposes a major reproducibility and accuracy gap in widely used off-the-shelf annotators (FairFace, DeepFace, FaceXFormer) on RFW and BFW.

#### Chapter 6 — WEG and REGI: A Diversified Dataset for a Theoretically-Grounded Demographic Annotator *(REGI-Face)*
- Constructs the **WEG** dataset from WebFace42M using identity-level majority voting with theoretical error bounds and **Iterative Proportional Fitting (IPF)** across fine-grained ethnicity and gender intersections.
- Proves that because angular-margin face recognition encoders distribute identity embeddings according to **von Mises-Fisher (vMF) mixtures** on the unit hypersphere, the Bayes-optimal decision boundary between demographic mixture components corresponds to an **RBF kernel SVM** head.
- Validates **REGI-Face** against 7 baselines (including generalist VLMs), achieving +7 to +10 accuracy points on ethnicity and doubling robustness and fairness, while introducing a **James–Stein regularized corrected estimator $$\hat{p}^{(\mathrm{corr})}_{\mathrm{reg}}$$** for downstream audits.

#### Chapter 7 — Beyond Face Recognition: Balanced Portrait Composition for Auditing VLMs *(WACV 2027)*
- Builds **BALPortraits**, a balanced, anonymized dataset of **9,000 fictional portraits** spanning 24 intersectional ethnicity $$\times$$ gender $$\times$$ age segments with rich facial appearance annotations and DiffMorpher anonymization guarantees.
- Audits **16 frontier and open-weight VLMs** across 4 indirect advertising-casting scenarios (100 occupations, 50 brands, activities, and financial products) combined with external prestige scores.
- Reveals through rank-based non-parametric tests and robust marginal-effect regressions that all 16 VLMs exhibit statistically significant, context-dependent intersectional biases that single-attribute or single-scenario audits fail to capture.

#### Chapter 8 — Opening: On the Challenge to Define Bias Across Multiple Domains *(WACV 2026 & WWW 2026)*
- Positions face demographic fairness along a broader **spectrum of subgroup definability**:
  - *Natural semantic groups in 3D perception:* **MVAT** (*WACV 2026*) uses temporal multi-view point-cloud aggregation and teacher-student distillation to mitigate visibility and projection biases in weakly supervised 3D object detection on nuScenes and Waymo.
  - *Constructed behavioral groups in recommender systems:* **Quantifying User Coherence** (*WWW 2026*) introduces information-theoretic **Mean Surprise $$S(u)$$** and **Mean Conditional Surprise $$CS(u)$$**, demonstrating across 7 algorithms and 9 datasets that model gains concentrate on coherent users while all architectures collapse on incoherent profiles.
