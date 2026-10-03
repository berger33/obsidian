---
id: software.seguranca.tranche06.000501
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

# TheHive: Arquitetura da Plataforma de Resposta a Incidentes (SIRP) — Fluxo `Alerts` -> `Cases` -> `Tasks` -> `Observables`

## Em uma frase
**TheHive** (`TheHive-Project/TheHive`, originalmente AGPLv3 em Scala) é uma plataforma colaborativa de resposta a incidentes de segurança (SIRP) projetada para SOCs, CSIRTs e CERTs conduzirem investigações estruturadas em tempo real.

## Por que importa
Substitui sistemas genéricos de chamados (como Jira ou ServiceNow sem modelo de segurança) por um fluxo nativo de DFIR onde alertas do SIEM e eventos do MISP são triados, transformados em casos com playbooks padronizados e enriquecidos com análise automatizada de observáveis.

## Como funciona
O modelo operacional do TheHive estrutura-se em cinco entidades interligadas: **Alerts** (eventos brutos recebidos de SIEM, EDR, caixas de phishing ou MISP com deduplicação por `sourceRef`), **Cases** (investigações formais abertas a partir de alertas ou do zero), **Tasks** (etapas do playbook atribuídas a analistas), **Task Logs** (registros cronológicos em Markdown com evidências anexadas) e **Observables** (artefatos técnicos como IPs, hashes, domínios, URLs, e-mails e arquivos com classificação `TLP` e `PAP`).

## Exemplo
```python
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CaseTask

api = TheHiveApi("https://thehive.soc.internal.corp", "SOC_ANALYST_API_KEY")
new_case = Case(
    title="Incidente #2026-104: Beaconing C2 Detectado em Estacao Financeira",
    tlp=2,  # TLP:AMBER
    pap=2,  # PAP:AMBER
    severity=3,  # High
    tags=["c2", "edr-alert", "finance-vlan"],
    tasks=[CaseTask(title="1. Isolar host no EDR"), CaseTask(title="2. Coletar dump de memoria RAM")]
)
response = api.create_case(new_case)
```

## Limites e trade-offs
Converter alertas de SIEM diretamente em `Cases` sem passar pela fila de triagem (`Alerts`) inunda o painel de investigação do SOC caso uma regra de correlação do SIEM sofra um pico de falsos positivos.

## Como verificar
Consulte a API do TheHive verificando `response.status_code == 201` e confirme a criação das `Tasks` vinculadas ao novo caso.

## Conexões
- [[thehive-templates-casos-playbooks-padronizados-metricas-kpis]] — Veja também: TheHive: Padronização de Playbooks de Resposta a Incidentes com `Case Templates`, `Tasks` Obrigatórias e Métricas Customizadas.
- [[thehive-ingestao-alertas-thehive4py-siem-phishing-deduplicacao]] — Referência cruzada direta com thehive-ingestao-alertas-thehive4py-siem-phishing-deduplicacao.
- [[thehive-orquestracao-cortex-analyzers-tlp-pap-opsec]] — Referência cruzada direta com thehive-orquestracao-cortex-analyzers-tlp-pap-opsec.

## Fontes
- [TheHive Project Official GitHub — SIRP Architecture & Features](https://raw.githubusercontent.com/TheHive-Project/TheHive/master/README.md) — documentação oficial do TheHive cobrindo Alerts, Cases, Tasks, Observables, Case Templates e integração MISP; consultado em 2026-10-03.
- [Cortex Official GitHub — Observable Analysis & Active Response Engine](https://raw.githubusercontent.com/TheHive-Project/Cortex/master/README.md) — documentação oficial do motor Cortex para execução isolada de Analyzers e Responders com guardrails TLP/PAP; consultado em 2026-10-03.
- [Cortex Analyzers & Responders Official Repository](https://github.com/TheHive-Project/cortex-analyzers) — catálogo oficial de Analyzers e Responders do projeto TheHive; consultado em 2026-10-03.
