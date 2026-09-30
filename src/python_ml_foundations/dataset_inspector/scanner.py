from pathlib import Path


def scan_files(directory: Path) -> list[Path]:
    """指定されたディレクトリ内のすべてのファイルを再帰的に取得します。"""
    return [path for path in directory.rglob("*") if path.is_file()]


def get_extension_counts(files: list[Path]) -> dict[str, int]:
    """ファイルの拡張子ごとの件数を集計します。"""
    counts: dict[str, int] = {}

    for file in files:
        extension = file.suffix.lower()

        if extension == "":
            extension = "<拡張子なし>"

        counts[extension] = counts.get(extension, 0) + 1

    return counts


def get_total_size(files: list[Path]) -> int:
    """指定されたファイル一覧の合計サイズをバイト単位で返します。"""
    return sum(file.stat().st_size for file in files)


def find_largest_file(files: list[Path]) -> Path | None:
    """最もサイズの大きいファイルを返し、ファイルが存在しない場合はNoneを返します。"""
    if not files:
        return None

    return max(
        files,
        key=lambda file: file.stat().st_size,
    )
