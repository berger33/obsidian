---
id: software.seguranca.tranche05.000430
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

# MISP: Ciclo de Vida do IOC com Sightings (Avistamentos), False-Positive Reports e *Decaying Models*

## Em uma frase
Para evitar que o banco de inteligência acumule milhões de indicadores obsoletos que geram alertas falsos eternos, o MISP implementa **Sightings** (avistamentos positivos, falsos positivos ou expiração) e **Decaying Models** (modelos matemáticos de decaimento de pontuação do IOC ao longo do tempo).

## Por que importa
Enquanto o hash SHA-256 de um binário de ransomware mantém alta confiabilidade por anos (decaimento lento), um endereço IP dinâmico usado por um botnet perde relevância em poucos dias (decaimento rápido) a menos que novos *Sightings* confirmem que ele continua ativo.

## Como funciona
Sempre que o SIEM, EDR ou NIDS detecta um indicador em produção, ele envia um registro de `Sighting` (`type: 0` para avistamento real, `type: 1` para falso positivo) via API (`/sightings/add/<attribute_id>`). Os *Decaying Models* calculam um `score` dinâmico de 0 a 100 combinando a idade do atributo, a taxa de decaimento da sua categoria e o histórico de *Sightings*, desativando o IOC nas exportações quando o score cai abaixo do `threshold`.

## Exemplo
```python
# Registrar via PyMISP que o SIEM observou um indicador ativo em produção hoje (Sighting type 0)
misp.add_sighting({
    "values": ["198.51.100.77"],
    "type": "0",
    "source": "SIEM-Splunk-Prod-Firewall"
})
```

## Limites e trade-offs
Não alimentar de volta os *Sightings* de falso positivo (`"type": "1"`) quando o SOC descarta um alerta no SIEM faz com que o mesmo IOC defeituoso continue gerando alertas repetidos todos os dias.

## Como verificar
Envie um `Sighting` de teste para um atributo em homologação e consulte a API com `"includeDecayScore": 1` para confirmar a atualização do score e do contador de avistamentos.

## Conexões
- [[mispsoc-workflows-automacao-gatilhos-bloqueio-publicacao]] — Veja também: MISP: Motor de Workflows Visuais, Gatilhos (`event-before-publish`) e Governança de Qualidade de CTI.
- [[mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies]] — Referência cruzada direta com mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies.
- [[mispsoc-exportacao-nids-suricata-zeek-rpz-stix-siem]] — Referência cruzada direta com mispsoc-exportacao-nids-suricata-zeek-rpz-stix-siem.
- [[mispsoc-automacao-pymisp-restsearch-ingestao-enriquecimento]] — Referência cruzada direta com mispsoc-automacao-pymisp-restsearch-ingestao-enriquecimento.

## Fontes
- [MISP Official GitHub — Core Functions & Threat Intelligence Platform](https://raw.githubusercontent.com/MISP/MISP/2.4/README.md) — documentação oficial do MISP cobrindo Events, Attributes, Objects, Galaxies, correlação e exportação NIDS; consultado em 2026-10-03.
- [PyMISP Official GitHub — Python Library & REST API](https://raw.githubusercontent.com/MISP/PyMISP/main/README.md) — documentação oficial da biblioteca PyMISP para automação de eventos, atributos, sightings e restSearch; consultado em 2026-10-03.
- [MISP OpenAPI Specification](https://www.misp-project.org/openapi/) — especificação OpenAPI da API REST do MISP; consultado em 2026-10-03.
