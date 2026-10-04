---
id: software.seguranca.tranche06.000519
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

# OpenCTI: Módulo de `Cases` (`Incident Response`, `Requests for Information — RFI`, `Requests for Takedown`) e `Analyst Workbenches`

## Em uma frase
Além de gerenciar inteligência de ameaças, o OpenCTI inclui o módulo nativo **Cases** (cobrindo *Incident Response*, *Requests for Information — RFIs* e *Requests for Takedown*) e **Analyst Workbenches** (áreas de rascunho para revisão e validação humana antes de comitar entidades no grafo principal).

## Por que importa
Permite que equipes de CTI e CSIRT recebam pedidos formais de investigação (*RFIs*) de executivos ou equipes de SOC, modelem um incidente de segurança como um contêiner STIX (`Case-Incident`) contendo a linha do tempo de observáveis, TTPs MITRE ATT&CK e tarefas, ou revisem extrações de relatórios PDF em um *Workbench* isolado antes de poluir o grafo de produção.

## Como funciona
Nos *Analyst Workbenches*, quando um analista importa um relatório PDF/Markdown (assistido por conectores de extração), os SDOs, SCOs e relacionamentos identificados ficam em estado de rascunho (*draft*) onde o analista pode corrigir tipos, ajustar marcações `TLP` e validar vínculos antes de clicar em *Validate & Import*.

## Exemplo
```graphql
# Criar um contêiner de Request for Information (RFI) via GraphQL para a equipe de Threat Intelligence
mutation CreateRfiCase {
  caseRfiAdd(
    input: {
      name: "RFI-2026-089: Avaliacao de Exposicao Setorial ao Grupo Akira"
      information_types: ["strategic-threat-landscape"]
      severity: "high"
      priority: "P1"
      confidence: 85
    }
  ) {
    id
    standard_id
    name
  }
}
```

## Limites e trade-offs
Importar relatórios brutos diretamente para o grafo principal sem passar pela revisão de um **Analyst Workbench** frequentemente introduz observáveis benignos (ex.: domínios de notícias citados no rodapé do PDF) vinculados incorretamente ao ator de ameaça.

## Como verificar
Importe um arquivo PDF de boletim de segurança selecionando a opção *Import into Analyst Workbench* e revise cada entidade extraída antes da submissão final.

## Conexões
- [[opencti-automacao-playbooks-enriquecimento-notificacoes-triage]] — Veja também: OpenCTI: Automação de Fluxos de Conhecimento com **Playbooks** (Gatilhos de Stream, Filtros, Enriquecimento, Marcação e Criação de Casos).
- [[opencti-desenvolvimento-conectores-pycti-stix2-bundles-workers]] — Veja também: OpenCTI: Desenvolvimento de Conectores Customizados com o SDK Python **`pycti`** (`OpenCTIConnectorHelper` e Envio de Bundles STIX 2.1).
- [[opencti-arquitetura-stix21-knowledge-graph-graphql-filigran]] — Referência cruzada direta com opencti-arquitetura-stix21-knowledge-graph-graphql-filigran.
- [[opencti-ontologia-stix21-sdos-scos-sros-rastreabilidade-fontes]] — Referência cruzada direta com opencti-ontologia-stix21-sdos-scos-sros-rastreabilidade-fontes.
- [[thehive-arquitetura-sirp-alerts-cases-tasks-observables]] — Referência cruzada direta com thehive-arquitetura-sirp-alerts-cases-tasks-observables.

## Fontes
- [OpenCTI Official GitHub — STIX 2.1 Cyber Threat Intelligence Platform](https://raw.githubusercontent.com/OpenCTI-Platform/opencti/master/README.md) — documentação oficial da plataforma OpenCTI cobrindo o grafo STIX 2.1, GraphQL, inferência e RBAC; consultado em 2026-10-03.
- [OpenCTI Connectors Official GitHub — Architecture & Classes](https://raw.githubusercontent.com/OpenCTI-Platform/connectors/master/README.md) — documentação oficial das 5 classes de conectores do OpenCTI (EXTERNAL_IMPORT, INTERNAL_ENRICHMENT, STREAM, etc.); consultado em 2026-10-03.
- [OpenCTI Official Documentation — Connectors Deployment](https://docs.opencti.io/latest/deployment/connectors/) — guia oficial de implantação e operação de conectores e workers do OpenCTI; consultado em 2026-10-03.
