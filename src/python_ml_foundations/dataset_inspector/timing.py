import logging
from collections.abc import Generator
from contextlib import contextmanager
from time import perf_counter

logger = logging.getLogger(__name__)


@contextmanager
def measure_time(task_name: str) -> Generator[None, None, None]:
    """指定された処理の実行時間を計測し、DEBUGログへ出力します。"""
    start_time = perf_counter()

    try:
        yield
    finally:
        elapsed_time = perf_counter() - start_time

        logger.debug(
            "%sを完了しました。処理時間: %.3f秒",
            task_name,
            elapsed_time,
        )
