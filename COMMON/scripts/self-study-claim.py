#!/usr/bin/env python3
"""Klaim topik self-study — koordinasi PC & SERVER agar saling melengkapi, tidak duplikat.

Status baris di COMMON/self-study/topics.md:
  - [ ] <topik>                  = bebas (belum dikerjakan siapa pun)
  - [p] <topik> [klaim <tgl> PC] = sedang dikerjakan PC (lokal)
  - [s] <topik> [klaim <tgl> SERVER] = sedang dikerjakan server (24/7)
  - [x] <topik> ...               = selesai

Pemakaian:
  python3 self-study-claim.py --claim PC|SERVER   # ambil topik pertama yang bebas (atau klaim basi >24 jam)
  python3 self-study-claim.py --status            # lihat status semua baris

Kalau tidak ada topik bebas → stdout "NONE".
File ditulis langsung (tanpa commit); pemanggil WAJIB git commit segera setelah klaim
supaya mesin lain tidak mengambil topik yang sama.
"""
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

TOPICS = Path(__file__).resolve().parent.parent.parent / "COMMON" / "self-study" / "topics.md"
STALE = timedelta(hours=24)
OWNERS = {"pc": "PC", "server": "SERVER"}


def parse_claim(line):
    m = re.match(r'^- \[(.)\] (.*)$', line)
    if not m:
        return None
    mark, rest = m.group(1), m.group(2)
    if mark == ' ':
        return ('free', None)
    if mark == 'x':
        return ('done', None)
    cm = re.search(r'\[([sp])\] (\d{4}-\d{2}-\d{2} \d{2}:\d{2}) (\w+)', rest)
    if cm:
        try:
            when = datetime.strptime(cm.group(2), "%Y-%m-%d %H:%M")
        except ValueError:
            when = None
        return ('claimed', (cm.group(1), when, cm.group(3)))
    return ('claimed', ('?', None, '?'))


def main():
    args = sys.argv[1:]
    if not args or args[0] not in ('--claim', '--status'):
        print("Usage: self-study-claim.py --claim PC|SERVER | --status")
        return 2
    text = TOPICS.read_text(encoding='utf-8')
    lines = text.splitlines()
    if args[0] == '--status':
        for line in lines:
            if parse_claim(line):
                print(line)
        return 0

    owner = OWNERS.get(args[1].lower())
    if not owner:
        print("owner harus PC atau SERVER")
        return 2
    now = datetime.now()
    for i, line in enumerate(lines):
        p = parse_claim(line)
        if not p or p[0] == 'done':
            continue
        if p[0] == 'free':
            mark = 'p' if owner == 'PC' else 's'
            topic = line[5:].strip()
            lines[i] = f"- [{mark}] {topic} [klaim {now:%Y-%m-%d %H:%M} {owner}]"
            TOPICS.write_text("\n".join(lines) + "\n", encoding='utf-8')
            print(topic)
            return 0
        if p[0] == 'claimed':
            kind, when, who = p[1]
            stale = (kind == '?' or when is None or (now - when) > STALE)
            if stale:
                mark = 'p' if owner == 'PC' else 's'
                cleaned = re.sub(r' \[(?:klaim|re-klaim) \d{4}-\d{2}-\d{2} \d{2}:\d{2} \w+\]', '', line)
                cleaned = re.sub(r'^- \[[sp]\]', f'- [{mark}]', cleaned)
                lines[i] = cleaned + f" [re-klaim {now:%Y-%m-%d %H:%M} {owner}]"
                TOPICS.write_text("\n".join(lines) + "\n", encoding='utf-8')
                topic = re.sub(r'\[re-klaim.*', '', cleaned).strip()
                topic = re.sub(r'^- \[\w\] ', '', topic)
                print(topic)
                return 0
    print("NONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())