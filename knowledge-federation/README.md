# Knowledge Federation

Federação de conhecimento em Markdown para Obsidian, organizada por domínio e mantida em lotes retomáveis.

## Estado real após o merge

O checkpoint preserva **1.000.000 de registros virtuais de catálogo**, mas eles não equivalem a um milhão de notas válidas: a auditoria encontrou marcadores de conteúdo-template nos 1.000.000 registros. O checkpoint indica 8.000 registros materializados; a materialização, por si só, não comprova conteúdo útil. O lote inicial de 100 notas físicas também falha nos critérios editoriais atuais.

A retomada mudou para lotes pequenos com fontes específicas e gate de qualidade. O primeiro lote piloto tem 8 notas autorais em `domains/software-0002/`; todas passaram pelos testes estruturais automatizados e aguardam revisão humana/factual. Nenhuma está contabilizada como validada por revisor.

Consulte [`STATUS-CONSOLIDACAO-1M.md`](STATUS-CONSOLIDACAO-1M.md) e [`exports/reports/note-quality-audit.md`](exports/reports/note-quality-audit.md) para números e pendências.

## Auditoria de qualidade

```bash
# Testes do gate
python3 -m unittest discover -s knowledge-federation/tests -v

# Arquivos ativos e checkpoint compactado (a extração usa cache temporário)
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

O gate exige frontmatter, no mínimo 100 palavras, seções de explicação/exemplo/limites/verificação, duas fontes HTTPS específicas, wikilinks resolvidos e ausência de marcadores de template conhecidos. Um passe indica **candidata para revisão**, não verificação factual. A contagem de notas validadas exige revisão humana registrada no frontmatter.

Para conferir a qualidade de outro cofre ou pasta, repita `--path`:

```bash
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains/software-0002 \
  --path outro-cofre/01-Notas
```

## Pipeline legado e cautela

`generate_seed_manifest.py` e `generate_batch.py` foram feitos para gerar sementes estruturais. Eles não produzem automaticamente conteúdo final validado. `audit_batch.py` agora mantém um lote em `needs_review` até passar pelos gates e só marca `complete` quando há aprovação humana identificada. Não escale a geração de sementes nem use contagens do ledger como contagem de notas válidas.

## Segurança

Domínios regulados, como cannabis medicinal e micologia/psilocibina, devem permanecer educacionais, científicos, legais, documentais e não operacionais. Qualquer conteúdo regulado precisa de revisão especializada adicional.
