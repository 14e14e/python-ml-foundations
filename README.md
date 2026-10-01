## Dataset Inspector

指定したディレクトリを再帰的に調査し、以下の情報を表示します。

- ファイル総数
- 合計ファイルサイズ
- 拡張子別ファイル数
- 最大ファイル

### 実行方法

```bash
uv run dataset-inspector ./sample_data
```

### テスト

```bash
uv run pytest
```
### コード品質チェック
```bash
uv run ruff check .
uv run ruff format --check .
```

### README更新後

```bash
git add README.md
git commit -m "文書: データセット調査CLIの使用方法を追加"
```