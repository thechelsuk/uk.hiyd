#!/usr/bin/env bash
# Re-download the self-hosted webfonts in assets/fonts/ (latin subset only —
# this site is English-only). Run this if assets/css/main.css's font
# families/weights ever change; then update the @font-face src paths there
# to match if filenames change too.
#
# Fonts are self-hosted (rather than @import-ing fonts.googleapis.com)
# specifically so the site works under a strict `default-src 'self'` CSP
# with no font/style exceptions needed.
set -euo pipefail
cd "$(dirname "$0")/.."

UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
mkdir -p assets/fonts

# family-query|output-name|weight
REQS=(
  "Fraunces:opsz,wght@9..144,600|Fraunces|600"
  "Fraunces:opsz,wght@9..144,700|Fraunces|700"
  "Inter:wght@400|Inter|400"
  "Inter:wght@500|Inter|500"
  "Inter:wght@600|Inter|600"
  "Inter:wght@700|Inter|700"
  "JetBrains+Mono:wght@400|JetBrains Mono|400"
  "JetBrains+Mono:wght@500|JetBrains Mono|500"
)

for r in "${REQS[@]}"; do
  IFS='|' read -r fam name weight <<< "$r"
  url=$(curl -s -A "$UA" "https://fonts.googleapis.com/css2?family=${fam}&display=swap" \
    | grep -A6 "/\* latin \*/" | grep -oE "https://fonts.gstatic.com/[^)]+\.woff2")
  slug=$(echo "$name" | tr -d ' ')
  echo "${name} ${weight} -> assets/fonts/${slug}-${weight}.woff2"
  curl -sL -o "assets/fonts/${slug}-${weight}.woff2" "$url"
done
