#!/usr/bin/env bash
# Link this skill into the global skill directories used by the local agents.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAME="sogeti-html-effectiveness"
TARGETS=(
  "$HOME/.agents/skills"
  "$HOME/.dsh/skills"
  "$HOME/.claude/skills"
  "$HOME/.codex/skills"
  "$HOME/.config/agents/skills"
)

for base in "${TARGETS[@]}"; do
  mkdir -p "$base"
  dest="$base/$NAME"
  if [ -e "$dest" ] && [ ! -L "$dest" ]; then
    echo "skip (real directory): $dest"
    continue
  fi
  ln -sfn "$ROOT" "$dest"
  echo "linked: $dest -> $ROOT"
done

echo "Done. Restart the agent session if the skill does not appear immediately."
