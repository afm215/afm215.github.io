---
title: "Portrait Fitness as a Pretext: Probing Implicit Demographic Bias in VLMs"
collection: publications
category: conferences
permalink: /publication/2026-09-01-portrait-fitness-pretext-vlm-bias
excerpt: "Auditing 16 frontier and open-weight Vision-Language Models on BALPortraits (9,000 fictional portraits across 24 ethnicity-gender-age segments) using an indirect advertising-casting pretext."
date: 2026-09-01
venue: "Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2027)"
paperurl: "/files/BALportrait.pdf"
bibtexurl: "/files/publications.bib"
citation: "Fournier-Montgieux, A., Le Borgne, H., Popescu, A., &amp; Luvison, B. (2027). &quot;Portrait Fitness as a Pretext: Probing Implicit Demographic Bias in VLMs.&quot; <i>IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2027)</i>."
---

{% include base_path %}

**Authors:** Alexandre Fournier-Montgieux, Hervé Le Borgne, Adrian Popescu, Bertrand Luvison  
**Venue:** IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2027)  

<p>
  <a href="{{ base_path }}/files/BALportrait.pdf" class="btn btn--primary">Download PDF</a>
  <a href="{{ base_path }}/files/publications.bib" class="btn btn--inverse">Download BibTeX</a>
</p>

## Abstract

We audit face-related bias in Vision-Language Models (VLMs) using **BALPortraits**, a new balanced dataset of **9,000 fictional portraits** across 24 ethnicity, gender, and age segments. Sixteen VLMs estimate portrait fitness scores for occupations, brands, activities, and banking or insurance products within an advertising-casting framework designed to avoid direct inference of protected attributes. Item-level estimations are aggregated with scenario-specific prestige scores to compare rankings across demographic groups. While the magnitude and direction of these biases vary across scenarios, model families, and demographic dimensions—with age, ethnicity, and gender contributing differently depending on the task—we find demographic dispersion across all evaluated models, with a majority of pairwise segment differences reaching statistical significance. This study introduces a controlled protocol to assess implicit face-related associations and demonstrates that single-scenario or single-attribute audits are insufficient.

![Top- and Bottom-Ranked Portraits in BALPortraits VLM Audit]({{ base_path }}/images/research/balportraits_teaser.png)

![Overview of the BALPortraits VLM Auditing Framework]({{ base_path }}/images/research/balportraits_overview.png)
