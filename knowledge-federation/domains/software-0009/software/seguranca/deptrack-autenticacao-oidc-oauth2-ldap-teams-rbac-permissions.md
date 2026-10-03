---
id: software.seguranca.tranche01.000039
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

# OWASP Dependency-Track Autenticação e RBAC (`OIDC`, `LDAP`, `API Keys` e *Portfolio Access Control*): governança multi-equipe

## Em uma frase
Para operação corporativa, o Dependency-Track suporta **OAuth 2.0 + OpenID Connect (OIDC)** para Single Sign-On, **Active Directory / LDAP**, usuários gerenciados internamente e **API Keys** vinculadas a **Teams**, combinados com permissões granulares (`BOM_UPLOAD`, `VULNERABILITY_ANALYSIS`, `POLICY_VIOLATION_ANALYSIS`, `ACCESS_MANAGEMENT`) e **Portfolio Access Control** por projeto.

## Por que importa
Em organizações grandes, a equipe de um produto precisa ter autonomia para fazer upload de SBOMs e auditar achados dos seus próprios microsserviços sem poder alterar políticas globais ou visualizar projetos confidenciais de outras unidades de negócio.

## Como funciona
No modelo de controle de acesso do Dependency-Track: 1) grupos do IdP OIDC/LDAP são mapeados automaticamente para **Teams**; 2) cada Team recebe apenas as permissões funcionais necessárias; e 3) com o *Portfolio Access Control* habilitado, cada projeto especifica quais Teams têm permissão de visualização e operação sobre ele.

## Exemplo
```bash
# Exemplo de variáveis de ambiente no container do Frontend e API Server para SSO via OpenID Connect (OIDC):
ALPINE_OIDC_ENABLED=true
ALPINE_OIDC_ISSUER=https://idp.internal.corp/realms/engineering
ALPINE_OIDC_CLIENT_ID=dependency-track
ALPINE_OIDC_USER_PROVISIONING=true
ALPINE_OIDC_TEAM_SYNCHRONIZATION=true
```

## Limites e trade-offs
Crie uma `Team` dedicada para automação de CI/CD contendo apenas as permissões mínimas (`BOM_UPLOAD`, `PROJECT_CREATION_UPLOAD` e `VIEW_PORTFOLIO`), nunca reutilizando chaves de API com permissão de administrador global (`ACCESS_MANAGEMENT`).

## Como verificar
Audite as equipes, chaves de API e permissões ativas em *Administration -> Access Management -> Teams*.

## Conexões
- [[deptrack-notificacoes-webhooks-slack-jira-defectdojo-integracoes]] — Veja também: OWASP Dependency-Track Notificações e Integrações: alertas em tempo real (`Slack`, `Teams`, `Jira`, `Webhooks`) e sincronização com `DefectDojo`.
- [[deptrack-repositorio-outdated-components-private-vuln-db-operacao-v5]] — Veja também: OWASP Dependency-Track Risco de Desatualização, Banco Privado de Vulnerabilidades e Evolução Arquitetural (`v4` -> `v5`).

## Fontes
- [OWASP Dependency-Track GitHub — README.md (Continuous SBOM Analysis Platform, CycloneDX, VEX, EPSS, Policy Engine & Ecosystem Integrations)](https://raw.githubusercontent.com/DependencyTrack/dependency-track/master/README.md) — README oficial do DependencyTrack/dependency-track documentando arquitetura API-first, consumo de SBOM CycloneDX, fontes de inteligência, EPSS e VEX; consultado em 2026-10-03.
- [OWASP Dependency-Track Official Documentation — Initial Startup & Operational Configuration (Admin Setup, Feeds, Mirroring & Portfolio Management)](https://docs.dependencytrack.org/getting-started/initial-startup/) — Documentação oficial de inicialização e operação do Dependency-Track cobrindo provisionamento, sincronização de bases NVD/OSV/EPSS e controle de acesso; consultado em 2026-10-03.
- [OWASP Dependency-Track — Official GitHub Repository](https://github.com/DependencyTrack/dependency-track) — Repositório oficial Apache-2.0 do OWASP Dependency-Track; consultado em 2026-10-03.
