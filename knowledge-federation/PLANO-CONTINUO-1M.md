# Plano contínuo para 1.000.000 de notas válidas

Atualizado em 2026-10-03. O nome `PLANO-CONTINUO-1M.md` permanece compatível com a meta ativa de **500 lotes × 2.000 notas substantivas = 1.000.000**. A execução ocorre em rodadas auditáveis; não há processamento em segundo plano e não será alegada conclusão antes do escopo total.

## Estado atual

- Meta ativa: **500 lotes de 2.000 notas = 1.000.000 notas válidas**.
- Notas válidas globais: **5540** (49 aprovações humanas históricas + 5491 revisões factuais por IA).
- Progresso: **5540 / 1.000.000 (0,5540%)**; faltam **994.460** notas válidas.
- Lotes completos: **2 / 500** (`software-testes-2000-0001` e `software-devops-2000-0002`).
- Primeiro lote `software-testes-2000-0001`: **2000 / 2.000 (100%)** notas válidas (9 humanas + 1991 IA); concluído (`complete`).
- Segundo lote `software-devops-2000-0002`: **2000 / 2.000 (100,00%)** notas válidas (2000 IA nas tranches 1–20); concluído (`complete`).
- Terceiro lote atual `software-seguranca-2000-0003`: **1500 / 2.000 (75,00%)** notas válidas (1500 IA nas tranches 1–15); faltam **500** notas substantivas.
- Arquivos Markdown ativos: **5640**; 100 com pendências de qualidade, excluídos da contagem.
- O checkpoint legado com 1.000.000 de registros virtuais continua fora da contagem de conteúdo válido.

## Dez passos e andamento

| # | Passo | Estado | Evidência / condição para avançar |
|---:|---|---|---|
| 1 | Fixar unidade de progresso e protocolo de contagem | **Concluído** | Só contar notas substantivas aprovadas pelo gate e com revisão factual humana ou por IA registrada separadamente. |
| 2 | Implementar registro de revisão por IA sem promovê-la a humana | **Concluído** | `note_quality.py`, `audit_note_quality.py` e `audit_batch.py` reconhecem revisor, data e relatório de IA. |
| 3 | Preservar aprovações humanas já concedidas | **Concluído** | As 49 aprovações históricas permanecem limitadas às notas aprovadas pelo usuário. |
| 4 | Conferir factual e registrar notas 10–2000 do primeiro lote | **Concluído (tranches 2–26)** | 1991 revisões por IA em relatórios das tranches 2–26, além das 9 aprovações humanas. |
| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3 (`software-seguranca-2000-0003`): 1500/1500 no gate (1500 IA). Global: 5640 arquivos, 5540 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 15 do lote 3](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-15.md). |
| 6 | Remediar as 100 notas legadas | **Inventário concluído; remediação pendente** | Reconstruir com fontes próprias ou mantê-las fora da contagem; não corrigir cosmeticamente em massa. |
| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Concluído** | 2000/2.000 (100%); todas as 2.000 notas substantivas contam com gate aprovado, fontes verificadas e revisão factual registrada (`complete`). |
| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 3 em 75%)** | Terceiro lote `software-seguranca-2000-0003` em 1500/2.000 notas válidas nas tranches 1–15; restam 500 notas neste lote e 497 lotes subsequentes. |
| 9 | Consolidar contagens por tranche, lote e global | **Contínuo** | Atualizar manifestos, relatórios, fila e MOC após auditoria; distinguir gate, revisão humana e revisão por IA. |
| 10 | Atingir a meta e publicar relatório final | **Em andamento; meta não atingida** | Progresso atual: 5540 notas válidas, 2/500 lotes completos. Publicar apenas ao atingir 1.000.000. |

## Regra de continuidade e contagem

Cada nota deve ser material, ter conteúdo próprio, passar pelo gate, incluir fontes específicas que sustentem as afirmações e receber revisão factual registrada antes de ser contabilizada. Revisão humana não é obrigatória para notas novas: revisão por IA é aceita se os campos `revisao_ia`, `revisor_ia`, `data_revisao_ia` e `relatorio_revisao_ia` forem preenchidos. A aprovação por IA nunca preenche nem altera campos humanos; as 49 aprovações históricas permanecem limitadas às notas aprovadas pelo usuário.

Não contar catálogo virtual, placeholders, IDs reservados, links, arquivos vazios, notas duplicadas ou lotes parciais como progresso qualificado. Publicar progresso parcial com numerador e denominador, sem apresentá-lo como conclusão.
