---
id: software.seguranca.tranche05.000427
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

# MISP: Exportação Automatizada de IOCs para Sensores Suricata, Zeek Intel Framework, DNS RPZ e STIX 2.1

## Em uma frase
O MISP atua como o hub central de geração de regras de detecção ao exportar atributos marcados com `to_ids=True` diretamente nos formatos nativos do **Suricata/Snort** (`returnFormat: suricata`), **Zeek Intelligence Framework** (`returnFormat: bro`), **DNS Response Policy Zones** (`returnFormat: rpz`) e **STIX 2.1** (`stix2`).

## Por que importa
Elimina a tradução manual de indicadores: assim que um evento de campanha é revisado e publicado no MISP, os sensores de rede NIDS/NSM e os resolvedores DNS corporativos recebem as novas regras em minutos.

## Como funciona
Na exportação `bro` (Zeek), o MISP gera arquivos tabulados com cabeçalho `#fields indicator indicator_type meta.source meta.url meta.do_notice` prontos para ingestão via `Intel::read_files`. Na exportação `rpz`, gera registros de zona DNS que redirecionam consultas a domínios de C2/phishing para `NXDOMAIN` ou *sinkhole* interno.

## Exemplo
```bash
# Exportar indicadores recentes do MISP diretamente no formato nativo do Zeek Intelligence Framework
curl -sS -X POST "https://misp.soc.internal.corp/attributes/restSearch" \
  -H "Authorization: ${MISP_API_KEY}" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "returnFormat": "bro",
    "to_ids": 1,
    "published": 1,
    "publish_timestamp": "14d",
    "enforceWarninglist": true
  }' > /opt/zeek/share/zeek/site/intel/misp-live.intel
```

## Limites e trade-offs
Indicadores de infraestrutura efêmera (como IPs em nuvens compartilhadas) perdem validade após algumas semanas; aplique sempre janelas temporais (`publish_timestamp: "14d"` ou `"30d"`) ou o modelo de *Decaying Models* do MISP na exportação para bloqueio ativo.

## Como verificar
Valide o cabeçalho `#fields indicator indicator_type` no arquivo `.intel` gerado e confirme que `enforceWarninglist: true` filtrou domínios benignos.

## Conexões
- [[mispsoc-enriquecimento-misp-modules-hover-expansion-import-export]] — Veja também: MISP: Enriquecimento e Expansão Automatizada com `misp-modules` (DNS, BGP/ASN, Shodan, VirusTotal, YARA e PDF).
- [[mispsoc-feeds-osint-caching-freetext-import-stix-taxii]] — Veja também: MISP: Gestão de Feeds OSINT (Caching vs Ingestão Seletiva), Free-Text Import e Integração STIX/TAXII.
- [[mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids]] — Referência cruzada direta com mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids.
- [[zeeknsm-intelligence-framework-ioc-matching-ips-domains-hashes-cif]] — Referência cruzada direta com zeeknsm-intelligence-framework-ioc-matching-ips-domains-hashes-cif.

## Fontes
- [MISP Official GitHub — Core Functions & Threat Intelligence Platform](https://raw.githubusercontent.com/MISP/MISP/2.4/README.md) — documentação oficial do MISP cobrindo Events, Attributes, Objects, Galaxies, correlação e exportação NIDS; consultado em 2026-10-03.
- [PyMISP Official GitHub — Python Library & REST API](https://raw.githubusercontent.com/MISP/PyMISP/main/README.md) — documentação oficial da biblioteca PyMISP para automação de eventos, atributos, sightings e restSearch; consultado em 2026-10-03.
- [MISP OpenAPI Specification](https://www.misp-project.org/openapi/) — especificação OpenAPI da API REST do MISP; consultado em 2026-10-03.
