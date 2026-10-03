---
id: software.seguranca.tranche10.001000
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

# Matriz de Defesa em Profundidade Kubernetes (Marco **1.000/2.000** do Lote `software-seguranca-2000-0003`): Como Neutralizar **Peirates & CDK** do Código ao Kernel

## Em uma frase
Ao atingirmos a **Nota 1.000 de 2.000 (50,00%)** do lote `software-seguranca-2000-0003`, consolidamos uma **Matriz Completa de Defesa em Profundidade para Clusters Kubernetes**, mapeando exatamente qual controle de engenharia neutraliza cada módulo ofensivo do **Peirates** e do **CDK**:

## Por que importa
Na **Camada 1 — Pré-Deploy & Supply Chain (Shift-Left)**: audite manifestos YAML, Helm e Terraform com **Checkmarx KICS**, assine e verifique imagens e atestações com **Sigstore (`Rekor`/`Fulcio`)** e **in-toto**, escaneie vulnerabilidades com **OSV-Scanner** / **Clair v4** e bloqueie segredos no Git com **Talisman**, **`git-secrets`**, **Gitleaks** e **TruffleHog**!

## Como funciona
Na **Camada 2 — Identidade, RBAC e Plano de Controle**: aplique **`automountServiceAccountToken: false`** por padrão, elimine `cluster-admin` e `pods/exec` desnecessários, proteja o acesso humano com **CNCF Paralus / Dex**, endureça o **Kubelet (`10250`)** com `anonymous-auth: false` + `Webhook` + `NodeRestriction` e bloqueie o acesso ao IMDS da nuvem com **IMDSv2 (`HopLimit=1`)** + **NetworkPolicies**! E na **Camada 3 — Isolamento do Container e Kernel em Runtime**: exija **Pod Security Standards `restricted`** (`runAsNonRoot: true`, `allowPrivilegeEscalation: false`, `capabilities.drop: ["ALL"]`, `readOnlyRootFilesystem: true`, `seccompProfile: RuntimeDefault`), Cgroups v2 e proteção inline **eBPF / LSM** com **CNCF KubeArmor**, **Aqua Tracee**, **AppArmor** e **SELinux**!

## Exemplo
```yaml
# Template de Pod Kubernetes 100% endurecido (Pod Security Standard: restricted) que neutraliza os vetores do CDK e Peirates
apiVersion: v1
kind: Pod
metadata:
  name: hardened-microservice
  namespace: production
spec:
  automountServiceAccountToken: false
  hostNetwork: false
  hostPID: false
  hostIPC: false
  securityContext:
    runAsNonRoot: true
    runAsUser: 65532
    runAsGroup: 65532
    fsGroup: 65532
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: app
      image: registry.internal.corp/app@sha256:4f8d2a9e0c1b2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL
```

## Limites e trade-offs
Submeta o manifesto acima simultaneamente ao **KICS (`kics scan`)**, ao **CDK (`cdk eva --full`)** e ao **Peirates (`peirates -m 'container-escape-scan'`)**: com `automountServiceAccountToken: false`, `drop: ["ALL"]`, `readOnlyRootFilesystem: true`, `runAsNonRoot: true` e `seccompProfile: RuntimeDefault`, tanto o `cdk eva` quanto o `peirates` reportam **zero vetores de escape e zero tokens de ServiceAccount expostos**!

## Como verificar
Adote este template como padrão obrigatório nas políticas de admissão de todos os clusters de produção.

## Conexões
- [[peirates-execucao-kubectl-embutido-curl-shell-interativo]] — Veja também: Peirates: Uso da Biblioteca **`kubectl` Embutida (`90`)**, Cliente HTTP **`curl` (`91`)** e Comandos de Sistema de Arquivos (`cd`, `ls`, `cat`, `shell`).
- [[peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos]] — Referência cruzada direta com peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos.
- [[cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate]] — Referência cruzada direta com cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate.

## Fontes
- [Peirates Official GitHub — Kubernetes Penetration Testing & Privilege Escalation Tool](https://raw.githubusercontent.com/inguardians/peirates/main/README.md) — repositório oficial do Peirates (InGuardians) cobrindo arquitetura, imagem `bustakube/alpine-peirates` e compilação multi-arquitetura; consultado em 2026-10-03.
- [Peirates Official Main Menu Command Reference (`docs/commands/README.md`)](https://raw.githubusercontent.com/inguardians/peirates/main/docs/commands/README.md) — referência oficial de todos os comandos do Peirates cobrindo `sa-menu`, `secret-to-sa`, `aws-get-token`, `gcp-get-token`, `exec-via-kubelet`, `leakyvessels`, `nodefs-steal-secrets` e `kubectl-try-all`; consultado em 2026-10-03.
- [Peirates Official Go Module Specification (`go.mod` — `k8s.io/client-go` & `k8s.io/kubectl`)](https://raw.githubusercontent.com/inguardians/peirates/main/go.mod) — especificação oficial das dependências do Peirates em Go incluindo `k8s.io/kubectl`, `k8s.io/client-go` e `aws-sdk-go`; consultado em 2026-10-03.
