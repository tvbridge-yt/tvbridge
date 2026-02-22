"""Tiny slugify helper.

Lowercases, replaces whitespace and punctuation with single dashes,
and trims leading or trailing dashes. Letters with diacritics are
preserved as-is so non-ASCII titles still produce a usable slug.
"""
from __future__ import annotations

import re

_NON_SLUG = re.compile(r"[^\w\-]+", re.UNICODE)
_DASHES = re.compile(r"-+")


def slugify(value: str) -> str:
    if value is None:
        return ""
    text = value.strip().lower()
    text = text.replace(" ", "-")
    text = _NON_SLUG.sub("-", text)
    text = _DASHES.sub("-", text)
    return text.strip("-")
