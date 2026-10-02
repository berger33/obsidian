# Status da meta ativa: 2.000.000 de notas válidas

Data do status: 2026-10-01. O nome `STATUS-CONSOLIDACAO-1M.md` é mantido por compatibilidade; a meta ativa foi atualizada para **1.000 lotes × 2.000 notas substantivas = 2.000.000**. A revisão humana não é requisito para novas notas; a revisão factual por IA deve ser registrada e não pode ser apresentada como aprovação humana.

## Resumo honesto

O merge preservou um catálogo histórico com **1.000.000 de registros virtuais** e texto-template em todos eles. Esse acervo não é conteúdo validado nem progresso da meta ativa. A auditoria de arquivos reais encontrou 289 notas Markdown ativas; 189 são substantivas, passaram pelo gate e receberam revisão factual registrada. As outras 100 mantêm pendências e continuam fora da contagem válida.

A meta final não foi atingida. Só contam notas substantivas com fontes específicas conferidas, gate aprovado e revisão factual registrada. Lotes incompletos e seus resultados devem ser reportados como progresso parcial; placeholders, IDs e materialização de arquivos não contam.

## Progresso auditado em 2026-10-01

| Métrica | Quantidade | Interpretação |
|---|---:|---|
| Meta ativa | 2.000.000 | 1.000 lotes completos × 2.000 notas válidas por lote |
| Lotes completos | 0 / 1.000 | O lote iniciado ainda não tem 2.000 notas |
| Progresso válido global | 189 / 2.000.000 (0,00945%) | 49 revisões humanas históricas + 140 revisões por IA registradas separadamente |
| Revisões humanas registradas | 49 | Aprovadas pelo usuário; não se estendem a conteúdo novo |
| Revisões factuais por IA registradas | 140 | Relatório individual no lote `software-testes-2000-0001`; não são humanas |
| Primeiro lote | 149 / 2.000 | 149 notas materiais válidas: 9 humanas + 140 IA; faltam 1.851 notas substantivas |
| Candidatas que passaram pelo gate automatizado | 189 | Todas receberam revisão factual registrada; gate sozinho não comprova veracidade |
| Arquivos Markdown ativos com pendências de qualidade | 100 | Sementes/legado; não contam até remediação e revisão |
| Registros virtuais no checkpoint histórico | 1.000.000 | Catálogo com template; excluído da contagem de notas válidas |
| Marcadores de conteúdo-template no ledger legado | 1.000.000 | Sumários/corpos-semente; não são notas substantivas |
| Caminhos marcados como materializados no checkpoint | 8.000 | Materialização não é validação editorial |
| Links wiki quebrados no Study Vault legado | 0 no relatório anterior | Auditoria de links não valida conteúdo factual |

A sequência de lotes no TAR e os 78 Study Packs continuam disponíveis como artefatos históricos. Seus números descrevem arquivos/entradas gerados a partir do ledger; as notas-template não entram na meta de conteúdo válido. O TAR é um snapshot anterior às aprovações registradas e não foi reconstruído.

## Trabalho feito nesta retomada

1. Adicionado gate reproduzível em `scripts/note_quality.py` e `scripts/audit_note_quality.py` para estrutura, conteúdo mínimo, fontes específicas, links e marcadores de template.
2. Separados os estados de revisão factual humana e por IA; o relatório de IA, responsável e data são obrigatórios para contar uma nota revisada por IA.
3. Atualizado `audit_batch.py`: um lote só pode ser `complete` após o gate e uma revisão factual registrada para cada nota, humana ou por IA.
4. Preservadas as 49 aprovações humanas anteriores, sem estendê-las a novas notas.
5. Revisadas factualmente por IA as 140 notas materiais 10–149 do lote de escala. Relatórios: [`tranches 2–3`](exports/reports/ai-review-software-testes-2000-0001.md), [`tranche 4`](exports/reports/ai-review-software-testes-2000-0001-tranche-04.md), [`tranche 5`](exports/reports/ai-review-software-testes-2000-0001-tranche-05.md), [`tranche 6`](exports/reports/ai-review-software-testes-2000-0001-tranche-06.md) e [`tranche 7`](exports/reports/ai-review-software-testes-2000-0001-tranche-07.md).
6. Resultado parcial do primeiro lote: 149/149 aprovadas pelo gate; 9 revisões humanas, 140 revisões por IA; 149 notas qualificadas sob o protocolo atualizado. O lote segue `in_progress` com meta de 2.000.
7. Mantidas as cinco séries autorais anteriores (40 notas humanas aprovadas) e as 100 notas legadas com falhas em suas filas próprias.

Relatório global: [`exports/reports/note-quality-audit.md`](exports/reports/note-quality-audit.md). Relatório do lote: [`exports/reports/note-quality-software-testes-2000-0001.md`](exports/reports/note-quality-software-testes-2000-0001.md). Registros separados por tipo de revisão: [`exports/reports/human-review-queue.md`](exports/reports/human-review-queue.md). Plano de continuidade: [`PLANO-CONTINUO-1M.md`](PLANO-CONTINUO-1M.md).

## Protocolo de qualidade e contagem

Uma nota candidata deve ter frontmatter rastreável, pelo menos 100 palavras, seções de explicação, exemplo, limites e verificação, duas fontes HTTPS específicas, wikilinks resolvidos e nenhum marcador conhecido de conteúdo-template. O gate é conservador e não avalia por si só se uma afirmação é verdadeira.

A contagem exige simultaneamente conteúdo substantivo, gate aprovado e revisão factual registrada:

- Humana: `revisao_humana: aprovada` + revisor humano identificado, apenas se a pessoa realmente revisou/aprovou.
- IA: `revisao_ia: aprovada`, `revisor_ia`, `data_revisao_ia` e `relatorio_revisao_ia`, após conferir as afirmações contra fontes específicas.

Os dois tipos de revisão são contabilizados separadamente. Revisão por IA não se transforma em aprovação humana. Em domínios regulados, podem existir requisitos adicionais de especialista e de segurança de conteúdo.

## Comandos de reprodução

```bash
python3 -m unittest discover -s knowledge-federation/tests -v
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

## Próximos marcos sem inflar contagens

1. Continuar o primeiro lote em tranches de notas reais até completar 2.000; conferir e registrar cada tranche antes de somar.
2. Só então iniciar o lote 2, repetindo o mesmo protocolo até completar 1.000 lotes.
3. Rodar gate, auditoria de links, deduplicação e revisão factual em cada tranche; regenerar manifesto, filas, relatórios e MOC.
4. Remediar as 100 sementes legadas apenas com fontes próprias e conteúdo substantivo; mantê-las fora da contagem enquanto houver pendências.
5. Publicar relatório final apenas depois de atingir 2.000.000 de notas válidas (1.000 lotes completos), nunca a partir de contagem de IDs ou placeholders.
