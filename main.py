"""Copy entry.txt to the output directory for the make.fun entry.

The entry is a houseplant's fortune, at most 120 characters.
It is written for a gardener judge, so the voice stays gentle and green.
The leaves reach for light; the roots stay humble and patient.
Water arrives on a Tuesday, right on schedule.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
