# Status da meta ativa: 1.000.000 de notas válidas

Data do status: 2026-10-03. A meta editorial ativa é **500 lotes × 2.000 notas substantivas = 1.000.000 de notas válidas**. Revisão humana não é requisito para novas notas; cada revisão factual por IA é registrada separadamente e nunca é apresentada como aprovação humana.

## Resumo honesto

O checkpoint histórico contém **1.000.000 de registros virtuais** com texto-template; não é conteúdo validado nem progresso da meta ativa. A auditoria encontrou 5440 arquivos Markdown ativos: 5340 notas substantivas passaram pelo gate e receberam revisão factual registrada (49 humanas históricas + 5291 por IA); outras 100 mantêm pendências e continuam fora da contagem.

A meta final não foi atingida. Só contam notas substantivas com fontes específicas conferidas, gate aprovado e revisão factual registrada. O primeiro lote (`software-testes-2000-0001`) está completo com 2.000 notas substantivas; placeholders, IDs e materialização de arquivos não contam.

## Progresso auditado em 2026-10-03

| Métrica | Quantidade | Interpretação |
|---|---:|---|
| Meta ativa | 1.000.000 | 500 lotes completos × 2.000 notas válidas por lote |
| Lotes completos | 2 / 500 | Dois primeiros lotes (`software-testes-2000-0001` e `software-devops-2000-0002`) concluídos com 2.000 notas cada |
| Progresso válido global | 5340 / 1.000.000 (0,5340%) | 49 revisões humanas históricas + 5291 revisões por IA registradas separadamente |
| Revisões humanas registradas | 49 | Aprovadas pelo usuário; não se estendem a conteúdo novo |
| Revisões factuais por IA registradas | 5291 | Relatórios das tranches 2–26 (`software-testes-2000-0001`), tranches 1–20 (`software-devops-2000-0002`) e tranches 1–13 (`software-seguranca-2000-0003`); não são humanas |
| Primeiro lote (`software-testes-2000-0001`) | 2000 / 2.000 (100%) | 9 humanas + 1991 IA; lote concluído (`complete`) |
| Segundo lote (`software-devops-2000-0002`) | 2000 / 2.000 (100,00%) | 2000 IA nas tranches 1–20 ([tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md)); lote concluído (`complete`) |
| Terceiro lote (`software-seguranca-2000-0003`) | 1300 / 2.000 (65,00%) | 1300 IA nas tranches 1–13 ([tranche 13](exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md)); faltam 700 notas substantivas |
| Candidatas que passaram pelo gate automatizado | 5340 | Todas receberam revisão factual registrada; gate sozinho não comprova veracidade |
| Arquivos Markdown ativos com pendências de qualidade | 100 | Sementes/legado; não contam até remediação e revisão |
| Registros virtuais no checkpoint histórico | 1.000.000 | Catálogo com template; excluído da contagem de notas válidas |
| Marcadores de conteúdo-template no ledger legado | 1.000.000 | Sumários/corpos-semente; não são notas substantivas |
| Caminhos marcados como materializados no checkpoint | 8.000 | Materialização não é validação editorial |
| Links wiki quebrados no Study Vault legado | 0 no relatório anterior | Auditoria de links não valida conteúdo factual |

A sequência de lotes no TAR e os 78 Study Packs continuam disponíveis como artefatos históricos. Seus números descrevem arquivos/entradas gerados a partir do ledger; as notas-template não entram na meta de conteúdo válido. O TAR é um snapshot anterior às aprovações registradas e não foi reconstruído.

## Trabalho feito nesta retomada

