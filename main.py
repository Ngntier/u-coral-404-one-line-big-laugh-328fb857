import os
from pathlib import Path

ENTRY = "I bought a standing desk to get healthier. It now displays my snacks at eye level, and my chair has officially filed for unemployment."

# The entry is a single line: write it exactly, with no trailing newline,
# so the file the judge reads is byte-identical to the line above.
def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
