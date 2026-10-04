---
id: software.seguranca.tranche06.000502
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

# TheHive: Padronização de Playbooks de Resposta a Incidentes com `Case Templates`, `Tasks` Obrigatórias e Métricas Customizadas

## Em uma frase
O motor de **Case Templates** do TheHive permite codificar os playbooks operacionais do SOC (ex.: *Phishing Triage*, *Ransomware Containment*, *Compromised Cloud IAM Key*, *Data Exfiltration*) em modelos reutilizáveis.

## Por que importa
Garante que, independentemente de qual analista de plantão assuma o incidente às 3h da manhã, todas as etapas críticas de contenção, preservação forense, erradicação e notificação regulatória sejam executadas na mesma ordem.

## Como funciona
Um `Case Template` pré-define o prefixo do título, a severidade padrão, os níveis `TLP` e `PAP`, as tags obrigatórias, a lista ordenada de **Tasks** (com descrições detalhadas em Markdown dos comandos e procedimentos) e **Custom Fields / Metrics** (ex.: `mttd_minutes`, `hosts_affected_count`, `data_exfiltrated_boolean`) que alimentam os dashboards gerenciais do SOC.

## Exemplo
```json
{
  "name": "Playbook-Ransomware-Response-v3",
  "titlePrefix": "[RANSOMWARE]",
  "severity": 4,
  "tlp": 3,
  "pap": 2,
  "tags": ["ransomware", "critical-response", "playbook-v3"],
  "tasks": [
    { "title": "Contencao de Rede: Isolar host via EDR Responder", "group": "Containment" },
    { "title": "Preservacao Forense: Coletar triagem Velociraptor e RAM", "group": "Forensics" },
    { "title": "Escopo: Exportar IOCs confirmados para o MISP", "group": "Intelligence" }
  ]
}
```

## Limites e trade-offs
Alterar um `Case Template` existente aplica as novas tarefas apenas aos casos criados **após** a edição; casos já abertos mantêm a estrutura de tarefas do momento da sua instanciação.

## Como verificar
Importe um alerta em homologação selecionando o template `Playbook-Ransomware-Response-v3` e confirme que todas as tarefas e grupos foram instanciados automaticamente.

## Conexões
- [[thehive-arquitetura-sirp-alerts-cases-tasks-observables]] — Veja também: TheHive: Arquitetura da Plataforma de Resposta a Incidentes (SIRP) — Fluxo `Alerts` -> `Cases` -> `Tasks` -> `Observables`.
- [[thehive-ingestao-alertas-thehive4py-siem-phishing-deduplicacao]] — Veja também: TheHive: Ingestão Automatizada de Alertas via `TheHive4py` (`type`, `source`, `sourceRef`), Merge em Casos e Correlação de Observáveis.
- [[thehive-orquestracao-cortex-responders-contencao-ativa-edr-firewall]] — Referência cruzada direta com thehive-orquestracao-cortex-responders-contencao-ativa-edr-firewall.

## Fontes
- [TheHive Project Official GitHub — SIRP Architecture & Features](https://raw.githubusercontent.com/TheHive-Project/TheHive/master/README.md) — documentação oficial do TheHive cobrindo Alerts, Cases, Tasks, Observables, Case Templates e integração MISP; consultado em 2026-10-03.
- [Cortex Official GitHub — Observable Analysis & Active Response Engine](https://raw.githubusercontent.com/TheHive-Project/Cortex/master/README.md) — documentação oficial do motor Cortex para execução isolada de Analyzers e Responders com guardrails TLP/PAP; consultado em 2026-10-03.
- [Cortex Analyzers & Responders Official Repository](https://github.com/TheHive-Project/cortex-analyzers) — catálogo oficial de Analyzers e Responders do projeto TheHive; consultado em 2026-10-03.
