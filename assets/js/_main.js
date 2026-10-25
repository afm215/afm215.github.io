/* ==========================================================================
   Various functions that we want to use within the template
   ========================================================================== */

/*jslint es6 */
'use strict';

// Constants for CDNs
const PLOTLY_URL = "https://cdn.jsdelivr.net/npm/plotly.js@3.6.0/dist/plotly.min.js";
const MERMAID_URL = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";

// Detect OS/browser preference
const browserPref = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

// Determine the computed theme, which can be "dark" or "light".
function determineComputedTheme() {
  // Determine the expected state of the theme toggle, which can be "dark", "light", or default "system"
  let themeSetting = localStorage.getItem("theme");
  themeSetting = (themeSetting != "dark" && themeSetting != "light" && themeSetting != "system") ? "system" : themeSetting;

  // Return the setting if set, or use the browser preference
  if (themeSetting != "system") {
    return themeSetting;
  }
  return browserPref ? "dark" : "light";
}

// Set the theme on page load or when explicitly called. Without an argument the
// theme is the stored preference or, failing that, the OS/browser preference.
function setTheme(theme) {
  const use_theme = theme || determineComputedTheme();

  if (use_theme === "dark") {
    $("html").attr("data-theme", "dark");
    $("#theme-icon").removeClass("fa-sun").addClass("fa-moon");
  } else if (use_theme === "light") {
    $("html").removeAttr("data-theme");
    $("#theme-icon").removeClass("fa-moon").addClass("fa-sun");
  }
}

// Toggle the theme manually
function toggleTheme() {
  const current_theme = $("html").attr("data-theme");
  const new_theme = current_theme === "dark" ? "light" : "dark";
  localStorage.setItem("theme", new_theme);
  setTheme(new_theme);
  redrawPlotly();
}

// Defer the loading of Mermaid to only if there is a field on the page to be rendered
let mermaidElements = document.querySelectorAll("pre>code.language-mermaid");
if (mermaidElements.length > 0) {
  document.addEventListener("readystatechange", function() {
    // Append the Mermaid module to the DOM
    const moduleScript = document.createElement('script');
    moduleScript.type = 'module';
    moduleScript.textContent = `
      import mermaid from '${MERMAID_URL}';
      mermaid.initialize({startOnLoad:true, theme:'default'});
      await mermaid.run({querySelector:'code.language-mermaid'});
    `;
    document.body.appendChild(moduleScript);
  });
}

/* ==========================================================================
   Plotly integration script so that Markdown codeblocks will be rendered
   ========================================================================== */

// Read the Plotly data from the code block, hide it, and render the chart as new node. This allows for the
// JSON data to be retrieve when the theme is switched. The listener should only be added if the data is
// actually present on the page.
//
// NOTE that plotlyDarkLayout and plotlyLightLayout will be exposed in the minimized file
let plotlyElements = document.querySelectorAll("pre>code.language-plotly");
if (plotlyElements.length > 0) {
  document.addEventListener("readystatechange", function() {
    // Return if not ready
    if (document.readyState !== "complete") {
      return;
    }

    // Prepare to load Plotly from the CDN
    const script = document.createElement('script');
    script.src = PLOTLY_URL;
    script.async = true;

    // Once loaded, update the page elements to work with it
    script.onload = function() {
      plotlyElements.forEach(function(elem) {
        // Parse the Plotly JSON data and hide it
        let jsonData = JSON.parse(elem.textContent);
        elem.parentElement.classList.add("hidden");

        // Add the Plotly node
        let chartElement = document.createElement("div");
        elem.parentElement.after(chartElement);

        // Set the theme for the plot and render it
        const theme = (determineComputedTheme() === "dark") ? plotlyDarkLayout : plotlyLightLayout;
        if (jsonData.layout) {
          jsonData.layout.template = (jsonData.layout.template) ? { ...theme, ...jsonData.layout.template } : theme;
        } else {
          jsonData.layout = { template: theme };
        }
        Plotly.react(chartElement, jsonData.data, jsonData.layout);
      });
    }

    // Add the script to the document
    document.head.appendChild(script);
  });
}

