"""Generate the portfolio illustrations for the HPC experimentation tooling and
sparse matrix optimization projects (PNG + SVG)."""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle

OUT_DIR = Path(__file__).resolve().parent.parent / "images" / "research"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Sized for ~550px-wide teasers: stacked panels, large type.
W = 6.6
INK = "#0f172a"
MUTED = "#475569"
GREY = "#64748b"
RNG = np.random.default_rng(7)


def box(ax, x, y, w, h, fc="#ffffff", ec="#cbd5e1", lw=1.3, r=0.1, z=2, ls="-"):
    ax.add_patch(
        FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                       facecolor=fc, edgecolor=ec, linewidth=lw, linestyle=ls, zorder=z)
    )


def pill(ax, x, y, w, h, text, fc, tc="#ffffff", fs=7.0, z=5):
    box(ax, x, y, w, h, fc=fc, ec="none", r=0.06, z=z)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
            color=tc, fontsize=fs, fontweight="bold", zorder=z + 1)


def arrow(ax, p1, p2, color=MUTED, lw=1.6, z=6, rad=0.0, ls="-"):
    ax.add_patch(
        FancyArrowPatch(p1, p2, arrowstyle="-|>", color=color, linewidth=lw, linestyle=ls,
                        mutation_scale=11, zorder=z, connectionstyle=f"arc3,rad={rad}")
    )


def panel_title(ax, x, y, title, chip, chip_fc):
    ax.text(x, y, title, ha="left", va="center", color=INK,
            fontsize=10.5, fontweight="bold", zorder=4)
    cw = len(chip) * 0.062 + 0.26
    pill(ax, W - 0.25 - cw, y - 0.11, cw, 0.22, chip, fc=chip_fc, fs=6.8)


def terminal_card(ax, x, y, w, h, title, accent, bg):
    box(ax, x, y, w, h, fc=bg, ec=accent, lw=1.5, r=0.1)
    box(ax, x, y + h - 0.34, w, 0.34, fc=accent, ec="none", r=0.1, z=3)
    ax.add_patch(Rectangle((x, y + h - 0.34), w, 0.17, fc=accent, ec="none", zorder=3))
    ax.text(x + 0.12, y + h - 0.17, title, ha="left", va="center",
            color="#ffffff", fontsize=7.4, fontweight="bold", family="monospace", zorder=4)


