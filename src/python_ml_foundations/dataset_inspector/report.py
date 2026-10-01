import json
from pathlib import Path

from python_ml_foundations.dataset_inspector.models import DatasetSummary


def format_size(size_bytes: int) -> str:
    """バイト単位のファイルサイズを、人間が読みやすい形式へ変換します。"""
    if size_bytes < 1024:
        return f"{size_bytes} B"

    size_kb = size_bytes / 1024

    if size_kb < 1024:
        return f"{size_kb:.2f} KB"

    size_mb = size_kb / 1024

    if size_mb < 1024:
        return f"{size_mb:.2f} MB"

    size_gb = size_mb / 1024

    return f"{size_gb:.2f} GB"


def format_report(
    summary: DatasetSummary,
    directory: Path,
) -> str:
    """データセットの調査結果を、人間が読みやすい文字列へ整形します。"""
    lines = [
        "データセット調査結果",
        "=" * 24,
        f"対象ディレクトリ: {directory}",
        f"ファイル数: {summary.total_files}",
        f"合計サイズ: {format_size(summary.total_size_bytes)}",
        "",
        "拡張子別ファイル数:",
    ]

    for extension, count in sorted(summary.extension_counts.items()):
        lines.append(f"  {extension}: {count}")

    lines.extend(
        [
            "",
            "最大ファイル:",
            f"  {summary.largest_file or 'なし'}",
        ]
    )

    return "\n".join(lines)


def format_json_report(summary: DatasetSummary) -> str:
    """データセットの調査結果をJSON形式の文字列へ変換します。"""
    return json.dumps(
        summary.to_dict(),
        ensure_ascii=False,
        indent=2,
    )
