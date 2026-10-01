# Status rumo a 1 milhão de notas válidas

Data da auditoria: 2026-10-01

## Resumo honesto

O merge preservou um **catálogo com 1.000.000 de registros virtuais**, não 1.000.000 de notas de conhecimento validadas. A auditoria direta do SQLite encontrou marcadores de texto-template em todos os registros virtuais. Há arquivos materializados e links, mas isso comprova presença e navegação, não qualidade editorial.

A meta de **1.000.000 de notas válidas ainda não foi atingida**. Para deixar essa diferença explícita, a contagem agora separa inventário, candidatas ao gate automatizado e notas com revisão humana registrada.

## Contagem auditada

| Métrica | Quantidade | Interpretação |
|---|---:|---|
| Registros virtuais no checkpoint | 1.000.000 | IDs de catálogo; não contar como notas válidas |
| Registros virtuais com marcadores de template | 1.000.000 | Sumário/corpo-semente genéricos |
| Caminhos marcados como materializados no checkpoint | 8.000 | Arquivos gerados não equivalem a conteúdo validado |
| Notas físicas registradas no checkpoint | 100 | Lote inicial; status profundo/revisado no schema legado: 0 |
| Arquivos Markdown ativos em `domains/` | 108 | 100 sementes antigas + 8 notas novas |
| Candidatas que passaram pelo gate automatizado | 8 | Prontas para revisão humana/factual; não são ainda “validadas” |
| Notas com revisão humana registrada | 0 | Nenhuma deve ser contabilizada como plenamente válida ainda |
| Links wiki quebrados no Study Vault legado | 0 no relatório anterior | Auditoria de links não valida conteúdo |
| Marcadores de conteúdo operacional regulado no ledger | 0 | Filtro de segurança preservado |

A sequência de lotes no TAR e os 78 Study Packs continuam disponíveis como **artefatos históricos de materialização**. Seus números descrevem arquivos/entradas gerados a partir do ledger; as notas-template não entram na meta de conteúdo válido.

## Trabalho feito nesta retomada

1. Adicionado um gate reproduzível em `scripts/note_quality.py` e `scripts/audit_note_quality.py`.
2. Atualizado `audit_batch.py`: links/frontmatter sem conteúdo não bastam para marcar um lote como concluído; `complete` requer gate automatizado e revisão humana identificada.
3. Criadas 8 notas autorais, com exemplos, limites, métodos de verificação e fontes primárias/especializadas, nos subdomínios software/backend, APIs, testes, dados e DevOps.
4. As 8 passaram pelo gate estrutural de conteúdo; revisão humana e checagem final das afirmações seguem pendentes.
5. Acrescentados 9 testes automatizados cobrindo notas completas, placeholders, bloqueio de materialização, fontes genéricas, wikilinks com alias/fragmento, estado de revisão e esquema do ledger.

Relatório executável: [`exports/reports/note-quality-audit.md`](exports/reports/note-quality-audit.md).
Mapa de navegação do primeiro lote: [`00-home-vault/MOCs/MOC-Confiabilidade-e-Contratos.md`](00-home-vault/MOCs/MOC-Confiabilidade-e-Contratos.md). O MOC não participa do gate de qualidade e sua existência não aprova o lote.

## Gate de qualidade adotado

Uma nota candidata deve ter frontmatter rastreável, pelo menos 100 palavras de conteúdo, seções de explicação, exemplo, limites e verificação, duas fontes HTTPS específicas, wikilinks resolvidos e nenhum marcador conhecido de conteúdo-template. O gate é deliberadamente conservador e pode exigir ajustes para domínios diferentes.

Um passe automatizado só produz o estado **pronta para revisão**. A promoção a nota válida exige conferência factual das fontes por uma pessoa revisora, identificada em `revisor`, e `revisao_humana: aprovada`. Em temas regulados, exige também revisão apropriada ao domínio e manutenção de conteúdo não operacional.

## Comandos de reprodução

```bash
python3 -m unittest discover -s knowledge-federation/tests -v
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

## Próximos marcos sem inflar contagens

1. Revisar as 8 candidatas e registrar a aprovação somente depois da checagem das fontes.
2. Produzir lotes editoriais pequenos por subdomínio, começando pelas áreas de maior utilidade e com fontes primárias.
3. Rodar gate, auditoria de links, deduplicação e revisão de domínio em cada lote.
4. Contabilizar separadamente `catalogadas`, `candidatas`, `revisadas` e `rejeitadas`; ampliar escala apenas quando a taxa de qualidade e o fluxo de revisão forem sustentáveis.
5. Reclassificar ou substituir progressivamente as 1.000.000 de entradas-template antes de declarar a meta cumprida.
