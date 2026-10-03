---
id: software.seguranca.tranche06.000507
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
fontes: ["https://raw.githubusercontent.com/TheHive-Project/TheHive/master/README.md", "https://raw.githubusercontent.com/TheHive-Project/Cortex/master/README.md", "https://github.com/TheHive-Project/cortex-analyzers"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# TheHive: Integração Bidirecional com o **MISP** (Importação Filtrada de Eventos para Alertas e Exportação de IOCs Confirmados)

## Em uma frase
O TheHive foi projetado desde a origem para operar em simbiose bidirecional com uma ou múltiplas instâncias **MISP**: importando novos eventos de inteligência como alertas e exportando de volta para o MISP apenas os observáveis marcados com `ioc=True` ao concluir um caso.

## Por que importa
Fecha o ciclo de inteligência (*Intelligence Loop*): uma investigação iniciada no SOC local descobre novos domínios e hashes do atacante; ao clicar em *Export to MISP* no caso do TheHive, esses indicadores viram um evento estruturado no MISP que atualiza imediatamente as regras do Suricata/Zeek e protege as demais unidades.

## Como funciona
Na configuração do conector MISP do TheHive, filtros granulares (`whitelist-tags`, `blacklist-tags`, `blacklist-orgs`, `max-attributes`, `max-age`) impedem que eventos gigantescos de feeds públicos OSINT do MISP inundem a fila de alertas do TheHive.

## Exemplo
```hocon
# Configuracao do conector MISP no TheHive com filtros estritos de tags e idade
misp {
  interval = 5m
  servers = [
    {
      name = "MISP-CSIRT-Internal"
      url = "https://misp.soc.internal.corp"
      auth {
        type = "key"
        key = "${MISP_THEHIVE_SYNC_KEY}"
      }
      purpose = ImportAndExport
      inclusionFilter {
        tags = ["tlp:amber", "tlp:green", "csirt:escalate-to-soc"]
        maxAge = 7 days
        maxAttributes = 200
      }
    }
  ]
}
```

## Limites e trade-offs
Configurar `purpose = ImportAndExport` sem definir `inclusionFilter` (especialmente `tags` e `maxAttributes`) fará o TheHive importar todos os eventos históricos do MISP como milhares de alertas na primeira sincronização.

## Como verificar
Crie um caso de teste no TheHive, marque apenas 1 observável como `ioc=True`, exporte para a instância MISP de homologação e confirme que apenas o artefato com `ioc=True` foi exportado com `to_ids=true`.

## Conexões
- [[thehive-orquestracao-cortex-responders-contencao-ativa-edr-firewall]] — Veja também: TheHive & Cortex: Contenção e Resposta Ativa a Incidentes com **Cortex Responders** (Isolamento EDR, Bloqueio Firewall/RPZ e Revogação IAM).
- [[thehive-desenvolvimento-analyzers-customizados-cortexutils-docker]] — Veja também: Cortex: Desenvolvimento de `Analyzers` e `Responders` Customizados em Python (`cortexutils`) e Isolamento em Containers Docker.
- [[thehive-arquitetura-sirp-alerts-cases-tasks-observables]] — Referência cruzada direta com thehive-arquitetura-sirp-alerts-cases-tasks-observables.
- [[thehive-governanca-observables-tlp-pap-ioc-sighted-marking]] — Referência cruzada direta com thehive-governanca-observables-tlp-pap-ioc-sighted-marking.
- [[mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies]] — Referência cruzada direta com mispsoc-arquitetura-threat-intelligence-events-attributes-objects-galaxies.

## Fontes
- [TheHive Project Official GitHub — SIRP Architecture & Features](https://raw.githubusercontent.com/TheHive-Project/TheHive/master/README.md) — documentação oficial do TheHive cobrindo Alerts, Cases, Tasks, Observables, Case Templates e integração MISP; consultado em 2026-10-03.
- [Cortex Official GitHub — Observable Analysis & Active Response Engine](https://raw.githubusercontent.com/TheHive-Project/Cortex/master/README.md) — documentação oficial do motor Cortex para execução isolada de Analyzers e Responders com guardrails TLP/PAP; consultado em 2026-10-03.
- [Cortex Analyzers & Responders Official Repository](https://github.com/TheHive-Project/cortex-analyzers) — catálogo oficial de Analyzers e Responders do projeto TheHive; consultado em 2026-10-03.
