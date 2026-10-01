from pathlib import Path

import pytest

from python_ml_foundations.dataset_inspector.errors import DatasetInspectionError
from python_ml_foundations.dataset_inspector.inspector import inspect_dataset


def test_inspect_dataset(tmp_path: Path) -> None:
    """データセットの概要情報が正しく作成されることを確認します。"""
    image_dir = tmp_path / "images"
    text_dir = tmp_path / "texts"

    image_dir.mkdir()
    text_dir.mkdir()

    (image_dir / "a.jpg").write_bytes(b"12345")
    (image_dir / "b.JPG").write_bytes(b"123")
    (text_dir / "note.txt").write_bytes(b"123456789")

    summary = inspect_dataset(tmp_path)

    assert summary.total_files == 3

    assert summary.total_size_bytes == 17

    assert summary.extension_counts == {
        ".jpg": 2,
        ".txt": 1,
    }

    assert summary.largest_file == text_dir / "note.txt"


def test_inspect_dataset_when_os_error(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """ファイルアクセスエラーが独自例外へ変換されることを確認します。"""

    def raise_os_error(directory: Path) -> list[Path]:
        """テスト用にOSErrorを発生させます。"""
        raise OSError("テスト用エラー")

    monkeypatch.setattr(
        "python_ml_foundations.dataset_inspector.inspector.scan_files",
        raise_os_error,
    )

    with pytest.raises(
        DatasetInspectionError,
        match="ファイルアクセスエラー",
    ):
        inspect_dataset(tmp_path)