function redrawPlotly() {
  plotlyElements.forEach(function(elem) {
    // Parse the Plotly JSON data
    let jsonData = JSON.parse(elem.textContent);

    // Get the Plotly node
    let chartElement = $(elem).parent().next().get(0);

    // Set the theme for the plot and render it
    const theme = (determineComputedTheme() === "dark") ? plotlyDarkLayout : plotlyLightLayout;
    if (jsonData.layout) {
      jsonData.layout.template = (jsonData.layout.template) ? { ...theme, ...jsonData.layout.template } : theme;
    } else {
      jsonData.layout = { template: theme };
    }
    Plotly.react(chartElement, jsonData.data, jsonData.layout);
  });
}

/* ==========================================================================
   3D von Mises-Fisher (vMF) Hypersphere Profile Picture Animation
   ========================================================================== */

const VmfAvatarAnimation = (function () {
  const TOTAL_DURATION_MS = 3000;
  const SPIN_END_MS = 1500;   // 0.0s -> 1.5s (50%)
  const ZOOM_END_MS = 2400;   // 1.5s -> 2.4s (30%)
  // 2.4s -> 3.0s (20%) reveal phase

  function clamp01(v) {
    return Math.max(0, Math.min(1, v));
  }

  function easeOutCubic(t) {
    const u = clamp01(t);
    return 1 - Math.pow(1 - u, 3);
  }

  function easeInOutCubic(t) {
    const u = clamp01(t);
    return u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2;
  }

  function normalize3(v) {
    const norm = Math.hypot(v[0], v[1], v[2]) || 1;
    return [v[0] / norm, v[1] / norm, v[2] / norm];
  }

  function cross3(a, b) {
    return [
      a[1] * b[2] - a[2] * b[1],
      a[2] * b[0] - a[0] * b[2],
      a[0] * b[1] - a[1] * b[0]
    ];
  }

  // Rotate 3D point: first around Y by rotY, then around X by rotX
  function rotatePoint(pt, rotX, rotY) {
    const cosY = Math.cos(rotY);
    const sinY = Math.sin(rotY);
    const x1 = pt[0] * cosY + pt[2] * sinY;
    const y1 = pt[1];
    const z1 = -pt[0] * sinY + pt[2] * cosY;

    const cosX = Math.cos(rotX);
    const sinX = Math.sin(rotX);
    const x2 = x1;
    const y2 = y1 * cosX - z1 * sinX;
    const z2 = y1 * sinX + z1 * cosX;

    return [x2, y2, z2];
  }

  // Compute rotation angles (rotX, rotY) that align unit vector mu to (0, 0, +1)
  function computeAligningAngles(mu) {
    const u = normalize3(mu);
    const rXZ = Math.hypot(u[0], u[2]);
    const targetRotY = -Math.atan2(u[0], u[2]);
    const targetRotX = Math.atan2(u[1], rXZ);
    return { rotX: targetRotX, rotY: targetRotY };
  }

  // Build tangent basis (u, v) orthogonal to unit vector mu
  function buildTangentBasis(mu) {
    const ref = Math.abs(mu[1]) < 0.85 ? [0, 1, 0] : [1, 0, 0];
    const u = normalize3(cross3(ref, mu));
    const v = normalize3(cross3(mu, u));
    return { u: u, v: v };
  }

  // Map spherical offset (theta polar angle from mu, phi azimuth) onto S^2
  function sphericalCapPoint(mu, basis, theta, phi) {
    const sinT = Math.sin(theta);
    const cosT = Math.cos(theta);
    const cosP = Math.cos(phi);
    const sinP = Math.sin(phi);
    return normalize3([
      cosT * mu[0] + sinT * (cosP * basis.u[0] + sinP * basis.v[0]),
      cosT * mu[1] + sinT * (cosP * basis.u[1] + sinP * basis.v[1]),
      cosT * mu[2] + sinT * (cosP * basis.u[2] + sinP * basis.v[2])
    ]);
  }

  // Build deterministic 3D hypersphere scene with 8 vMF components & geodesic wireframe
  function buildScene() {
    const rawComponents = [
      { mu: [0.42, -0.28, 0.86], kappa: 32, color: "#0ea5e9", darkColor: "#38bdf8", isTarget: true, label: "vMF(μ_AFM, κ)" },
      { mu: [-0.72, 0.38, 0.58], kappa: 24, color: "#e11d48", darkColor: "#fb7185", isTarget: false, label: "vMF(μ_2, κ)" },
      { mu: [0.68, 0.55, -0.48], kappa: 22, color: "#8b5cf6", darkColor: "#a78bfa", isTarget: false, label: "vMF(μ_3, κ)" },
      { mu: [-0.35, -0.78, 0.52], kappa: 26, color: "#10b981", darkColor: "#34d399", isTarget: false, label: "vMF(μ_4, κ)" },
      { mu: [0.15, 0.88, 0.45], kappa: 20, color: "#f59e0b", darkColor: "#fbbf24", isTarget: false, label: "vMF(μ_5, κ)" },
      { mu: [-0.82, -0.22, -0.53], kappa: 25, color: "#6366f1", darkColor: "#818cf8", isTarget: false, label: "vMF(μ_6, κ)" },
      { mu: [0.55, -0.62, -0.56], kappa: 24, color: "#14b8a6", darkColor: "#2dd4bf", isTarget: false, label: "vMF(μ_7, κ)" },
      { mu: [-0.18, 0.25, -0.95], kappa: 28, color: "#ec4899", darkColor: "#f472b6", isTarget: false, label: "vMF(μ_8, κ)" }
    ];

    const components = rawComponents.map(function (item, idx) {
      const mu = normalize3(item.mu);
      const basis = buildTangentBasis(mu);
      const points = [];
      const numPts = item.isTarget ? 22 : 16;

      for (let i = 0; i < numPts; i++) {
        // Golden-angle spiral + deterministic radial jitter concentrated around mu (cos(theta) > 0.94)
        const frac = (i + 0.5) / numPts;
        const theta = (item.isTarget ? 0.22 : 0.25) * Math.sqrt(frac);
        const phi = i * 2.399963229728653 + idx * 0.7;
        points.push(sphericalCapPoint(mu, basis, theta, phi));
      }

      // Concentric vMF density contour rings on S^2 (1-sigma and 2-sigma spherical caps)
      const rings = [0.12, 0.24].map(function (radiusRad) {
        const ringPts = [];
        const steps = 32;
        for (let s = 0; s <= steps; s++) {
          const phi = (s / steps) * Math.PI * 2;
          ringPts.push(sphericalCapPoint(mu, basis, radiusRad, phi));
        }
        return ringPts;
      });

      return {
        mu: mu,
        kappa: item.kappa,
        color: item.color,
        darkColor: item.darkColor,
        isTarget: item.isTarget,
        label: item.label,
        points: points,
        rings: rings
      };
    });

    // Geodesic latitude and longitude wireframe curves
    const wireframe = [];
    const latAngles = [-60, -30, 0, 30, 60];
    latAngles.forEach(function (deg) {
      const lat = (deg * Math.PI) / 180;
      const curve = [];
      const steps = 48;
      for (let i = 0; i <= steps; i++) {
        const lon = (i / steps) * Math.PI * 2;
        curve.push([
          Math.cos(lat) * Math.cos(lon),
          Math.sin(lat),
          Math.cos(lat) * Math.sin(lon)
        ]);
      }
      wireframe.push(curve);
    });

    const numMeridians = 6;
    for (let m = 0; m < numMeridians; m++) {
      const lon = (m / numMeridians) * Math.PI;
      const curve = [];
      const steps = 48;
      for (let i = 0; i <= steps; i++) {
        const angle = (i / steps) * Math.PI * 2;
        curve.push([
          Math.sin(angle) * Math.cos(lon),
          Math.cos(angle),
          Math.sin(angle) * Math.sin(lon)
        ]);
      }
      wireframe.push(curve);
    }

    const targetComp = components.find(function (c) { return c.isTarget; }) || components[0];
    const alignAngles = computeAligningAngles(targetComp.mu);

    return {
      components: components,
      wireframe: wireframe,
      targetAlign: alignAngles
    };
  }

  const defaultScene = buildScene();

  function computeTimelineState(elapsedMs, scene) {
    const activeScene = scene || defaultScene;
    const t = Math.max(0, elapsedMs);
    const targetRotX = activeScene.targetAlign.rotX;
    const targetRotY = activeScene.targetAlign.rotY;
    const startRotX = targetRotX - 0.85;
    const startRotY = targetRotY - Math.PI * 1.75;

    const spinRaw = clamp01(t / SPIN_END_MS);
    const spinEased = easeOutCubic(spinRaw);

    const rotX = startRotX + (targetRotX - startRotX) * spinEased;
    const rotY = startRotY + (targetRotY - startRotY) * spinEased;

    let phase = "spin";
    let zoomProgress = 0;
    let revealProgress = 0;
    let zoom = 1;
    let canvasOpacity = 1;
    let hudOpacity = 0;
    let facePreviewOpacity = 0;
    let done = false;

    if (t < SPIN_END_MS) {
      phase = "spin";
      // Fade in HUD lock badge during final 35% of spin phase
      hudOpacity = clamp01((spinRaw - 0.65) / 0.35);
    } else if (t < ZOOM_END_MS) {
      phase = "zoom";
      zoomProgress = clamp01((t - SPIN_END_MS) / (ZOOM_END_MS - SPIN_END_MS));
      const zoomEased = easeInOutCubic(zoomProgress);
      zoom = 1 + zoomEased * 4.5; // Reaches 5.5x at 2400ms
      hudOpacity = clamp01(1 - Math.max(0, (zoomProgress - 0.55) / 0.45));
      facePreviewOpacity = clamp01((zoomProgress - 0.25) / 0.75) * 0.85;
    } else if (t < TOTAL_DURATION_MS) {
      phase = "reveal";
      zoomProgress = 1;
      zoom = 5.5;
      revealProgress = clamp01((t - ZOOM_END_MS) / (TOTAL_DURATION_MS - ZOOM_END_MS));
      const revealEased = easeInOutCubic(revealProgress);
      canvasOpacity = 1 - revealEased;
      facePreviewOpacity = 0.85 + 0.15 * revealEased;
      hudOpacity = 0;
    } else {
      phase = "done";
      zoomProgress = 1;
      revealProgress = 1;
      zoom = 5.5;
      canvasOpacity = 0;
      facePreviewOpacity = 1;
      hudOpacity = 0;
      done = true;
    }

    return {
      phase: phase,
      spinProgress: spinRaw,
      zoomProgress: zoomProgress,
      revealProgress: revealProgress,
      rotX: rotX,
      rotY: rotY,
      zoom: zoom,
      canvasOpacity: canvasOpacity,
      hudOpacity: hudOpacity,
      facePreviewOpacity: facePreviewOpacity,
      done: done
    };
  }

  function shouldAutoPlay(pathname, basePath, reducedMotion) {
    if (reducedMotion) {
      return false;
    }
    const base = (basePath || "").replace(/\/+$/, "");
    let rel = pathname || "/";
    if (base && rel.indexOf(base) === 0) {
      rel = rel.slice(base.length) || "/";
    }
    return (
      rel === "/" ||
      rel === "/index.html" ||
      rel === "/about/" ||
      rel === "/about.html"
    );
  }

  function renderFrame(ctx, width, height, state, scene, imgElem, isDark) {
    ctx.clearRect(0, 0, width, height);
    const cx = width / 2;
    const cy = height / 2;
    const baseRadius = Math.min(width, height) * 0.39;
    const sphereRadius = baseRadius * state.zoom;

    ctx.save();
    // Clip to circular avatar boundary
    ctx.beginPath();
    ctx.arc(cx, cy, Math.min(width, height) * 0.5, 0, Math.PI * 2);
    ctx.clip();

    // 1. Background fill
    const bgGrad = ctx.createRadialGradient(cx, cy * 0.85, baseRadius * 0.1, cx, cy, Math.min(width, height) * 0.52);
    if (isDark) {
      bgGrad.addColorStop(0, "#1e293b");
      bgGrad.addColorStop(1, "#090d16");
    } else {
      bgGrad.addColorStop(0, "#f8fafc");
      bgGrad.addColorStop(1, "#e2e8f0");
    }
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, width, height);

    // Project 3D unit point onto 2D canvas
    function project(pt3) {
      const r = rotatePoint(pt3, state.rotX, state.rotY);
      const perspective = 2.6 / (2.6 - r[2] * 0.55);
      return {
        x: cx + r[0] * sphereRadius * perspective * 0.85,
        y: cy - r[1] * sphereRadius * perspective * 0.85,
        z: r[2],
        scale: perspective
      };
    }

    // 2. Sphere ambient glow & silhouette ring
    ctx.beginPath();
    ctx.arc(cx, cy, sphereRadius * 0.96, 0, Math.PI * 2);
    ctx.strokeStyle = isDark ? "rgba(148, 163, 184, 0.28)" : "rgba(71, 85, 105, 0.24)";
    ctx.lineWidth = 1.2;
    ctx.stroke();

    // 3. Geodesic wireframe curves
    const wireAlphaScale = clamp01(1 - state.zoomProgress * 0.65);
    scene.wireframe.forEach(function (curve) {
      for (let i = 1; i < curve.length; i++) {
        const p0 = project(curve[i - 1]);
        const p1 = project(curve[i]);
        const avgZ = (p0.z + p1.z) * 0.5;
        const depthAlpha = (avgZ > 0 ? 0.24 : 0.08) * wireAlphaScale;
        ctx.beginPath();
        ctx.moveTo(p0.x, p0.y);
        ctx.lineTo(p1.x, p1.y);
        ctx.strokeStyle = isDark
          ? "rgba(148, 163, 184, " + depthAlpha.toFixed(3) + ")"
          : "rgba(100, 116, 139, " + depthAlpha.toFixed(3) + ")";
        ctx.lineWidth = avgZ > 0 ? 0.9 : 0.6;
        ctx.stroke();
      }
    });

    // 4. Sort vMF components back-to-front by rotated mean z
    const sortedComps = scene.components
      .map(function (comp) {
        const projMu = project(comp.mu);
        return { comp: comp, projMu: projMu };
      })
      .sort(function (a, b) {
        return a.projMu.z - b.projMu.z;
      });

    sortedComps.forEach(function (entry) {
      const comp = entry.comp;
      const projMu = entry.projMu;
      const color = isDark ? comp.darkColor : comp.color;
      const isFront = projMu.z > -0.15;
      const nonTargetFade = comp.isTarget ? 1 : clamp01(1 - state.zoomProgress * 1.25);
      const baseAlpha = (isFront ? 0.9 : 0.22) * nonTargetFade;

      if (baseAlpha <= 0.01) {
        return;
      }

      // Draw mean direction vector from sphere origin (0,0,0) to mu_k
      ctx.save();
      ctx.globalAlpha = baseAlpha * (comp.isTarget ? 0.75 : 0.35);
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(projMu.x, projMu.y);
      ctx.strokeStyle = color;
      ctx.lineWidth = comp.isTarget ? 1.5 : 0.9;
      ctx.stroke();
      ctx.restore();

      // Draw concentric vMF density contour rings on S^2
      comp.rings.forEach(function (ring, rIdx) {
        ctx.save();
        ctx.beginPath();
        ring.forEach(function (pt, idx) {
          const p = project(pt);
          if (idx === 0) {
            ctx.moveTo(p.x, p.y);
          } else {
            ctx.lineTo(p.x, p.y);
          }
        });
        ctx.closePath();
        ctx.strokeStyle = color;
        ctx.globalAlpha = baseAlpha * (rIdx === 0 ? 0.85 : 0.45);
        ctx.lineWidth = comp.isTarget ? (rIdx === 0 ? 1.8 : 1.2) : 0.9;
        if (rIdx === 1) {
          ctx.setLineDash([3, 3]);
        }
        ctx.stroke();

        if (comp.isTarget && rIdx === 0) {
          ctx.fillStyle = color;
          ctx.globalAlpha = baseAlpha * 0.16;
          ctx.fill();
        }
        ctx.restore();
      });

      // Draw sampled vMF embedding points around mu_k
      comp.points.forEach(function (pt) {
        const p = project(pt);
        if (p.z < -0.35 && !comp.isTarget) {
          return;
        }
        ctx.save();
        ctx.globalAlpha = baseAlpha * (p.z > 0 ? 0.95 : 0.3);
        ctx.fillStyle = color;
        const ptRadius = (comp.isTarget ? 2.3 : 1.7) * Math.min(1.6, Math.sqrt(state.zoom));
        ctx.beginPath();
        ctx.arc(p.x, p.y, ptRadius, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      });

      // Draw target cluster center & emerging profile photo inside the zooming vMF cap
      if (comp.isTarget) {
        if (state.facePreviewOpacity > 0.01 && imgElem && imgElem.complete && imgElem.naturalWidth > 0) {
          ctx.save();
          const capRadius = Math.min(width, height) * 0.5 * clamp01(0.18 + state.zoomProgress * 0.82);
          ctx.beginPath();
          ctx.arc(projMu.x, projMu.y, capRadius, 0, Math.PI * 2);
          ctx.clip();
          ctx.globalAlpha = state.facePreviewOpacity;
          ctx.drawImage(imgElem, 0, 0, width, height);
          ctx.restore();
        }

        // Target centroid marker mu_AFM
        ctx.save();
        ctx.globalAlpha = clamp01(1 - state.zoomProgress * 0.8);
        ctx.fillStyle = "#ffffff";
        ctx.strokeStyle = color;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(projMu.x, projMu.y, 3.4, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();
        ctx.restore();

        // Target lock reticle & mathematical HUD badge: vMF(μ_AFM, κ)
        if (state.hudOpacity > 0.01) {
          ctx.save();
          ctx.globalAlpha = state.hudOpacity;
          ctx.strokeStyle = color;
          ctx.lineWidth = 1.3;
          const reticleR = 16 * Math.min(2.2, state.zoom);
          ctx.beginPath();
          ctx.arc(projMu.x, projMu.y, reticleR, 0, Math.PI * 2);
          ctx.stroke();

          // HUD pill label
          const labelText = comp.label;
          ctx.font = "600 10px -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, monospace";
          const textMetrics = ctx.measureText(labelText);
          const pillW = textMetrics.width + 12;
          const pillH = 17;
          const pillX = clamp01((projMu.x - pillW / 2) / width) * (width - pillW);
          const pillY = Math.max(8, projMu.y - reticleR - 22);

          ctx.fillStyle = isDark ? "rgba(15, 23, 42, 0.88)" : "rgba(255, 255, 255, 0.9)";
          ctx.strokeStyle = color;
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.roundRect ? ctx.roundRect(pillX, pillY, pillW, pillH, 8) : ctx.rect(pillX, pillY, pillW, pillH);
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = isDark ? "#e2e8f0" : "#0f172a";
          ctx.textAlign = "center";
          ctx.textBaseline = "middle";
          ctx.fillText(labelText, pillX + pillW / 2, pillY + pillH / 2);
          ctx.restore();
        }
      }
    });

    ctx.restore();
  }

  function initStage(stageElem) {
    if (!stageElem) {
      return;
    }
    const canvas = stageElem.querySelector(".vmf-avatar-canvas");
    const img = stageElem.querySelector("img");
    if (!canvas || !img) {
      return;
    }

    let animFrameId = null;

    function playAnimation() {
      if (animFrameId) {
        window.cancelAnimationFrame(animFrameId);
        animFrameId = null;
      }

      const rect = canvas.getBoundingClientRect();
      // Skip if hidden or tiny mobile icon
      if (rect.width < 60 || rect.height < 60) {
        canvas.style.opacity = "0";
        return;
      }

      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.round(rect.width * dpr);
      canvas.height = Math.round(rect.height * dpr);
      const ctx = canvas.getContext("2d");
      if (!ctx) {
        return;
      }
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      const startTime = performance.now();
      canvas.style.opacity = "1";

      function step(now) {
        const elapsed = now - startTime;
        const state = computeTimelineState(elapsed, defaultScene);
        const isDark = determineComputedTheme() === "dark";

        renderFrame(ctx, rect.width, rect.height, state, defaultScene, img, isDark);
        canvas.style.opacity = String(state.canvasOpacity.toFixed(3));

        if (!state.done) {
          animFrameId = window.requestAnimationFrame(step);
        } else {
          canvas.style.opacity = "0";
          animFrameId = null;
        }
      }

      animFrameId = window.requestAnimationFrame(step);
    }

    stageElem.addEventListener("click", function (e) {
      e.preventDefault();
      playAnimation();
    });

    stageElem.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        playAnimation();
      }
    });

    const reducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const basePath = stageElem.getAttribute("data-base-path") || "";
    const pathname = (window.location && window.location.pathname) || "/";

    if (shouldAutoPlay(pathname, basePath, reducedMotion)) {
      playAnimation();
    }
  }

  return {
    TOTAL_DURATION_MS: TOTAL_DURATION_MS,
    SPIN_END_MS: SPIN_END_MS,
    ZOOM_END_MS: ZOOM_END_MS,
    rotatePoint: rotatePoint,
    buildScene: buildScene,
    computeTimelineState: computeTimelineState,
    shouldAutoPlay: shouldAutoPlay,
    initStage: initStage
  };
})();

