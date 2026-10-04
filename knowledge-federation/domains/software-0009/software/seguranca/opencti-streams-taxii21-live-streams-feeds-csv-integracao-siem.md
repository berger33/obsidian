---
id: software.seguranca.tranche06.000517
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

# OpenCTI: Compartilhamento de Inteligência em Tempo Real — **Live Streams** (SSE), Coleções **TAXII 2.1** e **CSV Feeds** para Firewalls/EDRs

## Em uma frase
Na seção *Data -> Data Sharing*, o OpenCTI oferece três mecanismos nativos para distribuir inteligência filtrada para ferramentas de defesa sem precisar escrever código de integração customizado: **Live Streams**, **TAXII 2.1 Collections** e **CSV Feeds**.

## Por que importa
Diferentes ferramentas consomem formatos distintos: firewalls de borda (Palo Alto PAN-OS, Fortinet, Check Point) exigem *External Dynamic Lists* (EDLs) em texto/CSV simples; SIEMs modernos (Splunk, Elastic, Sentinel) consomem *Live Streams* contínuos em STIX 2.1; e plataformas parceiras consomem servidores *TAXII 2.1*.

## Como funciona
Cada Stream, Coleção TAXII ou Feed CSV é respaldado por um **filtro visual dinâmico** (ex.: `entity_type = Indicator AND revoked = false AND x_opencti_score >= 75 AND objectMarking IN [TLP:CLEAR, TLP:GREEN, TLP:AMBER]`) e restrito a grupos ou autenticado por token, garantindo que revogações e exclusões sejam propagadas instantaneamente para os sensores consumidores.

## Exemplo
```bash
# Consumir um CSV Feed autenticado do OpenCTI para alimentar uma External Dynamic List (EDL) de Firewall
curl -sS "https://opencti.soc.internal.corp/feeds/ip-blocklist-high-confidence.csv" \
  -H "Authorization: Bearer ${OPENCTI_FEED_READONLY_TOKEN}" | head -n 20
```

## Limites e trade-offs
Nunca crie um CSV Feed público sem autenticação (`Public feed`) contendo indicadores marcados com `TLP:AMBER` ou `TLP:RED`; o próprio OpenCTI exige definir quais marcações máximas um feed público pode expor.

## Como verificar
Acesse o endpoint `/taxii2/` ou o CSV Feed com o token de leitura e verifique que indicadores com `revoked = true` desaparecem imediatamente da lista.

## Conexões
- [[opencti-governanca-rbac-marking-definitions-tlp-confianca-organizacoes]] — Veja também: OpenCTI: Controle de Acesso Baseado em **Marking Definitions** (`TLP`, `PAP`, `Statement`), Segregação por Organizações e `Max Confidence Level`.
- [[opencti-automacao-playbooks-enriquecimento-notificacoes-triage]] — Veja também: OpenCTI: Automação de Fluxos de Conhecimento com **Playbooks** (Gatilhos de Stream, Filtros, Enriquecimento, Marcação e Criação de Casos).
- [[opencti-ciclo-vida-indicadores-decay-rules-score-revogacao]] — Referência cruzada direta com opencti-ciclo-vida-indicadores-decay-rules-score-revogacao.
- [[opencti-ecossistema-conectores-import-enrichment-stream-export]] — Referência cruzada direta com opencti-ecossistema-conectores-import-enrichment-stream-export.
- [[mispsoc-exportacao-nids-suricata-zeek-rpz-stix-siem]] — Referência cruzada direta com mispsoc-exportacao-nids-suricata-zeek-rpz-stix-siem.

## Fontes
- [OpenCTI Official GitHub — STIX 2.1 Cyber Threat Intelligence Platform](https://raw.githubusercontent.com/OpenCTI-Platform/opencti/master/README.md) — documentação oficial da plataforma OpenCTI cobrindo o grafo STIX 2.1, GraphQL, inferência e RBAC; consultado em 2026-10-03.
- [OpenCTI Connectors Official GitHub — Architecture & Classes](https://raw.githubusercontent.com/OpenCTI-Platform/connectors/master/README.md) — documentação oficial das 5 classes de conectores do OpenCTI (EXTERNAL_IMPORT, INTERNAL_ENRICHMENT, STREAM, etc.); consultado em 2026-10-03.
- [OpenCTI Official Documentation — Connectors Deployment](https://docs.opencti.io/latest/deployment/connectors/) — guia oficial de implantação e operação de conectores e workers do OpenCTI; consultado em 2026-10-03.
