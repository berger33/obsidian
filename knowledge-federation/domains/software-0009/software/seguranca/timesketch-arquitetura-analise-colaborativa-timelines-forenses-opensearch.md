---
id: software.seguranca.tranche06.000521
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/google/timesketch/master/README.md", "https://timesketch.org/guides/user/sketch-overview/", "https://timesketch.org/guides/admin/install/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Google Timesketch: Arquitetura de Análise Colaborativa de *Super-Timelines* Forenses (Python/Flask, Celery, PostgreSQL e OpenSearch)

## Em uma frase
**Timesketch** (`google/timesketch`, Apache-2.0) é a plataforma open-source desenvolvida no Google para análise colaborativa de linhas do tempo forenses (*Super-Timelines*), permitindo que múltiplos investigadores DFIR correlacionem milhões de eventos de dezenas de máquinas simultaneamente.

## Por que importa
Em um incidente complexo envolvendo movimentação lateral por 15 servidores Windows e Linux, analisar logs isolados em planilhas é inviável; o Timesketch unifica todos os artefatos temporais em um único **Sketch** indexado em **OpenSearch**, suportando anotações, estrelas, etiquetas, grafos, regras Sigma e *Stories*.

## Como funciona
A arquitetura do Timesketch combina uma aplicação web e API REST em Python/Flask (com frontend Vue.js), um banco relacional **PostgreSQL** (que armazena usuários, ACLs de sketches, metadados de timelines, views salvas e *Stories*), um cluster **OpenSearch** (onde cada timeline ou conjunto de timelines reside como índice de busca rápida) e workers **Celery/Redis** (que processam a ingestão assíncrona de arquivos Plaso/JSONL/CSV e executam os *Analyzers*).

## Exemplo
```bash
# Verificar o status dos servicos e listar todos os sketches e timelines via CLI administrativa tsctl
tsctl version
tsctl list-sketches
```

## Limites e trade-offs
Para arquivar um sketch concluído (`Archive`) e fechar os índices OpenSearch correspondentes liberando memória RAM do cluster, **todas** as timelines associadas devem estar no estado `ready` (nenhuma pode estar em `processing` ou `fail`) e o sketch não pode ter as labels `protected` ou `preserved`.

## Como verificar
Caso uma timeline fique travada em processamento, diagnostique com `tsctl timeline-status <TIMELINE_ID>` antes de gerenciar o ciclo de vida do sketch.

## Conexões
- [[timesketch-ingestao-plaso-log2timeline-jsonl-csv-timesketch-importer]] — Veja também: Timesketch: Geração de *Super-Timelines* com **Plaso (`log2timeline.py`)** e Ingestão via `timesketch_importer` (Plaso, JSONL e CSV).
- [[timesketch-linguagem-busca-opensearch-dsl-saved-views-context-query]] — Referência cruzada direta com timesketch-linguagem-busca-opensearch-dsl-saved-views-context-query.

## Fontes
- [Google Timesketch Official GitHub — Collaborative Forensic Timeline Analysis](https://raw.githubusercontent.com/google/timesketch/master/README.md) — documentação oficial do Google Timesketch para análise colaborativa de timelines forenses; consultado em 2026-10-03.
- [Timesketch Official User Guide — Sketch Overview & Lifecycle](https://timesketch.org/guides/user/sketch-overview/) — guia oficial de abas do Sketch (Explore, Stories, Intelligence), tsctl, arquivamento e labels de proteção; consultado em 2026-10-03.
- [Timesketch Official Admin Guide — Installation & Configuration](https://timesketch.org/guides/admin/install/) — guia oficial de administração, Analyzers, Sigma e DFIQ no Timesketch; consultado em 2026-10-03.
