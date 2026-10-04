"""Cross-note editorial checks for substantive generated prose."""
from __future__ import annotations

from collections import defaultdict
import re
from typing import Iterable

from note_quality import normalize


FRONTMATTER_RE = re.compile(r"\A---[ \t]*\r?\n.*?\r?\n---[ \t]*(?:\r?\n|$)", re.DOTALL)


def repeated_substantive_sentences(
    notes: Iterable[tuple[int, str]],
) -> dict[str, list[int]]:
    """Return exact prose sentences repeated across distinct notes.

    Short fragments and navigation/source sections are ignored. Sentences of
    eight or more words are treated as potential group-level boilerplate so a
    builder can stop and require review before writing a tranche.
    """
    occurrences: dict[str, set[int]] = defaultdict(set)
    for number, content in notes:
        frontmatter = FRONTMATTER_RE.match(content)
        body = content[frontmatter.end():] if frontmatter else content
        section = ""
        for line in body.splitlines():
            heading = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
            if heading:
                section = normalize(heading.group(1).strip())
                continue
            if section in {"fontes", "conexoes"} or not line.strip():
                continue
            for sentence in re.split(r"(?<=[.!?])\s+", line.strip()):
                words = re.findall(r"(?u)\b[\w]+(?:[-'][\w]+)*\b", sentence)
                if len(words) < 8:
                    continue
                normalized = normalize(sentence)
                normalized = re.sub(r"[^\w]+", " ", normalized).strip()
                if normalized:
                    occurrences[normalized].add(number)
    return {
        sentence: sorted(numbers)
        for sentence, numbers in occurrences.items()
        if len(numbers) > 1
    }
