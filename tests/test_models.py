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


def test_to_dict() -> None:
    """データセット概要がJSON変換可能な辞書へ正しく変換されることを確認します。"""
    summary = DatasetSummary(
        total_files=2,
        total_size_bytes=1024,
        extension_counts={
            ".jpg": 2,
        },
        largest_file=Path("sample.jpg"),
    )

    data = summary.to_dict()

    assert data["total_files"] == 2
    assert data["total_size_bytes"] == 1024
    assert data["total_size_mb"] == 1024 / (1024**2)
    assert data["extension_counts"] == {
        ".jpg": 2,
    }
    assert data["largest_file"] == "sample.jpg"
