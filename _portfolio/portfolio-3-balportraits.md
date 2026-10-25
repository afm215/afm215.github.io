---
title: "BALPortraits Dataset: Balanced Fictional Portraits for Intersectional VLM Bias Auditing (Release Coming Soon)"
excerpt: "Upcoming public release of BALPortraits, a balanced, anonymized dataset of 9,000 fictional portraits across 24 ethnicity-gender-age segments, introduced at WACV 2027 to audit implicit bias in 16 VLMs.<br/><img src='/images/research/balportraits_teaser.png' style='max-width: 550px; margin-top: 10px;'>"
collection: portfolio
---

{% include base_path %}

> **Release status:** the BALPortraits dataset is being prepared for public release. The dataset download link and the paper PDF will be added here once they are available.

<p>
  <a href="{{ base_path }}/publication/2026-09-01-portrait-fitness-pretext-vlm-bias" class="btn btn--primary">Paper Details</a>
  <span class="btn btn--info btn--disabled">PDF Coming Soon</span>
</p>

* **Dataset Content:** **9,000 fictional portraits** evenly balanced across 24 intersectional ethnicity $$\times$$ gender $$\times$$ age segments, with rich facial appearance annotations.
* **Construction & Anonymization:** Scaled diffusion-based latent trajectory morphing (**DiffMorpher**) and text-driven generation to synthesize hundreds of thousands of candidate faces, then curated the final set with verified identity-anonymization guarantees.
* **Intended Use:** Built to support the indirect advertising-casting auditing protocol of the paper (100 occupations, 50 brands, activities, and financial products weighted by external prestige scores), which surfaces implicit demographic associations in **16 frontier and open-weight VLMs** without triggering refusal guardrails.

![BALPortraits VLM Auditing Overview]({{ base_path }}/images/research/balportraits_overview.png)
