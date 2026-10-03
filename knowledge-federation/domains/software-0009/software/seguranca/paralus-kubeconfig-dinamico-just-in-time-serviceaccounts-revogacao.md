---
id: software.seguranca.tranche05.000445
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

# CNCF Paralus: Provisionamento *Just-in-Time* de ServiceAccounts, `kubeconfig` Auditado e Revogação Instantânea

## Em uma frase
Quando um usuário solicita acesso via `kubectl` (baixando seu `kubeconfig` no Paralus ou usando o terminal web *Prompt*), o Paralus provisiona *Just-in-Time* as credenciais e `ServiceAccounts` efêmeras no cluster de destino e permite revogar permissões ou certificados instantaneamente.

## Por que importa
No Kubernetes puro, certificados X.509 de cliente embutidos em arquivos `kubeconfig` não possuem lista de revogação (CRL) nativa no `kube-apiserver` e permanecem válidos até expirarem; como o `kubeconfig` do Paralus aponta para o proxy `user-relay` do Paralus, a revogação no plano de controle bloqueia o acesso no mesmo segundo.

## Como funciona
O administrador pode configurar o tempo de validade e rotação do `kubeconfig`, desativar o acesso `kubectl` CLI ou o terminal web por usuário, e revogar o certificado de cliente do `kubeconfig` em um clique caso o notebook de um engenheiro seja extraviado.

## Exemplo
```bash
# Baixar o kubeconfig gerenciado pelo Paralus para um cluster específico usando a CLI pctl
pctl get kubeconfig "prod-eks-sa-east-1" \
  --project "payments-platform" > ~/.kube/paralus-prod-payments.yaml

export KUBECONFIG=~/.kube/paralus-prod-payments.yaml
kubectl get pods -n payments
```

## Limites e trade-offs
Armazenar o arquivo `kubeconfig` baixado em diretórios com permissão de leitura global (`0644`) expõe o certificado de cliente a outros processos locais; defina sempre `chmod 600 ~/.kube/paralus-prod-payments.yaml`.

## Como verificar
Revogue a associação de role do usuário no Paralus e execute imediatamente `kubectl get pods` com o mesmo `kubeconfig`, confirmando que a requisição é negada em tempo real pelo proxy.

## Conexões
- [[paralus-federacao-sso-oidc-okta-entra-github-mapeamento-grupos]] — Veja também: CNCF Paralus: Federação SSO com Provedores OIDC (Okta, Microsoft Entra ID, Google, Keycloak e GitHub) e Mapeamento de Grupos.
- [[paralus-terminal-web-prompt-sessoes-efemeras-browser-kubectl]] — Veja também: CNCF Paralus: Acesso `kubectl` Browser-Based via Componente `Prompt` (Sessões Efêmeras sem Credenciais no Desktop).
- [[paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager]] — Referência cruzada direta com paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager.
- [[paralus-conexao-clusters-relay-agent-outbound-mtls-dial-in]] — Referência cruzada direta com paralus-conexao-clusters-relay-agent-outbound-mtls-dial-in.
- [[paralus-auditoria-completa-kubectl-api-relay-audit-logs-siem]] — Referência cruzada direta com paralus-auditoria-completa-kubectl-api-relay-audit-logs-siem.

## Fontes
- [CNCF Paralus Official GitHub — Zero-Trust Kubernetes Access Manager](https://raw.githubusercontent.com/paralus/paralus/main/README.md) — documentação oficial do Paralus cobrindo RBAC multi-cluster, SSO/OIDC, JIT ServiceAccounts e pctl; consultado em 2026-10-03.
- [Paralus Official Documentation — Zero Trust & Architecture](https://www.paralus.io/docs/) — guia oficial de arquitetura, Relay Agent, Projects, Roles e operação do Paralus; consultado em 2026-10-03.
- [Paralus Documentation — Audit Logs](https://www.paralus.io/docs/usage/audit-logs) — documentação oficial de System Audit Logs e Kubectl/Relay Audit Logs; consultado em 2026-10-03.
