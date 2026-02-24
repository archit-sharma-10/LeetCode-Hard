import os
import re

SRC_DIR = "src/leetcode"
README = "README.md"

# filename: _0287_Find_The_Duplicate_Number.java
file_pattern = re.compile(r"_([0-9]+)_(.+)\.java$")

topic_pattern = re.compile(r"^\s*Topic:\s*(.+)")
time_pattern = re.compile(r"^\s*Time:\s*(.+)")
notes_pattern = re.compile(r"^\s*Notes:\s*(.+)")

rows = []

if not os.path.isdir(SRC_DIR):
    raise RuntimeError(f"Directory not found: {SRC_DIR}")

for fname in os.listdir(SRC_DIR):
    path = os.path.join(SRC_DIR, fname)

    if not os.path.isfile(path):
        continue

    m = file_pattern.match(fname)
    if not m:
        continue

    num = int(m.group(1))
    title = m.group(2).replace("_", " ")

    topic = "—"
    time = "—"
    notes = "—"

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if topic == "—":
                mt = topic_pattern.match(line)
                if mt:
                    topic = mt.group(1).strip()

            if time == "—":
                mt = time_pattern.match(line)
                if mt:
                    time = mt.group(1).strip()

            if notes == "—":
                mn = notes_pattern.match(line)
                if mn:
                    notes = mn.group(1).strip()

    rows.append((num, title, topic, time, notes))

rows.sort(key=lambda x: x[0])

lines = []

# ===== README HEADER =====
lines.append("# LeetCode Problems\n\n")
lines.append("## ✅ Solved Problems\n\n")

# ===== TABLE =====
lines.append("| # | Title | Topic | Time | Notes |\n")
lines.append("|---|------|------|------|------|\n")

for num, title, topic, time, notes in rows:
    lines.append(f"| {num} | {title} | {topic} | {time} | {notes} |\n")

with open(README, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"README updated.")
