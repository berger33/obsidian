# Biblioteca e Federação de Conhecimento Obsidian

Repositório de vaults em português brasileiro, com taxonomia para Engenharia de Software, IA, Vibe Coding, Jogos, Negócio/Produto, Cannabis Medicinal em abordagem educacional/regulatória e Micologia segura.

## Estado da meta: 1 milhão de notas válidas

O merge trouxe um checkpoint com **1.000.000 de registros virtuais de catálogo**. Isso não significa 1.000.000 de notas válidas: a auditoria do SQLite identificou texto-template em todos os 1.000.000 registros. A contagem de arquivos e links dos pacotes antigos também não certifica conteúdo.

| Métrica auditada | Total | O que representa |
|---|---:|---|
| Registros virtuais no ledger | 1.000.000 | Inventário de IDs; não contar como conteúdo válido |
| Registros virtuais com marcadores de template | 1.000.000 | Sumários e sementes genéricos |
| Arquivos Markdown ativos em `knowledge-federation/domains/` | 108 | 100 sementes antigas + 8 notas autorais recentes |
| Candidatas aprovadas no gate automatizado | 8 | Aguardam revisão factual humana |
| Notas com revisão humana registrada | 0 | Nenhuma plenamente validada ainda |
| Registros do checkpoint marcados como materializados | 8.000 | Materialização não é validação editorial |

**A meta de 1.000.000 de notas válidas ainda não foi atingida.** O projeto está migrando de contagem por volume para lotes menores, auditáveis e com fontes específicas. Veja [`knowledge-federation/STATUS-CONSOLIDACAO-1M.md`](knowledge-federation/STATUS-CONSOLIDACAO-1M.md) e o [relatório de qualidade](knowledge-federation/exports/reports/note-quality-audit.md).

## Artefatos históricos do merge

Os pacotes continuam disponíveis para inspeção e recuperação. Seus números indicam entradas/arquivos gerados a partir do ledger, não notas editorialmente validadas.

| Pacote | Tamanho aproximado | Uso / ressalva |
|---|---:|---|
| `knowledge-federation/archives/merge-completo-materializado-1m.tar.xz` | 34 MB | Merge histórico com lotes e vaults materializados; o conteúdo-template não entra na meta de validade |
| `knowledge-federation/archives/study-vault-1m-packs.zip` | 19 MB | 78 Study Packs / arquivos gerados do ledger; não assumir que sejam 15.600 notas validadas |
| `knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz` | 24 MB | Checkpoint compacto do catálogo SQLite; 1.000.000 de registros virtuais |
| `knowledge-federation/archives/starter-vault-prioritario.zip` | 1,1 MB | Recorte de entrada; a quantidade de arquivos não é selo de qualidade |
| `vault-desenvolvimento-software-com-ia/` | ativo | Vault autoral amplo, mantido separadamente do ledger da meta de 1 milhão |

### Extrair lotes históricos sem criar 1 milhão de arquivos de uma vez

```bash
# Exemplo: extrair apenas um intervalo de lotes
mkdir -p /tmp/merge-parcial
tar -xJf knowledge-federation/archives/merge-completo-materializado-1m.tar.xz \
  -C /tmp/merge-parcial MERGE-COMPLETO/10-lotes/0001-0100
```

### Consultar o catálogo SQLite

```bash
python3 knowledge-federation/scripts/ledger_stats.py
python3 knowledge-federation/scripts/query_checkpoint.py "agentes" --domain ia --limit 20
```

## Retomada com gate de qualidade

O primeiro lote de retomada adiciona 8 notas de software sobre confiabilidade, contratos de API, observabilidade, SLOs, migrações e checks de merge. Todas passaram por verificações automatizadas de estrutura e fontes; a revisão humana/factual ainda está pendente.

```bash
# Testes do gate de qualidade
python3 -m unittest discover -s knowledge-federation/tests -v

# Reauditar notas ativas e o checkpoint compactado
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

O passe automatizado exige também wikilinks resolvidos e significa **pronta para revisão**, não “fato verificado”. A nota só deve ser promovida após checagem das fontes por pessoa revisora identificada no frontmatter. O fluxo e os critérios estão em [`knowledge-federation/README.md`](knowledge-federation/README.md).

## Segurança em domínios regulados

`cannabis-medicinal` e `micologia` permanecem restritos a conteúdo legal, educacional, científico, documental e de redução de danos. Não gerar instruções operacionais de cultivo, produção, extração, otimização de potência/rendimento ou evasão de fiscalização.
