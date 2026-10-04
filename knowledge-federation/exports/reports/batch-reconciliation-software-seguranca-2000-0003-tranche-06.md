# Reconciliação estrutural — lote `software-seguranca-2000-0003`, tranche 06

- Data: 2026-10-03
- Revisor da reconciliação: `Arena.ai Agent Mode`
- Escopo: conciliação entre os **600 arquivos Markdown materiais** em `knowledge-federation/domains/software-0009/software/seguranca/` (IDs 1–600, tranches 1–6), o manifesto [`software-seguranca-2000-0003.md`](../batches/software-seguranca-2000-0003.md), o MOC [`MOC-Seguranca-Software-0009.md`](../../00-home-vault/MOCs/MOC-Seguranca-Software-0009.md), o registro [`human-review-queue.md`](human-review-queue.md) e os documentos globais de status.

## Verificações executadas

1. **Correspondência 1:1 de arquivos no lote 3**:
   - Arquivos `.md` em `knowledge-federation/domains/software-0009/software/seguranca/`: **600** (100 da tranche 1 + 100 da tranche 2 + 100 da tranche 3 + 100 da tranche 4 + 100 da tranche 5 + 100 da tranche 6).
   - Entradas numeradas no manifesto `software-seguranca-2000-0003.md`: **600** (`1` a `600`).
   - Entradas numeradas no MOC `MOC-Seguranca-Software-0009.md`: **600** (`1` a `600`).
2. **Gate automatizado de qualidade (`audit_note_quality.py`)**:
   - Lote `software-seguranca-2000-0003`: **600/600 aprovadas**, **0** com pendências.
   - Global (`knowledge-federation/domains/`): **4740** arquivos ativos, **4640** válidas (**49** humanas históricas + **4591** revisadas por IA), **100** notas legadas com pendências excluídas da meta.
3. **Separação explícita entre revisão humana e revisão por IA**:
   - `revisao_humana: aprovada` permanece restrito às **49** notas históricas.
   - As 100 notas da tranche 06 do lote 3 (`software.seguranca.tranche06.000501` a `000600`) trazem `revisao_humana: nao_solicitada`, `revisor: ""`, `revisao_ia: aprovada`, `revisor_ia: "Arena.ai Agent Mode"` e apontam para [`ai-review-software-seguranca-2000-0003-tranche-06.md`](ai-review-software-seguranca-2000-0003-tranche-06.md).
   - No registro `human-review-queue.md`, as linhas **4541–4640** foram inseridas como `APROVADA POR IA`.
4. **Status do lote 3**:
   - Lote 1 (`software-testes-2000-0001`): `2000 / 2.000` (`100,00%`), status `complete`.
   - Lote 2 (`software-devops-2000-0002`): `2000 / 2.000` (`100,00%`), status `complete`.
   - Lote 3 (`software-seguranca-2000-0003`): `600 / 2.000` (`30,00%`), status `in_progress`, faltando 1.400 notas materiais.
   - Lotes completos no programa de 1M: **2 / 500**.
