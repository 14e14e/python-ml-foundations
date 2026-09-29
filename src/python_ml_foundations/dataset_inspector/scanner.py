from pathlib import Path


def scan_files(directory: Path) -> list[Path]:
    """Return all files under a directory recursively."""
    return [path for path in directory.rglob("*") if path.is_file()]
