---
id: software.seguranca.tranche06.000520
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/OpenCTI-Platform/opencti/master/README.md", "https://raw.githubusercontent.com/OpenCTI-Platform/connectors/master/README.md", "https://docs.opencti.io/latest/deployment/connectors/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenCTI: Desenvolvimento de Conectores Customizados com o SDK Python **`pycti`** (`OpenCTIConnectorHelper` e Envio de Bundles STIX 2.1)

## Em uma frase
A biblioteca oficial **`pycti`** (`OpenCTI-Platform/client-python`) fornece a classe **`OpenCTIConnectorHelper`**, que abstrai o registro do conector na plataforma, o gerenciamento de estado persistente (`get_state` / `set_state`), o agendamento de ciclos e o particionamento e envio de *STIX 2.1 Bundles* para a fila RabbitMQ dos workers.

## Por que importa
Permite integrar rapidamente fontes internas proprietárias (como alertas de antifraude bancária, honeypots internos ou listas de domínios recém-registrados de *typosquatting* da marca da empresa) diretamente na malha de conhecimento do OpenCTI.

## Como funciona
O conector instancia `OpenCTIConnectorHelper(config)`, lê o último cursor processado via `self.helper.get_state()`, constrói objetos com a biblioteca `stix2` (`stix2.Indicator`, `stix2.Malware`, `stix2.Relationship`), empacota-os em um `stix2.Bundle(objects=..., allow_custom=True)` e chama `self.helper.send_stix2_bundle(bundle.serialize(), work_id=work_id)`, finalizando o trabalho com `self.helper.api.work.to_processed(work_id, message)`.

## Exemplo
```python
import stix2
from pycti import OpenCTIConnectorHelper, Indicator as CtiIndicator

# Construir um objeto STIX 2.1 Indicator com ID determinístico do OpenCTI para envio via bundle
pattern = "[ipv4-addr:value = '203.0.113.99']"
stix_indicator = stix2.Indicator(
    id=CtiIndicator.generate_id(pattern),
    name="Honeypot SSH Brute-Force Source 203.0.113.99",
    pattern=pattern,
    pattern_type="stix",
    confidence=80,
    custom_properties={"x_opencti_main_observable_type": "IPv4-Addr", "x_opencti_score": 80}
)
bundle = stix2.Bundle(objects=[stix_indicator], allow_custom=True)
```

## Limites e trade-offs
Use sempre os geradores de ID determinísticos do `pycti` (`Indicator.generate_id(pattern)`, `Malware.generate_id(name)`, `IntrusionSet.generate_id(name)`) ao construir objetos `stix2`; gerar UUIDs aleatórios a cada execução do conector impedirá a deduplicação e criará objetos duplicados ou conflitos.

## Como verificar
Execute o script de teste gerando `CtiIndicator.generate_id(pattern)` duas vezes para o mesmo padrão STIX e confirme que o UUID v5 retornado é idêntico.

## Conexões
- [[opencti-gestao-casos-incident-response-rfi-tasks-workbenches]] — Veja também: OpenCTI: Módulo de `Cases` (`Incident Response`, `Requests for Information — RFI`, `Requests for Takedown`) e `Analyst Workbenches`.
- [[opencti-ecossistema-conectores-import-enrichment-stream-export]] — Referência cruzada direta com opencti-ecossistema-conectores-import-enrichment-stream-export.
- [[opencti-ontologia-stix21-sdos-scos-sros-rastreabilidade-fontes]] — Referência cruzada direta com opencti-ontologia-stix21-sdos-scos-sros-rastreabilidade-fontes.
- [[mispsoc-automacao-pymisp-restsearch-ingestao-enriquecimento]] — Referência cruzada direta com mispsoc-automacao-pymisp-restsearch-ingestao-enriquecimento.

## Fontes
- [OpenCTI Official GitHub — STIX 2.1 Cyber Threat Intelligence Platform](https://raw.githubusercontent.com/OpenCTI-Platform/opencti/master/README.md) — documentação oficial da plataforma OpenCTI cobrindo o grafo STIX 2.1, GraphQL, inferência e RBAC; consultado em 2026-10-03.
- [OpenCTI Connectors Official GitHub — Architecture & Classes](https://raw.githubusercontent.com/OpenCTI-Platform/connectors/master/README.md) — documentação oficial das 5 classes de conectores do OpenCTI (EXTERNAL_IMPORT, INTERNAL_ENRICHMENT, STREAM, etc.); consultado em 2026-10-03.
- [OpenCTI Official Documentation — Connectors Deployment](https://docs.opencti.io/latest/deployment/connectors/) — guia oficial de implantação e operação de conectores e workers do OpenCTI; consultado em 2026-10-03.
