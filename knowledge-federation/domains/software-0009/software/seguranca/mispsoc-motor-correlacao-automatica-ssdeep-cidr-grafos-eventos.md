---
id: software.seguranca.tranche05.000422
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

# MISP: Motor de Correlação Automática (Valores Exatos, Sub-redes CIDR e Fuzzy Hashing `ssdeep`)

## Em uma frase
O motor de correlação do MISP interliga automaticamente eventos e campanhas distintas sempre que um novo atributo inserido coincide com indicadores já armazenados na base.

## Por que importa
Permite que um analista investigando um incidente hoje descubra instantaneamente que o mesmo hash de certificado TLS, endereço IP de C2 ou *fuzzy hash* `ssdeep` de um binário reempacotado já foi observado há seis meses em outro incidente ou reportado por um CSIRT parceiro.

## Como funciona
Além da correspondência exata de valores (`value1 == value2`), o MISP executa correlação de blocos de rede **CIDR** (identificando se um IP recém-adicionado pertence a uma sub-rede `/24` maliciosa registrada em outro evento) e correlação de similaridade via **ssdeep** (detectando amostras de malware com percentual de sobreposição acima do limiar configurado). Atributos ruidosos que não devem gerar correlações espúrias podem ter `disable_correlation=True`.

## Exemplo
```python
from pymisp import MISPAttribute

attr = MISPAttribute()
attr.category = "Payload delivery"
attr.type = "sha256"
attr.value = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
attr.to_ids = True
attr.disable_correlation = False
```

## Limites e trade-offs
Habilitar correlação em atributos genéricos de status ou códigos de país sem `disable_correlation=True` cria milhares de arestas irrelevantes no grafo de eventos e degrada a performance do banco de dados.

## Como verificar
Insira o mesmo indicador de teste em dois eventos de laboratório com `disable_correlation=False` e verifique no campo `Related Events` a criação imediata do vínculo bidirecional.

## Conexões
- [[mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies]] — Veja também: MISP: Arquitetura da Plataforma de Threat Intelligence — Events, Attributes, Objects e Galaxies.
- [[mispsoc-taxonomias-tlp-pap-sharing-groups-federacao-sincronizacao]] — Veja também: MISP: Taxonomias Padronizadas (`TLP`, `PAP`, `admiralty-scale`), Sharing Groups e Sincronização Federada.
- [[mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids]] — Referência cruzada direta com mispsoc-prevencao-falsos-positivos-misp-warninglists-validacao-to-ids.
- [[mispsoc-automacao-pymisp-restsearch-ingestao-enriquecimento]] — Referência cruzada direta com mispsoc-automacao-pymisp-restsearch-ingestao-enriquecimento.

## Fontes
- [MISP Official GitHub — Core Functions & Threat Intelligence Platform](https://raw.githubusercontent.com/MISP/MISP/2.4/README.md) — documentação oficial do MISP cobrindo Events, Attributes, Objects, Galaxies, correlação e exportação NIDS; consultado em 2026-10-03.
- [PyMISP Official GitHub — Python Library & REST API](https://raw.githubusercontent.com/MISP/PyMISP/main/README.md) — documentação oficial da biblioteca PyMISP para automação de eventos, atributos, sightings e restSearch; consultado em 2026-10-03.
- [MISP OpenAPI Specification](https://www.misp-project.org/openapi/) — especificação OpenAPI da API REST do MISP; consultado em 2026-10-03.
