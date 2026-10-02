from __future__ import annotations

import sys
from pathlib import Path
import unittest

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from note_quality import assess_markdown, inspect_ledger_database  # noqa: E402
from kf_common import init_db  # noqa: E402
from generate_virtual_notes import ensure_virtual_schema  # noqa: E402
from audit_note_quality import markdown_link_index, unresolved_wikilinks  # noqa: E402
from audit_batch import suggested_batch_status  # noqa: E402
from materialize_batch import require_catalog_stub_opt_in  # noqa: E402


GOOD_NOTE = """---
id: software.tests.example.000001
tipo: conceito
dominio: software
subdominio: testes
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: pendente
revisor: \"\"
fontes: [\"https://example.org/spec/v1\", \"https://example.org/guide/testing\"]
---
# A concrete example

## Em uma frase
A testable rule connects an expected behavior to an observable result.

## Por que importa
Teams need evidence that a change preserves an important behavior. A test should describe the reason the behavior matters and the effect a user or dependent component can observe. It should avoid asserting incidental implementation details, because those details can change without changing the contract.

## Como funciona
Set up a known starting condition, perform one action, and assert a result at the boundary that matters. Keep the fixture small. When a failure occurs, the test output should identify the violated expectation without requiring a long investigation. Tests can run at different levels, and each level trades speed for fidelity.

## Exemplo
For a retry-safe request, send the same operation twice with one key and assert that one business object exists. Then send a changed payload with the same key and assert that the API rejects the ambiguous reuse.

## Limites
A passing test proves only the cases and assumptions encoded in that test. It does not establish that the requirements are complete or that the production environment is identical.

## Como verificar
Run the test against the supported runtime, deliberately break the behavior, and check that the test fails for the expected reason. Review whether the assertion would detect a user-visible regression rather than an internal refactor.

## Conexões
- [[other-test]] — related concept.

## Fontes
- [Specification](https://example.org/spec/v1) — normative behavior.
- [Testing guide](https://example.org/guide/testing) — practical test design.
"""


