---
id: software.seguranca.tranche06.000512
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
fontes: ["https://raw.githubusercontent.com/OpenCTI-Platform/opencti/master/README.md", "https://raw.githubusercontent.com/OpenCTI-Platform/connectors/master/README.md", "https://docs.opencti.io/latest/deployment/connectors/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenCTI: Modelagem com Objetos **STIX 2.1** — Domain Objects (SDOs), Cyber Observables (SCOs), Relationships (SROs) e `Confidence`

## Em uma frase
O esquema de dados do OpenCTI implementa fielmente a separação formal do padrão STIX 2.1 entre **STIX Domain Objects (SDOs)**, **STIX Cyber-observable Objects (SCOs)** e **STIX Relationship Objects (SROs)**.

## Por que importa
Evita a confusão comum entre um fato técnico bruto (*Observável / SCO*: o endereço IPv4 `198.51.100.44` existe) e uma hipótese analítica de detecção (*Indicador / SDO*: o padrão `[ipv4-addr:value = '198.51.100.44']` indica atividade do malware X entre a data A e a data B com confiança 85).

## Como funciona
Os **SDOs** modelam conceitos analíticos (`Threat-Actor`, `Intrusion-Set`, `Campaign`, `Malware`, `Tool`, `Attack-Pattern`, `Vulnerability`, `Indicator`, `Report`, `Case-Incident`, `Grouping`), os **SCOs** modelam artefatos técnicos (`IPv4-Addr`, `Domain-Name`, `StixFile`, `Url`, `X509-Certificate`, `Autonomous-System`) e os **SROs** são arestas tipadas com vigência temporal (`first_seen`, `last_seen`, `confidence`, `author` e `external_references`), como `Intrusion-Set --[uses]--> Malware` ou `Indicator --[based-on]--> IPv4-Addr`.

## Exemplo
```python
from pycti import OpenCTIApiClient

client = OpenCTIApiClient("https://opencti.soc.internal.corp", "OPENCTI_API_TOKEN")
indicator = client.indicator.create(
    name="C2 Domain evil-updater.example",
    pattern="[domain-name:value = 'evil-updater.example']",
    pattern_type="stix",
    x_opencti_main_observable_type="Domain-Name",
    confidence=85,
    x_opencti_CreateObservables=True
)
```

## Limites e trade-offs
Ao usar `x_opencti_CreateObservables=True` na criação de um `Indicator`, o OpenCTI extrai automaticamente o `Domain-Name` da expressão STIX e cria o SCO correspondente vinculado pela relação `based-on`.

## Como verificar
Consulte o indicador recém-criado na UI ou via `pycti` e confirme a presença do relacionamento `based-on` apontando para o observável `evil-updater.example`.

## Conexões
- [[opencti-arquitetura-stix21-knowledge-graph-graphql-filigran]] — Veja também: OpenCTI: Arquitetura da Plataforma de Threat Intelligence Baseada em Grafo de Conhecimento **STIX 2.1** e API GraphQL.
- [[opencti-ecossistema-conectores-import-enrichment-stream-export]] — Veja também: OpenCTI: Arquitetura dos Cinco Tipos de Conectores (`EXTERNAL_IMPORT`, `INTERNAL_IMPORT_FILE`, `INTERNAL_ENRICHMENT`, `INTERNAL_EXPORT_FILE` e `STREAM`).
- [[opencti-motor-inferencia-regras-deducao-relacoes-transitivas]] — Referência cruzada direta com opencti-motor-inferencia-regras-deducao-relacoes-transitivas.
- [[opencti-ciclo-vida-indicadores-decay-rules-score-revogacao]] — Referência cruzada direta com opencti-ciclo-vida-indicadores-decay-rules-score-revogacao.

## Fontes
- [OpenCTI Official GitHub — STIX 2.1 Cyber Threat Intelligence Platform](https://raw.githubusercontent.com/OpenCTI-Platform/opencti/master/README.md) — documentação oficial da plataforma OpenCTI cobrindo o grafo STIX 2.1, GraphQL, inferência e RBAC; consultado em 2026-10-03.
- [OpenCTI Connectors Official GitHub — Architecture & Classes](https://raw.githubusercontent.com/OpenCTI-Platform/connectors/master/README.md) — documentação oficial das 5 classes de conectores do OpenCTI (EXTERNAL_IMPORT, INTERNAL_ENRICHMENT, STREAM, etc.); consultado em 2026-10-03.
- [OpenCTI Official Documentation — Connectors Deployment](https://docs.opencti.io/latest/deployment/connectors/) — guia oficial de implantação e operação de conectores e workers do OpenCTI; consultado em 2026-10-03.
