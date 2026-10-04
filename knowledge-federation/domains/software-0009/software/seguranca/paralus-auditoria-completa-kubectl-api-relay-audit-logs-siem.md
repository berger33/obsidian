---
id: software.seguranca.tranche05.000448
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

# CNCF Paralus: Trilhas de Auditoria Imutáveis (`System Audit Logs` e `Kubectl / Relay Audit Logs`) para Conformidade e SIEM

## Em uma frase
O Paralus registra automaticamente duas trilhas de auditoria granulares: **System Audit Logs** (quem fez login, quem criou projetos, alterou grupos, importou clusters ou baixou um `kubeconfig`) e **Relay / Kubectl Audit Logs** (cada comando `kubectl` e chamada à API Kubernetes executada por cada usuário em qualquer cluster da frota).

## Por que importa
Para conformidade com PCI-DSS, SOC 2, ISO 27001 e investigações forenses, não basta saber que *"alguém com o certificado de admin deletou um Secret ou abriu um `kubectl exec` no pod de pagamentos"*; o Paralus atribui a ação nominalmente ao e-mail corporativo exato do usuário autenticado via OIDC.

## Como funciona
Cada evento de auditoria de `kubectl` captura o carimbo de tempo, o usuário real (`user`), o projeto, o nome do cluster, o namespace, o verbo da API Kubernetes (`get`, `list`, `create`, `delete`, `exec`, `port-forward`), o recurso/URL invocado e o código de resposta, permitindo filtragem por cluster, usuário ou intervalo de tempo e exportação para SIEM.

## Exemplo
```bash
# Consultar via API REST do Paralus os logs de auditoria de comandos kubectl executados nas últimas 24h
curl -sS "https://paralus.internal.corp/api/v1/audit/relay?project=payments-platform&time_from=24h" \
  -H "X-Paralus-API-KeyID: ${PARALUS_KEY_ID}" \
  -H "X-Paralus-API-Secret: ${PARALUS_SECRET}" | jq .
```

## Limites e trade-offs
Se os engenheiros ainda tiverem acesso direto à porta `6443` do `kube-apiserver` usando credenciais nativas da nuvem (ex.: `aws eks update-kubeconfig` direto) sem passar pelo Relay do Paralus, essas ações contornarão o `Relay Audit Log` do Paralus.

## Como verificar
Feche o acesso direto de usuários finais ao `kube-apiserver` e valide na aba *Audit Logs -> Kubectl* que 100% dos comandos `kubectl get` e `kubectl exec` aparecem atribuídos ao usuário SSO.

## Conexões
- [[paralus-automacao-cli-pctl-gitops-rbac-as-code-ci-cd]] — Veja também: CNCF Paralus: Automação Declarativa (*RBAC-as-Code*) com a CLI `pctl` e API REST em Pipelines GitOps.
- [[paralus-custom-roles-restricao-verbs-exec-portforward-secrets]] — Veja também: CNCF Paralus: Criação de `Custom Roles` Restritivas (Bloqueio de `pods/exec`, `pods/portforward` e Leitura de `secrets`).
- [[paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager]] — Referência cruzada direta com paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager.
- [[paralus-kubeconfig-dinamico-just-in-time-serviceaccounts-revogacao]] — Referência cruzada direta com paralus-kubeconfig-dinamico-just-in-time-serviceaccounts-revogacao.
- [[auditd-arquitetura-linux-audit-kernel-auditctl-augenrules]] — Referência cruzada direta com auditd-arquitetura-linux-audit-kernel-auditctl-augenrules.

## Fontes
- [CNCF Paralus Official GitHub — Zero-Trust Kubernetes Access Manager](https://raw.githubusercontent.com/paralus/paralus/main/README.md) — documentação oficial do Paralus cobrindo RBAC multi-cluster, SSO/OIDC, JIT ServiceAccounts e pctl; consultado em 2026-10-03.
- [Paralus Official Documentation — Zero Trust & Architecture](https://www.paralus.io/docs/) — guia oficial de arquitetura, Relay Agent, Projects, Roles e operação do Paralus; consultado em 2026-10-03.
- [Paralus Documentation — Audit Logs](https://www.paralus.io/docs/usage/audit-logs) — documentação oficial de System Audit Logs e Kubectl/Relay Audit Logs; consultado em 2026-10-03.
