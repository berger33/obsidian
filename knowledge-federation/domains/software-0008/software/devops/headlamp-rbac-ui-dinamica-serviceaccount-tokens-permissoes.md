---
id: software.devops.tranche14.001322
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

# Headlamp: Controles de UI Orientados por RBAC e Acesso via ServiceAccount Tokens

## Em uma frase
O Headlamp verifica dinamicamente as permissões **RBAC (Role-Based Access Control)** do token ou identidade OIDC do usuário na API do Kubernetes, ajustando a interface gráfica para habilitar ou ocultar botões de edição, criação e exclusão conforme o que o usuário realmente pode executar.

## Por que importa
Em muitas interfaces web, o usuário preenche um formulário inteiro de edição de manifesto apenas para receber um erro `403 Forbidden` ao clicar em salvar, ou, pior, a UI usa uma conta única privilegiada no backend.

## Como funciona
No Headlamp, as ações de leitura e escrita (`logs`, `exec`, editor de recursos com documentação integrada e deleção/atualização canceláveis) são executadas com as credenciais do próprio usuário; se o token usado tiver permissões muito restritas, a UI reflete imediatamente esse escopo.

## Exemplo
```bash
# Criar um token temporario de curta duracao para uma ServiceAccount com RBAC especifico:
kubectl -n kube-system create token headlamp-viewer --duration=1h
```

## Limites e trade-offs
Criar Secrets estáticos de token de ServiceAccount sem expiração (`kubernetes.io/service-account-token`) para login humano no Headlamp aumenta o risco caso o token vaze.

## Como verificar
Prefira autenticação OIDC integrada ao IdP corporativo ou gere tokens efêmeros via `kubectl create token --duration=1h` vinculados a Roles de escopo restrito.

## Conexões
- [[headlamp-arquitetura-web-ui-kubernetes-sig-ui-incluster-desktop]] — Veja também: Headlamp: Arquitetura da Interface Web Kubernetes Extensível (SIG UI) In-Cluster e Desktop.
- [[headlamp-multi-cluster-kubeconfig-separador-cluster-chooser]] — Veja também: Headlamp: Operação Multi-Cluster com Múltiplos Arquivos Kubeconfig.

## Fontes
- [Headlamp GitHub — README.md (Kubernetes SIG UI Web & Desktop App, RBAC-Aware Controls, Multi-Cluster & Plugins)](https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md) — README oficial do kubernetes-sigs/headlamp (Apache-2.0) detalhando funcionalidades multi-cluster, reflexão de permissões RBAC na UI, terminal/logs/editor e ecossistema de plugins no Artifact Hub; consultado em 2026-10-03.
- [Headlamp Official Documentation — In-Cluster Installation (Helm Chart, Cluster Inventory API, Multiple Kubeconfigs, TLS, OIDC & pluginsManager Sidecar)](https://headlamp.dev/docs/latest/installation/in-cluster/) — Guia oficial de implantação in-cluster do Headlamp cobrindo Helm chart, descoberta via ClusterProfile/secretreader, variáveis KUBECONFIG e sidecar pluginsManager; consultado em 2026-10-03.
- [Headlamp — Official GitHub Repository](https://github.com/kubernetes-sigs/headlamp) — Repositório oficial do Headlamp no Kubernetes SIG UI; consultado em 2026-10-03.
