---
id: software.devops.tranche14.001327
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md", "https://headlamp.dev/docs/latest/installation/in-cluster/", "https://github.com/kubernetes-sigs/headlamp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Headlamp: Operações Interativas de Logs, Terminal Exec, Editor com Documentação e Ações Canceláveis

## Em uma frase
O Headlamp combina visualização de estado com recursos interativos de operação: streaming de logs de containers, terminal interativo (`exec`), editor de recursos YAML com documentação de schema integrada e operações de criação/atualização/deleção **canceláveis**.

## Por que importa
Ao editar um manifesto YAML no navegador ou excluir acidentalmente o recurso errado, a falta de documentação dos campos da spec e a execução imediata sem janela de cancelamento causam erros operacionais.

## Como funciona
Na interface do Headlamp, o editor de recursos exibe a descrição oficial dos campos do Kubernetes ao lado do YAML, e ações mutáveis oferecem uma janela curta de cancelamento na UI antes que a requisição final seja efetivada, respeitando sempre se o RBAC do usuário permite `patch`, `update`, `delete` ou `pods/exec`.

## Exemplo
```bash
# Verificar se o usuario atual possui permissao para exec e logs via RBAC:
kubectl auth can-i create pods/exec -n default
kubectl auth can-i get pods/log -n default
```

## Limites e trade-offs
Conceder a permissão `pods/exec` em produção para perfis de visualização (`view`) permite que usuários abram um terminal interativo dentro dos containers pelo Headlamp e leiam variáveis de ambiente sensíveis.

## Como verificar
Separe os ClusterRoles: conceda apenas `get`, `list`, `watch` e `pods/log` para desenvolvedores em produção e restrinja `pods/exec` a papéis de resposta a incidentes.

## Conexões
- [[headlamp-autenticacao-oidc-ingress-tls-passthrough-backend]] — Veja também: Headlamp: Autenticação OIDC Corporativa, Ingress e Terminação TLS no Backend.
- [[headlamp-desenvolvimento-plugins-frontend-sdk-typescript-react]] — Veja também: Headlamp: Desenvolvimento de Plugins Customizados para Plataformas Internas (IDPs).

## Fontes
- [Headlamp GitHub — README.md (Kubernetes SIG UI Web & Desktop App, RBAC-Aware Controls, Multi-Cluster & Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md) — README oficial do kubernetes-sigs/headlamp (Apache-2.0) detalhando funcionalidades multi-cluster, reflexão de permissões RBAC na UI, terminal/logs/editor e ecossistema de plugins no Artifact Hub; consultado em 2026-10-03.
- [Headlamp Official Documentation — In-Cluster Installation (Helm Chart, Cluster Inventory API, Multiple Kubeconfigs, TLS, OIDC & pluginsManager Sidecar)](https://headlamp.dev/docs/latest/installation/in-cluster/) — Guia oficial de implantação in-cluster do Headlamp cobrindo Helm chart, descoberta via ClusterProfile/secretreader, variáveis KUBECONFIG e sidecar pluginsManager; consultado em 2026-10-03.
- [Headlamp — Official GitHub Repository](https://github.com/kubernetes-sigs/headlamp) — Repositório oficial do Headlamp no Kubernetes SIG UI; consultado em 2026-10-03.
