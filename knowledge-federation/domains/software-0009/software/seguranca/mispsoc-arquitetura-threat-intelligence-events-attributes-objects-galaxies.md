---
id: software.seguranca.tranche05.000421
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

# MISP: Arquitetura da Plataforma de Threat Intelligence — Events, Attributes, Objects e Galaxies

## Em uma frase
**MISP** (*Malware Information Sharing Platform*, AGPLv3) é a plataforma open-source padrão para coleta, estruturação, correlação e compartilhamento de inteligência de ameaças cibernéticas (CTI) e Indicadores de Comprometimento (IOCs) entre SOCs, CSIRTs e ISACs.

## Por que importa
Substitui planilhas e relatórios PDF desestruturados por um modelo de dados acionável que alimenta automaticamente SIEMs, firewalls, EDRs e sensores de rede (Suricata, Zeek) enquanto preserva o contexto estratégico do ator de ameaça.

## Como funciona
A ontologia do MISP organiza-se em quatro camadas: **Events** (o envelope de um incidente ou campanha), **Attributes** (indicadores atômicos tipados como `ip-dst`, `domain`, `sha256`, `ja3-fingerprint-md5`, `yara`, `sigma`, com flag booleana `to_ids`), **Objects** (agrupamentos estruturados de atributos como um objeto `file` contendo `filename` + `md5` + `sha256` + `entropy` conectados por *Object References*) e **Galaxies / Clusters** (contexto de alto nível como grupos APT, malwares e técnicas MITRE ATT&CK).

## Exemplo
```python
from pymisp import PyMISP, MISPEvent, MISPObject

misp = PyMISP("https://misp.soc.internal.corp", "AUTOMATION_API_KEY", ssl=True)
event = MISPEvent()
event.info = "Campanha Phishing Credenciais VPN - Outubro 2026"
event.distribution = 0  # Your organization only
event.threat_level_id = 2  # Medium
event.analysis = 1  # Ongoing
created = misp.add_event(event, pythonify=True)
```

## Limites e trade-offs
Marcar `to_ids=True` indiscriminadamente em atributos informativos (como o IP de um servidor DNS público citado no relatório ou um domínio legítimo usado como chamariz) gerará tempestades de falsos positivos nos sensores NIDS/SIEM que consomem o MISP.

## Como verificar
Consulte `misp.get_event(created.uuid, pythonify=True)` e confirme a integridade dos metadados `distribution`, `threat_level_id` e `analysis`.

## Conexões
- [[mispsoc-motor-correlacao-automatica-ssdeep-cidr-grafos-eventos]] — Veja também: MISP: Motor de Correlação Automática (Valores Exatos, Sub-redes CIDR e Fuzzy Hashing `ssdeep`).
- [[mispsoc-taxonomias-tlp-pap-sharing-groups-federacao-sincronizacao]] — Referência cruzada direta com mispsoc-taxonomias-tlp-pap-sharing-groups-federacao-sincronizacao.
- [[mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids]] — Referência cruzada direta com mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids.

## Fontes
- [MISP Official GitHub — Core Functions & Threat Intelligence Platform](https://raw.githubusercontent.com/MISP/MISP/2.4/README.md) — documentação oficial do MISP cobrindo Events, Attributes, Objects, Galaxies, correlação e exportação NIDS; consultado em 2026-10-03.
- [PyMISP Official GitHub — Python Library & REST API](https://raw.githubusercontent.com/MISP/PyMISP/main/README.md) — documentação oficial da biblioteca PyMISP para automação de eventos, atributos, sightings e restSearch; consultado em 2026-10-03.
- [MISP OpenAPI Specification](https://www.misp-project.org/openapi/) — especificação OpenAPI da API REST do MISP; consultado em 2026-10-03.
