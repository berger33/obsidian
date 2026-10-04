---
id: software.seguranca.tranche06.000514
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

# OpenCTI: Motor de Raciocínio e Inferência (`Rule Engine`) para Dedução Automática de Relações Transitivas no Grafo

## Em uma frase
O OpenCTI incorpora um **Rule Engine** (motor de inferência lógica) que analisa continuamente as relações explícitas inseridas no grafo STIX 2.1 e cria automaticamente **relações inferidas** (*inferred relationships*) baseadas em regras lógicas de transitividade.

## Por que importa
Se o Relatório A documenta que o `Intrusion-Set APT-X` **`uses`** o `Malware Loader-Y`, e uma investigação de incidente local documenta que o `Malware Loader-Y` **`targets`** a `Organization Banco-Z`, o motor de inferência deduz automaticamente que `APT-X` **`targets`** `Banco-Z` sem exigir que o analista crie essa aresta manualmente.

## Como funciona
Crucialmente, as relações inferidas mantêm um ponteiro direto para as relações de origem (*explanations*): se uma das relações originais for excluída ou tiver sua validade encerrada, o motor de inferência remove imediatamente a relação deduzida, garantindo zero órfãos lógicos no grafo.

## Exemplo
```graphql
# Consultar relacoes STIX incluindo explicitamente aquelas deduzidas pelo Rule Engine (is_inferred)
query CheckInferredRelations($fromId: [String]) {
  stixCoreRelationships(fromId: $fromId, first: 25) {
    edges {
      node {
        id
        relationship_type
        is_inferred
        to {
          ... on BasicObject {
            id
            entity_type
          }
        }
      }
    }
  }
}
```

## Limites e trade-offs
Habilitar regras de inferência em uma base onde conectores de baixa qualidade inserem relações especulativas com `confidence` alta amplificará falsas atribuições; ajuste o nível máximo de confiança de cada conector (`CONNECTOR_CONFIDENCE_LEVEL`).

## Como verificar
Ative uma regra de inferência em *Settings -> Customization -> Rules* e verifique na visualização de grafo de um ator de ameaça as arestas tracejadas marcadas como `Inferred`.

## Conexões
- [[opencti-ecossistema-conectores-import-enrichment-stream-export]] — Veja também: OpenCTI: Arquitetura dos Cinco Tipos de Conectores (`EXTERNAL_IMPORT`, `INTERNAL_IMPORT_FILE`, `INTERNAL_ENRICHMENT`, `INTERNAL_EXPORT_FILE` e `STREAM`).
- [[opencti-ciclo-vida-indicadores-decay-rules-score-revogacao]] — Veja também: OpenCTI: Ciclo de Vida de Indicadores — **Decay Rules** (Curvas de Decaimento de `x_opencti_score`), Expiração `valid_until` e Revogação.
- [[opencti-arquitetura-stix21-knowledge-graph-graphql-filigran]] — Referência cruzada direta com opencti-arquitetura-stix21-knowledge-graph-graphql-filigran.
- [[opencti-ontologia-stix21-sdos-scos-sros-rastreabilidade-fontes]] — Referência cruzada direta com opencti-ontologia-stix21-sdos-scos-sros-rastreabilidade-fontes.
- [[opencti-governanca-rbac-marking-definitions-tlp-confianca-organizacoes]] — Referência cruzada direta com opencti-governanca-rbac-marking-definitions-tlp-confianca-organizacoes.

## Fontes
- [OpenCTI Official GitHub — STIX 2.1 Cyber Threat Intelligence Platform](https://raw.githubusercontent.com/OpenCTI-Platform/opencti/master/README.md) — documentação oficial da plataforma OpenCTI cobrindo o grafo STIX 2.1, GraphQL, inferência e RBAC; consultado em 2026-10-03.
- [OpenCTI Connectors Official GitHub — Architecture & Classes](https://raw.githubusercontent.com/OpenCTI-Platform/connectors/master/README.md) — documentação oficial das 5 classes de conectores do OpenCTI (EXTERNAL_IMPORT, INTERNAL_ENRICHMENT, STREAM, etc.); consultado em 2026-10-03.
- [OpenCTI Official Documentation — Connectors Deployment](https://docs.opencti.io/latest/deployment/connectors/) — guia oficial de implantação e operação de conectores e workers do OpenCTI; consultado em 2026-10-03.
