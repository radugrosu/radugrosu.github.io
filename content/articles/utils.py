import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def normalize(v):
    return v/np.linalg.norm(v)

def sbv(i, n=3):
    """return the i-th standard basis vector"""
    return np.eye(n)[:, [i-1]]


def plot_scatter(X, t, cols, cls=1, figsize=(8, 5), **kwargs):
    x, y = X[:, cols].T
    colors = t != cls
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(x, y, c=colors, cmap=plt.cm.Accent, alpha=0.5)
    ax.set(**kwargs)
    return fig, ax

def plot_boundary(ax, w, ann="", **kwargs):
    xlim = np.round(ax.get_xlim(), 2)
    ylim = ax.get_ylim()
    ybound = -(w[0] + w[1]*xlim) / w[2]
    ax.plot(xlim, ybound, **kwargs)
    ax.set(ylim=ylim, xlim=xlim)
    if ann:
        ax.annotate(ann, xy=(-(w[0] + w[2]*ylim[-1]) / w[1], ylim[-1]))
    
def add_legend(ax, t):
    cmap = plt.cm.Accent
    classes = np.unique(t)
    colors = cmap((classes - classes.min()) / (classes.max() - classes.min()))
    circles=[plt.Line2D([0], [0], color='w', marker='o', markersize=8,
                    markerfacecolor=list(color)) for color in colors[::-1]]
    leg = plt.legend(circles, map(str, classes), loc="center left", 
                     bbox_to_anchor = (1, 0.5), numpoints=1, title='Class')


def plot_decision(X, t, clf, ax=None, pad=0.5, grid_step=0.1):
    x_min, x_max = X[:, 0].min() - pad, X[:, 0].max() + pad
    y_min, y_max = X[:, 1].min() - pad, X[:, 1].max() + pad
    xx, yy = np.meshgrid(np.arange(x_min, x_max, grid_step),
                         np.arange(y_min, y_max, grid_step))
    z = np.c_[xx.ravel(), yy.ravel()]
    Z = clf.score(z).reshape(xx.shape)
    ax.plot(clf.X_sv[:, 0], clf.X_sv[:, 1], 'ro', mfc='none', ms=8, alpha=0.5);
    ax.scatter(X[:, 0], X[:, 1], c=t, cmap=plt.cm.Accent);
    pcm = ax.contourf(xx, yy, Z, 10, cmap=plt.cm.RdBu, alpha=0.2)
    if hasattr(clf, "C"):
        ax.annotate(f"C: {clf.C:.2f}", (0.05, 0.05), xycoords='axes fraction')
#     ax.set(xlim=(x_min, x_max), ylim=(y_min, y_max))
    if hasattr(clf, "X_svc"):
        ax.plot(clf.X_svc[:, 0], clf.X_svc[:, 1], 'wx', mfc='none', ms=6);
    return ax, pcm


def plot_classification(ax, w, mesh_size=0.1, plt_settings=None):
    xlim = np.round(ax.get_xlim(), 1)
    ylim = np.round(ax.get_ylim(), 1)
    xgrid, ygrid = np.mgrid[xlim[0]:xlim[1]:mesh_size, 
                            ylim[0]:ylim[1]:mesh_size]
    xy = np.c_[np.ones(xgrid.size), xgrid.ravel(), ygrid.ravel()]
    Z  = xy @ w > 0  
    ax.contourf(xgrid, ygrid, Z.reshape(xgrid.shape), N=2, alpha=0.4)
    ax.set(xlim=xlim, ylim=ylim)
    if plt_settings:
        ax.set(**plt_settings)
    return ax

from mpl_toolkits.mplot3d import Axes3D
def plot_transform(c1, c2, phi1, phi2):
    fig = plt.figure(figsize=(11, 5))
    ax1 = fig.add_subplot(131)
    ax1.scatter(c1[:, 0], c1[:, 1], s=20)
    ax1.scatter(c2[:, 0], c2[:, 1], s=20);
    ax1.set(xlim=(-2, 2), ylim=(-2, 2))
    ax1.annotate('Original feature space', xy=(0.5,0.98), 
                 ha='center', va='top',
                 xycoords='axes fraction', fontsize=12)
    ax1.set(xlabel='$x_1$', ylabel='$x_2$')
    ax2 = fig.add_subplot(132, projection='3d')
    ax2.scatter(c1[:, 0], c1[:, 1], phi1(c1))
    ax2.scatter(c2[:, 0], c2[:, 1], phi1(c2));
    ax2.view_init(elev=8., azim=30)
    ax2.set(xlabel='$x_1$', ylabel='$x_2$')
    ax2.annotate('Custom transform',
                 xy=(0.5,0.98), ha='center', va='top',
                 xycoords='axes fraction', fontsize=12)
    ax2.annotate('$(x_1,x_2)$ -> $(x_1,x_2,x_1^2 + x_2^2)$',
                 xy=(0.5,0.88), ha='center', va='top',
                 xycoords='axes fraction', fontsize=12)

    ax3 = fig.add_subplot(133, projection='3d')
    ax3.scatter(c1[:, 0]**2, c1[:, 1]**2, phi2(c1))
    ax3.scatter(c2[:, 0]**2, c2[:, 1]**2, phi2(c2))
    ax3.view_init(elev=8., azim=320)
    ax3.set(xlabel='$x_1$', ylabel='$x_2$')
    ax3.annotate('Transform assoc. with\n a polynomial kernel',
                 xy=(0.5,0.98), ha='center', va='top',
                 xycoords='axes fraction', fontsize=12)
    ax3.annotate('$(x_1,x_2) \mapsto (x_1^2,x_2^2,\sqrt{2}x_1 x_2)$',
                 xy=(0.5,0.88), ha='center', va='top',
                 xycoords='axes fraction', fontsize=12)
    fig.tight_layout()
