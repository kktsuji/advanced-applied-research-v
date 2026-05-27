# advanced-applied-research-v

Lecture report of university

## Usage

### Generate Report PDF

1. `git clone git@github.com:kktsuji/advanced-applied-research-4.git` on WSL
2. `cd advanced-applied-research-4`
3. `docker build -t pandoc/japanese .` to build the Docker image
4. Execute following command to generate PDF file from Markdown file:

```bash
docker run --rm \
       --volume "$(pwd):/data" \
       --user $(id -u):$(id -g) \
       pandoc/japanese \
       docs/report.md \
       -o docs/report.pdf \
       --resource-path=docs \
       --pdf-engine=lualatex -V documentclass=ltjsarticle
```

### Regenerate Figures

レポート内の図は事前にレンダリングした PNG (`docs/figs/*.png`) を画像参照する方式で運用しています。図のソースを変更した場合は以下の手順で再生成してください。

#### Mermaid 図（図1, 2, 8, 9）

ソースは `docs/figs/src/*.mmd` にあります。`mermaid-cli` の Docker イメージで PNG にレンダリングします。

```bash
for name in sdlc_workflow spec_kit_workflow variability_suppression value_creation; do
  docker run --rm -u $(id -u):$(id -g) \
    -v "$(pwd)/docs/figs:/data" \
    minlag/mermaid-cli \
    -i "src/${name}.mmd" -o "${name}.png" -b transparent -s 2
done
```

#### Matplotlib 図（図3, 4, 5, 6, 7）

ソースは `scripts/generate_figures.py` です。Python は venv を使ってください。

```bash
python -m venv .venv
source .venv/bin/activate
pip install matplotlib numpy  # 初回のみ
python scripts/generate_figures.py
```
