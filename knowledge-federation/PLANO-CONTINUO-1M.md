# Plano contínuo para 1.000.000 de notas válidas

Atualizado em 2026-10-04. A meta editorial ativa é **500 lotes × 2.000 notas = 1.000.000**; cada tranche contém 100 notas e só entra na contagem após gate e revisão factual registrados.

## Estado atual

- Meta ativa: **500 lotes de 2.000 notas = 1.000.000 notas válidas**.
- Notas válidas globais: **5740** (49 aprovações humanas históricas + 5691 revisões factuais por IA).
- Progresso: **5740 / 1.000.000 (0,5740%)**; faltam **994260** notas válidas.
- Lotes completos: **2 / 500** (`software-testes-2000-0001`, `software-devops-2000-0002`).
- Primeiro lote `software-testes-2000-0001`: **2000 / 2.000 (100%)** notas válidas (9 humanas + 1991 IA); concluído (`complete`).
- Segundo lote `software-devops-2000-0002`: **2000 / 2.000 (100,00%)** notas válidas (2000 IA nas tranches 1–20); concluído (`complete`).
- Terceiro lote `software-seguranca-2000-0003`: **1700 / 2.000 (85,00%)** notas válidas (1700 IA nas tranches 1–17); faltam **300** notas substantivas.
- Arquivos Markdown ativos: **5840**; 100 com pendências de qualidade, excluídos da contagem.
- O checkpoint legado com 1.000.000 de registros virtuais continua fora da contagem de conteúdo válido.

## Dez passos e andamento

| # | Passo | Estado | Evidência / condição para avançar |
|---:|---|---|---|
| 1 | Fixar unidade de progresso e protocolo de contagem | **Concluído** | Só contar notas substantivas aprovadas pelo gate e com revisão factual humana ou por IA registrada separadamente. |
| 2 | Implementar registro de revisão por IA sem promovê-la a humana | **Concluído** | `note_quality.py`, `audit_note_quality.py` e `audit_batch.py` reconhecem revisor, data e relatório de IA. |
| 3 | Preservar aprovações humanas já concedidas | **Concluído** | As 49 aprovações históricas permanecem limitadas às notas aprovadas pelo usuário. |
| 4 | Conferir factual e registrar notas 10–2000 do primeiro lote | **Concluído (tranches 2–26)** | 1991 revisões por IA em relatórios das tranches 2–26, além das 9 aprovações humanas. |
| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2: 2000/2000 (`complete`). Lote 3: 1700/2.000 (1700 IA; status `in_progress`). Global: 5840 arquivos, 5740 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 17](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-17.md). |
| 6 | Remediar as 100 notas legadas | **Inventário concluído; remediação pendente** | Reconstruir com fontes próprias ou mantê-las fora da contagem; não corrigir cosmeticamente em massa. |
| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Concluído** | 2000/2.000 (100%); todas as 2.000 notas substantivas contam com gate aprovado, fontes verificadas e revisão factual registrada (`complete`). |
| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento** | Lote 3 em 1700/2.000 nas tranches 1–17; restam 300 notas neste lote e 497 lotes subsequentes.
| 9 | Consolidar contagens por tranche, lote e global | **Contínuo** | Atualizar manifestos, relatórios, fila e MOC após auditoria; distinguir gate, revisão humana e revisão por IA. |
| 10 | Atingir a meta e publicar relatório final | **Em andamento; meta não atingida** | Progresso atual: 5740 notas válidas, 2/500 lotes completos. Publicar apenas ao atingir 1.000.000. |

## Regra de continuidade e contagem

Cada nota deve ser material, ter conteúdo próprio, passar pelo gate, incluir fontes específicas que sustentem as afirmações e receber revisão factual registrada antes de ser contabilizada. Revisão humana não é obrigatória para notas novas: revisão por IA é aceita se os campos `revisao_ia`, `revisor_ia`, `data_revisao_ia` e `relatorio_revisao_ia` forem preenchidos. A aprovação por IA nunca preenche nem altera campos humanos; as 49 aprovações históricas permanecem limitadas às notas aprovadas pelo usuário.

Não contar catálogo virtual, placeholders, IDs reservados, links, arquivos vazios, notas duplicadas ou lotes parciais como progresso qualificado. Publicar progresso parcial com numerador e denominador, sem apresentá-lo como conclusão.
