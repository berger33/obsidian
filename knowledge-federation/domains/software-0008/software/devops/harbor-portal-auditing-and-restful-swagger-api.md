---
id: software.devops.tranche02.000146
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

# Portal gráfico, trilha de auditoria de operações e API RESTful com Swagger UI embutido

## Em uma frase
A seção `Features` e a seção `API` do README descrevem três recursos de governança e automação do Harbor: **Graphical user portal** (para navegar, pesquisar repositórios e gerenciar projetos), **Auditing** (todas as operações nos repositórios são rastreadas por meio de logs) e **RESTful API** (APIs RESTful para operações administrativas e integração com sistemas externos, acompanhadas de um Swagger UI embutido e especificação em `api/v2.0/swagger.yaml`).

## Por que importa
Equipes de segurança precisam de trilhas de auditoria completas sobre quem enviou, baixou ou excluiu cada artefato, enquanto equipes de plataforma precisam provisionar projetos, cotas e contas robô programaticamente via API REST.

## Como funciona
Automatize a criação de projetos, regras de replicação e permissões consumindo a API RESTful v2.0 do Harbor e encaminhe os logs de auditoria de operações para a plataforma central de observabilidade.

## Exemplo
Um controlador de plataforma consulta a especificação `api/v2.0/swagger.yaml` e provisiona automaticamente um novo projeto no Harbor sempre que um novo microsserviço é criado.

## Limites e trade-offs
Proteja os tokens de acesso à API administrativa do Harbor em cofres de segredos e aplique privilégio mínimo às contas de automação.

## Como verificar
Conferi as seções Features e API no README oficial de `goharbor/harbor`.

## Conexões
- [[harbor-image-deletion-and-garbage-collection]] — Veja também: Exclusão de imagens e jobs de garbage collection para liberar manifests e blobs órfãos.
- [[harbor-deployment-options-docker-compose-helm-operator]] — Veja também: Opções de implantação: Docker Compose, Helm Chart (harbor-helm) e Harbor Operator.

## Fontes
- [Harbor — GitHub README](https://raw.githubusercontent.com/goharbor/harbor/main/README.md) — Visão geral do Harbor como registro cloud-native na CNCF, features (RBAC, replicação, scan, LDAP/OIDC, GC, auditoria, API REST), instalação e verificação de assinatura com Cosign (v2.15.0+).; consultado em 2026-10-03.
- [Harbor Documentation — Installation & Configuration Guide](https://goharbor.io/docs/latest/install-config/) — Guia oficial de instalação, configuração e matriz de compatibilidade do Harbor referenciada no README.; consultado em 2026-10-03.
