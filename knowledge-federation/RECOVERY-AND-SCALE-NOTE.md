# Retomada pós-merge: escala com qualidade

Data: 2026-10-01. A meta ativa substituiu o escopo anterior: **1.000 lotes × 2.000 notas substantivas = 2.000.000 notas válidas**. Revisão humana não é obrigatória para notas novas; revisão factual por IA é aceita somente quando registrada separadamente, com relatório.

## Estado observado

Os artefatos massivos permanecem como arquivos históricos compactados; não precisam ser recriados para continuar. O checkpoint legado contém 1.000.000 de registros virtuais, 8.000 caminhos marcados como materializados e 100 registros físicos iniciais. A auditoria encontrou marcadores de texto-template nos 1.000.000 registros virtuais, e os 100 arquivos físicos iniciais têm pendências no gate. Eles não contam como notas válidas.

No diretório ativo `knowledge-federation/domains/` há 179 arquivos: 100 notas legadas com pendências e 79 notas autorais substantivas. As 79 passaram pelo gate e receberam revisão factual: 49 aprovações humanas históricas e 30 revisões por IA. O primeiro lote `software-testes-2000-0001` contém 39 notas qualificadas de 2.000 (9 humanas + 30 IA); está em andamento. Veja os [relatórios globais](exports/reports/note-quality-audit.md), o [manifesto](exports/batches/software-testes-2000-0001.md), os relatórios de IA ([tranches 2–3](exports/reports/ai-review-software-testes-2000-0001.md), [tranche 4](exports/reports/ai-review-software-testes-2000-0001-tranche-04.md)) e o [registro de revisões](exports/reports/human-review-queue.md).

## Decisão técnica e estados

Manter a arquitetura ledger-first para inventário, sem confundir catálogo com conteúdo. Separar explicitamente:

1. **catalogada** — ID e taxonomia; não conta como conteúdo;
2. **candidata** — nota substantiva e gate automatizado aprovado;
3. **validada** — fontes/afirmações confrontadas e revisão factual registrada por pessoa ou IA; tipo e responsável ficam explícitos;
4. **rejeitada/needs-review** — não contabilizada até ser corrigida e revisada.

Materializar um arquivo Markdown não muda por si só seu estado. Revisão por IA não é aprovação humana. Geradores de sementes servem ao planejamento, não à contagem de notas válidas.

## Ferramentas

- `scripts/note_quality.py` — regras reutilizáveis de gate, com revisão humana e revisão por IA distintas.
- `scripts/audit_note_quality.py` — auditoria de arquivos ativos e, opcionalmente, do checkpoint SQLite compactado.
- `scripts/audit_batch.py` — só marca um lote `complete` quando todas as notas passam pelos gates e têm revisão factual humana ou por IA registrada.
- `tests/test_note_quality.py` — regressões do gate para notas completas, placeholders, fontes, links e metadata de revisão humana/IA.

## Comandos de retomada

```bash
python3 -m unittest discover -s knowledge-federation/tests -v
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

## Próximo ciclo

1. Continuar o lote atual em tranches de notas reais até completar 2.000, sem IDs reservados ou placeholders.
2. Para cada nota, consultar as fontes específicas, revisar as afirmações e registrar um relatório factual por IA antes de contar.
3. Auditar gate, fontes, links, duplicatas e segurança; atualizar manifesto, índice, filas e contadores.
4. Só iniciar o próximo lote de 2.000 após fechar o atual. Repetir até 1.000 lotes completos.
5. Publicar o relatório final apenas ao concluir os 2.000.000 de notas válidas.
