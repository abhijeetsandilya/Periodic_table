import matplotlib.pyplot as plt
import math
from electron import bohr_distribution, config

def bohr_figure(Z, size=(5,5)):
    shells = bohr_distribution(Z)
    fig, ax = plt.subplots(figsize=size)
    ax.set_aspect('equal')
    ax.axis('off')

    # nucleus
    ax.scatter(0,0, s=450, color='maroon', zorder=6)
    ax.text(0,0, str(Z), color='white', ha='center', va='center', fontsize=10, zorder=7)

    for i, ecount in enumerate(shells):
        if ecount == 0:
            continue
        r = 0.6 + i * 0.55
        circ = plt.Circle((0,0), r, fill=False, linestyle='--', linewidth=1)
        ax.add_patch(circ)
        for k in range(ecount):
            theta = 2 * math.pi * (k / max(ecount,1))
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            ax.scatter(x, y, s=30, zorder=5)

    maxr = 0.6 + (len([s for s in shells if s>0])-1)*0.55 + 0.6
    ax.set_xlim(-maxr, maxr)
    ax.set_ylim(-maxr, maxr)
    ax.set_title(f"Bohr-style shells — Z={Z}")
    return fig

def subshell_bar(Z, size=(6,3)):
    cfg = config(Z)
    subs = [s for s,_ in cfg]
    counts = [c for _,c in cfg]
    fig, ax = plt.subplots(figsize=size)
    y = range(len(subs))
    ax.barh(y, counts, align='center')
    ax.set_yticks(y)
    ax.set_yticklabels(subs)
    ax.set_xlabel("Electrons")
    ax.set_title(f"Electron config (Aufbau-like) — Z={Z}")
    for i,c in enumerate(counts):
        ax.text(c + 0.1, i, str(c), va='center')
    fig.tight_layout()
    return fig
