import logging


def configure_logging(verbose: bool) -> None:
    """実行モードに応じてログ出力を設定します。"""
    level = logging.DEBUG if verbose else logging.WARNING

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
