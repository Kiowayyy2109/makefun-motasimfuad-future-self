import os

LINE = "Future you here: stop rewriting that function. It works. You just do not like how it looks."

LIMIT = 200
if len(LINE) != 91 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 91 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# Future self as the senior dev: stop refactoring what already works.
