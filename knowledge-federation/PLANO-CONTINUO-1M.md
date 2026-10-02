# Plano contínuo para 2.000.000 de notas válidas

Atualizado em 2026-10-01. O nome `PLANO-CONTINUO-1M.md` é mantido por compatibilidade; a meta anterior de 1.000.000 foi substituída por **1.000 lotes × 2.000 notas substantivas = 2.000.000**. Este documento acompanha execução em rodadas; não há processamento em segundo plano. O relatório final será produzido somente ao concluir o escopo total.

## Estado atual

- Meta: **1.000 lotes de 2.000 notas = 2.000.000 notas válidas**.
- Notas válidas atuais: **139** (49 com aprovação humana histórica + 90 com revisão factual por IA registrada separadamente).
- Progresso válido global: **139 / 2.000.000 (0,00695%)**; faltam **1.999.861** notas válidas.
- Lotes completos: **0 / 1.000**. Lote iniciado: `software-testes-2000-0001` (1º lote, ainda incompleto).
- Primeiro lote: meta **2.000**; **99 notas materiais** já passaram pelo gate e por revisão factual (9 humanas + 90 IA). Faltam **1.901** notas substantivas para completá-lo.
- Arquivos ativos com pendências de qualidade: **100**; excluídos da contagem até serem corrigidos e revisados.
- O snapshot histórico de 1.000.000 de registros virtuais continua sendo catálogo/template; não é progresso para a meta de notas válidas.

## Dez passos e andamento

| # | Passo | Estado | Evidência / condição para avançar |
|---:|---|---|---|
| 1 | Fixar a unidade de progresso e o protocolo de contagem | **Concluído** | Contar somente notas substantivas que passam o gate e têm revisão factual humana ou por IA registrada; distinguir os dois tipos. |
| 2 | Implementar registro de revisão por IA sem promovê-la a humana | **Concluído** | `note_quality.py`, `audit_note_quality.py` e `audit_batch.py` reconhecem revisão por IA com revisor, data e relatório. |
| 3 | Preservar aprovações humanas já concedidas | **Concluído** | As 49 aprovações históricas permanecem como humanas; não foram estendidas a novas notas. |
| 4 | Conferir factual e registrar as notas 10–99 do primeiro lote | **Concluído** | [Relatórios factuais por IA das tranches 2–3](exports/reports/ai-review-software-testes-2000-0001.md), [`tranche 4`](exports/reports/ai-review-software-testes-2000-0001-tranche-04.md), [`tranche 5`](exports/reports/ai-review-software-testes-2000-0001-tranche-05.md) e [`tranche 6`](exports/reports/ai-review-software-testes-2000-0001-tranche-06.md); 90 revisões factuais por IA, além das 9 aprovações humanas. |
| 5 | Rodar o gate, testes, auditorias e verificação de diff | **Concluído para o estado atual** | Auditoria do lote: 99/99 no gate, 9 humanas, 90 IA, 99 válidas. Global: 239 arquivos, 139 candidatas, 139 válidas, 100 com pendências legadas; testes e `git diff --check` aprovados. |
| 6 | Remediar as 100 notas legadas | **Inventário concluído; remediação pendente** | [Fila legada](exports/reports/legacy-remediation-queue.md) lista pendências; reconstruir com fontes específicas ou manter fora da contagem, sem correção cosmética em massa. |
| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Em andamento** | 99/2.000 notas válidas; continuar apenas com conteúdo substantivo, fontes verificadas e revisão factual documentada. |
| 8 | Abrir e executar lotes subsequentes, sempre com 2.000 notas cada | **Pendente após o lote 1** | Identificadores de lote não contam como progresso; um lote só fica completo quando tem 2.000 notas qualificadas. |
| 9 | Consolidar contagens auditáveis por lote e globalmente | **Contínuo** | Atualizar manifesto, relatórios, índice e contagem após cada tranche real; distinguir humanas, IA, gate e notas ainda não revisadas. |
| 10 | Chegar a 1.000 lotes completos e então publicar o relatório final | **Em andamento; meta não atingida** | Progresso auditado atual: 139 notas válidas, 0 lotes completos de 1.000. O relatório final não deve ser publicado antes de concluir o escopo. |

## Regra de continuidade e contagem

Cada nota precisa ser material e ter conteúdo próprio, passar pelo gate automatizado, incluir fontes específicas que sustentem as afirmações e receber revisão factual registrada antes de ser contabilizada. Revisão humana não é obrigatória para notas novas: a revisão por IA é aceita quando explicitamente registrada em `revisao_ia`, `revisor_ia`, `data_revisao_ia` e `relatorio_revisao_ia`. Aprovação por IA nunca preenche nem altera os campos humanos. As 49 aprovações humanas históricas permanecem limitadas às notas que o usuário aprovou.

Não contar catálogo virtual, placeholders, IDs reservados, links, arquivos vazios, nota duplicada ou lote parcial como nota válida concluída. Relatar progresso parcial com numerador e denominador; nunca apresentá-lo como conclusão. Trabalhar em tranches de conteúdo real e revisar factual e separadamente antes de somar as notas.
