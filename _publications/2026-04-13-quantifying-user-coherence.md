---
title: "Quantifying User Coherence: A Unified Framework for Analyzing Recommender Systems Across Domains"
collection: publications
category: conferences
permalink: /publication/2026-04-13-quantifying-user-coherence
excerpt: "Information-theoretic Mean Surprise S(u) and Mean Conditional Surprise CS(u) explaining user-level performance disparities across 7 recommendation architectures and 9 datasets."
date: 2026-04-13
venue: "Proceedings of the ACM Web Conference 2026 (WWW '26)"
paperurl: "/files/Quantifying.pdf"
bibtexurl: "/files/publications.bib"
citation: "Soumm, M., Fournier-Montgieux, A., Popescu, A., &amp; Delezoide, B. (2026). &quot;Quantifying User Coherence: A Unified Framework for Analyzing Recommender Systems Across Domains.&quot; <i>Proceedings of the ACM Web Conference 2026 (WWW &apos;26)</i>. DOI: 10.1145/3774904.3792563."
---

{% include base_path %}

**Authors:** Michaël Soumm\*, Alexandre Fournier-Montgieux\*, Adrian Popescu, Bertrand Delezoide (*equal contribution*)  
**Venue:** Proceedings of the ACM Web Conference 2026 (WWW '26), Dubai, UAE  

<p>
  <a href="https://dl.acm.org/doi/10.1145/3774904.3792563" class="btn btn--primary">ACM Digital Library (DOI)</a>
  <a href="{{ base_path }}/files/Quantifying.pdf" class="btn btn--info">Download PDF</a>
</p>

## Abstract

The performance of Recommender Systems (RS) varies significantly across users, yet the underlying reasons for this variance remain poorly understood. This paper introduces a unified framework to analyze and explain this performance gap by quantifying user profile characteristics. We propose two novel, information-theoretic measures: **Mean Surprise** \\(S(u)\\), which captures a user's deviation from popular items and is closely related to popularity bias, and **Mean Conditional Surprise** \\(CS(u)\\), which measures the internal coherence of a user's interactions in a domain-agnostic manner. Through extensive experiments on 7 algorithms and 9 datasets, we demonstrate that these measures are strong predictors of recommendation performance. Our analysis reveals that performance gains from complex models are concentrated on "coherent" users, while all algorithms perform poorly on "incoherent" users. We show how these measures provide practical utility for the Web community by: (1) enabling robust, stratified evaluation to identify model weaknesses; (2) facilitating a novel analysis of the behavioral alignment of recommendations; and (3) guiding targeted system design, validated by training a specialized model on coherent users that achieves superior performance with significantly less data.

![Recall@20 Stratified by User Coherence]({{ base_path }}/images/research/user_coherence_recall.png)
