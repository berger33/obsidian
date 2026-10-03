---
id: software.seguranca.tranche05.000423
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

# MISP: Taxonomias Padronizadas (`TLP`, `PAP`, `admiralty-scale`), Sharing Groups e Sincronização Federada

## Em uma frase
O MISP governa a classificação e o controle de disseminação da inteligência através de **Taxonomies** padronizadas (como `tlp:red`, `tlp:amber`, `tlp:amber+strict`, `tlp:green`, `tlp:clear`, `PAP` e `admiralty-scale`), níveis de `distribution` (`0` a `4`) e **Sharing Groups** criptograficamente delimitados.

## Por que importa
Impede que indicadores sensíveis de uma investigação em andamento (`tlp:red` ou `Your organization only`) vazem acidentalmente durante a sincronização automática (*Push/Pull*) com instâncias MISP externas ou comunidades setoriais.

## Como funciona
As regras de sincronização de servidores remotos (`Sync Servers`) suportam filtros granulares por tags (`Tag Filters` no Push e no Pull): por exemplo, um servidor corporativo pode ser configurado para realizar **Push** apenas de eventos publicados (`published=True`) que possuam explicitamente a tag `tlp:green` ou `tlp:clear` e nunca enviar eventos marcados com `tlp:amber` ou `internal-investigation`.

## Exemplo
```python
# Aplicar tag TLP:AMBER+STRICT e restringir distribuição apenas à própria organização (0)
misp.tag(event.uuid, "tlp:amber+strict")
event.distribution = 0
misp.update_event(event)
```

## Limites e trade-offs
Publicar um evento (`misp.publish(event)`) com `distribution = 3` (*All communities*) sem revisar as regras de filtro do servidor de sincronização enviará os indicadores imediatamente para todas as instâncias conectadas via Push.

## Como verificar
Inspecione a configuração de cada `Sync Server` na instância MISP e confirme que a regra de Push exige presença explícita de tags autorizadas (`OR` `tlp:clear`, `tlp:green`) e bloqueia `tlp:red`.

## Conexões
- [[mispsoc-motor-correlacao-automatica-ssdeep-cidr-grafos-eventos]] — Veja também: MISP: Motor de Correlação Automática (Valores Exatos, Sub-redes CIDR e Fuzzy Hashing `ssdeep`).
- [[mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids]] — Veja também: MISP: Prevenção de Falsos Positivos e Auto-Sabotagem com `misp-warninglists`.
- [[mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies]] — Referência cruzada direta com mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies.
- [[mispsoc-workflows-automacao-gatilhos-bloqueio-publicacao]] — Referência cruzada direta com mispsoc-workflows-automacao-gatilhos-bloqueio-publicacao.
- [[mispsoc-feeds-osint-caching-freetext-import-stix-taxii]] — Referência cruzada direta com mispsoc-feeds-osint-caching-freetext-import-stix-taxii.

## Fontes
- [MISP Official GitHub — Core Functions & Threat Intelligence Platform](https://raw.githubusercontent.com/MISP/MISP/2.4/README.md) — documentação oficial do MISP cobrindo Events, Attributes, Objects, Galaxies, correlação e exportação NIDS; consultado em 2026-10-03.
- [PyMISP Official GitHub — Python Library & REST API](https://raw.githubusercontent.com/MISP/PyMISP/main/README.md) — documentação oficial da biblioteca PyMISP para automação de eventos, atributos, sightings e restSearch; consultado em 2026-10-03.
- [MISP OpenAPI Specification](https://www.misp-project.org/openapi/) — especificação OpenAPI da API REST do MISP; consultado em 2026-10-03.