1. Mantidos gate reproduzível e registro separado de revisão humana e por IA; o relatório, responsável e data são obrigatórios para contar revisão por IA.
2. Preservadas as 49 aprovações humanas anteriores, sem estendê-las a novas notas.
3. Revisadas factualmente por IA as notas 10–2000 do lote (1991 no total), com relatórios das [tranches 2–3](exports/reports/ai-review-software-testes-2000-0001.md), [4](exports/reports/ai-review-software-testes-2000-0001-tranche-04.md), [5](exports/reports/ai-review-software-testes-2000-0001-tranche-05.md), [6](exports/reports/ai-review-software-testes-2000-0001-tranche-06.md), [7](exports/reports/ai-review-software-testes-2000-0001-tranche-07.md), [8](exports/reports/ai-review-software-testes-2000-0001-tranche-08.md), [9](exports/reports/ai-review-software-testes-2000-0001-tranche-09.md), [10](exports/reports/ai-review-software-testes-2000-0001-tranche-10.md), [11](exports/reports/ai-review-software-testes-2000-0001-tranche-11.md) e [12](exports/reports/ai-review-software-testes-2000-0001-tranche-12.md) [13](exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md), [15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md), [16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md), [17](exports/reports/ai-review-software-testes-2000-0001-tranche-17.md), [18](exports/reports/ai-review-software-testes-2000-0001-tranche-18.md), [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md), [23](exports/reports/ai-review-software-testes-2000-0001-tranche-23.md), [24](exports/reports/ai-review-software-testes-2000-0001-tranche-24.md), [25](exports/reports/ai-review-software-testes-2000-0001-tranche-25.md) e [26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md).
4. Resultado final do primeiro lote: 2000/2000 aprovadas pelo gate; nove revisões humanas e 1991 revisões por IA no total após a tranche 26, incluindo as 41 novas revisões das notas 1960–2000. O lote atingiu o alvo de 2.000 e passa ao estado `complete`. O segundo lote [`software-devops-2000-0002`](exports/batches/software-devops-2000-0002.md) atingiu 2000/2.000 notas válidas (`complete`) após a [tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md) ([reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md)), e o terceiro lote [`software-seguranca-2000-0003`](exports/batches/software-seguranca-2000-0003.md) está em 1300/2.000 notas válidas após a [tranche 13](exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md) ([reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-13.md)).
5. Mantidas as 100 notas legadas com falhas nas filas de remediação, sem contá-las.

Relatórios atualizados: [reconciliação da tranche 26](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md), [auditoria global](exports/reports/note-quality-audit.md), [auditoria do lote](exports/reports/note-quality-software-testes-2000-0001.md), [registro separado de revisões](exports/reports/human-review-queue.md) e [plano de continuidade](PLANO-CONTINUO-1M.md).

## Protocolo de qualidade e contagem

Uma nota candidata deve ter frontmatter rastreável, pelo menos 100 palavras, seções de explicação, exemplo, limites e verificação, duas fontes HTTPS específicas, wikilinks resolvidos e nenhum marcador conhecido de conteúdo-template. O gate não comprova por si só que uma afirmação é verdadeira.

A contagem exige conteúdo substantivo, gate aprovado e revisão factual registrada:

- Humana: `revisao_humana: aprovada` + revisor humano identificado, apenas após aprovação real.
- IA: `revisao_ia: aprovada`, `revisor_ia`, `data_revisao_ia` e `relatorio_revisao_ia`, após confronto factual com fontes.

Os dois tipos permanecem separados. Em domínios regulados podem existir requisitos adicionais de especialista e segurança de conteúdo.

## Comandos de reprodução

```bash
python3 -m unittest discover -s knowledge-federation/tests -v
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

## Próximos marcos sem inflar contagens

1. Primeiro lote (`software-testes-2000-0001`) concluído com 2.000/2.000 notas substantivas, fontes verificadas e revisão factual por tranche.
2. Só declarar o lote completo quando 2.000 notas tiverem gate e revisão factual registrados.
3. Continuar o terceiro lote `software-seguranca-2000-0003` (atualmente em 1300/2.000; faltam 700 notas substantivas) e os 497 lotes subsequentes, preservando 2.000 notas qualificadas por lote e total ativo de 500 lotes.
4. Remediar as 100 notas legadas apenas com fontes próprias e conteúdo substantivo; mantê-las fora da contagem enquanto houver pendências.
5. Publicar relatório final somente após atingir 1.000.000 de notas válidas (500 lotes completos), nunca por contagem de IDs ou placeholders.