if (typeof window !== "undefined") {
  window.VmfAvatarAnimation = VmfAvatarAnimation;
}

/* ==========================================================================
   Actions that should occur when the page has been fully loaded
   ========================================================================== */

$(document).ready(function () {
  // SCSS SETTINGS - These should be the same as the settings in the relevant files
  const scssLarge = 925;          // pixels, from /_sass/_themes.scss
  const scssMastheadHeight = 70;  // pixels, from the current theme (e.g., /_sass/theme/_default.scss)

  // If the user hasn't chosen a theme, follow the OS preference
  setTheme();
  window.matchMedia('(prefers-color-scheme: dark)')
        .addEventListener("change", (e) => {
          if (!localStorage.getItem("theme")) {
            setTheme(e.matches ? "dark" : "light");
          }
        });

  // Enable the theme toggle
  $('#theme-toggle').on('click', toggleTheme);

  // Enable the sticky footer
  var bumpIt = function () {
    $("body").css("padding-bottom", "0");
    $("body").css("margin-bottom", $(".page__footer").outerHeight(true));
  }
  $(window).resize(function () {
    didResize = true;
  });
  setInterval(function () {
    if (didResize) {
      didResize = false;
      bumpIt();
    }}, 250);
  var didResize = false;
  bumpIt();

  // Follow menu drop down
  $(".author__urls-wrapper button").on("click", function () {
    $(".author__urls").fadeToggle("fast", function () { });
    $(".author__urls-wrapper button").toggleClass("open");
  });

  // Restore the follow menu if toggled on a window resize
  jQuery(window).on('resize', function () {
    if ($('.author__urls.social-icons').css('display') == 'none' && $(window).width() >= scssLarge) {
      $(".author__urls").css('display', 'block')
    }
  });

  // Initialize 3D vMF hypersphere profile picture animation
  document.querySelectorAll(".author__avatar-stage").forEach(function (stageElem) {
    VmfAvatarAnimation.initStage(stageElem);
  });

});
