#!/bin/sh
# One-time setup: after every `git pull`, download PDFs for any new arXiv
# papers in the inbox, in the background. Changes no tracked files.
# Run once from the vault root:   sh pipeline/install_hooks.sh
# Undo:                           rm .git/hooks/post-merge .git/hooks/post-rewrite
set -e
root=$(git rev-parse --show-toplevel)
hooks="$root/.git/hooks"
mkdir -p "$hooks"

cat > "$hooks/post-merge" <<'HOOK'
#!/bin/sh
# Installed by pipeline/install_hooks.sh
root=$(git rev-parse --show-toplevel)
py=$(command -v python3 || command -v python) || exit 0
(
  cd "$root" || exit 0
  "$py" -I pipeline/fetch_arxiv.py
) > "$root/.git/fetch_arxiv.log" 2>&1 &
echo "Downloading new paper PDFs in the background (log: .git/fetch_arxiv.log)"
HOOK
chmod +x "$hooks/post-merge"

# `git pull --rebase` fires post-rewrite instead of post-merge
cat > "$hooks/post-rewrite" <<'HOOK'
#!/bin/sh
# Installed by pipeline/install_hooks.sh
[ "$1" = "rebase" ] && exec "$(git rev-parse --show-toplevel)/.git/hooks/post-merge"
exit 0
HOOK
chmod +x "$hooks/post-rewrite"

echo "Installed. PDFs for new arXiv papers will download after each git pull."
