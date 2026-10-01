# Retomada pós-merge: escala com qualidade

Data: 2026-10-01

## Estado observado após integrar o merge

Os artefatos massivos estão presentes como arquivos compactados versionados; não precisam ser recriados para continuar o trabalho. O checkpoint contém 1.000.000 de registros virtuais, 8.000 com caminho marcado como materializado e 100 registros físicos iniciais.

A auditoria de qualidade encontrou marcadores de texto-template em todos os 1.000.000 registros virtuais. Os 100 arquivos iniciais também não passam no novo gate editorial. Isso explica por que os antigos números de catálogo, arquivos, lotes e links não devem ser apresentados como 1 milhão de notas válidas.

No diretório ativo `knowledge-federation/domains/` há 108 arquivos: 100 sementes antigas e 8 notas autorais da retomada. As 8 passam pelo gate estrutural automatizado, mas ainda aguardam revisão humana/factual.

## Decisão técnica

Manter a arquitetura ledger-first para inventário e armazenamento, mas separar explicitamente quatro estados:

1. **catalogada** — ID e taxonomia; não conta como conteúdo;
2. **candidata** — corpo substantivo e gate automatizado aprovado;
3. **validada** — fontes e afirmações revisadas por pessoa identificada;
4. **rejeitada/needs-review** — não contabilizada até ser corrigida.

Materializar um arquivo Markdown não promove o registro de estado. Geradores de sementes servem ao planejamento, não à contagem de notas válidas.

## Ferramentas adicionadas

- `scripts/note_quality.py` — regras reutilizáveis de avaliação estrutural e detecção de placeholders.
- `scripts/audit_note_quality.py` — auditoria dos arquivos ativos e, opcionalmente, do checkpoint SQLite compactado.
- `scripts/audit_batch.py` — agora exige aprovação humana registrada antes de marcar um lote como `complete`.
- `tests/test_note_quality.py` — regressões do gate para sementes, fontes genéricas e revisão humana.

## Comandos de retomada

```bash
python3 -m unittest discover -s knowledge-federation/tests -v
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

## Próximo ciclo recomendado

1. Revisar as 8 notas candidatas e confirmar as referências.
2. Registrar revisão humana somente depois da conferência efetiva.
3. Criar novos lotes pequenos, com conceitos específicos e fontes adequadas ao subdomínio.
4. Auditar conteúdo, fontes, links, duplicatas e segurança antes de materializar/exportar.
5. Reclassificar ou substituir progressivamente os registros-template; nunca elevar contagens por repetição de títulos ou arquivos.
