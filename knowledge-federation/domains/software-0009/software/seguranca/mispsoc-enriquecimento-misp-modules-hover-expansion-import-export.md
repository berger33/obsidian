---
id: software.seguranca.tranche05.000426
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

# MISP: Enriquecimento e Expansão Automatizada com `misp-modules` (DNS, BGP/ASN, Shodan, VirusTotal, YARA e PDF)

## Em uma frase
O subsistema **`misp-modules`** é um serviço Python independente (executado em porta local `6666`) que estende o MISP com dezenas de módulos de expansão (*expansion* / *hover*), importação (OCR, STIX, relatórios de ameaças) e exportação customizada.

## Por que importa
Permite que o analista passe o cursor ou clique em *Enrich* sobre um IP/domínio/hash no MISP para consultar instantaneamente Passive DNS, ASN/BGP, WHOIS, Shodan, AbuseIPDB, MalwareBazaar ou VirusTotal e converter o retorno em novos objetos vinculados ao evento.

## Como funciona
Os módulos são divididos em `expansion` (que consultam APIs externas e retornam atributos/objetos propostos), `import_mod` (que analisam arquivos externos) e `export_mod` (que formatam eventos em relatórios Markdown/PDF ou formatos de ferramentas específicas).

## Exemplo
```bash
# Verificar se o daemon misp-modules está escutando em loopback e listar todos os módulos carregados
curl -sS http://127.0.0.1:6666/modules | jq -r '.[].name' | sort
```

## Limites e trade-offs
Acionar módulos de enriquecimento que consultam serviços públicos externos (como VirusTotal ou URLScan) sobre um domínio ou hash confidencial de um ataque direcionado (`tlp:red`) pode alertar o atacante que monitora consultas públicas pelo seu próprio artefato.

## Como verificar
Restrinja na configuração do MISP quais módulos de expansão externos podem ser acionados em eventos marcados com `tlp:red` ou `tlp:amber+strict`.

## Conexões
- [[mispsoc-automacao-pymisp-restsearch-ingestao-enriquecimento]] — Veja também: MISP: Automação em Python com `PyMISP` e Consultas Avançadas na API `/attributes/restSearch`.
- [[mispsoc-exportacao-nids-suricata-zeek-rpz-stix-siem]] — Veja também: MISP: Exportação Automatizada de IOCs para Sensores Suricata, Zeek Intel Framework, DNS RPZ e STIX 2.1.
- [[mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies]] — Referência cruzada direta com mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies.
- [[mispsoc-workflows-automacao-gatilhos-bloqueio-publicacao]] — Referência cruzada direta com mispsoc-workflows-automacao-gatilhos-bloqueio-publicacao.

## Fontes
- [MISP Official GitHub — Core Functions & Threat Intelligence Platform](https://raw.githubusercontent.com/MISP/MISP/2.4/README.md) — documentação oficial do MISP cobrindo Events, Attributes, Objects, Galaxies, correlação e exportação NIDS; consultado em 2026-10-03.
- [PyMISP Official GitHub — Python Library & REST API](https://raw.githubusercontent.com/MISP/PyMISP/main/README.md) — documentação oficial da biblioteca PyMISP para automação de eventos, atributos, sightings e restSearch; consultado em 2026-10-03.
- [MISP OpenAPI Specification](https://www.misp-project.org/openapi/) — especificação OpenAPI da API REST do MISP; consultado em 2026-10-03.
