import logging

import pytest

from python_ml_foundations.dataset_inspector.timing import measure_time


def test_measure_time(
    caplog: pytest.LogCaptureFixture,
) -> None:
    """処理時間がDEBUGログへ出力されることを確認します。"""
    with caplog.at_level(logging.DEBUG), measure_time("テスト処理"):
        pass

    assert "テスト処理を完了しました" in caplog.text
    assert "処理時間:" in caplog.text


def test_measure_time_when_exception_occurs(
    caplog: pytest.LogCaptureFixture,
) -> None:
    """処理中に例外が発生しても処理時間が記録されることを確認します。"""
    with (
        caplog.at_level(logging.DEBUG),
        pytest.raises(RuntimeError),
        measure_time("例外テスト"),
    ):
        raise RuntimeError("テスト用エラー")

    assert "例外テストを完了しました" in caplog.text
