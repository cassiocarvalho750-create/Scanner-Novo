name: Scanner DIDI ADX BB

on:
  schedule:
    # horarios em UTC. Brasilia = UTC-3.
    # 13h BR = 16h UTC | 16h BR = 19h UTC | 19h BR = 22h UTC
    - cron: '0 16,19,22 * * 1-5'   # seg a sex
  workflow_dispatch:   # permite rodar manualmente pelo botao tambem

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - name: Baixar os arquivos do repositorio
        uses: actions/checkout@v4

      - name: Instalar Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Instalar bibliotecas
        run: pip install yfinance pandas numpy

      - name: Rodar o scanner e gerar o site
        run: python run_cloud.py

      - name: Publicar no GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
