import re

with open(r"c:\Users\TLP-001\Documents\GitHub\Project_1_docs\presentation\presentation.tex", "r", encoding="utf-8") as f:
    text = f.read()

match = re.search(r"(.*?)(\\begin\{document\})(.*)", text, re.DOTALL)
pre_doc = match.group(1) + match.group(2) + "\n"
body = match.group(3)

frames_raw = re.split(r"\\begin\{frame\}", body)

def get_content(raw):
    end_idx = raw.find(r"\end{frame}")
    return raw[:end_idx] + "\\end{frame}\n\n"

frames = []
for f in frames_raw[1:]:
    if f.startswith("[plain]"):
        frames.append({"title": "Title", "content": "\\begin{frame}" + get_content(f)})
    else:
        tm = re.match(r"\{(.*?)\}", f)
        title = tm.group(1) if tm else "Unknown"
        frames.append({"title": title, "content": "\\begin{frame}" + get_content(f)})

# Create new frames array based on Shussman flow
new_frames = []

# 1. Title
new_frames.append(frames[0]["content"])

# 2. MOTIVATION
# Take MOTIVATION & THE 1.5D PARADIGM, change its title to MOTIVATION
# Actually, the original is split into two columns. Let us just rename it.
f_mot = frames[2]["content"].replace("{MOTIVATION \& THE 1.5D PARADIGM}", "{MOTIVATION}")
new_frames.append(f_mot)

# 3. THE MECHANISM
# From GOVERNING 2D RADIATION DIFFUSION
f_mech = frames[3]["content"].replace("{GOVERNING 2D RADIATION DIFFUSION}", "{THE MECHANISM}")
new_frames.append(f_mech)

# 4. PREVIOUS WORKS
# I will create a new slide
f_prev = "\\begin{frame}{PREVIOUS WORKS}\n" + \
"  \\begin{itemize}\n" + \
"    \\item \\textbf{1D Analytical Models (e.g., Hammer-Rosen 2003):} Provide scaling laws but fail to capture radial leakage and 2D wavefront curvature.\n" + \
"    \\item \\textbf{Pure 2D/3D Numerical Simulations:} Computationally expensive and opaque regarding underlying physical scaling.\n" + \
"    \\item \\textbf{Our Need:} A computationally efficient model bridging analytical clarity with 2D geometrically complex radiation phenomena.\n" + \
"  \\end{itemize}\n" + \
"\\end{frame}\n\n"
new_frames.append(f_prev)

# 5. OUR WORK - OVERVIEW
# Use PRESENTATION OUTLINE but rename
f_over = frames[1]["content"].replace("{PRESENTATION OUTLINE}", "{OUR WORK - OVERVIEW}")
new_frames.append(f_over)

# 6. ASSUMPTIONS
f_ass = "\\begin{frame}{ASSUMPTIONS}\n" + \
"  \\begin{itemize}\n" + \
"    \\item \\textbf{Optically Thick Core:} Transport governed by non-linear radiation diffusion.\n" + \
"    \\item \\textbf{Separation of Variables:} Axial transport decoupled from radial perturbation.\n" + \
"    \\item \\textbf{Material Properties:} Defined via power-law relations for opacity ($\\alpha, \\lambda$) and specific heat.\n" + \
"  \\end{itemize}\n" + \
"\\end{frame}\n\n"
new_frames.append(f_ass)

# 7. STATEMENT OF THE PROBLEM
f_prob = frames[4]["content"].replace("{THE 1D CENTERLINE SOLVER (APPENDIX A)}", "{STATEMENT OF THE PROBLEM}")
new_frames.append(f_prob)

# 8. THE ABLATION REGION 1 (Centerline / Foam compression)
f_abl1 = frames[5]["content"].replace("{WALL LOSS \& FOAM COMPRESSION ($\\rho_{\\text{eff}}$)}", "{THE ABLATION REGION}")
new_frames.append(f_abl1)

# 9. THE ABLATION REGION 2 (Optically thin transport)
f_abl2 = frames[6]["content"].replace("{THE OPTICALLY THIN REGIME \& TRANSPORT LIMITS}", "{THE ABLATION REGION - THIN LIMITS}")
new_frames.append(f_abl2)