# --------------------------------------------------------------------------- A
def panel_slurm(ax, y0, y1):
    panel_title(ax, 0.25, y1 - 0.18, "Slurm Job Generator",
                "2024 – 2026 · Python", "#1d4ed8")

    # Generator card
    ox, oy, ow, oh = 0.25, y0 + 0.1, 2.35, y1 - y0 - 0.6
    terminal_card(ax, ox, oy, ow, oh, ">_ create_slurm_generator.py", "#1d4ed8", "#eff6ff")

    ax.text(ox + 0.14, oy + oh - 0.56, "jobs.conf  →  N × sbatch", ha="left", va="center",
            color=INK, fontsize=7.6, fontweight="bold", family="monospace", zorder=4)
    bullets = [
        "resources checked against\neach cluster's configuration",
        "hundreds of independent jobs\nfrom a single config",
    ]
    ty = oy + oh - 0.8
    for text in bullets:
        n = text.count("\n") + 1
        ax.text(ox + 0.16, ty, "•", ha="left", va="top", color="#1d4ed8",
                fontsize=8.5, fontweight="bold", zorder=4)
        ax.text(ox + 0.32, ty, text, ha="left", va="top", color=MUTED,
                fontsize=7.6, linespacing=1.2, zorder=4)
        ty -= 0.38 + 0.17 * (n - 1)

    # Cluster cards
    clusters = [
        ("Jean Zay", "NVIDIA A100 / V100 · CUDA", "#15803d", "#dcfce7"),
        ("Adastra", "AMD MI250X · ROCm", "#b91c1c", "#fee2e2"),
        ("Factory-IA", "CEA GPU cluster", "#4338ca", "#e0e7ff"),
    ]
    cx, cw, ch = 3.4, 2.95, 0.54
    gap = (oh - 3 * ch) / 2
    src = (ox + ow + 0.03, oy + oh / 2)
    for i, (name, hw, acc, bg) in enumerate(clusters):
        cy = oy + oh - ch - i * (ch + gap)
        box(ax, cx, cy, cw, ch, fc="#ffffff", ec=acc, lw=1.4, r=0.08)
        ax.plot([cx + 0.07, cx + 0.07], [cy + 0.1, cy + ch - 0.1], color=acc,
                lw=3.5, solid_capstyle="round", zorder=3)
        ax.text(cx + 0.2, cy + ch - 0.17, name, ha="left", va="center", color=INK,
                fontsize=9.0, fontweight="bold", zorder=4)
        ax.text(cx + 0.2, cy + 0.16, hw, ha="left", va="center", color=MUTED,
                fontsize=7.2, zorder=4)
        # GPU node glyph: 2 x 4 grid
        gx0, gy0, s, g = cx + cw - 0.92, cy + 0.1, 0.16, 0.05
        for r in range(2):
            for c in range(4):
                ax.add_patch(Rectangle((gx0 + c * (s + g), gy0 + r * (s + g)), s, s,
                                       fc=bg, ec=acc, lw=0.9, zorder=4))
        arrow(ax, src, (cx - 0.03, cy + ch / 2), color=acc, lw=1.5,
              rad=-0.15 if i == 0 else (0.15 if i == 2 else 0.0))

    ax.text(src[0] + 0.4, src[1] + 0.14, "sbatch ×N", ha="center", va="bottom",
            color=GREY, fontsize=6.8, style="italic", zorder=4)


