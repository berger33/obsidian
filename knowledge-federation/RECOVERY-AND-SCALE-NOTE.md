# Retomada pós-merge: escala com qualidade

Atualizado em 2026-10-03. A meta ativa é **500 lotes × 2.000 notas substantivas = 1.000.000 de notas válidas**. Revisão humana não é obrigatória para novas notas; revisão factual por IA é aceita somente quando registrada separadamente, com relatório.

## Estado editorial atual

Os artefatos massivos permanecem como arquivos históricos compactados e não precisam ser recriados para continuar. O checkpoint legado contém 1.000.000 de registros virtuais, 8.000 caminhos marcados como materializados e 100 registros físicos iniciais. Os registros virtuais têm texto-template e os arquivos legados têm pendências; não contam como notas válidas.

No diretório ativo `knowledge-federation/domains/` há 5240 arquivos: 100 legados com pendências e 5140 notas válidas pelo protocolo atual (49 aprovações humanas históricas + 5091 revisões por IA). O primeiro lote `software-testes-2000-0001` atingiu 2000/2.000 notas válidas (9 humanas + 1991 IA, `complete`); o segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`, [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em andamento (`in_progress`) com 1100/2.000 notas válidas revisadas por IA até a [tranche 11](exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md), com [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-11.md); as notas 550–649 passaram pelo gate e têm relatório de revisão factual por IA da [tranche 12](exports/reports/ai-review-software-testes-2000-0001-tranche-12.md); as notas 450–549 estão na [tranche 11](exports/reports/ai-review-software-testes-2000-0001-tranche-11.md), e as 350–449 na [tranche 10](exports/reports/ai-review-software-testes-2000-0001-tranche-10.md).

## Decisão técnica e estados

Manter inventário e conteúdo separados, sem confundir catálogo com conhecimento:

1. **catalogada** — ID e taxonomia; não conta como conteúdo;
2. **candidata** — nota substantiva e gate automatizado aprovado;
3. **validada** — fontes/afirmações confrontadas e revisão factual registrada por pessoa ou IA, com tipo e responsável explícitos;
4. **rejeitada/needs-review** — não contabilizada até correção e revisão.

Materializar um arquivo Markdown não muda seu estado. Revisão por IA não é aprovação humana. Geradores de sementes servem ao planejamento, não à contagem de notas válidas.

## Ferramentas e comandos

- `scripts/note_quality.py` — regras reutilizáveis de gate e distinção de revisões.
- `scripts/audit_note_quality.py` — auditoria de arquivos ativos e do checkpoint SQLite compactado.
- `scripts/audit_batch.py` — só marca lote `complete` quando todas as notas passam gate e têm revisão factual registrada.
- `tests/test_note_quality.py` — regressões do gate para conteúdo, fontes, links e metadata de revisão.

```bash
python3 -m unittest discover -s knowledge-federation/tests -v
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

## Próximo ciclo

1. Primeiro lote (`software-testes-2000-0001`) concluído com 2.000/2.000 notas qualificadas em tranches de conteúdo real.
2. Consultar fontes específicas, revisar afirmações e registrar relatório factual por IA antes de contar cada nota nova.
3. Auditar gate, fontes, links e duplicatas; atualizar manifesto, índice, fila e métricas.
4. Continuar o terceiro lote `software-seguranca-2000-0003` (1100/2.000; faltam 900 notas qualificadas) até 2.000 antes de abrir os 497 lotes seguintes.
5. Publicar o relatório final apenas após atingir 1.000.000 de notas válidas.
