import argparse
from pathlib import Path

import pytest

from python_ml_foundations.dataset_inspector.cli import validate_directory


def test_validate_directory(tmp_path: Path) -> None:
    """存在するディレクトリが正しくPathとして返されることを確認します。"""
    result = validate_directory(str(tmp_path))

    assert result == tmp_path


def test_validate_directory_when_not_exists(
    tmp_path: Path,
) -> None:
    """存在しないパスを指定した場合にエラーになることを確認します。"""
    missing_directory = tmp_path / "存在しないディレクトリ"

    with pytest.raises(argparse.ArgumentTypeError):
        validate_directory(str(missing_directory))


def test_validate_directory_when_file(
    tmp_path: Path,
) -> None:
    """ファイルを指定した場合にエラーになることを確認します。"""
    file_path = tmp_path / "sample.txt"
    file_path.write_text(
        "sample",
        encoding="utf-8",
    )

    with pytest.raises(argparse.ArgumentTypeError):
        validate_directory(str(file_path))
