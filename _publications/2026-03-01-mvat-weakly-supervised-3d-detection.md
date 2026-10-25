---
title: "MVAT: Multi-View Aware Teacher for Weakly Supervised 3D Object Detection"
collection: publications
category: conferences
permalink: /publication/2026-03-01-mvat-weakly-supervised-3d-detection
excerpt: "Temporal multi-view point-cloud aggregation and curriculum Teacher-Student distillation for 3D object detection from weak 2D bounding-box supervision on nuScenes and Waymo."
date: 2026-03-01
venue: "Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2026)"
paperurl: "/files/MVAT.pdf"
bibtexurl: "/files/publications.bib"
citation: "Lahlali, S., Fournier-Montgieux, A., Granger, N., Le Borgne, H., &amp; Pham, Q.-C. (2026). &quot;MVAT: Multi-View Aware Teacher for Weakly Supervised 3D Object Detection.&quot; <i>IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)</i>."
---

{% include base_path %}

**Authors:** Saad Lahlali, Alexandre Fournier-Montgieux, Nicolas Granger, Hervé Le Borgne, Quoc-Cuong Pham  
**Venue:** IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2026)  

<p>
  <a href="https://openaccess.thecvf.com/content/WACV2026/papers/Lahlali_MVAT_Multi-View_Aware_Teacher_for_Weakly_Supervised_3D_Object_Detection_WACV_2026_paper.pdf" class="btn btn--primary">CVF OpenAccess</a>
  <a href="{{ base_path }}/files/MVAT.pdf" class="btn btn--info">Download PDF</a>
</p>

## Abstract

Annotating 3D data remains a costly bottleneck for 3D object detection, motivating the development of weakly supervised annotation methods that rely on more accessible 2D box annotations. However, relying solely on 2D boxes introduces projection ambiguities since a single 2D box can correspond to multiple valid 3D poses. Furthermore, partial object visibility under a single viewpoint setting makes accurate 3D box estimation difficult. We propose **MVAT**, a novel framework that leverages temporal multi-view information present in sequential data to address these challenges. Our approach aggregates object-centric point clouds across time to build 3D object representations as dense and complete as possible. A Teacher-Student distillation paradigm is employed: the Teacher network generates high-quality pseudo-labels from temporally aggregated static objects, which the Student learns to predict from a single viewpoint for both static and moving objects, guided by a multi-view 2D projection loss. Experiments on the **nuScenes** and **Waymo Open** datasets demonstrate state-of-the-art performance for weakly supervised 3D object detection, significantly narrowing the gap with fully supervised methods without requiring any 3D box annotations.
