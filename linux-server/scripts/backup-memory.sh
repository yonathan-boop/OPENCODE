#!/bin/bash
set -u

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

REPO=/root/memory
LOG=/var/log/memory-backup.log
BRANCH=main

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG"
}

cd "$REPO" || { log "ERROR: cannot cd to $REPO"; exit 1; }

if ! git pull --rebase origin "$BRANCH" >>"$LOG" 2>&1; then
    log "PULL FAILED - detail stderr di atas"
    exit 1
fi

git add -A

if git diff --cached --quiet; then
    log "no changes"
    exit 0
fi

if ! git commit -m "auto-backup $(date '+%Y-%m-%d %H:%M')" >>"$LOG" 2>&1; then
    log "COMMIT FAILED"
    exit 1
fi

ncommits=$(git rev-list --count "origin/$BRANCH..HEAD")

if ! git push origin "$BRANCH" >>"$LOG" 2>&1; then
    log "PUSH FAILED - detail stderr di atas"
    exit 1
fi

log "SUCCESS: $ncommits commit(s) pushed to origin/$BRANCH (HEAD $(git rev-parse --short HEAD))"
exit 0
