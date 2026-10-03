---
id: software.seguranca.tranche05.000429
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/MISP/MISP/2.4/README.md", "https://raw.githubusercontent.com/MISP/PyMISP/main/README.md", "https://www.misp-project.org/openapi/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# MISP: Motor de Workflows Visuais, Gatilhos (`event-before-publish`) e Governança de Qualidade de CTI

## Em uma frase
O sistema de **Workflows** do MISP permite desenhar pipelines visuais baseados em grafos (com nós de gatilho *Trigger*, lógica condicional *Logic* e ação *Action*) que interceptam eventos do ciclo de vida da inteligência dentro da plataforma.

## Por que importa
Garante governança obrigatória antes que qualquer analista publique um evento: um workflow no gatilho bloqueante `event-before-publish` pode impedir a publicação se o evento não tiver uma tag `tlp:*`, se faltar classificação MITRE ATT&CK ou se contiver atributos `to_ids=True` que colidam com uma *warninglist*.

## Como funciona
Além de bloqueios de conformidade, workflows não bloqueantes (`attribute-after-save`, `event-after-publish`) podem disparar notificações via Webhook para o SIEM/SOAR, enviar alertas ao Mattermost/Slack/Teams do SOC ou acionar enriquecimento automático via `misp-modules`.

## Exemplo
```json
{
  "trigger": "event-before-publish",
  "check": "check-if-tagged",
  "tag_Required": "tlp:*",
  "on_failure": "block-execution-and-log"
}
```

## Limites e trade-offs
Ao criar workflows que enviam payloads via módulo `Webhook` após `event-after-publish`, adicione sempre um nó de filtro lógico anterior (`if-tagged: tlp:clear OR tlp:green`) caso o receptor do webhook seja um sistema externo.

## Como verificar
Simule a tentativa de publicar um evento de teste sem tag `tlp:*` e confirme que o workflow `event-before-publish` bloqueia a publicação e exibe a mensagem de erro no log de auditoria do workflow.

## Conexões
- [[mispsoc-feeds-osint-caching-freetext-import-stix-taxii]] — Veja também: MISP: Gestão de Feeds OSINT (Caching vs Ingestão Seletiva), Free-Text Import e Integração STIX/TAXII.
- [[mispsoc-colaboracao-sightings-opinions-decaying-models-ciclo-vida]] — Veja também: MISP: Ciclo de Vida do IOC com Sightings (Avistamentos), False-Positive Reports e *Decaying Models*.
- [[mispsoc-taxonomias-tlp-pap-sharing-groups-federacao-sincronizacao]] — Referência cruzada direta com mispsoc-taxonomias-tlp-pap-sharing-groups-federacao-sincronizacao.
- [[mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids]] — Referência cruzada direta com mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids.
- [[mispsoc-enriquecimento-misp-modules-hover-expansion-import-export]] — Referência cruzada direta com mispsoc-enriquecimento-misp-modules-hover-expansion-import-export.

## Fontes
- [MISP Official GitHub — Core Functions & Threat Intelligence Platform](https://raw.githubusercontent.com/MISP/MISP/2.4/README.md) — documentação oficial do MISP cobrindo Events, Attributes, Objects, Galaxies, correlação e exportação NIDS; consultado em 2026-10-03.
- [PyMISP Official GitHub — Python Library & REST API](https://raw.githubusercontent.com/MISP/PyMISP/main/README.md) — documentação oficial da biblioteca PyMISP para automação de eventos, atributos, sightings e restSearch; consultado em 2026-10-03.
- [MISP OpenAPI Specification](https://www.misp-project.org/openapi/) — especificação OpenAPI da API REST do MISP; consultado em 2026-10-03.