# --------------------------------------------------------------------------- B
def panel_optuna(ax, y0, y1):
    acc, bg = "#0e7490", "#ecfeff"
    panel_title(ax, 0.25, y1 - 0.18, "Multi-Node Optuna Search & Analysis",
                "Optuna · Python", acc)

    top = y1 - 0.5
    bot = y0 + 0.16
    mid = (top + bot) / 2

    # Independent jobs on different nodes
    jw, jh = 0.95, 0.4
    jobs = [("job 1", "node A"), ("job 2", "node B"), ("job N", "node C")]
    jgap = (top - bot - 3 * jh) / 2
    sx = 0.25 + jw + 0.38
    sw, sh = 1.35, top - bot
    for i, (job, node) in enumerate(jobs):
        jy = top - jh - i * (jh + jgap)
        box(ax, 0.25, jy, jw, jh, fc="#ffffff", ec=acc, lw=1.2, r=0.06)
        ax.text(0.25 + 0.1, jy + jh / 2, job, ha="left", va="center", color=INK,
                fontsize=7.4, fontweight="bold", family="monospace", zorder=4)
        ax.text(0.25 + jw - 0.1, jy + jh / 2, node, ha="right", va="center",
                color=MUTED, fontsize=6.6, zorder=4)
        arrow(ax, (0.25 + jw + 0.04, jy + jh / 2), (sx - 0.04, mid + (1 - i) * 0.35),
              color=acc, lw=1.3)

    # Shared study: trials from every node, best-so-far curve
    box(ax, sx, bot, sw, sh, fc=bg, ec=acc, lw=1.4, r=0.08)
    ax.text(sx + sw / 2, top - 0.17, "shared study", ha="center", va="center",
            color=acc, fontsize=7.4, fontweight="bold", zorder=4)
    n = 28
    tx = np.linspace(sx + 0.15, sx + sw - 0.15, n)
    val = 0.35 + 0.5 * (1 - np.exp(-np.arange(n) / 8)) + 0.12 * RNG.standard_normal(n)
    val = (val - val.min()) / (val.max() - val.min())
    py0, ph = bot + 0.2, sh - 0.62
    cols = [acc, "#0891b2", "#67e8f9"]
    ax.scatter(tx, py0 + val * ph, s=5, c=[cols[k % 3] for k in range(n)],
               edgecolors="none", zorder=4)
    ax.step(tx, py0 + np.maximum.accumulate(val) * ph, where="post", color=INK,
            lw=1.0, zorder=5)

    # Marginal effects of hyperparameters on each metric (illustrative values)
    ex0 = sx + sw + 0.5
    arrow(ax, (sx + sw + 0.04, mid), (ex0 - 0.06, mid), color=acc, lw=1.5)
    params = ["lr", "batch_size", "weight_decay", "dropout"]
    metrics = ["metric 1", "metric 2", "metric 3"]
    eff = np.array([[0.8, -0.5, 0.1], [-0.2, 0.1, -0.6], [0.3, 0.05, 0.2], [-0.1, -0.7, 0.4]])
    pval = np.array([[0.001, 0.02, 0.6], [0.3, 0.5, 0.004], [0.04, 0.8, 0.2], [0.7, 0.002, 0.03]])
    lab_w = 0.86
    cw = (W - 0.25 - ex0 - lab_w) / 3
    rh = (top - bot - 0.6) / 4
    ax.text(ex0 + (lab_w + 3 * cw) / 2, top - 0.05, "marginal effect · p-value", ha="center",
            va="center", color=INK, fontsize=7.4, fontweight="bold", zorder=4)
    hy = top - 0.3
    for j, m in enumerate(metrics):
        ax.text(ex0 + lab_w + (j + 0.5) * cw, hy, m, ha="center", va="center",
                color=MUTED, fontsize=6.4, zorder=4)
    for i, p in enumerate(params):
        ry = hy - 0.14 - (i + 1) * rh
        ax.text(ex0 + lab_w - 0.06, ry + rh / 2, p, ha="right", va="center", color=INK,
                fontsize=6.4, family="monospace", zorder=4)
        for j in range(3):
            e = eff[i, j]
            base = np.array([14, 116, 144]) if e > 0 else np.array([194, 65, 12])
            a = 0.15 + 0.8 * min(abs(e), 1)
            fc = tuple((1 - a) + a * base / 255)
            ax.add_patch(Rectangle((ex0 + lab_w + j * cw + 0.02, ry + 0.02), cw - 0.04,
                                   rh - 0.04, fc=fc, ec="none", zorder=3))
            stars = "**" if pval[i, j] < 0.01 else ("*" if pval[i, j] < 0.05 else "")
            ax.text(ex0 + lab_w + (j + 0.5) * cw, ry + rh / 2, f"{e:+.1f}{stars}",
                    ha="center", va="center", fontsize=6.3, fontweight="bold",
                    color="#ffffff" if a > 0.55 else INK, zorder=4)
    ax.text(ex0 + lab_w + 1.5 * cw, bot - 0.04, "* p < 0.05   ** p < 0.01   (illustrative)",
            ha="center", va="bottom", color=GREY, fontsize=6.0, style="italic", zorder=4)


