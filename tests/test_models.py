from pathlib import Path

from python_ml_foundations.dataset_inspector.models import DatasetSummary


def test_total_size_mb() -> None:
    """バイト単位のサイズがMB単位へ正しく変換されることを確認します。"""
    summary = DatasetSummary(
        total_files=1,
        total_size_bytes=1024**2,
        extension_counts={".txt": 1},
        largest_file=Path("sample.txt"),
    )

    assert summary.total_size_mb == 1.0
