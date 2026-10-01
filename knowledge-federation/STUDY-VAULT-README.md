# Study Vault — pacote histórico de 78 subdomínios

Data: 2026-10-01

> **Ressalva de qualidade:** o pacote contém 15.600 arquivos de nota materializados a partir do ledger, mas as contagens e a auditoria de links não comprovam conteúdo válido. A auditoria encontrou texto-template nos registros virtuais que alimentam o pacote. Não contabilize esses arquivos como 15.600 notas validadas. Veja [`STATUS-CONSOLIDACAO-1M.md`](STATUS-CONSOLIDACAO-1M.md).

## Entrega principal

```text
knowledge-federation/archives/study-vault-1m-packs.zip
```

Abra esse zip como vault no Obsidian. Ponto de entrada:

```text
00-Inicio/Home.md
```

## Conteúdo consolidado

- **15.600 arquivos de nota materializados** a partir do ledger (`78 packs × 200 arquivos`).
- **78 study packs temáticos** organizados pelos subdomínios de `config/taxonomy.json`; cobertura taxonômica não é avaliação de conteúdo.
- **85 MOCs** (`78` MOCs de subdomínio + `7` MOCs mestres por domínio).
- **5 trilhas guiadas**.
- **6 playbooks e matrizes de decisão**.
- **9 arquivos Canvas** (`Mapa-Geral.canvas`, `Trilhas-e-Playbooks.canvas` e 7 canvases por domínio).
- **Configuração de Graph View** com cores por domínio (`.obsidian/graph.json`).
- Auditoria histórica de links: **0 links wiki quebrados** em 93.894 analisados. Isso confirma resolução de links, não substância, fontes ou exatidão factual.

## Trilhas guiadas incluídas

```text
Trilha — Orquestrador de IA
Trilha — Fullstack com IA
Trilha — Jogos 2D, Online e MMO
Trilha — Produto, Carreira e MVP
Trilha — Ciências Reguladas com Segurança
```

## Playbooks e matrizes incluídos

```text
Playbook — Como estudar um pack
Playbook — Como materializar novos recortes
Checklist — Fontes e Volatilidade
Matriz — Ferramentas de IA para Desenvolvimento
Matriz — Engine para Jogos
Perguntas para profissionais em domínios regulados
```

## Auditoria

Relatório dentro do vault (`_meta/auditoria-study-vault.md`) e em `knowledge-federation/exports/reports/auditoria-study-vault.md`:

```text
Study packs (subdomínios): 78
Arquivos de nota nos packs (não validados editorialmente): 15600
Arquivos Markdown totais no vault: 15776
MOCs (78 subdomínios + 7 domínios + Home): 86
Trilhas e Playbooks: 11
Arquivos Canvas: 9
Links wiki analisados: 93894
Links quebrados: 0
```

## Observação sobre escala

O ledger completo permanece compactado em:

```text
knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

A sequência de 5.000 lotes (1.000.000 arquivos-placeholder) e este vault (15.600 arquivos de nota derivados do catálogo) estão consolidados em; esses totais não representam notas validadas:

```text
knowledge-federation/archives/merge-completo-materializado-1m.tar.xz
```
