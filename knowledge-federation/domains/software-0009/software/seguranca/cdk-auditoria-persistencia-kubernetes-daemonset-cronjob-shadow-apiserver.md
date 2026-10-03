---
id: software.seguranca.tranche10.000988
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
fontes: ["https://raw.githubusercontent.com/cdk-team/CDK/main/README.md", "https://raw.githubusercontent.com/cdk-team/CDK/main/go.mod"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Análise de Técnicas de **Persistência em Kubernetes** Mapeadas pelo CDK (`k8s-backdoor-daemonset`, `k8s-cronjob`, `k8s-shadow-apiserver` e `CVE-2020-8554`)

## Em uma frase
Para que analistas de **SOC, DFIR e Threat Hunting em Kubernetes** saibam o que procurar durante uma investigação de comprometimento de cluster, é essencial estudar as quatro técnicas de **Persistência e Interceptação em Kubernetes** documentadas na matriz MITRE ATT&CK / CDK:

## Por que importa
A primeira é **`k8s-backdoor-daemonset`**: como um `DaemonSet` garante que uma cópia do Pod rode automaticamente em **todos os nós atuais e futuros do cluster**, atacantes que conquistam permissão de criação de workloads implantam um DaemonSet camuflado no namespace `kube-system`. A segunda é **`k8s-cronjob`**: agenda um `CronJob` periódico que reabre um canal de comando se o Pod original for morto.

## Como funciona
A terceira — e mais furtiva! — é **`k8s-shadow-apiserver`**: implanta um segundo Pod de `kube-apiserver` estático no nó mestre apontando para o mesmo `etcd`, mas com flags de autenticação anônima (`--anonymous-auth=true`) e **auditoria desativada**! E a quarta é o ataque de Man-in-the-Middle interno **`k8s-mitm-clusterip` (`CVE-2020-8554`)**, onde alguém com permissão de criar/editar um `Service` define `externalIPs` para sequestrar tráfego dentro do cluster!

## Exemplo
```bash
# Comandos de Threat Hunting (Blue Team) com kubectl para auditar DaemonSets, CronJobs, ExternalIPs (CVE-2020-8554) e Pods de API Server
kubectl get daemonsets,cronjobs -A
kubectl get svc -A -o json | jq -r '.items[] | select(.spec.externalIPs != null) | "\(.metadata.namespace)/\(.metadata.name): \(.spec.externalIPs)"'
kubectl get pods -n kube-system -l component=kube-apiserver -o wide
```

## Limites e trade-offs
Como bloquear preventivamente o vetor **`CVE-2020-8554` (`spec.externalIPs`)** e a criação de `DaemonSets` não-autorizados? Usando uma política **OPA Gatekeeper / Kyverno** (ou o webhook oficial `externalip-webhook`) que proíbe qualquer usuário que não seja a pipeline de infraestrutura de usar o campo `spec.externalIPs` em objetos `Service`!

## Como verificar
Monitore continuamente a criação de novos `DaemonSets`, `CronJobs` e `Static Pods` (`/etc/kubernetes/manifests/`) com o **Tracee** e **Velociraptor**.

## Conexões
- [[cdk-auditoria-cloud-metadata-imds-ak-leakage-istio-route-localnet]] — Veja também: CDK: Auditoria de **Cloud Metadata API (IMDS)**, Varredura de Chaves (**`ak-leakage`**), Sidecar **Istio (`istio-check`)** e `route_localnet` (`CVE-2020-8558`).
- [[cdk-entrega-binarios-containers-restritos-dev-tcp-thin-builds-deteccao]] — Veja também: Análise de Entrega *Fileless/In-Band* em Containers (`/dev/tcp`, `thin` builds) e Como **Bloquear na Camada de Runtime (`KubeArmor` / `Tracee`)**.
- [[cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate]] — Referência cruzada direta com cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate.
- [[cdk-pos-exploracao-kubernetes-kcurl-ectl-secrets-rbac-service-probe]] — Referência cruzada direta com cdk-pos-exploracao-kubernetes-kcurl-ectl-secrets-rbac-service-probe.

## Fontes
- [CDK Official GitHub — Zero-Dependency Container Penetration Toolkit (`evaluate`, `run` & `tool` Modules)](https://raw.githubusercontent.com/cdk-team/CDK/main/README.md) — documentação oficial do CDK cobrindo o avaliador `cdk evaluate`, módulos de escape (capabilities, cgroups, userns, docker.sock, runc, containerd-shim) e utilitários (`kcurl`, `ucurl`, `ectl`, `probe`); consultado em 2026-10-03.
- [CDK Official Go Module Specification (`go.mod`)](https://raw.githubusercontent.com/cdk-team/CDK/main/go.mod) — especificação oficial de pacotes Go do CDK (`containerd`, `gopsutil`, `tcell`, `golang.org/x/sys`); consultado em 2026-10-03.
