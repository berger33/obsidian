---
id: software.seguranca.tranche06.000511
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

# OpenCTI: Arquitetura da Plataforma de Threat Intelligence Baseada em Grafo de Conhecimento **STIX 2.1** e API GraphQL

## Em uma frase
**OpenCTI** (*Open Cyber Threat Intelligence Platform*, `OpenCTI-Platform/opencti`, Apache-2.0, mantido pela Filigran) é uma plataforma moderna de gestão de conhecimento e observáveis de inteligência de ameaças construída nativamente sobre o padrão **OASIS STIX 2.1** e exposta via API **GraphQL**.

## Por que importa
Conecta a inteligência estratégica e geopolítica (atores de ameaça, campanhas, vitimologia por setor/país e relatórios de inteligência) diretamente à inteligência tática e operacional (técnicas MITRE ATT&CK, vulnerabilidades CVE, malwares e indicadores de comprometimento) com rastreabilidade até a fonte primária.

## Como funciona
A pilha de infraestrutura do OpenCTI combina uma aplicação Node.js/TypeScript e frontend React com **OpenSearch/Elasticsearch** (armazenamento do grafo de entidades e relacionamentos STIX), **Redis** (gerenciamento de sessões, cache e streams de eventos em tempo real), **RabbitMQ** (filas de processamento assíncrono dos workers e conectores) e **MinIO/S3** (armazenamento de relatórios PDF e artefatos binários).

## Exemplo
```graphql
# Consulta GraphQL na API do OpenCTI listando Intrusion Sets e suas relacoes STIX
query ListIntrusionSets {
  intrusionSets(first: 10, orderBy: name, orderMode: asc) {
    edges {
      node {
        id
        standard_id
        name
        description
        confidence
      }
    }
  }
}
```

## Limites e trade-offs
Cada entidade no OpenCTI possui um `standard_id` determinístico STIX 2.1 (ex.: `intrusion-set--...` calculado a partir das propriedades canônicas), o que impede a duplicação de atores de ameaça ou técnicas ATT&CK quando ingeridos de múltiplas fontes distintas.

## Como verificar
Execute uma query GraphQL autenticada (`Authorization: Bearer <TOKEN>`) em `/graphql` consultando `{ about { version } }` para validar a saúde da instância.

## Conexões
- [[opencti-ontologia-stix21-sdos-scos-sros-rastreabilidade-fontes]] — Veja também: OpenCTI: Modelagem com Objetos **STIX 2.1** — Domain Objects (SDOs), Cyber Observables (SCOs), Relationships (SROs) e `Confidence`.
- [[opencti-ecossistema-conectores-import-enrichment-stream-export]] — Referência cruzada direta com opencti-ecossistema-conectores-import-enrichment-stream-export.
- [[mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies]] — Referência cruzada direta com mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies.

## Fontes
- [OpenCTI Official GitHub — STIX 2.1 Cyber Threat Intelligence Platform](https://raw.githubusercontent.com/OpenCTI-Platform/opencti/master/README.md) — documentação oficial da plataforma OpenCTI cobrindo o grafo STIX 2.1, GraphQL, inferência e RBAC; consultado em 2026-10-03.
- [OpenCTI Connectors Official GitHub — Architecture & Classes](https://raw.githubusercontent.com/OpenCTI-Platform/connectors/master/README.md) — documentação oficial das 5 classes de conectores do OpenCTI (EXTERNAL_IMPORT, INTERNAL_ENRICHMENT, STREAM, etc.); consultado em 2026-10-03.
- [OpenCTI Official Documentation — Connectors Deployment](https://docs.opencti.io/latest/deployment/connectors/) — guia oficial de implantação e operação de conectores e workers do OpenCTI; consultado em 2026-10-03.
