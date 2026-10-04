---
id: software.seguranca.tranche06.000509
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

# TheHive: Customização de `Report Templates` do Cortex (Short / Long Reports), Fusão de Casos (`Case Merging`) e Fechamento Auditável

## Em uma frase
O TheHive possui um motor de **Report Templates** em AngularJS/HTML que formata o JSON bruto retornado pelos *Analyzers* do Cortex em duas visualizações: **Short Report** (as badges de taxonomia exibidas na linha do observável) e **Long Report** (o relatório detalhado formatado ao clicar no resultado da análise).

## Por que importa
Além da visualização de relatórios, quando dois analistas investigam alertas distintos que acabam revelando o mesmo grupo atacante ou observáveis em comum, a funcionalidade de **Case Merging** funde os dois casos preservando todas as tarefas, logs, anexos e observáveis deduplicados.

## Como funciona
No encerramento de um caso, o TheHive exige classificar a resolução (`TruePositive` — `WithImpact` ou `WithoutImpact`, `FalsePositive`, `Indeterminate`, `Other`) e preencher o resumo executivo de fechamento, gerando métricas auditáveis de taxa de falsos positivos por regra do SIEM e MTTR (*Mean Time to Respond*).

## Exemplo
```python
# Consultar via API REST do TheHive todos os casos abertos que compartilham um mesmo observavel para fusao
import requests

resp = requests.post(
    "https://thehive.soc.internal.corp/api/case/ artifact/_search",
    headers={"Authorization": "Bearer SOC_ANALYST_API_KEY"},
    json={"query": {"_field": "data", "_value": "198.51.100.214"}}
)
```

## Limites e trade-offs
Ao realizar o *Merge* de dois casos com níveis de `TLP` ou `PAP` diferentes, revise sempre a classificação do caso resultante para garantir que ele assuma o nível mais restritivo entre os dois.

## Como verificar
Encerre um caso de teste preenchendo `resolutionStatus = "TruePositive"` e `impactStatus = "NoImpact"` e verifique a atualização imediata no dashboard de métricas.

## Conexões
- [[thehive-desenvolvimento-analyzers-customizados-cortexutils-docker]] — Veja também: Cortex: Desenvolvimento de `Analyzers` e `Responders` Customizados em Python (`cortexutils`) e Isolamento em Containers Docker.
- [[thehive-multi-tenancy-organizacoes-rbac-auditoria-webhooks]] — Veja também: TheHive & Cortex: Multi-Tenancy por Organizações, RBAC, Autenticação SSO/LDAP/OAuth2 e Notificações via Webhooks.
- [[thehive-arquitetura-sirp-alerts-cases-tasks-observables]] — Referência cruzada direta com thehive-arquitetura-sirp-alerts-cases-tasks-observables.
- [[thehive-templates-casos-playbooks-padronizados-metricas-kpis]] — Referência cruzada direta com thehive-templates-casos-playbooks-padronizados-metricas-kpis.

## Fontes
- [TheHive Project Official GitHub — SIRP Architecture & Features](https://raw.githubusercontent.com/TheHive-Project/TheHive/master/README.md) — documentação oficial do TheHive cobrindo Alerts, Cases, Tasks, Observables, Case Templates e integração MISP; consultado em 2026-10-03.
- [Cortex Official GitHub — Observable Analysis & Active Response Engine](https://raw.githubusercontent.com/TheHive-Project/Cortex/master/README.md) — documentação oficial do motor Cortex para execução isolada de Analyzers e Responders com guardrails TLP/PAP; consultado em 2026-10-03.
- [Cortex Analyzers & Responders Official Repository](https://github.com/TheHive-Project/cortex-analyzers) — catálogo oficial de Analyzers e Responders do projeto TheHive; consultado em 2026-10-03.
