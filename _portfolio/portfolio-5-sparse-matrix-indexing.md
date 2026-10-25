---
title: "High-Performance Sparse Matrix Optimization: Dynamic int32/int64 Indexing in SciPy (WWW 2026)"
excerpt: "Recompiled SciPy so that sparse matrices switch their index encoding dynamically between int32 and int64, making ultra-large item co-occurrence and conditional entropy computations fit in RAM for the WWW 2026 user coherence study.<br/><img src='/images/research/sparse_indexing_teaser.png' style='max-width: 550px; margin-top: 10px;'>"
collection: portfolio
---

{% include base_path %}

<p>
  <a href="{{ base_path }}/publication/2026-04-13-quantifying-user-coherence" class="btn btn--primary">Paper Details</a>
  <a href="{{ base_path }}/files/Quantifying.pdf" class="btn btn--info">Download PDF</a>
</p>

![User-item interactions, item co-occurrence graph and CS(u), computed with sparse matrices whose indices switch from int32 to int64 on demand]({{ base_path }}/images/research/sparse_indexing_teaser.png)

* **Problem:** Cross-domain user coherence and conditional surprise estimation ($$CS(u)$$) across 9 large-scale recommendation datasets requires ultra-large item co-occurrence and conditional entropy matrices, whose memory and runtime costs became the bottleneck of the study.
* **Dynamic Index Encoding:** Recompiled **SciPy** so that sparse matrices switch their index encoding dynamically, keeping compact `int32` indices when they suffice and promoting to `int64` only when sizes require it.
* **Outcome:** Made these computations fit within tight RAM constraints for the *Quantifying User Coherence* paper (WWW 2026).
