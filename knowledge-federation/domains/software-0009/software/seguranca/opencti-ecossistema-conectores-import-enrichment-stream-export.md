---
id: software.seguranca.tranche06.000513
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

# OpenCTI: Arquitetura dos Cinco Tipos de Conectores (`EXTERNAL_IMPORT`, `INTERNAL_IMPORT_FILE`, `INTERNAL_ENRICHMENT`, `INTERNAL_EXPORT_FILE` e `STREAM`)

## Em uma frase
A integração do OpenCTI com o ecossistema de segurança (`OpenCTI-Platform/connectors`) é realizada por microserviços Python independentes que se comunicam com a plataforma via API GraphQL, filas RabbitMQ e streams Redis, classificados em cinco categorias arquiteturais.

## Por que importa
Desacoplar a ingestão e o enriquecimento do núcleo da plataforma garante que um conector lento ou uma falha de API externa jamais degrade a performance do banco de grafos ou da interface dos analistas.

## Como funciona
As cinco classes são: **(1) `EXTERNAL_IMPORT`** (busca dados periodicamente de fontes externas como MITRE ATT&CK, MISP, AlienVault OTX, Mandiant, Abuse.ch, CISA KEV e envia bundles STIX2 para os workers), **(2) `INTERNAL_IMPORT_FILE`** (extrai entidades de PDFs, relatórios Markdown ou STIX enviados na plataforma), **(3) `INTERNAL_ENRICHMENT`** (enriquece observáveis sob demanda ou em *auto-trigger* com VirusTotal, Shodan, CrowdSec, GreyNoise), **(4) `INTERNAL_EXPORT_FILE`** (exporta relatórios em STIX2, CSV, PDF) e **(5) `STREAM`** (consome o stream Redis ao vivo do OpenCTI para sincronizar indicadores em tempo real com Splunk, Elastic, Sentinel, QRadar ou Tanium).

## Exemplo
```yaml
# Exemplo de servico de conector EXTERNAL_IMPORT (MITRE ATT&CK) em docker-compose.yml
connector-mitre:
  image: opencti/connector-mitre:6.3.6
  environment:
    - OPENCTI_URL=http://opencti:8080
    - OPENCTI_TOKEN=${OPENCTI_MITRE_CONNECTOR_TOKEN}
    - CONNECTOR_ID=88ec0c6a-13ce-5e39-b486-354fe4a7084f
    - CONNECTOR_NAME=MITRE Datasets
    - CONNECTOR_SCOPE=tool,report,malware,identity,campaign,intrusion-set,attack-pattern,course-of-action
    - CONNECTOR_CONFIDENCE_LEVEL=90
    - MITRE_INTERVAL=7
  restart: always
```

## Limites e trade-offs
Todo conector envia pacotes para a fila RabbitMQ, que só são gravados no OpenCTI pelos **OpenCTI Workers** (`opencti/worker`); se os containers de `worker` estiverem parados ou subdimensionados, as filas de conectores ficarão acumuladas em `Pending` na tela *Data -> Ingestion -> Connectors*.

## Como verificar
Inspecione na aba *Connectors* que tanto os conectores ativos quanto os `Workers` estão reportando batimentos cardíacos (`Active`) e fila sem gargalo.

## Conexões
- [[opencti-ontologia-stix21-sdos-scos-sros-rastreabilidade-fontes]] — Veja também: OpenCTI: Modelagem com Objetos **STIX 2.1** — Domain Objects (SDOs), Cyber Observables (SCOs), Relationships (SROs) e `Confidence`.
- [[opencti-motor-inferencia-regras-deducao-relacoes-transitivas]] — Veja também: OpenCTI: Motor de Raciocínio e Inferência (`Rule Engine`) para Dedução Automática de Relações Transitivas no Grafo.
- [[opencti-arquitetura-stix21-knowledge-graph-graphql-filigran]] — Referência cruzada direta com opencti-arquitetura-stix21-knowledge-graph-graphql-filigran.
- [[opencti-streams-taxii21-live-streams-feeds-csv-integracao-siem]] — Referência cruzada direta com opencti-streams-taxii21-live-streams-feeds-csv-integracao-siem.
- [[thehive-sincronizacao-bidirecional-misp-import-export-iocs]] — Referência cruzada direta com thehive-sincronizacao-bidirecional-misp-import-export-iocs.

## Fontes
- [OpenCTI Official GitHub — STIX 2.1 Cyber Threat Intelligence Platform](https://raw.githubusercontent.com/OpenCTI-Platform/opencti/master/README.md) — documentação oficial da plataforma OpenCTI cobrindo o grafo STIX 2.1, GraphQL, inferência e RBAC; consultado em 2026-10-03.
- [OpenCTI Connectors Official GitHub — Architecture & Classes](https://raw.githubusercontent.com/OpenCTI-Platform/connectors/master/README.md) — documentação oficial das 5 classes de conectores do OpenCTI (EXTERNAL_IMPORT, INTERNAL_ENRICHMENT, STREAM, etc.); consultado em 2026-10-03.
- [OpenCTI Official Documentation — Connectors Deployment](https://docs.opencti.io/latest/deployment/connectors/) — guia oficial de implantação e operação de conectores e workers do OpenCTI; consultado em 2026-10-03.
