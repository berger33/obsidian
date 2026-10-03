---
id: software.seguranca.tranche06.000523
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

# Timesketch: Sintaxe de Busca OpenSearch Query String, Filtros de Tipo de Dados (`data_type`), *Context Queries* e *Saved Views*

## Em uma frase
Na aba **Explore** do Timesketch, o analista filtra dezenas de milhões de eventos combinando expressões **OpenSearch Query String** (operadores booleanos `AND`/`OR`/`NOT`, curingas, expressões regulares `/.../` e faixas numéricas), filtros de intervalo de tempo (*Timefilter*), etiquetas (`__ts_star`, `__ts_comment`) e **Saved Views**.

## Por que importa
O campo **`data_type`** atribuído pelos parsers do Plaso é a âncora mais poderosa para buscas cirúrgicas: por exemplo, `data_type:"windows:evtx:record"` filtra apenas logs de eventos do Windows, `data_type:"windows:registry:key_value"` filtra chaves de Registro e `data_type:"fs:stat"` filtra metadados de sistema de arquivos.

## Como funciona
Quando o investigador encontra um evento suspeito (ex.: o download de um script PowerShell às `14:05:12Z`), clicar no ícone de **Context Query** ao lado do evento abre instantaneamente uma janela temporal simétrica (ex.: `± 5 minutos` antes e depois daquele segundo exato) mostrando tudo o que aconteceu no sistema imediatamente antes e imediatamente após o evento pivô.

## Exemplo
```text
# Buscar logins RDP bem-sucedidos (Event ID 4624 LogonType 10) ou criacao de servicos (7045) no Windows
data_type:"windows:evtx:record" AND ((event_identifier:4624 AND xml_string:*LogonType\>10*) OR event_identifier:7045)
```

## Limites e trade-offs
Buscas que iniciam com curinga à esquerda (`*mimikatz*`) em campos não-tokenizados exigem varredura cara em índices grandes do OpenSearch; restrinja sempre primeiro pelo `data_type` e por um intervalo de tempo (*Timerange*) antes de usar expressões regulares complexas.

## Como verificar
Salve as queries recorrentes de triagem como **Saved Views** no sketch para que toda a equipe de resposta a incidentes acesse os mesmos recortes com um clique.

## Conexões
- [[timesketch-ingestao-plaso-log2timeline-jsonl-csv-timesketch-importer]] — Veja também: Timesketch: Geração de *Super-Timelines* com **Plaso (`log2timeline.py`)** e Ingestão via `timesketch_importer` (Plaso, JSONL e CSV).
- [[timesketch-analisadores-automaticos-analyzers-chain-tagger-similarity]] — Veja também: Timesketch: Execução de **Analyzers** Automatizados em Background (Taggers, Chain Analyzer, Account Finder, Domain/Hash Enrichment).
- [[timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch]] — Referência cruzada direta com timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch.
- [[timesketch-investigacao-guiada-dfiq-questions-facets-approaches]] — Referência cruzada direta com timesketch-investigacao-guiada-dfiq-questions-facets-approaches.

## Fontes
- [Google Timesketch Official GitHub — Collaborative Forensic Timeline Analysis](https://raw.githubusercontent.com/google/timesketch/master/README.md) — documentação oficial do Google Timesketch para análise colaborativa de timelines forenses; consultado em 2026-10-03.
- [Timesketch Official User Guide — Sketch Overview & Lifecycle](https://timesketch.org/guides/user/sketch-overview/) — guia oficial de abas do Sketch (Explore, Stories, Intelligence), tsctl, arquivamento e labels de proteção; consultado em 2026-10-03.
- [Timesketch Official Admin Guide — Installation & Configuration](https://timesketch.org/guides/admin/install/) — guia oficial de administração, Analyzers, Sigma e DFIQ no Timesketch; consultado em 2026-10-03.
