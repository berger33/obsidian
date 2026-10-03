---
id: software.seguranca.tranche05.000442
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/paralus/paralus/main/README.md", "https://www.paralus.io/docs/", "https://www.paralus.io/docs/usage/audit-logs"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CNCF Paralus: Conexão Segura de Clusters Privados via Relay Agent (Túnel mTLS Outbound sem Expor o `kube-apiserver`)

## Em uma frase
Ao importar um cluster Kubernetes existente (EKS, GKE, AKS, OpenShift, k3s ou bare-metal atrás de firewall/NAT) no Paralus, a plataforma gera um manifesto de bootstrap contendo o **`relay-agent`** e o **`prompt`** (proxy de sessão interativa).

## Por que importa
Permite gerenciar o acesso de engenheiros a dezenas de clusters isolados em VPCs privadas ou datacenters on-premises sem abrir nenhuma regra de firewall de entrada (*inbound*) nem criar VPNs ponto a ponto para cada cluster.

## Como funciona
O `relay-agent` rodando no namespace `paralus-system` do cluster de destino inicia uma conexão gRPC/mTLS de saída (porta `443`) para o endpoint `cdrelay.<dominio>` do Paralus Core. Quando um usuário autenticado executa `kubectl get pods`, a requisição chega ao `user-relay` do Paralus, é validada contra as políticas RBAC ativas e viaja pelo túnel reverso até o `kube-apiserver` local do cluster.

## Exemplo
```bash
# Baixar o manifesto de bootstrap de um cluster registrado via CLI pctl e aplicá-lo no cluster alvo
pctl get cluster "prod-eks-sa-east-1" -o yaml > /tmp/cluster-bootstrap.yaml
kubectl apply -f /tmp/cluster-bootstrap.yaml

# Verificar no cluster alvo se o relay-agent conectou-se com sucesso ao Paralus Core
kubectl -n paralus-system get pods
```

## Limites e trade-offs
Se o certificado mTLS do `relay-agent` ou a conectividade de saída para `cdrelay.<dominio>:443` for interrompida por um proxy corporativo que realiza inspeção TLS (*SSL Bump*), o túnel mTLS falhará; adicione o FQDN do `cdrelay` à lista de bypass de inspeção TLS.

## Como verificar
Verifique na UI ou via `pctl get clusters` que o cluster importado atingiu o status `HEALTHY` / `Ready`.

## Conexões
- [[paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager]] — Veja também: CNCF Paralus: Arquitetura de Gerenciamento de Acesso Zero-Trust para Frotas de Clusters Kubernetes.
- [[paralus-organizacao-projects-groups-custom-roles-namespace-rbac]] — Veja também: CNCF Paralus: Modelo Multi-Tenant com `Projects`, `Groups`, Papéis Pré-Configurados e `Custom Roles` por Namespace.
- [[paralus-kubeconfig-dinamico-just-in-time-serviceaccounts-revogacao]] — Referência cruzada direta com paralus-kubeconfig-dinamico-just-in-time-serviceaccounts-revogacao.
- [[ziti-dark-services-routers-eliminacao-portas-inbound-outbound-fabric]] — Referência cruzada direta com ziti-dark-services-routers-eliminacao-portas-inbound-outbound-fabric.

## Fontes
- [CNCF Paralus Official GitHub — Zero-Trust Kubernetes Access Manager](https://raw.githubusercontent.com/paralus/paralus/main/README.md) — documentação oficial do Paralus cobrindo RBAC multi-cluster, SSO/OIDC, JIT ServiceAccounts e pctl; consultado em 2026-10-03.
- [Paralus Official Documentation — Zero Trust & Architecture](https://www.paralus.io/docs/) — guia oficial de arquitetura, Relay Agent, Projects, Roles e operação do Paralus; consultado em 2026-10-03.
- [Paralus Documentation — Audit Logs](https://www.paralus.io/docs/usage/audit-logs) — documentação oficial de System Audit Logs e Kubectl/Relay Audit Logs; consultado em 2026-10-03.
