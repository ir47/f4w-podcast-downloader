import sys
from pathlib import Path

# Allow `from util import ...` and `from runner import ...` in tests,
# mirroring the bare imports that runner.py itself uses at runtime.
sys.path.insert(0, str(Path(__file__).parent.parent / "podcastDownloader"))
