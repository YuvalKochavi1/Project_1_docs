import re

with open(r"c:\Users\TLP-001\Documents\GitHub\Project_1_docs\presentation\presentation.tex", "r", encoding="utf-8") as f:
    text = f.read()

match = re.search(r"(.*?)(\\begin\{document\})(.*)", text, re.DOTALL)
pre = match.group(1) + match.group(2) + "\n"
body = match.group(3)

fs = re.split(r"\\begin\{frame\}", body)[1:]
def frame(idx, title=None):
    if idx >= len(fs):
        print(f"Warning: frame {idx} out of range (max {len(fs)-1}). Using empty frame.")
        return "\\begin{frame}{" + (title or "Empty") + "}\n\\end{frame}\n\n"
    c = "\\begin{frame}" + fs[idx][:fs[idx].find(r"\end{frame}")+11] + "\n\n"
    if title:
        if title == "Title":
            pass # leave as is
        else:
            return re.sub(r"\\begin\{frame\}(\[.*?\])?\{.*?\}", "\\begin{frame}{" + title + "}", c, count=1)
    return c

new_seq = []
new_seq.append(frame(0)) # Title
new_seq.append(frame(2, "MOTIVATION")) # MOTIVATION & THE 1.5D PARADIGM
new_seq.append(frame(3, "THE MECHANISM")) # GOVERNING 2D RADIATION DIFFUSION

prev = r"""\begin{frame}{PREVIOUS WORKS}
  \begin{itemize}
    \item \textbf{1D Analytical Models (e.g., Hammer-Rosen 2003):} Provide scaling laws but fail to capture radial leakage and 2D wavefront curvature.
    \item \textbf{Pure 2D/3D Numerical Simulations:} Computationally expensive and opaque regarding underlying physical scaling.
    \item \textbf{Our Need:} A computationally efficient model bridging analytical clarity with 2D geometrically complex radiation phenomena.
  \end{itemize}
\end{frame}

"""
new_seq.append(prev)

new_seq.append(frame(1, "OUR WORK - OVERVIEW")) # PRESENTATION OUTLINE

assum = r"""\begin{frame}{ASSUMPTIONS}
  \begin{itemize}
    \item \textbf{Optically Thick Core:} Transport governed by non-linear radiation diffusion.
    \item \textbf{Separation of Variables:} Axial transport decoupled from radial perturbation.
    \item \textbf{Material Properties:} Defined via power-law relations for opacity ($\alpha, \lambda$) and specific heat.
  \end{itemize}
\end{frame}

"""
new_seq.append(assum)

new_seq.append(frame(4, "STATEMENT OF THE PROBLEM")) # THE 1D CENTERLINE SOLVER (APPENDIX A)
new_seq.append(frame(5, "THE ABLATION REGION")) # WALL LOSS & FOAM COMPRESSION (\rho_{eff})
new_seq.append(frame(6, "THE ABLATION REGION")) # THE OPTICALLY THIN REGIME & TRANSPORT LIMITS
new_seq.append(frame(7, "THE SELF SIMILAR EQUATION")) # DYNAMIC OPACITY COUPLING (g_{eff})
new_seq.append(frame(8, "RESULTS")) # DISCREPANCY WITH ADVANCED SIMULATIONS
new_seq.append(frame(9, "THE SHOCK REGION")) # 2D Bessel CURVATURE MODEL
new_seq.append(frame(10, "THE SELF SIMILAR EQUATION")) # THE HURRICANE-HAMMER EIGENEQUATION
new_seq.append(frame(11, "FULL SOLUTION")) # DYNAMIC, TIME-VARYING CURVATURE
new_seq.append(frame(12, "COMPARISON TO NUMERICAL SIMULATIONS")) # HENYEY TEMPERATURE PROFILE RECONSTRUCTION

# In original, we only had 14 indices (0 to 14) which is 15 frames total. 
# We need to map 13 and 14 as well.
new_seq.append(frame(13, "COMPARISON TO NUMERICAL SIMULATIONS")) # SPATIALLY-RESOLVED RADIATION FLUX CURVATURE
new_seq.append(frame(14, "COMPARISON TO NUMERICAL SIMULATIONS")) # WALL INTERFACE & LATERAL ABLATION PROFILE

# 15, 16, 17 were not present in the original apparently (length 15). 
# We can create new frames for those or skip them.
# The previous list of frames had a SUMMARY frame. Let us check where SUMMARY was.
# Let us run a check again before writing.

