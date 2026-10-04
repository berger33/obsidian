---
id: software.devops.tranche02.000141
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

# Definição do Harbor como registro cloud-native que armazena, assina e escaneia artefatos

## Em uma frase
O README oficial no repositório `goharbor/harbor` define o Harbor como um projeto open source de registro cloud-native confiável (`trusted cloud native registry`) hospedado pela Cloud Native Computing Foundation (CNCF) que armazena, assina e escaneia conteúdo, estendendo o Docker Distribution open source com funcionalidades exigidas por empresas como segurança, identidade, gerenciamento, controle de acesso, auditoria de atividades e replicação entre registros.

## Por que importa
Posicionar um registro completo próximo ao ambiente de build e execução melhora a eficiência de transferência de imagens e adiciona controles de segurança que um registro OCI básico sem camada de governança não oferece.

## Como funciona
Utilize releases estáveis oficiais do Harbor (`github.com/goharbor/harbor/releases`) para hospedar tanto imagens de contêineres quanto Helm charts em ambientes de Kubernetes e CI/CD.

## Exemplo
Uma plataforma Kubernetes corporativa hospeda internamente o Harbor como registro centralizado para os pipelines de Tekton e os controladores de Argo CD e Flux.

## Limites e trade-offs
O próprio README alerta no topo que a branch `main` pode estar em estado instável ou mesmo quebrado durante o desenvolvimento; use sempre as releases oficiais para obter binários estáveis.

## Como verificar
Conferi os avisos de topo, a abertura e a seção Features no README oficial de `goharbor/harbor`.

## Conexões
- [[harbor-rbac-projects-ldap-and-oidc-identity]] — Veja também: Controle de acesso baseado em papéis (RBAC) por projeto e autenticação LDAP/AD e OIDC.

## Fontes
- [Harbor — GitHub README](https://raw.githubusercontent.com/goharbor/harbor/main/README.md) — Visão geral do Harbor como registro cloud-native na CNCF, features (RBAC, replicação, scan, LDAP/OIDC, GC, auditoria, API REST), instalação e verificação de assinatura com Cosign (v2.15.0+).; consultado em 2026-10-03.
- [Harbor Documentation — Installation & Configuration Guide](https://goharbor.io/docs/latest/install-config/) — Guia oficial de instalação, configuração e matriz de compatibilidade do Harbor referenciada no README.; consultado em 2026-10-03.
