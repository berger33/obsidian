---
id: software.devops.tranche02.000142
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/goharbor/harbor/main/README.md", "https://goharbor.io/docs/latest/install-config/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Controle de acesso baseado em papéis (RBAC) por projeto e autenticação LDAP/AD e OIDC

## Em uma frase
A seção `Features` do README destaca três capacidades integradas de identidade e autorização no Harbor: **Role based access control** (usuários acessam diferentes repositórios por meio de `projects` e podem ter permissões distintas para imagens ou Helm charts dentro de um projeto), **LDAP/AD support** (integração com diretórios corporativos existentes e importação de grupos LDAP para atribuir permissões a projetos específicos) e **OIDC support** (uso de OpenID Connect para verificar identidades em provedores externos com Single Sign-On no portal do Harbor).

## Por que importa
Em organizações com dezenas de equipes e ambientes, segregar artefatos por projeto no Harbor e vincular permissões diretamente aos grupos corporativos de LDAP/AD ou OIDC elimina o gerenciamento manual de contas isoladas.

## Como funciona
Crie um projeto separado no Harbor para cada domínio ou equipe, integre a autenticação ao provedor OIDC ou diretório LDAP/AD corporativo e restrinja permissões de push às contas de serviço de CI/CD.

## Exemplo
Desenvolvedores entram no portal web do Harbor via SSO OIDC com permissão de leitura, enquanto apenas a conta robô do pipeline de CI possui permissão de escrita no projeto de produção.

## Limites e trade-offs
Consulte a lista oficial de adaptadores OIDC compatíveis (`harbor-compatibility-list/#oidc-adapters`) ao configurar provedores de identidade externos.

## Como verificar
Conferi a seção Features e a seção Compatibility no README oficial de `goharbor/harbor`.

## Conexões
- [[harbor-trusted-cloud-native-registry-overview]] — Veja também: Definição do Harbor como registro cloud-native que armazena, assina e escaneia artefatos.
- [[harbor-policy-based-replication-multi-registry]] — Veja também: Replicação baseada em políticas com filtros, retentativa automática e adaptadores.

## Fontes
- [Harbor — GitHub README](https://raw.githubusercontent.com/goharbor/harbor/main/README.md) — Visão geral do Harbor como registro cloud-native na CNCF, features (RBAC, replicação, scan, LDAP/OIDC, GC, auditoria, API REST), instalação e verificação de assinatura com Cosign (v2.15.0+).; consultado em 2026-10-03.
- [Harbor Documentation — Installation & Configuration Guide](https://goharbor.io/docs/latest/install-config/) — Guia oficial de instalação, configuração e matriz de compatibilidade do Harbor referenciada no README.; consultado em 2026-10-03.
