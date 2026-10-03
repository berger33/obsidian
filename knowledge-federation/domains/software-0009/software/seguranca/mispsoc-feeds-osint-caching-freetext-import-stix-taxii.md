---
id: software.seguranca.tranche05.000428
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

# MISP: Gestão de Feeds OSINT (Caching vs Ingestão Seletiva), Free-Text Import e Integração STIX/TAXII

## Em uma frase
O MISP inclui suporte nativo a dezenas de **Feeds OSINT** pré-configurados (CIRCL OSINT, abuse.ch URLhaus/ThreatFox/Feodo Tracker, Botvrij, PhishTank) que podem ser meramente cacheados em Redis para correlação rápida (*Cache Feed*) ou ingeridos seletivamente como eventos.

## Por que importa
Ingerir milhões de indicadores brutos de feeds públicos diretamente na tabela de atributos do banco de dados sem filtro infla a base e gera ruído; o modo *Cache Feeds* permite correlacionar os eventos internos contra todos os feeds OSINT em memória sem poluir o banco principal.

## Como funciona
Quando o analista investiga um relatório de ameaça externo (blog post ou boletim de segurança), a ferramenta **Free-Text Import** analisa o texto bruto, extrai automaticamente hashes, IPs, domínios, CVEs e URLs usando heurísticas de *defanging* (`hxxps://`, `198[.]51[.]100[.]1`) e propõe os tipos de atributos correspondentes para revisão antes de salvar.

## Exemplo
```bash
# Disparar atualização do cache de todos os feeds OSINT habilitados via API REST do MISP
curl -sS -X POST "https://misp.soc.internal.corp/feeds/cacheFeeds/all" \
  -H "Authorization: ${MISP_API_KEY}" \
  -H "Accept: application/json" | jq .
```

## Limites e trade-offs
Se um feed OSINT externo for configurado para ingestão automática completa com publicação imediata, falsos positivos daquele feed público serão propagados automaticamente para os seus sensores internos; prefira manter feeds públicos apenas em modo *Cache* para correlação e enriquecimento.

## Como verificar
Execute `/feeds/cacheFeeds/all` e verifique na tela de Feeds que o status de cache aparece atualizado e que overlaps aparecem destacados nos eventos internos.

## Conexões
- [[mispsoc-exportacao-nids-suricata-zeek-rpz-stix-siem]] — Veja também: MISP: Exportação Automatizada de IOCs para Sensores Suricata, Zeek Intel Framework, DNS RPZ e STIX 2.1.
- [[mispsoc-workflows-automacao-gatilhos-bloqueio-publicacao]] — Veja também: MISP: Motor de Workflows Visuais, Gatilhos (`event-before-publish`) e Governança de Qualidade de CTI.
- [[mispsoc-motor-correlacao-automatica-ssdeep-cidr-grafos-eventos]] — Referência cruzada direta com mispsoc-motor-correlacao-automatica-ssdeep-cidr-grafos-eventos.
- [[mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids]] — Referência cruzada direta com mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids.
- [[mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies]] — Referência cruzada direta com mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies.

## Fontes
- [MISP Official GitHub — Core Functions & Threat Intelligence Platform](https://raw.githubusercontent.com/MISP/MISP/2.4/README.md) — documentação oficial do MISP cobrindo Events, Attributes, Objects, Galaxies, correlação e exportação NIDS; consultado em 2026-10-03.
- [PyMISP Official GitHub — Python Library & REST API](https://raw.githubusercontent.com/MISP/PyMISP/main/README.md) — documentação oficial da biblioteca PyMISP para automação de eventos, atributos, sightings e restSearch; consultado em 2026-10-03.
- [MISP OpenAPI Specification](https://www.misp-project.org/openapi/) — especificação OpenAPI da API REST do MISP; consultado em 2026-10-03.
