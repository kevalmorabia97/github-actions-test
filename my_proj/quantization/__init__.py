"""Compile and cache the C++ extension on first import."""

from pathlib import Path

from torch.utils.cpp_extension import load

lltm_ext = load(
    name="lltm_ext",
    sources=[Path(__file__).parent / "src/lltm.cpp"],
    verbose=True,
)
