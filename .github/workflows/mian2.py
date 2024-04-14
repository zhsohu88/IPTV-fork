name: 央视p

on:
  schedule:
    - cron: '0 20 * * *'
  workflow_dispatch:
    分支:
      - main

jobs:
  run_script:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install requests

    - name: Run Python script
      run: python ys.py

    - name: Commit and push if changed
      run: |
        git config --local user.email "github-actions[bot]@users.noreply.github.com"
        git config --local user.name "github-actions[bot]"
        git diff
        if [[ -f "cs.m3u" ]]; then
          git add cs.m3u
        fi
        if ! git diff --staged --quiet; then
          git commit -m "Auto-update live.m3u"
          git push
        fi

    env:
      TZ: Asia/Shanghai
