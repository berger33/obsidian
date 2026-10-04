# Knowledge Federation

Federação de conhecimento em Markdown para Obsidian, organizada por domínio e mantida em lotes auditáveis.

## Meta editorial ativa

A meta ativa é **500 lotes × 2.000 notas substantivas = 1.000.000 de notas válidas**. A revisão humana não é obrigatória para notas novas; cada nota que contar precisa passar pelo gate automatizado e receber revisão factual humana ou por IA, registrada separadamente. Uma revisão por IA nunca é apresentada como aprovação humana.

O checkpoint legado ainda contém 1.000.000 de registros virtuais de catálogo, mas a auditoria encontrou marcadores de template nos 1.000.000 registros. Eles não equivalem a notas válidas e não avançam a meta editorial.

- Arquivos Markdown ativos: **6140** (100 notas legadas com pendências + 6040 notas autorais substantivas).
- Notas válidas pelo protocolo atual: **6040** (49 aprovações humanas históricas + 5991 revisões factuais por IA).
- Progresso: **6040 / 1.000.000 (0,6040%)**; faltam 993.960 notas válidas.
- Lotes completos: **3 / 500** (`software-testes-2000-0001`, `software-devops-2000-0002` e `software-seguranca-2000-0003`).
- Primeiro lote concluído `software-testes-2000-0001`: **2000 / 2.000** notas válidas (100%); 9 humanas e 1991 por IA; status `complete`.
- Segundo lote concluído `software-devops-2000-0002`: **2000 / 2.000** notas válidas (100,00%); 2000 por IA ([tranche 20](exports/reports/ai-review-software-devops-2000-0002-tranche-20.md) e [reconciliação](exports/reports/batch-reconciliation-software-devops-2000-0002-tranche-20.md)); status `complete`.
- Terceiro lote concluído `software-seguranca-2000-0003`: **2000 / 2.000** notas válidas (`complete`); 2000 por IA ([tranche 20](exports/reports/ai-review-software-seguranca-2000-0003-tranche-20.md) e [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-20.md)).
- Quarto lote aberto `software-criacao-ia-2000-0004`: **0 / 2.000** notas; 20 tranches planejadas; escopo de engenharia e criação de programas, apps e jogos com IA ([manifesto](exports/batches/software-criacao-ia-2000-0004.md), [abertura](exports/reports/batch-opening-software-criacao-ia-2000-0004.md) e [MOC](00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)).
- As **100** notas legadas com pendências continuam excluídas.

Consulte os [manifestos de lote](exports/batches/), as [auditorias e relatórios](exports/reports/), o [registro separado de revisões](exports/reports/human-review-queue.md), a [fila de remediação legada](exports/reports/legacy-remediation-queue.md), o [plano para 1 milhão](PLANO-CONTINUO-1M.md) e o [status auditado](STATUS-CONSOLIDACAO-1M.md). Os relatórios factuais por IA do primeiro lote de testes `software-testes-2000-0001` são [tranches 2–3](exports/reports/ai-review-software-testes-2000-0001.md), [4](exports/reports/ai-review-software-testes-2000-0001-tranche-04.md), [5](exports/reports/ai-review-software-testes-2000-0001-tranche-05.md), [6](exports/reports/ai-review-software-testes-2000-0001-tranche-06.md), [7](exports/reports/ai-review-software-testes-2000-0001-tranche-07.md), [8](exports/reports/ai-review-software-testes-2000-0001-tranche-08.md), [9](exports/reports/ai-review-software-testes-2000-0001-tranche-09.md) e [10](exports/reports/ai-review-software-testes-2000-0001-tranche-10.md), [11](exports/reports/ai-review-software-testes-2000-0001-tranche-11.md) e [12](exports/reports/ai-review-software-testes-2000-0001-tranche-12.md), [13](exports/reports/ai-review-software-testes-2000-0001-tranche-13.md), [14](exports/reports/ai-review-software-testes-2000-0001-tranche-14.md), [15](exports/reports/ai-review-software-testes-2000-0001-tranche-15.md), [16](exports/reports/ai-review-software-testes-2000-0001-tranche-16.md), [17](exports/reports/ai-review-software-testes-2000-0001-tranche-17.md), [18](exports/reports/ai-review-software-testes-2000-0001-tranche-18.md), [19](exports/reports/ai-review-software-testes-2000-0001-tranche-19.md), [20](exports/reports/ai-review-software-testes-2000-0001-tranche-20.md), [21](exports/reports/ai-review-software-testes-2000-0001-tranche-21.md), [22](exports/reports/ai-review-software-testes-2000-0001-tranche-22.md), [23](exports/reports/ai-review-software-testes-2000-0001-tranche-23.md), [24](exports/reports/ai-review-software-testes-2000-0001-tranche-24.md), [25](exports/reports/ai-review-software-testes-2000-0001-tranche-25.md) e [26](exports/reports/ai-review-software-testes-2000-0001-tranche-26.md); veja também a [reconciliação da tranche 26](exports/reports/batch-reconciliation-software-testes-2000-0001-tranche-26.md). Para o lote 3 concluído, consulte a [tranche 20](exports/reports/ai-review-software-seguranca-2000-0003-tranche-20.md) e sua [reconciliação](exports/reports/batch-reconciliation-software-seguranca-2000-0003-tranche-20.md); o lote 4 está aberto em 0/2.000 para engenharia e criação com IA, conforme o [relatório de abertura](exports/reports/batch-opening-software-criacao-ia-2000-0004.md).

## Auditoria de qualidade

```bash
# Testes do gate
python3 -m unittest discover -s knowledge-federation/tests -v

# Arquivos ativos e checkpoint compactado (a extração usa cache temporário)
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

O gate exige frontmatter, no mínimo 100 palavras, seções de explicação/exemplo/limites/verificação, duas fontes HTTPS específicas, wikilinks resolvidos e ausência de marcadores conhecidos de template. O passe automático apenas atesta esses critérios; não comprova a verdade das afirmações. A contagem válida também requer revisão factual registrada.

### Metadados de revisão

- Humana: `revisao_humana: aprovada` e `revisor`, exclusivamente após aprovação humana real.
- IA: `revisao_ia: aprovada`, `revisor_ia`, `data_revisao_ia` e `relatorio_revisao_ia`, após conferência factual contra fontes.

Os relatórios mostram separadamente aprovações humanas e revisões por IA. Notas sem revisão factual permanecem candidatas e não contam.

## Pipeline de lotes

`generate_seed_manifest.py` e `generate_batch.py` foram feitos para gerar sementes estruturais; não produzem automaticamente conteúdo final validado. `audit_batch.py` mantém lotes em `needs_review` se houver falhas estruturais/de qualidade e só os marca `complete` quando todas as notas passam o gate e têm revisão factual humana ou por IA registrada. A fonte do tipo de revisão continua no frontmatter; o estado genérico no ledger não substitui essa distinção. O `audit_batch.py` exige lote registrado no SQLite e não audita sozinho um manifesto mantido apenas em Markdown; nesse fluxo, rode o gate por arquivos e reconcilie explicitamente manifesto, notas e fila antes de atualizar a contagem.

Não escale a geração de sementes nem use contagens do ledger, IDs ou links como contagem de notas válidas. Um lote só conta como completo quando contém 2.000 notas substantivas qualificadas.

## Segurança

Domínios regulados, como cannabis medicinal e micologia/psilocibina, devem permanecer educacionais, científicos, legais, documentais e não operacionais. Qualquer conteúdo regulado pode exigir revisão especializada adicional.
