---
id: software.seguranca.tranche06.000515
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

# OpenCTI: Ciclo de Vida de Indicadores — **Decay Rules** (Curvas de Decaimento de `x_opencti_score`), Expiração `valid_until` e Revogação

## Em uma frase
Para evitar que SIEMs e sensores conectados aos streams do OpenCTI gerem alertas falsos eternos por causa de IPs ou domínios reciclados, o OpenCTI gerencia o ciclo de vida de cada `Indicator` através de **Decay Rules** (regras matemáticas de decaimento do atributo `x_opencti_score` de `0` a `100`).

## Por que importa
Um endereço IPv4 de proxy residencial usado em um ataque hoje pode ser reatribuído a um usuário doméstico legítimo em 15 dias; as *Decay Rules* reduzem progressivamente o `x_opencti_score` ao longo dos dias até atingir o limiar de revogação (`revoke_score`), marcando automaticamente `revoked = true`.

## Como funciona
Cada *Decay Rule* pode ser filtrada pelo tipo de observável principal (`x_opencti_main_observable_type`: ex.: decaimento rápido de 15 dias para `IPv4-Addr` e `Url`, médio de 60 dias para `Domain-Name` e lento de 365 dias para `StixFile` hashes), definindo pontos de queda (`decay_points`, ex.: `[80, 50, 20]`), tempo de vida (`decay_lifetime`) e pontuação de revogação (`decay_revoke_score`). Quando um conector `STREAM` detecta que o indicador passou para `revoked = true`, ele instrui imediatamente o SIEM/EDR receptor a remover o IOC da lista de detecção ativa.

## Exemplo
```graphql
# Consultar indicadores ativos com score elevado e ainda nao revogados pelas Decay Rules
query ActiveHighScoreIndicators {
  indicators(
    first: 50
    filters: {
      mode: and
      filters: [
        { key: "revoked", values: ["false"] }
        { key: "x_opencti_score", values: ["70"], operator: gt }
      ]
      filterGroups: []
    }
  ) {
    edges {
      node {
        id
        name
        pattern
        x_opencti_score
        valid_until
        revoked
      }
    }
  }
}
```

## Limites e trade-offs
Se um indicador em decaimento receber um novo **Sighting** (avistamento real confirmado em produção) ou uma nova atualização de fonte confiável com pontuação superior, o OpenCTI reaquece (*bumps*) o `x_opencti_score` e estende `valid_until`.

## Como verificar
Inspecione a aba *Lifecycle* dentro da página de detalhes de um `Indicator` no OpenCTI para visualizar a curva exata de decaimento e as datas projetadas para cada queda de score e revogação.

## Conexões
- [[opencti-motor-inferencia-regras-deducao-relacoes-transitivas]] — Veja também: OpenCTI: Motor de Raciocínio e Inferência (`Rule Engine`) para Dedução Automática de Relações Transitivas no Grafo.
- [[opencti-governanca-rbac-marking-definitions-tlp-confianca-organizacoes]] — Veja também: OpenCTI: Controle de Acesso Baseado em **Marking Definitions** (`TLP`, `PAP`, `Statement`), Segregação por Organizações e `Max Confidence Level`.
- [[opencti-ontologia-stix21-sdos-scos-sros-rastreabilidade-fontes]] — Referência cruzada direta com opencti-ontologia-stix21-sdos-scos-sros-rastreabilidade-fontes.
- [[opencti-streams-taxii21-live-streams-feeds-csv-integracao-siem]] — Referência cruzada direta com opencti-streams-taxii21-live-streams-feeds-csv-integracao-siem.
- [[mispsoc-colaboracao-sightings-opinions-decaying-models-ciclo-vida]] — Referência cruzada direta com mispsoc-colaboracao-sightings-opinions-decaying-models-ciclo-vida.

## Fontes
- [OpenCTI Official GitHub — STIX 2.1 Cyber Threat Intelligence Platform](https://raw.githubusercontent.com/OpenCTI-Platform/opencti/master/README.md) — documentação oficial da plataforma OpenCTI cobrindo o grafo STIX 2.1, GraphQL, inferência e RBAC; consultado em 2026-10-03.
- [OpenCTI Connectors Official GitHub — Architecture & Classes](https://raw.githubusercontent.com/OpenCTI-Platform/connectors/master/README.md) — documentação oficial das 5 classes de conectores do OpenCTI (EXTERNAL_IMPORT, INTERNAL_ENRICHMENT, STREAM, etc.); consultado em 2026-10-03.
- [OpenCTI Official Documentation — Connectors Deployment](https://docs.opencti.io/latest/deployment/connectors/) — guia oficial de implantação e operação de conectores e workers do OpenCTI; consultado em 2026-10-03.
