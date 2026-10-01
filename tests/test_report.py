import json
from pathlib import Path

from python_ml_foundations.dataset_inspector.models import DatasetSummary
from python_ml_foundations.dataset_inspector.report import (
    format_json_report,
    format_report,
    format_size,
)


def test_format_size_bytes() -> None:
    """1024バイト未満のサイズがB単位で表示されることを確認します。"""
    assert format_size(500) == "500 B"


def test_format_size_kb() -> None:
    """KB単位への変換が正しく行われることを確認します。"""
    assert format_size(2048) == "2.00 KB"


def test_format_size_mb() -> None:
    """MB単位への変換が正しく行われることを確認します。"""
    assert format_size(1024**2) == "1.00 MB"


def test_format_report() -> None:
    """データセットの概要がレポート文字列へ正しく変換されることを確認します。"""
    summary = DatasetSummary(
        total_files=3,
        total_size_bytes=2048,
        extension_counts={
            ".jpg": 2,
            ".txt": 1,
        },
        largest_file=Path("sample_data/image.jpg"),
    )

    report = format_report(
        summary,
        Path("sample_data"),
    )

    assert "ファイル数: 3" in report
    assert "合計サイズ: 2.00 KB" in report
    assert ".jpg: 2" in report
    assert ".txt: 1" in report
    assert "sample_data/image.jpg" in report


def test_format_json_report() -> None:
    """データセット概要が正しいJSON形式へ変換されることを確認します。"""
    summary = DatasetSummary(
        total_files=2,
        total_size_bytes=1024,
        extension_counts={
            ".jpg": 2,
        },
        largest_file=Path("sample_data/image.jpg"),
    )

    json_text = format_json_report(summary)
    data = json.loads(json_text)

    assert data["total_files"] == 2
    assert data["total_size_bytes"] == 1024
    assert data["extension_counts"] == {
        ".jpg": 2,
    }
    assert data["largest_file"] == "sample_data/image.jpg"
