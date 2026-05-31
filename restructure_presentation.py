import re

with open(r"c:\Users\TLP-001\Documents\GitHub\Project_1_docs\presentation\presentation.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Extract pre-document and document
match = re.search(r"(.*?)(\\begin\{document\})(.*)", text, re.DOTALL)
pre_doc = match.group(1) + match.group(2) + "\n"
body = match.group(3)

# Extract frames
frames_raw = re.split(r"\\begin\{frame\}", body)

def get_frame_content(raw):
    end_idx = raw.find(r"\end{frame}")
    return raw[:end_idx] + "\\end{frame}\n\n"

# The first element is pre-frame stuff, but actually Title Slide might be [plain]
frames = []
for i, f in enumerate(frames_raw[1:]):
    if f.startswith("[plain]"):
        title = "Title"
    else:
        title_match = re.match(r"\{(.*?)\}", f)
        title = title_match.group(1) if title_match else "Unknown"
    frames.append({"title": title, "raw": "\\begin{frame}" + get_frame_content(f)})

print("Extracted frames:")
for f in frames:
    print(f["title"])