# --------------------------------------------------------------------------- C
def panel_scratch(ax, y0, y1):
    acc, bg = "#7c3aed", "#f5f3ff"
    panel_title(ax, 0.25, y1 - 0.18, "Scratch Management Library",
                "multi-node · Python", acc)

    top = y1 - 0.48
    bot = y0 + 0.14

    # Shared storage on both sides: dataset in (left), results out (right)
    sw = 1.2
    sy, sh = bot + 0.18, top - bot - 0.36

    def storage(x, label, shard_fc, shard_ec, shard_ls):
        box(ax, x, sy, sw, sh, fc="#ffffff", ec="#94a3b8", lw=1.3, r=0.08)
        ax.text(x + sw / 2, sy + sh - 0.2, "Shared storage", ha="center", va="center",
                color=INK, fontsize=7.6, fontweight="bold", zorder=4)
        for k in range(2):
            box(ax, x + 0.18, sy + sh - 0.6 - k * 0.27, sw - 0.36, 0.2, fc=shard_fc,
                ec=shard_ec, lw=0.8, r=0.03, z=3, ls=shard_ls)
        ax.text(x + sw / 2, sy + 0.22, label, ha="center", va="center",
                color=MUTED, fontsize=6.8, family="monospace", zorder=4)

    sx = 0.25
    rx = W - 0.25 - sw
    storage(sx, "dataset", "#e2e8f0", "#94a3b8", "-")
    storage(rx, "results", "none", GREY, "--")

    # Compute nodes: one leader process extracts, the others wait and read locally
    nx = sx + sw + 0.72
    nw = rx - 0.72 - nx
    nh = (top - bot - 0.2) / 2
    ax.text((sx + sw + nx) / 2, (top + bot) / 2, "1 copy\nper node", ha="center",
            va="center", color=acc, fontsize=6.4, fontweight="bold",
            linespacing=1.1, zorder=4)
    ax.text((nx + nw + rx) / 2, (top + bot) / 2, "coordinated\nsave", ha="center",
            va="center", color=GREY, fontsize=6.4, fontweight="bold",
            linespacing=1.1, zorder=4)
    for i in range(2):
        ny = top - nh - i * (nh + 0.2)
        box(ax, nx, ny, nw, nh, fc=bg, ec=acc, lw=1.4, r=0.08)
        ax.text(nx + 0.12, ny + nh - 0.15, f"Node {i + 1}", ha="left", va="center",
                color=INK, fontsize=7.8, fontweight="bold", zorder=4)
        # local scratch strip
        box(ax, nx + 0.12, ny + 0.08, nw - 0.24, 0.2, fc="#ede9fe", ec=acc, lw=0.9, r=0.03, z=3)
        ax.text(nx + nw / 2, ny + 0.18, "local scratch", ha="center", va="center",
                color=acc, fontsize=6.6, family="monospace", zorder=4)
        # processes
        ps, pg = 0.26, 0.1
        px0 = nx + nw - 0.12 - 4 * ps - 3 * pg
        py = ny + 0.38
        for k in range(4):
            lead = k == 0
            box(ax, px0 + k * (ps + pg), py, ps, ps, fc=acc if lead else "#ffffff",
                ec=acc, lw=1.1, r=0.04, z=4)
            ax.text(px0 + k * (ps + pg) + ps / 2, py + ps / 2, f"P{k}", ha="center",
                    va="center", color="#ffffff" if lead else acc, fontsize=6.4,
                    fontweight="bold", zorder=5)
        ax.text(nx + 0.12, ny + nh - 0.36, "1 extract,\n3 wait", ha="left", va="center",
                color=MUTED, fontsize=6.3, linespacing=1.1, zorder=4)
        # one transfer per node in, coordinated save out
        sgn = 1 if i == 0 else -1
        arrow(ax, (sx + sw + 0.04, (top + bot) / 2 + sgn * 0.3), (nx - 0.04, ny + nh / 2),
              color=acc, lw=1.5)
        arrow(ax, (nx + nw + 0.04, ny + nh / 2), (rx - 0.04, (top + bot) / 2 + sgn * 0.3),
              color=GREY, lw=1.2, ls="--")


