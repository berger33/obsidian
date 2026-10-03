---
id: software.seguranca.tranche06.000524
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

# Timesketch: Execução de **Analyzers** Automatizados em Background (Taggers, Chain Analyzer, Account Finder, Domain/Hash Enrichment)

## Em uma frase
Assim que uma nova timeline termina de ser indexada no Timesketch, os workers Celery podem executar dezenas de **Analyzers** automatizados sobre os eventos para marcar anomalias, extrair atributos do sistema, encadear eventos relacionados e consultar bases de inteligência.

## Por que importa
Em vez de o analista buscar manualmente cada técnica conhecida em uma timeline de 10 milhões de linhas, os *Analyzers* pré-classificam os eventos adicionando estrelas, comentários explicativos, tags (ex.: `logon-type-10`, `suspicious-execution`) e atributos de resumo do host.

## Como funciona
Os principais *Analyzers* incluem: **Tagger** (aplica tags baseadas em queries YAML pré-definidas), **Chain Analyzer** (rastreia cadeias de eventos conectados, como um arquivo baixado pelo navegador Chrome que posteriormente é executado como binário no `Prefetch`), **Account Finder** / **Feature Extraction** (extrai contas de usuário, IPs e domínios observados na máquina), **NTFS Timestomp Analyzer** (compara `$Standard_Information` vs `$File_Name` na MFT para detectar adulteração de datas *timestomping*) e conectores de CTI (MISP, OpenCTI, VirusTotal, Yeti).

## Exemplo
```python
from timesketch_api_client import config

ts = config.get_client()
sketch = ts.get_sketch(42)
timeline = sketch.get_timeline(timeline_id=7)

# Disparar os analyzers de deteccao de Timestomping NTFS e regras Sigma sobre a timeline
sessions = timeline.run_analyzers(analyzer_names=["ntfs_timestomp", "sigma"])
for s in sessions:
    print(s.status_string)
```

## Limites e trade-offs
Executar todos os *Analyzers* externos de enriquecimento simultaneamente em dezenas de timelines pode esgotar cotas de API externas; configure `AUTO_SKETCH_ANALYZERS` no `/etc/timesketch/timesketch.conf` apenas para os analisadores locais rápidos (Tagger, Feature Extraction, Timestomp, Sigma).

## Como verificar
Verifique na aba *Analyzers* do sketch os resultados consolidados e filtre por `tag:*` na aba *Explore* para inspecionar os eventos marcados.

## Conexões
- [[timesketch-linguagem-busca-opensearch-dsl-saved-views-context-query]] — Veja também: Timesketch: Sintaxe de Busca OpenSearch Query String, Filtros de Tipo de Dados (`data_type`), *Context Queries* e *Saved Views*.
- [[timesketch-deteccao-ameacas-regras-sigma-tsctl-sigma-analyzer]] — Veja também: Timesketch: Caça a Ameaças (*Threat Hunting*) Retroativa em Timelines com Regras **Sigma** e `tsctl`.
- [[timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch]] — Referência cruzada direta com timesketch-arquitetura-analise-colaborativa-timelines-forenses-opensearch.
- [[timesketch-aba-intelligence-iocs-integracao-yeti-misp-opencti]] — Referência cruzada direta com timesketch-aba-intelligence-iocs-integracao-yeti-misp-opencti.

## Fontes
- [Google Timesketch Official GitHub — Collaborative Forensic Timeline Analysis](https://raw.githubusercontent.com/google/timesketch/master/README.md) — documentação oficial do Google Timesketch para análise colaborativa de timelines forenses; consultado em 2026-10-03.
- [Timesketch Official User Guide — Sketch Overview & Lifecycle](https://timesketch.org/guides/user/sketch-overview/) — guia oficial de abas do Sketch (Explore, Stories, Intelligence), tsctl, arquivamento e labels de proteção; consultado em 2026-10-03.
- [Timesketch Official Admin Guide — Installation & Configuration](https://timesketch.org/guides/admin/install/) — guia oficial de administração, Analyzers, Sigma e DFIQ no Timesketch; consultado em 2026-10-03.
