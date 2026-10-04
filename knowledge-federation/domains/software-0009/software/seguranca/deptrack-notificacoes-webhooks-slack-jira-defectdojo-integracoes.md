---
id: software.seguranca.tranche01.000038
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/DependencyTrack/dependency-track/master/README.md", "https://docs.dependencytrack.org/getting-started/initial-startup/", "https://github.com/DependencyTrack/dependency-track"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP Dependency-Track Notificações e Integrações: alertas em tempo real (`Slack`, `Teams`, `Jira`, `Webhooks`) e sincronização com `DefectDojo`

## Em uma frase
O Dependency-Track possui um sistema configurável de **Notificações** (suportando **Slack**, **Microsoft Teams**, **Mattermost**, **Webex**, **Email**, **Jira** e **Webhooks** HTTP) e integrações nativas com plataformas de gestão de vulnerabilidades como **OWASP DefectDojo**, **Fortify SSC**, **ThreadFix** e **Kenna Security**.

## Por que importa
Se o Dependency-Track descobrir à meia-noite que um componente de produção acabou de receber uma CVE crítica (`NEW_VULNERABILITY`) ou violou uma política (`POLICY_VIOLATION`), a equipe responsável precisa receber um ticket no Jira ou alerta no Slack automaticamente.

## Como funciona
As regras de notificação (*Notification Rules*) são configuradas por escopo (`PORTFOLIO` ou `SYSTEM`), nível (`INFORMATIONAL`, `WARNING`, `ERROR`) e gatilhos específicos (`NEW_VULNERABILITY`, `NEW_VULNERABLE_DEPENDENCY`, `POLICY_VIOLATION`, `BOM_CONSUMED`, `BOM_PROCESSED`, `VEX_CONSUMED`), podendo ser filtradas apenas para os projetos de uma equipe.

## Exemplo
```json
{
  "scope": "PORTFOLIO",
  "notificationLevel": "WARNING",
  "triggerType": "NEW_VULNERABILITY",
  "publisher": "SLACK"
}
```

## Limites e trade-offs
Vincule cada regra de notificação de `NEW_VULNERABILITY` e `POLICY_VIOLATION` apenas aos projetos ativos (`active: true`) da equipe dona do serviço para evitar fadiga de alertas com repositórios arquivados.

## Como verificar
Teste o disparo de uma regra de notificação em *Administration -> Notifications -> Rules* verificando a entrega no canal ou webhook de destino.

## Conexões
- [[deptrack-monitoramento-servicos-externos-apis-trust-boundary-cyclonedx]] — Veja também: OWASP Dependency-Track Inventário de Serviços e APIs: rastreamento de provedores externos, classificação de dados e *Trust Boundaries*.
- [[deptrack-autenticacao-oidc-oauth2-ldap-teams-rbac-permissions]] — Veja também: OWASP Dependency-Track Autenticação e RBAC (`OIDC`, `LDAP`, `API Keys` e *Portfolio Access Control*): governança multi-equipe.

## Fontes
- [OWASP Dependency-Track GitHub — README.md (Continuous SBOM Analysis Platform, CycloneDX, VEX, EPSS, Policy Engine & Ecosystem Integrations)](https://raw.githubusercontent.com/DependencyTrack/dependency-track/master/README.md) — README oficial do DependencyTrack/dependency-track documentando arquitetura API-first, consumo de SBOM CycloneDX, fontes de inteligência, EPSS e VEX; consultado em 2026-10-03.
- [OWASP Dependency-Track Official Documentation — Initial Startup & Operational Configuration (Admin Setup, Feeds, Mirroring & Portfolio Management)](https://docs.dependencytrack.org/getting-started/initial-startup/) — Documentação oficial de inicialização e operação do Dependency-Track cobrindo provisionamento, sincronização de bases NVD/OSV/EPSS e controle de acesso; consultado em 2026-10-03.
- [OWASP Dependency-Track — Official GitHub Repository](https://github.com/DependencyTrack/dependency-track) — Repositório oficial Apache-2.0 do OWASP Dependency-Track; consultado em 2026-10-03.
