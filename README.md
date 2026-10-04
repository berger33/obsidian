# Biblioteca e Federação de Conhecimento Obsidian

Repositório de vaults em português brasileiro, com taxonomia para Engenharia de Software, IA, Vibe Coding, Jogos, Negócio/Produto, Cannabis Medicinal em abordagem educacional/regulatória e Micologia segura.

## Meta editorial ativa: 1.000.000 de notas válidas

A meta atual é **500 lotes de 2.000 notas substantivas** (1.000.000 no total). Cada nota só conta depois de passar pelo gate automatizado e receber revisão factual registrada por uma pessoa ou por IA; os dois tipos de revisão permanecem separados. A aprovação por IA não é aprovação humana. O relatório final será publicado ao término do escopo, não como resultado parcial.

| Métrica auditada | Total | O que representa |
|---|---:|---|
| Meta | 1.000.000 | 500 lotes completos × 2.000 notas qualificadas |
| Lotes completos | 3 / 500 | Lotes `software-testes-2000-0001`, `software-devops-2000-0002` e `software-seguranca-2000-0003` concluídos com 2.000 notas válidas cada |
| Notas válidas contabilizadas | 6340 / 1.000.000 (0,6340%) | 49 com aprovação humana histórica + 6291 com revisão factual por IA |
| Notas com revisão humana registrada | 49 | Aprovações anteriores do usuário; não ampliadas a conteúdo novo |
| Notas com revisão factual por IA registrada | 6291 | Revisões dos três lotes completos (5991) + 300 notas nas tranches 1–3 do lote 4; não são humanas |
| Primeiro lote `software-testes-2000-0001` | 2000 / 2.000 (100%) | 9 aprovadas por humano + 1991 por IA; lote concluído (`complete`) |
| Segundo lote `software-devops-2000-0002` | 2000 / 2.000 (100,00%) | 2000 aprovadas por IA nas tranches 1–20; lote concluído (`complete`) |
| Terceiro lote `software-seguranca-2000-0003` | 2000 / 2.000 (100,00%) | 2000 revisões factuais por IA nas tranches 1–20; concluído (`complete`) |
| Quarto lote `software-criacao-ia-2000-0004` | 300 / 2.000 (15,00%) | Tranches 1–3 concluídas (300 IA); 17 tranches planejadas sem IDs reservados; foco em engenharia e criação de programas, apps e jogos com IA |
| Arquivos Markdown ativos em `knowledge-federation/domains/` | 6440 | 100 notas legadas com pendências + 6340 notas autorais substantivas |
| Notas legadas fora da contagem | 100 | Ainda têm falhas de conteúdo/fontes; consulte a fila de remediação |

O checkpoint histórico preserva **1.000.000 de registros virtuais de catálogo**, com marcadores de template nos 1.000.000 registros, e 8.000 caminhos marcados como materializados. Isso não equivale a notas válidas nem avança a meta de 1 milhão. Os pacotes antigos permanecem disponíveis para inspeção e recuperação, não como prova de conteúdo validado.

## Artefatos históricos do merge

| Pacote | Tamanho aproximado | Uso / ressalva |
|---|---:|---|
| `knowledge-federation/archives/merge-completo-materializado-1m.tar.xz` | 33,1 MB | Snapshot histórico de lotes e vaults; inclui conteúdo-template/candidatas antigas, não 1 milhão de notas válidas |
| `knowledge-federation/archives/study-vault-1m-packs.zip` | 19 MB | 78 Study Packs e arquivos derivados do ledger; não assumir que sejam notas validadas |
| `knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz` | 24 MB | Checkpoint SQLite do catálogo histórico de 1 milhão de registros virtuais |
| `knowledge-federation/archives/starter-vault-prioritario.zip` | 1,1 MB | Recorte de entrada; quantidade de arquivos não é selo de qualidade |
| `vault-desenvolvimento-software-com-ia/` | ativo | Vault autoral amplo, mantido separadamente do checkpoint histórico |

