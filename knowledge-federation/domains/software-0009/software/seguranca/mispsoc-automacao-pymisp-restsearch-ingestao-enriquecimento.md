---
id: software.seguranca.tranche05.000425
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

# MISP: Automação em Python com `PyMISP` e Consultas Avançadas na API `/attributes/restSearch`

## Em uma frase
A biblioteca oficial **`PyMISP`** (`MISP/PyMISP`, Python 3.10+) encapsula a API REST OpenAPI do MISP, tratando `MISPEvent`, `MISPObject` e `MISPAttribute` como dicionários mutáveis Python (`MutableMapping`) e expondo o motor unificado de busca **`restSearch`**.

## Por que importa
Permite que playbooks de SOAR e scripts de resposta a incidentes consultem milhões de indicadores em milissegundos, filtrem por janela temporal (`timestamp`, `publish_timestamp`), tipo, tags e `to_ids`, e anexem novos artefatos coletados na investigação.

## Como funciona
O método `misp.rest_search(controller='attributes', ...)` aceita dezenas de filtros combinados (`type_attribute`, `tags`, `to_ids`, `last`, `enforce_warninglist`, `include_context`, `return_format`) e exporta diretamente no formato desejado (`json`, `csv`, `suricata`, `zeek`, `rpz`, `stix2`, `yara`).

## Exemplo
```python
from pymisp import PyMISP

misp = PyMISP("https://cti-hub.soc.internal.corp", "SOAR_READONLY_API_KEY", ssl=True)

# Buscar todos os domínios e IPs maliciosos publicados nas últimas 24h com to_ids=1 e filtrados por warninglists
results = misp.rest_search(
    controller="attributes",
    return_format="json",
    type_attribute=["ip-dst", "domain", "hostname"],
    to_ids=1,
    published=True,
    publish_timestamp="24h",
    enforce_warninglist=True,
    tags=["tlp:clear", "tlp:green", "tlp:amber"],
)
```

## Limites e trade-offs
Evite buscar todos os eventos completos sem paginação (`limit` e `page`) ou sem filtro temporal (`publish_timestamp="24h"` / `"7d"`) em jobs agendados de alta frequência, pois sobrecarrega o MySQL/MariaDB da instância MISP.

## Como verificar
Execute a busca `rest_search` com `limit=10` e valide que todos os atributos retornados possuem `"to_ids": true` e pertencem a eventos publicados.

## Conexões
- [[mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids]] — Veja também: MISP: Prevenção de Falsos Positivos e Auto-Sabotagem com `misp-warninglists`.
- [[mispsoc-enriquecimento-misp-modules-hover-expansion-import-export]] — Veja também: MISP: Enriquecimento e Expansão Automatizada com `misp-modules` (DNS, BGP/ASN, Shodan, VirusTotal, YARA e PDF).
- [[mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies]] — Referência cruzada direta com mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies.
- [[mispsoc-exportacao-nids-suricata-zeek-rpz-stix-siem]] — Referência cruzada direta com mispsoc-exportacao-nids-suricata-zeek-rpz-stix-siem.

## Fontes
- [MISP Official GitHub — Core Functions & Threat Intelligence Platform](https://raw.githubusercontent.com/MISP/MISP/2.4/README.md) — documentação oficial do MISP cobrindo Events, Attributes, Objects, Galaxies, correlação e exportação NIDS; consultado em 2026-10-03.
- [PyMISP Official GitHub — Python Library & REST API](https://raw.githubusercontent.com/MISP/PyMISP/main/README.md) — documentação oficial da biblioteca PyMISP para automação de eventos, atributos, sightings e restSearch; consultado em 2026-10-03.
- [MISP OpenAPI Specification](https://www.misp-project.org/openapi/) — especificação OpenAPI da API REST do MISP; consultado em 2026-10-03.