# --------------------------------------------------------------------------- D
def sparse_matrix(ax, x, y, s, n=64, density=0.045):
    box(ax, x, y, s, s, fc="#ffffff", ec="#94a3b8", lw=1.2, r=0.04)
    # Long-tailed activity: few heavy users / popular items, many sparse ones.
    row_w = RNG.pareto(1.2, n) + 1
    col_w = RNG.pareto(1.2, n) + 1
    p = np.outer(row_w, col_w)
    p = p / p.sum() * density * n * n
    mask = RNG.random((n, n)) < np.clip(p, 0, 1)
    rows, cols = np.nonzero(mask)
    cell = s / n
    ax.scatter(x + (cols + 0.5) * cell, y + s - (rows + 0.5) * cell, s=1.6,
               color="#b45309", marker="s", linewidths=0, zorder=4)
    return mask


def cooccurrence_graph(ax, x, y, s, n_nodes=12):
    box(ax, x, y, s, s, fc="#ffffff", ec="#94a3b8", lw=1.2, r=0.04)
    ang = np.linspace(0, 2 * np.pi, n_nodes, endpoint=False) + 0.3
    rad = 0.36 * s * (0.75 + 0.45 * RNG.random(n_nodes))
    px = x + s / 2 + rad * np.cos(ang)
    py = y + s / 2 + rad * np.sin(ang)
    px[0], py[0] = x + s / 2, y + s / 2 + 0.03 * s
    deg = RNG.pareto(1.0, n_nodes) + 1
    deg[0] = deg.max() * 1.6
    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            wgt = deg[i] * deg[j]
            if RNG.random() < min(0.95, 0.08 * wgt):
                ax.plot([px[i], px[j]], [py[i], py[j]], color="#0f766e",
                        lw=0.5 + 1.4 * min(wgt, 6) / 6, alpha=0.45, zorder=3,
                        solid_capstyle="round")
    sizes = 0.028 * s * (deg / deg.max()) ** 0.5 + 0.02 * s
    for i in range(n_nodes):
        ax.add_patch(Circle((px[i], py[i]), sizes[i], fc="#14b8a6", ec="#0f766e",
                            lw=1.0, zorder=5))


def panel_sparse(ax, y0, y1):
    panel_title(ax, 0.25, y1 - 0.18, "High-Performance Sparse Matrix Optimization",
                "WWW 2026 · SciPy", "#b45309")

    s = 1.45
    my = y0 + 0.42
    mx = 0.3
    sparse_matrix(ax, mx, my, s, density=0.055)
    ax.text(mx + s / 2, my - 0.17, "User × Item interactions (CSR)\n9 recommendation datasets",
            ha="center", va="top", color=MUTED, fontsize=7.2, linespacing=1.15, zorder=4)

    gap = 0.82
    gx = mx + s + gap
    cooccurrence_graph(ax, gx, my, s)
    ax.text(gx + s / 2, my - 0.17, "Item co-occurrence graph\n(ultra-large, sparse)",
            ha="center", va="top", color=MUTED, fontsize=7.2, linespacing=1.15, zorder=4)

    def labelled_arrow(xa, xb, top, bottom=None):
        arrow(ax, (xa, my + s / 2), (xb, my + s / 2), color="#b45309", lw=1.7)
        ax.text((xa + xb) / 2, my + s / 2 + 0.12, top, ha="center", va="bottom",
                color="#9a3412", fontsize=6.8, fontweight="bold", linespacing=1.15, zorder=4)
        if bottom:
            ax.text((xa + xb) / 2, my + s / 2 - 0.12, bottom, ha="center", va="top",
                    color=GREY, fontsize=6.6, style="italic", linespacing=1.15, zorder=4)

    labelled_arrow(mx + s + 0.08, gx - 0.08, "recompiled\nSciPy",
                   "int32 → int64\non demand")

    # Output card
    ox = gx + s + gap
    ow = W - 0.25 - ox
    oh = s
    box(ax, ox, my, ow, oh, fc="#fffbeb", ec="#b45309", lw=1.5, r=0.1)
    ax.text(ox + ow / 2, my + oh - 0.4, "$CS(u)$", ha="center", va="center",
            color="#9a3412", fontsize=17, fontweight="bold", zorder=4)
    ax.text(ox + ow / 2, my + oh / 2 - 0.12, "Mean Conditional\nSurprise", ha="center",
            va="center", color=INK, fontsize=8.0, fontweight="bold",
            linespacing=1.15, zorder=4)
    ax.text(ox + ow / 2, my + 0.2, "$H(i \\mid j)$ per user", ha="center",
            va="center", color=MUTED, fontsize=7.4, zorder=4)
    labelled_arrow(gx + s + 0.08, ox - 0.08, "conditional\nentropy", "RAM-bounded")


