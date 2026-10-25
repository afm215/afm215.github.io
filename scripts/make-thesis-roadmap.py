"""Generate a simple, readable PhD Thesis Roadmap diagram (PNG + SVG)."""

from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT_DIR = Path(__file__).resolve().parent.parent / "images" / "research"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Figure is sized so that 10pt text stays legible once scaled to ~800px wide.
W, H = 9.6, 7.3
MARGIN = 0.3
COL_W, COL_GAP = 2.8, 0.3
COLS = [MARGIN + i * (COL_W + COL_GAP) for i in range(3)]

INK = "#0f172a"
MUTED = "#475569"
GREY = "#64748b"


def box(ax, x, y, w, h, fc="#ffffff", ec="#cbd5e1", lw=1.4, r=0.12, z=2, ls="-"):
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h,
            boxstyle=f"round,pad=0,rounding_size={r}",
            facecolor=fc, edgecolor=ec, linewidth=lw, linestyle=ls, zorder=z,
        )
    )


def pill(ax, x, y, w, h, text, fc, tc="#ffffff", fs=7.4, z=5):
    box(ax, x, y, w, h, fc=fc, ec="none", r=0.07, z=z)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            color=tc, fontsize=fs, fontweight="bold", zorder=z + 1)


def arrow(ax, p1, p2, color=MUTED, lw=1.8, style="-|>", ls="-", z=6):
    ax.add_patch(
        FancyArrowPatch(p1, p2, arrowstyle=style, color=color, linewidth=lw,
                        linestyle=ls, mutation_scale=13, zorder=z)
    )


def card(ax, x, y, w, h, chapter, title, keywords, accent, venue=None,
         venue_bg="#e2e8f0", venue_fg=INK):
    box(ax, x, y, w, h, fc="#ffffff", ec=accent, lw=1.8, r=0.12, z=2)
    ax.plot([x + 0.075, x + 0.075], [y + 0.16, y + h - 0.16], color=accent,
            linewidth=4.5, solid_capstyle="round", zorder=3)

    top = y + h - 0.32
    pill(ax, x + 0.2, top, 1.0, 0.22, chapter, fc=accent, fs=7.4)
    if venue:
        vw = len(venue) * 0.066 + 0.26
        pill(ax, x + w - vw - 0.15, top, vw, 0.22, venue, fc=venue_bg, tc=venue_fg, fs=7.0)

    ty = top - 0.1
    ax.text(x + 0.2, ty, title, ha="left", va="top", color=INK,
            fontsize=10.2, fontweight="bold", linespacing=1.15, zorder=4)
    n_title = title.count("\n") + 1
    ky = ty - 0.175 * n_title - 0.08
    ax.text(x + 0.2, ky, keywords, ha="left", va="top", color=MUTED,
            fontsize=8.6, linespacing=1.2, zorder=4)


