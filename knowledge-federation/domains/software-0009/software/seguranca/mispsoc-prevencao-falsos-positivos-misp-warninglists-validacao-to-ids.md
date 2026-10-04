---
id: software.seguranca.tranche05.000424
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

# MISP: Prevenção de Falsos Positivos e Auto-Sabotagem com `misp-warninglists`

## Em uma frase
As **`misp-warninglists`** formam um catálogo mantido pela comunidade contendo centenas de listas de ativos legítimos conhecidos (IPs e domínios de CDNs Cloudflare/Akamai/Fastly, servidores DNS públicos `8.8.8.8`/`1.1.1.1`, endpoints do Microsoft 365/Google Workspace/AWS, domínios Alexa/Tranco Top 1M e faixas RFC 1918).

## Por que importa
Se um analista importar automaticamente os IPs/domínios extraídos de um sandbox de malware sem filtrá-los contra as *warninglists*, e o malware tiver feito um teste de conectividade contra `login.microsoftonline.com` ou `1.1.1.1`, exportar esse atributo com `to_ids=True` para o firewall bloqueará a própria empresa.

## Como funciona
No MISP, as *warninglists* podem ser acionadas na interface visual, na API REST (`/warninglists/checkValue`) ou impostas como bloqueio automático no momento da exportação de regras IDS (`enforceWarninglist=1`), removendo automaticamente da saída qualquer atributo que colida com uma lista de alerta habilitada.

## Exemplo
```bash
# Consultar a API do MISP para verificar se candidatos a IOC colidem com alguma misp-warninglist
curl -sS -X POST "https://misp.soc.internal.corp/warninglists/checkValue" \
  -H "Authorization: ${MISP_API_KEY}" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '["8.8.8.8", "login.microsoftonline.com", "malicious-c2-domain.example"]' | jq .
```

## Limites e trade-offs
Sempre passe `"enforceWarninglist": True` nas consultas `restSearch` que alimentam bloqueios automáticos em firewalls, EDRs ou RPZ DNS para garantir que um erro humano de marcação `to_ids` jamais derrube serviços críticos.

## Como verificar
Execute o `curl` acima contra `/warninglists/checkValue` e confirme que `8.8.8.8` e `login.microsoftonline.com` retornam matches nas warninglists de DNS público e Microsoft Office 365.

## Conexões
- [[mispsoc-taxonomias-tlp-pap-sharing-groups-federacao-sincronizacao]] — Veja também: MISP: Taxonomias Padronizadas (`TLP`, `PAP`, `admiralty-scale`), Sharing Groups e Sincronização Federada.
- [[mispsoc-automacao-pymisp-restsearch-ingestao-enriquecimento]] — Veja também: MISP: Automação em Python com `PyMISP` e Consultas Avançadas na API `/attributes/restSearch`.
- [[mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies]] — Referência cruzada direta com mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies.
- [[mispsoc-exportacao-nids-suricata-zeek-rpz-stix-siem]] — Referência cruzada direta com mispsoc-exportacao-nids-suricata-zeek-rpz-stix-siem.
- [[zeeknsm-intelligence-framework-ioc-matching-ips-domains-hashes-cif]] — Referência cruzada direta com zeeknsm-intelligence-framework-ioc-matching-ips-domains-hashes-cif.

## Fontes
- [MISP Official GitHub — Core Functions & Threat Intelligence Platform](https://raw.githubusercontent.com/MISP/MISP/2.4/README.md) — documentação oficial do MISP cobrindo Events, Attributes, Objects, Galaxies, correlação e exportação NIDS; consultado em 2026-10-03.
- [PyMISP Official GitHub — Python Library & REST API](https://raw.githubusercontent.com/MISP/PyMISP/main/README.md) — documentação oficial da biblioteca PyMISP para automação de eventos, atributos, sightings e restSearch; consultado em 2026-10-03.
- [MISP OpenAPI Specification](https://www.misp-project.org/openapi/) — especificação OpenAPI da API REST do MISP; consultado em 2026-10-03.
