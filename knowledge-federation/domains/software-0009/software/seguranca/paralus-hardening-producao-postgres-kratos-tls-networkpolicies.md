---
id: software.seguranca.tranche05.000450
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

# CNCF Paralus: Hardening da Própria Instalação do Paralus (Certificados TLS, Isolamento de Rede e Proteção de Segredos)

## Em uma frase
Como o Paralus atua como o ponto central de autenticação e autorização para toda a frota de clusters Kubernetes, o cluster hospedeiro onde o Paralus Core roda deve ser tratado como infraestrutura **Tier Zero** com *hardening* rigoroso.

## Por que importa
O comprometimento do namespace `paralus` ou do seu banco PostgreSQL permitiria a um atacante injetar associações `CLUSTER_ADMIN` em qualquer cluster conectado via `relay-agent`.

## Como funciona
Em produção, substitua certificados autoassinados por certificados TLS gerenciados pelo `cert-manager` para os três domínios (`console`, `core-connector` e `cdrelay`), externalize o banco PostgreSQL para uma instância gerenciada com mTLS e criptografia KMS, proteja os segredos do Ory Kratos/Paralus via External Secrets Operator e aplique `NetworkPolicies` estritas no namespace `paralus`.

## Exemplo
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: isolate-paralus-control-plane
  namespace: paralus
spec:
  podSelector: {}
  policyTypes: ["Ingress", "Egress"]
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: ingress-nginx
```

## Limites e trade-offs
Nunca instale o plano de controle do Paralus dentro de um cluster compartilhado com cargas de trabalho não confiáveis de desenvolvimento; isole-o em um cluster de gerenciamento dedicado.

## Como verificar
Verifique `kubectl -n paralus get networkpolicies,ingress,certificates` e confirme que todos os endpoints HTTPS do Paralus apresentam certificados TLS válidos e isolamento de rede ativo.

## Conexões
- [[paralus-custom-roles-restricao-verbs-exec-portforward-secrets]] — Veja também: CNCF Paralus: Criação de `Custom Roles` Restritivas (Bloqueio de `pods/exec`, `pods/portforward` e Leitura de `secrets`).
- [[paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager]] — Referência cruzada direta com paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager.
- [[paralus-conexao-clusters-relay-agent-outbound-mtls-dial-in]] — Referência cruzada direta com paralus-conexao-clusters-relay-agent-outbound-mtls-dial-in.
- [[bloodhound-governanca-tier-zero-high-value-assets-isolamento-privilegio]] — Referência cruzada direta com bloodhound-governanca-tier-zero-high-value-assets-isolamento-privilegio.

## Fontes
- [CNCF Paralus Official GitHub — Zero-Trust Kubernetes Access Manager](https://raw.githubusercontent.com/paralus/paralus/main/README.md) — documentação oficial do Paralus cobrindo RBAC multi-cluster, SSO/OIDC, JIT ServiceAccounts e pctl; consultado em 2026-10-03.
- [Paralus Official Documentation — Zero Trust & Architecture](https://www.paralus.io/docs/) — guia oficial de arquitetura, Relay Agent, Projects, Roles e operação do Paralus; consultado em 2026-10-03.
- [Paralus Documentation — Audit Logs](https://www.paralus.io/docs/usage/audit-logs) — documentação oficial de System Audit Logs e Kubectl/Relay Audit Logs; consultado em 2026-10-03.
