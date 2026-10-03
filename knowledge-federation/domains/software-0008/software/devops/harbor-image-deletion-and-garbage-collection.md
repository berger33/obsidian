---
id: software.devops.tranche02.000145
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

# Exclusão de imagens e jobs de garbage collection para liberar manifests e blobs órfãos

## Em uma frase
Na seção `Features`, o item **Image deletion & garbage collection** explica que administradores de sistema podem executar jobs de coleta de lixo (`garbage collection jobs`) para que imagens — incluindo manifests pendentes (`dangling manifests`) e blobs não referenciados (`unreferenced blobs`) — sejam efetivamente excluídas e seu espaço em disco liberado periodicamente.

## Por que importa
Em registros OCI, apagar uma tag ou manifesto pela API apenas remove a referência lógica; sem agendar o garbage collection, os blobs de camadas antigas continuam ocupando terabytes de armazenamento.

## Como funciona
Combine políticas de retenção de tags por projeto com a execução periódica de jobs de garbage collection no Harbor para recuperar espaço de armazenamento de camadas não referenciadas.

## Exemplo
Após os pipelines de CI gerarem milhares de builds semanais, o job agendado de garbage collection do Harbor remove os manifests pendentes e blobs órfãos no fim de semana.

## Limites e trade-offs
Planeje a janela de execução do garbage collection e monitore o uso de I/O do backend de armazenamento durante a varredura de blobs.

## Como verificar
Conferi a seção Features no README oficial de `goharbor/harbor`.

## Conexões
- [[harbor-vulnerability-scanning-and-deployment-policies]] — Veja também: Scan regular de vulnerabilidades e políticas para impedir o deploy de imagens vulneráveis.
- [[harbor-portal-auditing-and-restful-swagger-api]] — Veja também: Portal gráfico, trilha de auditoria de operações e API RESTful com Swagger UI embutido.

## Fontes
- [Harbor — GitHub README](https://raw.githubusercontent.com/goharbor/harbor/main/README.md) — Visão geral do Harbor como registro cloud-native na CNCF, features (RBAC, replicação, scan, LDAP/OIDC, GC, auditoria, API REST), instalação e verificação de assinatura com Cosign (v2.15.0+).; consultado em 2026-10-03.
- [Harbor Documentation — Installation & Configuration Guide](https://goharbor.io/docs/latest/install-config/) — Guia oficial de instalação, configuração e matriz de compatibilidade do Harbor referenciada no README.; consultado em 2026-10-03.
