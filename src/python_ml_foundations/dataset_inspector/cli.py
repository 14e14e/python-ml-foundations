import argparse
import logging
from pathlib import Path

from python_ml_foundations.dataset_inspector.errors import DatasetInspectionError
from python_ml_foundations.dataset_inspector.inspector import inspect_dataset
from python_ml_foundations.dataset_inspector.logging_utils import (
    configure_logging,
)
from python_ml_foundations.dataset_inspector.report import (
    format_json_report,
    format_report,
)
from python_ml_foundations.dataset_inspector.settings import (
    AppConfig,
    OutputFormat,
)
from python_ml_foundations.dataset_inspector.timing import measure_time

logger = logging.getLogger(__name__)


def validate_directory(value: str) -> Path:
    """CLIから渡された値が有効なディレクトリであることを確認します。"""
    directory = Path(value).expanduser()

    if not directory.exists():
        raise argparse.ArgumentTypeError(f"指定されたパスが存在しません: {directory}")

    if not directory.is_dir():
        raise argparse.ArgumentTypeError(
            f"指定されたパスはディレクトリではありません: {directory}"
        )

    return directory


def build_parser() -> argparse.ArgumentParser:
    """dataset-inspector用のコマンドライン引数パーサーを作成します。"""
    parser = argparse.ArgumentParser(
        prog="dataset-inspector",
        description="指定したディレクトリ内のデータセットを調査します。",
    )

    parser.add_argument(
        "directory",
        type=validate_directory,
        help="調査対象となるディレクトリを指定します。",
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="調査結果をJSON形式で表示します。",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="詳細な実行ログを表示します。",
    )

    return parser


def build_config(args: argparse.Namespace) -> AppConfig:
    """コマンドライン引数からアプリケーション設定を作成します。"""
    output_format = OutputFormat.JSON if args.json else OutputFormat.TEXT

    return AppConfig(
        directory=args.directory,
        output_format=output_format,
        verbose=args.verbose,
    )


def main() -> None:
    """コマンドラインアプリケーションのメイン処理を実行します。"""
    parser = build_parser()
    args = parser.parse_args()

    config = build_config(args)

    configure_logging(config.verbose)

    logger.debug(
        "アプリケーションを開始します。対象: %s",
        config.directory,
    )

    try:
        with measure_time("データセット調査"):
            summary = inspect_dataset(config.directory)

    except DatasetInspectionError as error:
        parser.error(str(error))

    if config.output_format == OutputFormat.JSON:
        report = format_json_report(summary)
    else:
        report = format_report(
            summary,
            config.directory,
        )

    print(report)