def build_roadmap():
    plt.rcParams["font.sans-serif"] = ["Segoe UI", "DejaVu Sans", "Arial", "Helvetica"]
    plt.rcParams["mathtext.fontset"] = "dejavusans"

    fig, ax = plt.subplots(figsize=(W, H), dpi=300)
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    fig.patch.set_facecolor("#ffffff")

    full_w = W - 2 * MARGIN
    centers = [c + COL_W / 2 for c in COLS]

    # ---------------------------------------------------------------- Part I
    box(ax, MARGIN, 5.6, full_w, 1.45, fc="#f8fafc", ec="#cbd5e1", lw=1.2, r=0.14, z=1, ls="--")
    ax.text(MARGIN + 0.2, 6.9, "PART I · CONTEXT & BACKGROUND", ha="left", va="center",
            color=GREY, fontsize=7.6, fontweight="bold", zorder=3)

    half = (full_w - 0.3) / 2
    card(ax, MARGIN, 5.72, half, 1.0, "CHAPTER 1", "Introduction",
         "Societal harms · GDPR / AI Act / BIPA · Scaling laws ($\\mathrm{PL}^\\star$)",
         accent="#475569")
    card(ax, MARGIN + half + 0.3, 5.72, half, 1.0, "CHAPTER 2", "Related Work",
         "Hyperspherical FR · Datasets · Fairness audits & annotators",
         accent="#475569")
    arrow(ax, (MARGIN + half + 0.02, 6.22), (MARGIN + half + 0.28, 6.22))

    for cx in centers:
        arrow(ax, (cx, 5.6), (cx, 5.36))

    # -------------------------------------------------------------- Pillars
    pillars = [
        ("PILLAR I · STATISTICAL AUDITING", "#1d4ed8", "#eff6ff", "#93c5fd"),
        ("PILLAR II · RELIABLE ANNOTATION", "#7a1248", "#fdf2f8", "#f472b6"),
        ("PILLAR III · SYNTHESIS & VLM AUDITING", "#b45309", "#fffbeb", "#fbbf24"),
    ]
    for (label, fc, bg, ec), x in zip(pillars, COLS):
        box(ax, x, 1.4, COL_W, 3.95, fc=bg, ec=ec, lw=1.2, r=0.14, z=1)
        pill(ax, x + 0.15, 5.02, COL_W - 0.3, 0.25, label, fc=fc, fs=7.4)

    # Pillar I — Chapter 3 (cross-cutting toolbox)
    x0 = COLS[0]
    card(ax, x0 + 0.15, 2.45, COL_W - 0.3, 1.55, "CHAPTER 3",
         "Statistical Tools for\nBias Analysis",
         "Information-theoretic floor\nLatent-space ANOVA\nMarginal effects (AME) & SIMEX",
         accent="#1d4ed8", venue="FaVFA", venue_bg="#dbeafe", venue_fg="#1e40af")
    box(ax, x0 + 0.15, 1.58, COL_W - 0.3, 0.5, fc="#dbeafe", ec="#60a5fa", lw=1.1, r=0.08, z=3, ls="--")
    ax.text(x0 + COL_W / 2, 1.83, "Audit toolbox reused\nin Chapters 4 – 7", ha="center",
            va="center", color="#1e3a8a", fontsize=7.8, fontweight="bold", zorder=4)

    # Pillar II — Chapters 5 & 6
    x1 = COLS[1]
    card(ax, x1 + 0.15, 3.45, COL_W - 0.3, 1.4, "CHAPTER 5",
         "Annotator Reliability\nDiagnostic (REDI)",
         "HomE · MiMA · MaMA metrics\nPlug-in estimator bias proof",
         accent="#7a1248", venue="arXiv 2025", venue_bg="#fce7f3", venue_fg="#831843")
    card(ax, x1 + 0.15, 1.55, COL_W - 0.3, 1.4, "CHAPTER 6",
         "WEG Dataset &\nREGI-Face Annotator",
         "IPF-balanced WebFace42M\nvMF + RBF-SVM head · $\\hat{p}^{(\\mathrm{corr})}$",
         accent="#7a1248", venue="REGI-Face", venue_bg="#fce7f3", venue_fg="#831843")
    arrow(ax, (centers[1], 3.43), (centers[1], 2.99), color="#7a1248", lw=2.0)

    # Pillar III — Chapters 4 & 7
    x2 = COLS[2]
    card(ax, x2 + 0.15, 3.45, COL_W - 0.3, 1.4, "CHAPTER 4",
         "Mitigating Bias in\nFR Training Data",
         "FaVGen controlled synthesis\nBalanced demographics, age & pose",
         accent="#0f766e", venue="WACV 2025", venue_bg="#ccfbf1", venue_fg="#115e59")
    card(ax, x2 + 0.15, 1.55, COL_W - 0.3, 1.4, "CHAPTER 7",
         "Auditing VLMs with\nBalanced Portraits",
         "BALPortraits · 9,000 portraits\n16 VLMs · casting scenarios",
         accent="#c2410c", venue="WACV 2027", venue_bg="#ffedd5", venue_fg="#9a3412")
    arrow(ax, (centers[2], 3.43), (centers[2], 2.99), color="#b45309", lw=2.0)

    # Cross-pillar dependencies
    arrow(ax, (x0 + COL_W - 0.13, 3.75), (x1 + 0.13, 3.75), color="#1d4ed8")   # Ch3 -> Ch5
    arrow(ax, (x0 + COL_W - 0.13, 2.75), (x1 + 0.13, 2.75), color="#1d4ed8", ls="--")  # Ch3 -> Ch6
    arrow(ax, (x1 + COL_W - 0.13, 2.25), (x2 + 0.13, 2.25), color="#7a1248")   # Ch6 -> Ch7

    # ------------------------------------------------------------- Chapter 8
    for cx in centers:
        arrow(ax, (cx, 1.4), (cx, 1.17), color="#334155")

    card(ax, MARGIN, 0.25, full_w, 0.9, "CHAPTER 8",
         "Opening: Defining Bias Across Domains",
         "3D object detection (MVAT, WACV 2026)  ·  Faces & VLMs (Ch. 3 – 7)  ·  "
         "Recommender systems (User Coherence, WWW 2026)",
         accent="#0f172a", venue="WACV 2026 · WWW 2026")

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    png_path = OUT_DIR / "thesis_roadmap.png"
    svg_path = OUT_DIR / "thesis_roadmap.svg"
    fig.savefig(png_path, dpi=300, bbox_inches="tight", pad_inches=0.04)
    fig.savefig(svg_path, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    print(f"Saved {png_path} and {svg_path}")


if __name__ == "__main__":
    build_roadmap()
