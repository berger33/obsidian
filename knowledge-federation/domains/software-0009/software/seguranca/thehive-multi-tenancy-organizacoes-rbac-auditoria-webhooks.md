---
id: software.seguranca.tranche06.000510
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

# TheHive & Cortex: Multi-Tenancy por Organizações, RBAC, Autenticação SSO/LDAP/OAuth2 e Notificações via Webhooks

## Em uma frase
Tanto o TheHive quanto o Cortex suportam nativamente **Multi-Tenancy baseado em Organizações**, onde cada unidade de negócios ou cliente de um MSSP opera em uma organização totalmente isolada, com seus próprios casos, templates, chaves de API e instâncias de Analyzers/Responders.

## Por que importa
Em um CSIRT corporativo global ou MSSP, analistas da filial A jamais devem visualizar incidentes confidenciais da filial B ou do conselho executivo, a menos que o caso seja explicitamente compartilhado.

## Como funciona
O controle de acesso combina autenticação corporativa (Active Directory/LDAP, OAuth2/OIDC, certificados X.509 ou chaves de API dedicadas para contas de serviço) com perfis granulares (`org-admin`, `read`, `write`, `analyze`) e **Webhooks** de saída que enviam eventos em tempo real (`case_create`, `case_task_log_create`, `case_artifact_create`) para canais de guerra no Mattermost/Slack ou motores de automação.

## Exemplo
```hocon
# Configuracao de Webhook de saida no TheHive para acionar automacao SOAR a cada mudanca em casos
webhooks {
  endpoints = [
    {
      name = "soar-audit-receiver"
      url = "https://soar.soc.internal.corp/webhooks/thehive"
      version = 0
      wsConfig {}
      includedTheHiveOrganisations = ["CSIRT-Global"]
    }
  ]
}
```

## Limites e trade-offs
Nunca utilize uma conta com papel `superAdmin` (administrador de plataforma que cria organizações) para investigar casos ou rodar Analyzers; no TheHive e no Cortex, `superAdmin` e contas operacionais de organização (`org-admin` / `analyst`) são estritamente segregados.

## Como verificar
Valide na matriz de usuários que as contas de integração (`TheHive4py` / SIEM feeder) pertencem exclusivamente à organização operacional com permissões restritas à criação de alertas.

## Conexões
- [[thehive-templates-relatorios-curtos-longos-fusao-casos]] — Veja também: TheHive: Customização de `Report Templates` do Cortex (Short / Long Reports), Fusão de Casos (`Case Merging`) e Fechamento Auditável.
- [[thehive-arquitetura-sirp-alerts-cases-tasks-observables]] — Referência cruzada direta com thehive-arquitetura-sirp-alerts-cases-tasks-observables.
- [[thehive-orquestracao-cortex-analyzers-tlp-pap-opsec]] — Referência cruzada direta com thehive-orquestracao-cortex-analyzers-tlp-pap-opsec.
- [[opencti-arquitetura-stix21-knowledge-graph-graphql-filigran]] — Referência cruzada direta com opencti-arquitetura-stix21-knowledge-graph-graphql-filigran.

## Fontes
- [TheHive Project Official GitHub — SIRP Architecture & Features](https://raw.githubusercontent.com/TheHive-Project/TheHive/master/README.md) — documentação oficial do TheHive cobrindo Alerts, Cases, Tasks, Observables, Case Templates e integração MISP; consultado em 2026-10-03.
- [Cortex Official GitHub — Observable Analysis & Active Response Engine](https://raw.githubusercontent.com/TheHive-Project/Cortex/master/README.md) — documentação oficial do motor Cortex para execução isolada de Analyzers e Responders com guardrails TLP/PAP; consultado em 2026-10-03.
- [Cortex Analyzers & Responders Official Repository](https://github.com/TheHive-Project/cortex-analyzers) — catálogo oficial de Analyzers e Responders do projeto TheHive; consultado em 2026-10-03.