### Extrair lotes históricos sem criar 1 milhão de arquivos de uma vez

```bash
mkdir -p /tmp/merge-parcial
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz \
  -C /tmp/merge-parcial MERGE-COMPLETO/10-lotes/0001-0100
```

### Consultar o catálogo SQLite

```bash
python3 knowledge-federation/scripts/ledger_stats.py
python3 knowledge-federation/scripts/query_checkpoint.py "agentes" --domain ia --limit 20
```

## Retomada editorial e relatórios

O primeiro lote concluído é `software-testes-2000-0001` (2000/2.000, 9 humanas + 1991 IA, `complete`), o segundo lote concluído é [`software-devops-2000-0002`](knowledge-federation/exports/batches/software-devops-2000-0002.md) (2000/2.000, `complete`, [tranche 20](knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md), [reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-devops-2000-0002.md) e [MOC de DevOps](knowledge-federation/00-home-vault/MOCs/MOC-DevOps-Software-0008.md)), e o terceiro lote [`software-seguranca-2000-0003`](knowledge-federation/exports/batches/software-seguranca-2000-0003.md) foi concluído em 2000/2.000 (`complete`) após a [tranche 20](knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-20.md) ([reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-20.md), [auditoria do lote](knowledge-federation/exports/reports/note-quality-software-seguranca-2000-0003.md) e [MOC de Segurança](knowledge-federation/00-home-vault/MOCs/MOC-Seguranca-Software-0009.md)). O quarto lote [`software-criacao-ia-2000-0004`](knowledge-federation/exports/batches/software-criacao-ia-2000-0004.md) está em 300/2.000 após a tranche 3, com foco em engenharia e criação de programas, apps e jogos com IA ([revisão factual](knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md), [reconciliação](knowledge-federation/exports/reports/batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md), [auditoria da tranche](knowledge-federation/exports/reports/note-quality-software-criacao-ia-2000-0004-tranche-03.md) e [MOC](knowledge-federation/00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)). A [auditoria global](knowledge-federation/exports/reports/note-quality-audit.md), o [manifesto do lote](knowledge-federation/exports/batches/software-testes-2000-0001.md), os relatórios factuais por IA ([tranches 2–3](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md), [4](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-04.md), [5](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-05.md), [6](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-06.md), [7](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-07.md), [8](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md), [9](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md), [10](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md), [11](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md), [12](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md) e [13](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md) e [14](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-14.md), [15](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md), [16](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md), [17](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md), [18](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md), [19](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md), [23](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md), [24](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md), [25](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md) e [26](knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-26.md)), além da [reconciliação da tranche 26](knowledge-federation/exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md), o [registro de revisões](knowledge-federation/exports/reports/human-review-queue.md), a [fila legada](knowledge-federation/exports/reports/legacy-remediation-queue.md), o [plano de execução contínua](knowledge-federation/PLANO-CONTINUO-1M.md) e o [MOC de testes](knowledge-federation/00-home-vault/MOCs/MOC-Testes-Software-0007.md) mantêm o estado auditável.

```bash
# Testes do gate
python3 -m unittest discover -s knowledge-federation/tests -v

# Reauditar notas ativas e o checkpoint histórico
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

O gate verifica frontmatter, conteúdo mínimo, seções, fontes específicas, wikilinks e marcadores de template; não comprova a verdade das afirmações. Para contar, cada nota deve ter revisão factual registrada. Revisão humana usa `revisao_humana`/`revisor`; revisão por IA usa `revisao_ia`, `revisor_ia`, `data_revisao_ia` e `relatorio_revisao_ia`. Veja [`knowledge-federation/README.md`](knowledge-federation/README.md) para o protocolo e os comandos.

## Segurança em domínios regulados

`cannabis-medicinal` e `micologia` permanecem restritos a conteúdo legal, educacional, científico, documental e de redução de danos. Não gerar instruções operacionais de cultivo, produção, extração, otimização de potência/rendimento ou evasão de fiscalização.