# 10. THE SELF SIMILAR EQUATION
f_ss1 = frames[7]["content"].replace("{DYNAMIC OPACITY COUPLING ($g_{\\text{eff}}$)}", "{THE SELF SIMILAR EQUATION - OPACITY COUPLING}")
new_frames.append(f_ss1)

# 11. RESULTS
f_res1 = frames[8]["content"].replace("{DISCREPANCY WITH ADVANCED SIMULATIONS}", "{RESULTS - 1D TRANSPORT DISCREPANCY}")
new_frames.append(f_res1)

# 12. THE SHOCK REGION
f_shk = frames[9]["content"].replace("{2D Bessel CURVATURE MODEL}", "{THE SHOCK REGION - 2D CURVATURE MODEL}")
new_frames.append(f_shk)

# 13. THE SELF SIMILAR EQUATION
f_ss2 = frames[10]["content"].replace("{THE HURRICANE-HAMMER EIGENEQUATION}", "{THE SELF SIMILAR EQUATION - EIGENEQUATION}")
new_frames.append(f_ss2)

# 14. FULL SOLUTION
f_full = frames[11]["content"].replace("{DYNAMIC, TIME-VARYING CURVATURE}", "{FULL SOLUTION}")
new_frames.append(f_full)

# 15. COMPARISON TO NUMERICAL SIMULATIONS
f_cmp1 = frames[12]["content"].replace("{HENYEY TEMPERATURE PROFILE RECONSTRUCTION}", "{COMPARISON TO NUMERICAL SIMULATIONS - SPATIAL}")
new_frames.append(f_cmp1)

# 16. COMPARISON TO NUMERICAL SIMULATIONS
f_cmp2 = frames[13]["content"].replace("{SPATIALLY-RESOLVED RADIATION FLUX CURVATURE}", "{COMPARISON TO NUMERICAL SIMULATIONS - FLUX}")
new_frames.append(f_cmp2)

# 17. COMPARISON TO NUMERICAL SIMULATIONS
f_cmp3 = frames[14]["content"].replace("{WALL INTERFACE \& LATERAL ABLATION PROFILE}", "{COMPARISON TO NUMERICAL SIMULATIONS - ABLATION}")
new_frames.append(f_cmp3)

# 18. PIECEWISE EOS CALCULATION 1
f_piece1 = frames[15]["content"].replace("{THE POST-BREAKOUT TEMPORAL STAGGERING}", "{PIECEWISE EOS CALCULATION - STAGGERING}")
new_frames.append(f_piece1)

# 19. PIECEWISE EOS CALCULATION 2
f_piece2 = frames[16]["content"].replace("{FLUX CURVATURE RESULTS \& VALIDATION ($\\text{Ta}_2\\text{O}_5$)}", "{PIECEWISE EOS CALCULATION - VALIDATION}")
new_frames.append(f_piece2)

# 20. EXPERIMENTAL COMPARISON / PIECEWISE
f_piece3 = frames[17]["content"].replace("{DISCUSSION: EXPERIMENTAL COMPARISON}", "{POST-PROCESSING \& EXPERIMENTAL COMPARISON}")
new_frames.append(f_piece3)

# 21. SUMMARY
f_sum = frames[18]["content"]
new_frames.append(f_sum)

# Reassemble
section_markers = [
    "\\section{Motivation \& Overview}\n",
    "\\section{Problem \& Assumptions}\n",
    "\\section{1D Flow \& Centerline}\n",
    "\\section{2D Curvature \& Shock Extension}\n",
    "\\section{Comparisons \& Summary}\n"
]

out = pre_doc + "\n" + section_markers[0] + \
      new_frames[0] + new_frames[1] + new_frames[2] + new_frames[3] + new_frames[4] + \
      section_markers[1] + new_frames[5] + new_frames[6] + \
      section_markers[2] + new_frames[7] + new_frames[8] + new_frames[9] + new_frames[10] + \
      section_markers[3] + new_frames[11] + new_frames[12] + new_frames[13] + \
      section_markers[4] + "".join(new_frames[14:]) + "\n\\end{document}\n"

with open(r"c:\Users\TLP-001\Documents\GitHub\Project_1_docs\presentation\presentation.tex", "w", encoding="utf-8") as f:
    f.write(out)

