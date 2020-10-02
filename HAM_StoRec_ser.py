# CA1 heteroassociative memory network: Storage and recall
# CA1 PCs, BCs, AACs, BSCs and OLMs (using moderate cell models)
# EC, CA3 (excitatory) and Septal (inhibitory) inputs
# Cycle is: Recall-Storage-Recall etc
# Serial code adapted from Hines' ran3ser.hoc
# VCU & BPG 8-1-09

# Results reported in V. Cutsuridis, S. Cobb and B.P. Graham,
# "Encoding and retrieval in a model of the hippocampal CA1 microcircuit",
# Hippocampus, in press, DOI 10.1002/hipo.20661, 2009.

from neuron import h, gui
import numpy as np
import random
import math

h.xopen("HAM_StoRec_ser.hoc")


