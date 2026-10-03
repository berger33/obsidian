---
id: software.seguranca.tranche06.000518
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

# OpenCTI: Automação de Fluxos de Conhecimento com **Playbooks** (Gatilhos de Stream, Filtros, Enriquecimento, Marcação e Criação de Casos)

## Em uma frase
O motor de **Playbooks** do OpenCTI (*Data -> Processing -> Playbooks*) permite construir automações reativas em grafo que escutam todos os eventos de criação, modificação ou exclusão no *stream* interno da plataforma e executam cadeias de transformação e resposta.

## Por que importa
Elimina o trabalho manual repetitivo de triagem: por exemplo, sempre que um novo `Indicator` do tipo `Domain-Name` ou `IPv4-Addr` entrar na plataforma com `x_opencti_score >= 80`, o playbook pode acionar automaticamente conectores de enriquecimento, adicionar um rótulo, reduzir ou elevar a confiança e abrir um `Case-Incident` se o indicador tiver um `Sighting` interno.

## Como funciona
Os nós disponíveis nos Playbooks incluem: *Listen knowledge events*, *Filter knowledge*, *Enrich through connector*, *Manipulate knowledge* (alterar TLP, score, labels, autor), *Reduce knowledge*, *Container wrapper* (empacotar em um Report ou Case-Incident) e *Send to notifier* (e-mail/webhook).

## Exemplo
```json
{
  "playbook_name": "Auto-Enrich-And-Escalate-Sighted-IOCs",
  "trigger": "knowledge_created",
  "filter": {
    "entity_type": ["Indicator", "Stix-Cyber-Observable"],
    "x_opencti_score_gt": 80
  },
  "steps": [
    "enrich_connector:virustotal",
    "enrich_connector:crowdsec",
    "manipulate_labels:add:auto-triaged"
  ]
}
```

## Limites e trade-offs
Cuidado com loops infinitos de Playbooks: se um Playbook escuta eventos de **atualização** (`Update` event) de `Indicator` e um de seus passos modifica o próprio `Indicator`, ele re-acionará a si mesmo indefinidamente caso o filtro de entrada não exclua objetos já processados.

## Como verificar
Ative o Playbook em homologação, crie um indicador de teste que case com o filtro e verifique no painel de execução do Playbook a conclusão de cada etapa.

## Conexões
- [[opencti-streams-taxii21-live-streams-feeds-csv-integracao-siem]] — Veja também: OpenCTI: Compartilhamento de Inteligência em Tempo Real — **Live Streams** (SSE), Coleções **TAXII 2.1** e **CSV Feeds** para Firewalls/EDRs.
- [[opencti-gestao-casos-incident-response-rfi-tasks-workbenches]] — Veja também: OpenCTI: Módulo de `Cases` (`Incident Response`, `Requests for Information — RFI`, `Requests for Takedown`) e `Analyst Workbenches`.
- [[opencti-ecossistema-conectores-import-enrichment-stream-export]] — Referência cruzada direta com opencti-ecossistema-conectores-import-enrichment-stream-export.
- [[mispsoc-workflows-automacao-gatilhos-bloqueio-publicacao]] — Referência cruzada direta com mispsoc-workflows-automacao-gatilhos-bloqueio-publicacao.

## Fontes
- [OpenCTI Official GitHub — STIX 2.1 Cyber Threat Intelligence Platform](https://raw.githubusercontent.com/OpenCTI-Platform/opencti/master/README.md) — documentação oficial da plataforma OpenCTI cobrindo o grafo STIX 2.1, GraphQL, inferência e RBAC; consultado em 2026-10-03.
- [OpenCTI Connectors Official GitHub — Architecture & Classes](https://raw.githubusercontent.com/OpenCTI-Platform/connectors/master/README.md) — documentação oficial das 5 classes de conectores do OpenCTI (EXTERNAL_IMPORT, INTERNAL_ENRICHMENT, STREAM, etc.); consultado em 2026-10-03.
- [OpenCTI Official Documentation — Connectors Deployment](https://docs.opencti.io/latest/deployment/connectors/) — guia oficial de implantação e operação de conectores e workers do OpenCTI; consultado em 2026-10-03.
