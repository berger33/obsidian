---
id: software.seguranca.tranche10.000992
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/inguardians/peirates/main/README.md", "https://raw.githubusercontent.com/inguardians/peirates/main/docs/commands/README.md", "https://raw.githubusercontent.com/inguardians/peirates/main/go.mod"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Peirates: Coleta de Tokens (`list-secrets`, **`secret-to-sa`**), Prechecks **`set-auth-can-i`** e Força Bruta de Contextos (**`kubectl-try-all-until-success`**)

## Em uma frase
Em um cluster Kubernetes com dezenas de microsserviços e operadores, cada Pod frequentemente roda com uma `ServiceAccount` diferente — e uma única `ServiceAccount` com permissões excessivas (como um operador de CI/CD ou monitoramento) pode permitir comprometer todo o cluster.

## Por que importa
No Peirates, o fluxo de escalação via identidades funciona através dos comandos: **(1) `sa-menu` (`1`)** e **`ns-menu` (`2`)** — gerenciam as `ServiceAccounts` carregadas e alternam de namespace; **(2) `list-secrets` (`10`)** e **`secret-to-sa` (`11`)** — listam objetos `Secret` acessíveis no cluster e **importam tokens de ServiceAccount armazenados em Secrets diretamente para o chaveiro `sa-menu` do Peirates**!; e **(3) `set-auth-can-i` (`92`)** — configura verificações prévias de autorização RBAC (`SelfSubjectAccessReview`) antes de disparar comandos!

## Como funciona
Quando você já coletou 15 tokens de `ServiceAccount` diferentes no `sa-menu` e quer descobrir qual deles tem permissão para ler um segredo ou criar um Pod em `kube-system`, os comandos **`kubectl-try-all`** e **`kubectl-try-all-until-success`** testam a operação iterando automaticamente por todos os contextos armazenados!

## Exemplo
```text
# Fluxo no prompt interativo do Peirates: listar Secrets, importar um token para o sa-menu e testar permissoes em todos os contextos
[peirates]# list-secrets
[peirates]# secret-to-sa
[peirates]# kubectl-try-all get secrets -n kube-system
```

## Limites e trade-offs
Nota arquitetural importante do Kubernetes 1.24+: embora o Kubernetes tenha deixado de criar Secrets de token estático automaticamente para cada ServiceAccount (usando a *TokenRequest API* com tokens vinculados ao ciclo de vida do Pod), muitos clusters ainda mantêm Secrets do tipo `kubernetes.io/service-account-token` criados manualmente para integrações legadas de CI/CD — que têm validade infinita e são capturados por `secret-to-sa`!

## Como verificar
Audite e remova todos os Secrets legados do tipo `kubernetes.io/service-account-token` do seu cluster com `kubectl get secrets -A --field-selector type=kubernetes.io/service-account-token`.

## Conexões
- [[peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos]] — Veja também: **Peirates (`inguardians/peirates`)**: Arquitetura da Plataforma de Pentest Kubernetes, Gestão de **Múltiplos Contextos de `ServiceAccount` (`sa-menu`)** e Modo `-m`.
- [[peirates-coleta-credenciais-cloud-imds-aws-gcp-kops-s3-gcs]] — Veja também: Peirates na Nuvem (**AWS EKS / kOps & Google GKE**): Comandos **`aws-get-token`**, **`gcp-get-token`**, **`gcp-attack-kube-env`** e **`aws-attack-kops-1`**.
- [[peirates-roubo-credenciais-filesystem-no-nodefs-steal-secrets-cert-menu]] — Referência cruzada direta com peirates-roubo-credenciais-filesystem-no-nodefs-steal-secrets-cert-menu.

## Fontes
- [Peirates Official GitHub — Kubernetes Penetration Testing & Privilege Escalation Tool](https://raw.githubusercontent.com/inguardians/peirates/main/README.md) — repositório oficial do Peirates (InGuardians) cobrindo arquitetura, imagem `bustakube/alpine-peirates` e compilação multi-arquitetura; consultado em 2026-10-03.
- [Peirates Official Main Menu Command Reference (`docs/commands/README.md`)](https://raw.githubusercontent.com/inguardians/peirates/main/docs/commands/README.md) — referência oficial de todos os comandos do Peirates cobrindo `sa-menu`, `secret-to-sa`, `aws-get-token`, `gcp-get-token`, `exec-via-kubelet`, `leakyvessels`, `nodefs-steal-secrets` e `kubectl-try-all`; consultado em 2026-10-03.
- [Peirates Official Go Module Specification (`go.mod` — `k8s.io/client-go` & `k8s.io/kubectl`)](https://raw.githubusercontent.com/inguardians/peirates/main/go.mod) — especificação oficial das dependências do Peirates em Go incluindo `k8s.io/kubectl`, `k8s.io/client-go` e `aws-sdk-go`; consultado em 2026-10-03.
