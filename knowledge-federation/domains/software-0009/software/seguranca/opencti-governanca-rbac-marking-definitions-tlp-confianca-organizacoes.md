---
id: software.seguranca.tranche06.000516
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

# OpenCTI: Controle de Acesso Baseado em **Marking Definitions** (`TLP`, `PAP`, `Statement`), Segregação por Organizações e `Max Confidence Level`

## Em uma frase
O modelo de segurança do OpenCTI combina **Role-Based Access Control (RBAC)** (definindo capacidades como `KNOWLEDGE_KNUPDATE`, `SETTINGS_SETACCESSES`), segregação multi-tenant por **Organizations** e filtragem obrigatória no nível de linha por **STIX Marking Definitions** (`TLP:CLEAR`, `TLP:GREEN`, `TLP:AMBER`, `TLP:AMBER+STRICT`, `TLP:RED`).

## Por que importa
Mesmo que um usuário ou conector de API possua permissão de leitura na base de conhecimento, ele **jamais** verá no GraphQL ou na interface qualquer entidade, relatório ou relacionamento cujo `objectMarking` exceda as marcações explicitamente autorizadas para o seu Grupo.

## Como funciona
Adicionalmente, cada Usuário ou Grupo no OpenCTI possui um **Max Confidence Level** (`0` a `100`) e uma política de sobrescrita: um conector de feed OSINT público configurado com `Max Confidence Level = 40` nunca conseguirá sobrescrever um atributo ou relação que já foi validado manualmente por um analista humano do CSIRT com `Confidence = 90`.

## Exemplo
```python
# Criar um relatorio STIX no OpenCTI aplicando explicitamente a marcacao TLP:AMBER
tlp_amber = client.marking_definition.read(
    filters={"mode": "and", "filters": [{"key": "definition", "values": ["TLP:AMBER"]}], "filterGroups": []}
)
report = client.report.create(
    name="Analise Tecnica de Campanha Direcionada Q4",
    published="2026-10-03T12:00:00Z",
    report_types=["threat-report"],
    confidence=90,
    objectMarking=[tlp_amber["id"]]
)
```

## Limites e trade-offs
Criar contas de serviço para conectores `EXTERNAL_IMPORT` com `Max Confidence Level = 100` permite que feeds automatizados externos alterem descrições, nomes e scores curados manualmente pela equipe interna de CTI; limite feeds externos entre `30` e `70`.

## Como verificar
Teste consultar a API GraphQL usando um token pertencente a um grupo restrito apenas a `TLP:CLEAR` e `TLP:GREEN` e confirme que o relatório `TLP:AMBER` acima não é retornado.

## Conexões
- [[opencti-ciclo-vida-indicadores-decay-rules-score-revogacao]] — Veja também: OpenCTI: Ciclo de Vida de Indicadores — **Decay Rules** (Curvas de Decaimento de `x_opencti_score`), Expiração `valid_until` e Revogação.
- [[opencti-streams-taxii21-live-streams-feeds-csv-integracao-siem]] — Veja também: OpenCTI: Compartilhamento de Inteligência em Tempo Real — **Live Streams** (SSE), Coleções **TAXII 2.1** e **CSV Feeds** para Firewalls/EDRs.
- [[opencti-arquitetura-stix21-knowledge-graph-graphql-filigran]] — Referência cruzada direta com opencti-arquitetura-stix21-knowledge-graph-graphql-filigran.
- [[opencti-ecossistema-conectores-import-enrichment-stream-export]] — Referência cruzada direta com opencti-ecossistema-conectores-import-enrichment-stream-export.
- [[mispsoc-taxonomias-tlp-pap-sharing-groups-federacao-sincronizacao]] — Referência cruzada direta com mispsoc-taxonomias-tlp-pap-sharing-groups-federacao-sincronizacao.

## Fontes
- [OpenCTI Official GitHub — STIX 2.1 Cyber Threat Intelligence Platform](https://raw.githubusercontent.com/OpenCTI-Platform/opencti/master/README.md) — documentação oficial da plataforma OpenCTI cobrindo o grafo STIX 2.1, GraphQL, inferência e RBAC; consultado em 2026-10-03.
- [OpenCTI Connectors Official GitHub — Architecture & Classes](https://raw.githubusercontent.com/OpenCTI-Platform/connectors/master/README.md) — documentação oficial das 5 classes de conectores do OpenCTI (EXTERNAL_IMPORT, INTERNAL_ENRICHMENT, STREAM, etc.); consultado em 2026-10-03.
- [OpenCTI Official Documentation — Connectors Deployment](https://docs.opencti.io/latest/deployment/connectors/) — guia oficial de implantação e operação de conectores e workers do OpenCTI; consultado em 2026-10-03.
