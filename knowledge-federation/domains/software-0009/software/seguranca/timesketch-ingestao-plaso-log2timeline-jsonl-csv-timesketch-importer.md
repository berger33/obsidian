---
id: software.seguranca.tranche06.000522
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

# Timesketch: Geração de *Super-Timelines* com **Plaso (`log2timeline.py`)** e Ingestão via `timesketch_importer` (Plaso, JSONL e CSV)

## Em uma frase
O Timesketch ingere linhas do tempo geradas pelo framework **Plaso (`log2timeline`)** (arquivos `.plaso`) ou eventos estruturados em **JSONL** (JSON Lines) e **CSV**, tanto pela interface web quanto programaticamente via CLI e biblioteca **`timesketch-import-client`** (`timesketch_importer`).

## Por que importa
O `log2timeline.py` extrai carimbos de tempo de centenas de fontes forenses de uma imagem de disco ou coleta de triagem (MFT `$Standard_Information`/`$File_Name`, Windows Event Logs `.evtx`, Prefetch, Amcache, Shimcache, Registry Hives, histórico de navegadores, `syslog`/`journald`/`auditd` e metadados de arquivos), normalizando tudo para UTC.

## Como funciona
Para ingestão em JSONL ou CSV, cada evento enviado ao Timesketch deve conter no mínimo três campos obrigatórios: **`message`** (resumo textual do evento), **`datetime`** (string ISO 8601 com fuso horário, ex.: `2026-10-03T14:22:10.123456+00:00`) e **`timestamp_desc`** (o significado semântico daquele carimbo de tempo, ex.: `File Creation Time`, `Last Connection Time` ou `Event Logged`).

## Exemplo
```bash
# Extrair super-timeline forense de uma imagem de disco com log2timeline e enviar ao Timesketch via CLI
log2timeline.py --storage-file /cases/host01.plaso /cases/host01-disk.raw

timesketch_importer --host https://timesketch.dfir.internal.corp \
  --sketch_id 42 \
  --timeline_name "wkst-fin-09-super-timeline" \
  /cases/host01.plaso
```

## Limites e trade-offs
Omitir o fuso horário em `datetime` ao importar arquivos CSV/JSONL customizados ou misturar horários locais de servidores em fusos diferentes sem normalizar para **UTC (`+00:00` / `Z`)** corrompe a correlação cronológica entre múltiplas máquinas no mesmo sketch.

## Como verificar
Valide um arquivo JSONL antes do upload com `head -n 5 events.jsonl | jq -e '.message and .datetime and .timestamp_desc'`.

## Conexões
- [[timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch]] — Veja também: Google Timesketch: Arquitetura de Análise Colaborativa de *Super-Timelines* Forenses (Python/Flask, Celery, PostgreSQL e OpenSearch).
- [[timesketch-linguagem-busca-opensearch-dsl-saved-views-context-query]] — Veja também: Timesketch: Sintaxe de Busca OpenSearch Query String, Filtros de Tipo de Dados (`data_type`), *Context Queries* e *Saved Views*.

## Fontes
- [Google Timesketch Official GitHub — Collaborative Forensic Timeline Analysis](https://raw.githubusercontent.com/google/timesketch/master/README.md) — documentação oficial do Google Timesketch para análise colaborativa de timelines forenses; consultado em 2026-10-03.
- [Timesketch Official User Guide — Sketch Overview & Lifecycle](https://timesketch.org/guides/user/sketch-overview/) — guia oficial de abas do Sketch (Explore, Stories, Intelligence), tsctl, arquivamento e labels de proteção; consultado em 2026-10-03.
- [Timesketch Official Admin Guide — Installation & Configuration](https://timesketch.org/guides/admin/install/) — guia oficial de administração, Analyzers, Sigma e DFIQ no Timesketch; consultado em 2026-10-03.
