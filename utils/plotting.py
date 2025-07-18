# utils/plotting.py
# This file contains helper functions used across multiple chapters for plotting.
# Keeping them here avoids code duplication and keeps chapter files cleaner.

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import urllib.parse

def plot_vectors(vectors, colors, ax, labels=None):
    """
    Plots a list of vectors on a given Matplotlib Axes object.
    
    Args:
        vectors (list): A list of 2D numpy arrays (the vectors).
        colors (list): A list of color strings for each vector.
        ax (matplotlib.axes.Axes): The axes object to plot on.
        labels (list, optional): A list of labels for the legend. Defaults to None.
    """
    # Create a default label list if none is provided
    if labels is None:
        labels = [f'v{i+1}={vec}' for i, vec in enumerate(vectors)]

    for i, vec in enumerate(vectors):
        ax.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy', scale=1, color=colors[i], zorder=3, label=labels[i])
    
def setup_plot(ax, title, xlim=(-5, 5), ylim=(-5, 5)):
    """
    Sets up a standard 2D plot for our visualizations.
    
    Args:
        ax (matplotlib.axes.Axes): The axes object to set up.
        title (str): The title for the plot.
        xlim (tuple, optional): The x-axis limits. Defaults to (-5, 5).
        ylim (tuple, optional): The y-axis limits. Defaults to (-5, 5).
    """
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, linestyle='--')
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.set_title(title, fontsize=16)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

def image_search_button(label, search_term):
    """
    Creates a Streamlit link button that searches Google Images in a new tab.
    (As specified in LESSON_DESIGN_GUIDE.md)
    """
    encoded_term = urllib.parse.quote_plus(search_term)
    url = f"https://www.google.com/search?q={encoded_term}&tbm=isch"
    st.link_button(f"🖼️ See images of: {label}", url, use_container_width=True)