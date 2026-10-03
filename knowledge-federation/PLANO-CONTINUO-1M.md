# Plano contínuo para 1.000.000 de notas válidas

Atualizado em 2026-10-03. O nome `PLANO-CONTINUO-1M.md` permanece compatível com a meta ativa de **500 lotes × 2.000 notas substantivas = 1.000.000**. A execução ocorre em rodadas auditáveis; não há processamento em segundo plano e não será alegada conclusão antes do escopo total.

## Estado atual

- Meta ativa: **500 lotes de 2.000 notas = 1.000.000 notas válidas**.
- Notas válidas globais: **3640** (49 aprovações humanas históricas + 3591 revisões factuais por IA).
- Progresso: **3640 / 1.000.000 (0,3640%)**; faltam **996.360** notas válidas.
- Lotes completos: **1 / 500** (`software-testes-2000-0001`).
- Primeiro lote `software-testes-2000-0001`: **2000 / 2.000 (100%)** notas válidas (9 humanas + 1991 IA); concluído (`complete`).
- Segundo lote atual `software-devops-2000-0002`: **1600 / 2.000 (80,00%)** notas válidas (1600 IA nas tranches 1–16); faltam **400** notas substantivas.
- Arquivos Markdown ativos: **3740**; 100 com pendências de qualidade, excluídos da contagem.
- O checkpoint legado com 1.000.000 de registros virtuais continua fora da contagem de conteúdo válido.

## Dez passos e andamento

| # | Passo | Estado | Evidência / condição para avançar |
|---:|---|---|---|
| 1 | Fixar unidade de progresso e protocolo de contagem | **Concluído** | Só contar notas substantivas aprovadas pelo gate e com revisão factual humana ou por IA registrada separadamente. |
| 2 | Implementar registro de revisão por IA sem promovê-la a humana | **Concluído** | `note_quality.py`, `audit_note_quality.py` e `audit_batch.py` reconhecem revisor, data e relatório de IA. |
| 3 | Preservar aprovações humanas já concedidas | **Concluído** | As 49 aprovações históricas permanecem limitadas às notas aprovadas pelo usuário. |
| 4 | Conferir factual e registrar notas 10–2000 do primeiro lote | **Concluído (tranches 2–26)** | 1991 revisões por IA em relatórios das tranches 2–26, além das 9 aprovações humanas. |
| 5 | Rodar gate, testes, auditorias e diff | **Concluído para o estado atual** | Lote 1: 2000/2000 (`complete`). Lote 2 (`software-devops-2000-0002`): 1600/1600 no gate (1600 IA). Global: 3740 arquivos, 3640 válidas, 100 com pendências legadas; veja a [reconciliação da tranche 16 do lote 2](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-16.md). |
| 6 | Remediar as 100 notas legadas | **Inventário concluído; remediação pendente** | Reconstruir com fontes próprias ou mantê-las fora da contagem; não corrigir cosmeticamente em massa. |
| 7 | Completar o lote `software-testes-2000-0001` até 2.000 notas | **Concluído** | 2000/2.000 (100%); todas as 2.000 notas substantivas contam com gate aprovado, fontes verificadas e revisão factual registrada (`complete`). |
| 8 | Abrir lotes subsequentes de 2.000 notas | **Em andamento (lote 2 em 80%)** | Segundo lote `software-devops-2000-0002` com 1600/2.000 notas válidas nas tranches 1–16; restam 400 notas neste lote e 498 lotes subsequentes. |
| 9 | Consolidar contagens por tranche, lote e global | **Contínuo** | Atualizar manifestos, relatórios, fila e MOC após auditoria; distinguir gate, revisão humana e revisão por IA. |
| 10 | Atingir a meta e publicar relatório final | **Em andamento; meta não atingida** | Progresso atual: 3640 notas válidas, 1/500 lotes completos. Publicar apenas ao atingir 1.000.000. |

## Regra de continuidade e contagem

Cada nota deve ser material, ter conteúdo próprio, passar pelo gate, incluir fontes específicas que sustentem as afirmações e receber revisão factual registrada antes de ser contabilizada. Revisão humana não é obrigatória para notas novas: revisão por IA é aceita se os campos `revisao_ia`, `revisor_ia`, `data_revisao_ia` e `relatorio_revisao_ia` forem preenchidos. A aprovação por IA nunca preenche nem altera campos humanos; as 49 aprovações históricas permanecem limitadas às notas aprovadas pelo usuário.

Não contar catálogo virtual, placeholders, IDs reservados, links, arquivos vazios, notas duplicadas ou lotes parciais como progresso qualificado. Publicar progresso parcial com numerador e denominador, sem apresentá-lo como conclusão.