def index_strip(ax, y):
    """int32 index array promoted to int64 only when an index outgrows int32."""
    acc, ink = "#b45309", "#9a3412"
    ch, n = 0.24, 6
    ax.text(0.3, y + ch / 2, "sparse indices", ha="left", va="center", color=INK,
            fontsize=7.4, fontweight="bold", zorder=4)

    def cells(x, w, fc, label):
        for k in range(n):
            ax.add_patch(Rectangle((x + k * w, y), w, ch, fc=fc, ec=acc, lw=0.9, zorder=4))
        ax.text(x + n * w / 2, y - 0.07, label, ha="center", va="top", color=ink,
                fontsize=6.8, fontweight="bold", family="monospace", zorder=5)
        return x + n * w

    x1 = cells(1.45, 0.17, "#fef3c7", "int32 · 4 B")
    x2 = x1 + 1.75
    arrow(ax, (x1 + 0.08, y + ch / 2), (x2 - 0.08, y + ch / 2), color=acc, lw=1.5)
    ax.text((x1 + x2) / 2, y + ch / 2 - 0.08, "only when an index exceeds 2³¹ − 1",
            ha="center", va="top", color=GREY, fontsize=6.4, style="italic", zorder=4)
    cells(x2, 0.29, "#fde68a", "int64 · 8 B")


def new_figure(h, bands):
    fig, ax = plt.subplots(figsize=(W, h), dpi=300)
    ax.set_xlim(0, W)
    ax.set_ylim(0, h)
    ax.axis("off")
    fig.patch.set_facecolor("#ffffff")
    for lo, hi in bands:
        box(ax, 0.08, lo, W - 0.16, hi - lo, fc="#f8fafc", ec="#e2e8f0", lw=1.0, r=0.14, z=0)
    return fig, ax


def save(fig, name):
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    png = OUT_DIR / f"{name}.png"
    svg = OUT_DIR / f"{name}.svg"
    fig.savefig(png, dpi=300, bbox_inches="tight", pad_inches=0.03)
    fig.savefig(svg, bbox_inches="tight", pad_inches=0.03)
    plt.close(fig)
    print(f"Saved {png} and {svg}")


def build():
    plt.rcParams["font.sans-serif"] = ["Segoe UI", "DejaVu Sans", "Arial", "Helvetica"]
    plt.rcParams["font.monospace"] = ["Cascadia Mono", "Consolas", "DejaVu Sans Mono"]
    plt.rcParams["mathtext.fontset"] = "dejavusans"

    # HPC tooling, bottom to top: scratch, Optuna, Slurm
    h = 7.55
    b1, b2 = 2.52, 5.0
    bands = [(0.08, b1 - 0.06), (b1 + 0.06, b2 - 0.06), (b2 + 0.06, h - 0.08)]
    fig, ax = new_figure(h, bands)
    panel_scratch(ax, *bands[0])
    panel_optuna(ax, *bands[1])
    panel_slurm(ax, *bands[2])
    save(fig, "hpc_tooling_teaser")

    # Sparse matrix optimization: pipeline above, index encoding strip below
    h = 3.0
    fig, ax = new_figure(h, [(0.08, h - 0.08)])
    panel_sparse(ax, 0.62, h - 0.08)
    index_strip(ax, 0.36)
    save(fig, "sparse_indexing_teaser")


if __name__ == "__main__":
    build()
