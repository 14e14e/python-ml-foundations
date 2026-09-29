from pathlib import Path


def scan_files(directory: Path) -> list[Path]:
    """指定されたディレクトリ内のすべてのファイルをスキャンし、ファイルパスのリストを返します。"""
    return [path for path in directory.rglob("*") if path.is_file()]


def get_extension_counts(files: list[Path]) -> dict[str, int]:
    """Count files by extension."""
    counts: dict[str, int] = {}

    for file in files:
        extension = file.suffix.lower()

        if extension == "":
            extension = "<no_extension>"

        counts[extension] = counts.get(extension, 0) + 1

    return counts


def get_total_size(files: list[Path]) -> int:
    """Return total file size in bytes."""
    return sum(file.stat().st_size for file in files)


def find_largest_file(files: list[Path]) -> Path | None:
    """Return the largest file, or None when no files exist."""
    if not files:
        return None

    return max(
        files,
        key=lambda file: file.stat().st_size,
    )