class NoteQualityTests(unittest.TestCase):
    def test_substantive_note_passes_automated_gate(self) -> None:
        result = assess_markdown(GOOD_NOTE, "good.md")
        self.assertTrue(result["ready_for_review"], result["errors"])
        self.assertGreaterEqual(result["word_count"], 100)
        self.assertEqual(result["source_count"], 2)
        self.assertFalse(result["human_reviewed"])

    def test_template_seed_is_not_mistaken_for_a_valid_note(self) -> None:
        seed = """---
id: software.test.000001
tipo: conceito
dominio: software
subdominio: testes
ultima_verificacao: 2026-10-01
validade: volatil
status: semente
fontes: []
---
# Teste — vscale1 #000001
## Em uma frase
Nota semente sobre o tema.
## Por que importa
Esta nota foi criada como registro virtual ledger-first para estudo incremental.
## Como funciona
Em lotes futuros, expanda a nota com fontes iniciais a verificar.
"""
        result = assess_markdown(seed, "seed.md")
        self.assertFalse(result["ready_for_review"])
        self.assertTrue(any(error.startswith("template_phrase:") for error in result["errors"]))
        self.assertIn("placeholder_title", result["errors"])
        self.assertTrue(any(error.startswith("insufficient_specific_sources:") for error in result["errors"]))

    def test_bare_domain_homepages_are_not_specific_sources(self) -> None:
        note = GOOD_NOTE.replace(
            "https://example.org/spec/v1", "https://example.org/"
        ).replace("https://example.org/guide/testing", "https://example.org/")
        result = assess_markdown(note, "generic-sources.md")
        self.assertIn("insufficient_specific_sources:0/2", result["errors"])

    def test_human_review_requires_an_approval_and_reviewer(self) -> None:
        note = GOOD_NOTE.replace("revisao_humana: pendente", "revisao_humana: aprovada")
        self.assertFalse(assess_markdown(note)["human_reviewed"])
        note = note.replace('revisor: ""', "revisor: revisao-tecnica")
        self.assertTrue(assess_markdown(note)["human_reviewed"])

    def test_ai_review_requires_explicit_approval_reviewer_date_and_report(self) -> None:
        reviewed = GOOD_NOTE.replace(
            'revisor: ""',
            'revisor: ""\nrevisao_ia: aprovada\nrevisor_ia: "Arena.ai Agent Mode"\n'
            'data_revisao_ia: 2026-10-01\nrelatorio_revisao_ia: "exports/reports/ai-review.md"',
        )
        result = assess_markdown(reviewed, "ai-reviewed.md")
        self.assertTrue(result["ai_reviewed"])
        self.assertFalse(result["human_reviewed"])
        self.assertTrue(result["valid_reviewed"])

        incomplete = reviewed.replace('relatorio_revisao_ia: "exports/reports/ai-review.md"', "")
        result = assess_markdown(incomplete, "ai-reviewed-incomplete.md")
        self.assertFalse(result["ai_reviewed"])
        self.assertFalse(result["valid_reviewed"])

    def test_batch_can_complete_with_ai_review_without_human_approval(self) -> None:
        self.assertEqual(suggested_batch_status(True, True, 20, 20), "complete")
        self.assertEqual(suggested_batch_status(True, True, 20, 19), "ready_for_review")
        self.assertEqual(suggested_batch_status(False, True, 20, 20), "needs_review")

    def test_catalog_stub_materialization_requires_explicit_opt_in(self) -> None:
        with self.assertRaisesRegex(SystemExit, "Bloqueado"):
            require_catalog_stub_opt_in(1, False)
        self.assertIsNone(require_catalog_stub_opt_in(1, True))
        self.assertIsNone(require_catalog_stub_opt_in(0, False))

    def test_wikilinks_must_resolve_in_the_supplied_vault_index(self) -> None:
        content = "[[known-note]] and [[missing-note|alias]]"
        unresolved = unresolved_wikilinks(content, {"known-note"}, set())
        self.assertEqual(unresolved, ["missing-note|alias"])

    def test_wikilinks_resolve_frontmatter_aliases_and_fragments(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "target.md").write_text(
                '---\naliases: ["Friendly Alias", second-name]\n---\n# Target\n',
                encoding="utf-8",
            )
            known_stems, known_paths = markdown_link_index([root])
        unresolved = unresolved_wikilinks(
            "[[Friendly Alias#Limits|read more]] and [[second-name]]",
            known_stems,
            known_paths,
        )
        self.assertEqual(unresolved, [])

    def test_registry_schemas_track_quality_state(self) -> None:
        import sqlite3

        con = sqlite3.connect(":memory:")
        init_db(con)
        ensure_virtual_schema(con)
        note_columns = {row[1] for row in con.execute("PRAGMA table_info(notes)")}
        virtual_columns = {row[1] for row in con.execute("PRAGMA table_info(virtual_notes)")}
        self.assertIn("quality_status", note_columns)
        self.assertIn("quality_status", virtual_columns)
        con.close()

    def test_ledger_inspection_distinguishes_catalogue_from_content(self) -> None:
        import sqlite3
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "ledger.sqlite"
            con = sqlite3.connect(db)
            con.executescript("""
                CREATE TABLE virtual_notes (
                    id TEXT, title TEXT, summary TEXT, body_seed TEXT,
                    materialized_path TEXT
                );
                INSERT INTO virtual_notes VALUES (
                    'v1', 'Topic vscale1 #000001', 'Nota virtual sobre Topic',
                    'Esta nota foi criada como registro virtual ledger-first.', 'notes/topic.md'
                );
                INSERT INTO virtual_notes VALUES (
                    'v2', 'Other topic', 'Nota virtual sobre Other topic',
                    'Esta nota foi criada como registro virtual ledger-first.', NULL
                );
                CREATE TABLE notes (id TEXT, status TEXT);
                INSERT INTO notes VALUES ('n1', 'drafted');
            """)
            con.commit()
            con.close()
            counts = inspect_ledger_database(db)
        self.assertEqual(counts["virtual_records"], 2)
        self.assertEqual(counts["virtual_materialized"], 1)
        self.assertEqual(counts["virtual_placeholder_records"], 2)
        self.assertEqual(counts["physical_records"], 1)
        self.assertEqual(counts["physical_deep_records"], 0)


if __name__ == "__main__":
    unittest.main()
