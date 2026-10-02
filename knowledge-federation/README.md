# Knowledge Federation

Federação de conhecimento em Markdown para Obsidian, organizada por domínio e mantida em lotes auditáveis.

## Meta editorial ativa

A meta ativa é **500 lotes × 2.000 notas substantivas = 1.000.000 de notas válidas**. A revisão humana não é obrigatória para notas novas; cada nota que contar precisa passar pelo gate automatizado e receber revisão factual humana ou por IA, registrada separadamente. Uma revisão por IA nunca é apresentada como aprovação humana.

O checkpoint legado ainda contém 1.000.000 de registros virtuais de catálogo, mas a auditoria encontrou marcadores de template nos 1.000.000 registros. Eles não equivalem a notas válidas e não avançam a meta editorial.

- Arquivos Markdown ativos: **489** (100 notas legadas com pendências + 389 notas autorais substantivas).
- Notas válidas pelo protocolo atual: **389** (49 aprovações humanas históricas + 340 revisões factuais por IA).
- Progresso: **389 / 1.000.000 (0,0389%)**; faltam 999.611 notas válidas.
- Lotes completos: **0 / 500**.
- Lote em andamento `software-testes-2000-0001`: **349 / 2.000** notas válidas; 9 humanas e 340 por IA; faltam 1.651 notas materiais.
- As **100** notas legadas com pendências continuam excluídas.

Consulte os [manifestos de lote](exports/batches/), as [auditorias e relatórios](exports/reports/), o [registro separado de revisões](exports/reports/human-review-queue.md), a [fila de remediação legada](exports/reports/legacy-remediation-queue.md), o [plano para 1 milhão](PLANO-CONTINUO-1M.md) e o [status auditado](STATUS-CONSOLIDACAO-1M.md). Os relatórios factuais por IA do lote atual são [tranches 2–3](exports/reports/ai-review-software-testes-2000-0001.md), [4](exports/reports/ai-review-software-testes-2000-0001-tranche-04.md), [5](exports/reports/ai-review-software-testes-2000-0001-tranche-05.md), [6](exports/reports/ai-review-software-testes-2000-0001-tranche-06.md), [7](exports/reports/ai-review-software-testes-2000-0001-tranche-07.md), [8](exports/reports/ai-review-software-testes-2000-0001-tranche-08.md) e [9](exports/reports/ai-review-software-testes-2000-0001-tranche-09.md).

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

`generate_seed_manifest.py` e `generate_batch.py` foram feitos para gerar sementes estruturais; não produzem automaticamente conteúdo final validado. `audit_batch.py` mantém lotes em `needs_review` se houver falhas estruturais/de qualidade e só os marca `complete` quando todas as notas passam o gate e têm revisão factual humana ou por IA registrada. A fonte do tipo de revisão continua no frontmatter; o estado genérico no ledger não substitui essa distinção.

Não escale a geração de sementes nem use contagens do ledger, IDs ou links como contagem de notas válidas. Um lote só conta como completo quando contém 2.000 notas substantivas qualificadas.

## Segurança

Domínios regulados, como cannabis medicinal e micologia/psilocibina, devem permanecer educacionais, científicos, legais, documentais e não operacionais. Qualquer conteúdo regulado pode exigir revisão especializada adicional.
