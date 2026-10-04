from __future__ import annotations

import copy
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(SCRIPT_DIR))

import reconcile_security_scale_tranche as reconcile  # noqa: E402


class ReconcileSecurityScaleTests(unittest.TestCase):
    def test_successive_future_tranches_reconcile_idempotent_indexes(self) -> None:
        source_manifest = (
            REPO_ROOT / "knowledge-federation/exports/batches/software-seguranca-2000-0003.md"
        ).read_text(encoding="utf-8")
        published = [
            int(match)
            for match in re.findall(r"(?m)^## Tranche (\d+) —", source_manifest)
        ]
        latest = max(published, default=16)
        future = list(range(latest + 1, min(latest + 2, 20) + 1))
        if not future:
            self.skipTest("o lote 3 já está completo; não há tranches futuras para simular")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            knowledge_federation = temp_root / "knowledge-federation"
            paths = [
                Path("README.md"),
                Path("knowledge-federation/README.md"),
                Path("knowledge-federation/README-1M.md"),
                Path("knowledge-federation/STATUS-CONSOLIDACAO-1M.md"),
                Path("knowledge-federation/PLANO-CONTINUO-1M.md"),
                Path("knowledge-federation/RECOVERY-AND-SCALE-NOTE.md"),
                Path("knowledge-federation/exports/batches/software-seguranca-2000-0003.md"),
                Path("knowledge-federation/exports/reports/human-review-queue.md"),
                Path("knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md"),
                Path("knowledge-federation/00-home-vault/Home.md"),
                Path("knowledge-federation/00-home-vault/Indice-Global.md"),
            ]
            for relative in paths:
                destination = temp_root / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(REPO_ROOT / relative, destination)

            def fixture_groups(tranche: int) -> list[dict]:
                groups = copy.deepcopy(reconcile.load_groups(17))
                for group_index, group in enumerate(groups, start=1):
                    group["group_title"] = f"Fixture sintética tranche {tranche} — grupo {group_index}"
                    group["fact_check"] = (
                        "Conferência sintética usada somente para testar reconciliação sequencial. "
                        "Nenhuma alegação factual desta fixture é publicada como nota."
                    )
                    group["coverage_review"] = (
                        "Fixture sintética para testar que a reconciliação conserva e atualiza "
                        "a seção de cobertura anterior entre tranches sem duplicar entradas."
                    )
                    for row_index, row in enumerate(group["notes"], start=1):
                        row["slug"] = f"fixture-tranche{tranche}-g{group_index:02d}-n{row_index:02d}"
                        row["title"] = (
                            f"Fixture de reconciliação da tranche {tranche}, "
                            f"grupo {group_index}, nota {row_index}"
                        )
                return groups

            def apply(tranche: int) -> None:
                groups = fixture_groups(tranche)
                start = (tranche - 1) * 100 + 1
                count = tranche * 100
                valid = 5640 + (tranche - 16) * 100
                ai = 5591 + (tranche - 16) * 100
                active = 5740 + (tranche - 16) * 100
                complete = tranche == 20
                complete_batches = 3 if complete else 2
                report_name = f"ai-review-{reconcile.BATCH_ID}-tranche-{tranche:02d}.md"
                recon_name = f"batch-reconciliation-{reconcile.BATCH_ID}-tranche-{tranche:02d}.md"
                reconcile.update_manifest_and_moc(
                    tranche, start, count, groups, "2026-10-04", report_name, recon_name, complete
                )
                reconcile.update_queue(tranche, start, count, ai, valid, groups, "2026-10-04")
                reconcile.update_global_documents(
                    tranche, count, valid, ai, active, complete_batches, "2026-10-04",
                    report_name, recon_name, complete
                )
                reconcile.write_reconciliation_report(
                    tranche, start, count, valid, ai, active, groups, "2026-10-04", complete,
                    "passou", "passou"
                )

            with patch.object(reconcile, "ROOT", temp_root), patch.object(reconcile, "KF", knowledge_federation):
                for tranche in future:
                    apply(tranche)

            final_tranche = future[-1]
            expected_count = final_tranche * 100
            expected_valid = 5640 + (final_tranche - 16) * 100
            expected_ai = 5591 + (final_tranche - 16) * 100
            expected_active = 5740 + (final_tranche - 16) * 100
            expected_pct = f"{expected_valid / 10000:.4f}".replace(".", ",")
            expected_batch_pct = f"{expected_count / 20:.2f}".replace(".", ",")

            manifest = (knowledge_federation / "exports/batches/software-seguranca-2000-0003.md").read_text()
            moc = (knowledge_federation / "00-home-vault/MOCs/MOC-Seguranca-Software-0009.md").read_text()
            queue = (knowledge_federation / "exports/reports/human-review-queue.md").read_text()
            readme = (knowledge_federation / "README.md").read_text()
            readme_1m = (knowledge_federation / "README-1M.md").read_text()
            root_readme = (temp_root / "README.md").read_text()
            status = (knowledge_federation / "STATUS-CONSOLIDACAO-1M.md").read_text()
            plan = (knowledge_federation / "PLANO-CONTINUO-1M.md").read_text()
            recovery = (knowledge_federation / "RECOVERY-AND-SCALE-NOTE.md").read_text()
            home = (knowledge_federation / "00-home-vault/Home.md").read_text()
            index = (knowledge_federation / "00-home-vault/Indice-Global.md").read_text()

            for tranche in future:
                self.assertEqual(manifest.count(f"## Tranche {tranche} —"), 1)
                self.assertEqual(moc.count(f"## Tranche {tranche} (IDs {(tranche - 1) * 100 + 1}–{tranche * 100})"), 1)
                self.assertTrue(
                    (knowledge_federation / f"exports/reports/batch-reconciliation-{reconcile.BATCH_ID}-tranche-{tranche:02d}.md").is_file()
                )
            self.assertTrue(manifest.endswith("\n"))
            self.assertFalse(manifest.endswith("\n\n"))
            self.assertTrue(moc.endswith("\n"))
            self.assertFalse(moc.endswith("\n\n"))
            self.assertEqual(moc.count("- Reconciliação mais recente:"), 1)
            self.assertIn(
                f"batch-reconciliation-{reconcile.BATCH_ID}-tranche-{final_tranche:02d}.md", moc
            )
            queue_rows = [
                line for line in queue.splitlines()
                if f"| `{reconcile.BATCH_ID}` |" in line
            ]
            queue_positions = [int(line.split("|", 2)[1].strip()) for line in queue_rows]
            self.assertEqual(len(queue_rows), expected_count)
            self.assertEqual(len(set(queue_positions)), len(queue_positions))
            self.assertIn(f"Notas válidas pelo protocolo atual: **{expected_valid}**", readme)
            self.assertIn(f"{expected_valid} notas válidas", readme_1m)
            self.assertNotIn("knowledge-federation/knowledge-federation/", readme_1m)
            self.assertIn(f"{expected_valid} / 1.000.000 ({expected_pct}%)", root_readme)
            self.assertIn(f"## Progresso auditado em 2026-10-04", status)
            self.assertIn(
                f"| Progresso válido global | {expected_valid} / 1.000.000 ({expected_pct}%) |", status
            )
            self.assertIn(
                f"com {expected_count}/2.000 notas válidas", status
            )
            self.assertIn(
                f"| 10 | Atingir a meta e publicar relatório final | **Em andamento; meta não atingida** | "
                f"Progresso atual: {expected_valid} notas válidas", plan
            )
            self.assertIn(f"No diretório ativo `knowledge-federation/domains/` há {expected_active} arquivos", recovery)
            recovery_steps = [
                line for line in recovery.splitlines()
                if line.startswith("4. ") and ("terceiro lote" in line or "lote 3 em" in line)
            ]
            self.assertEqual(len(recovery_steps), 1)
            if final_tranche == 20:
                self.assertEqual(
                    recovery_steps[0],
                    "4. Com o lote 3 em 2.000/2.000, abrir o quarto lote sem contar a preparação como progresso.",
                )
            else:
                self.assertEqual(
                    recovery_steps[0],
                    f"4. Continuar o terceiro lote `{reconcile.BATCH_ID}` "
                    f"({expected_count}/2.000; faltam {2000 - expected_count} notas qualificadas) "
                    "até 2.000 antes de abrir os 497 lotes seguintes.",
                )
            self.assertIn(f"{expected_count} notas do terceiro lote de escala", home)
            self.assertIn(f"- Os lotes atuais totalizam {expected_valid} notas válidas", index)


if __name__ == "__main__":
    unittest.main()
