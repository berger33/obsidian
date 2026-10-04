---
id: software.devops.tranche14.001326
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
fontes: ["https://headlamp.dev/docs/latest/installation/in-cluster/", "https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md", "https://github.com/kubernetes-sigs/headlamp"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Headlamp: Autenticação OIDC Corporativa, Ingress e Terminação TLS no Backend

## Em uma frase
Para ambientes corporativos in-cluster, o Headlamp suporta integração nativa com provedores **OIDC** (Keycloak, Dex, Okta, Azure AD) e terminação TLS tanto no controlador de Ingress (padrão) quanto diretamente no container backend do Headlamp.

## Por que importa
Quando um Ingress Controller opera em modo **TLS Passthrough** (como NGINX TLS passthrough ou transport server), o backend do Headlamp precisa terminar a conexão HTTPS diretamente no Pod.

## Como funciona
Configura-se o Ingress com cert-manager (ou aplica-se o template oficial `kubernetes-headlamp-ingress-sample.yaml` substituindo `__URL__` pelo domínio real) e parametrizam-se as credenciais OIDC (`clientID`, `clientSecret`, `issuerURL`, `scopes`) no Helm chart para que o fluxo SSO repasse o token OIDC do usuário diretamente ao `kube-apiserver`.

## Exemplo
```bash
curl -s https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/kubernetes-headlamp-ingress-sample.yaml \
  | sed -e 's/__URL__/headlamp.internal.corp/' > headlamp-ingress.yaml
kubectl apply -f ./headlamp-ingress.yaml
```

## Limites e trade-offs
Aplicar o arquivo `kubernetes-headlamp-ingress-sample.yaml` diretamente sem substituir o placeholder `__URL__` cria uma regra de Ingress inválida para o host literal `__URL__`.

## Como verificar
Substitua sempre `__URL__` pelo FQDN real (ou configure a seção `ingress` diretamente no `values.yaml` do Helm chart).

## Conexões
- [[headlamp-plugins-manager-sidecar-artifacthub-extensoes]] — Veja também: Headlamp: Gerenciamento de Plugins de UI In-Cluster via Sidecar (pluginsManager e Artifact Hub).
- [[headlamp-operacoes-interativas-logs-exec-editor-cancelavel]] — Veja também: Headlamp: Operações Interativas de Logs, Terminal Exec, Editor com Documentação e Ações Canceláveis.

## Fontes
- [Headlamp GitHub — README.md (Kubernetes SIG UI Web & Desktop App, RBAC-Aware Controls, Multi-Cluster & Plugins)](https://headlamp.dev/docs/latest/installation/in-cluster/) — README oficial do kubernetes-sigs/headlamp (Apache-2.0) detalhando funcionalidades multi-cluster, reflexão de permissões RBAC na UI, terminal/logs/editor e ecossistema de plugins no Artifact Hub; consultado em 2026-10-03.
- [Headlamp Official Documentation — In-Cluster Installation (Helm Chart, Cluster Inventory API, Multiple Kubeconfigs, TLS, OIDC & pluginsManager Sidecar)](https://raw.githubusercontent.com/kubernetes-sigs/headlamp/main/README.md) — Guia oficial de implantação in-cluster do Headlamp cobrindo Helm chart, descoberta via ClusterProfile/secretreader, variáveis KUBECONFIG e sidecar pluginsManager; consultado em 2026-10-03.
- [Headlamp — Official GitHub Repository](https://github.com/kubernetes-sigs/headlamp) — Repositório oficial do Headlamp no Kubernetes SIG UI; consultado em 2026-10-03.
