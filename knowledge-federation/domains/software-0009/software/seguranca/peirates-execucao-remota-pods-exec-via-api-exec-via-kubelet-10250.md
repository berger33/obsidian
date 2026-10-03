---
id: software.seguranca.tranche10.000994
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

# Peirates: Movimentação Lateral e Execução Remota em Pods via **`exec-via-api` (`21`)** e **Kubelet API (`exec-via-kubelet` `22` na Porta `10250`)**

## Em uma frase
Quando um atacante dentro de um cluster Kubernetes quer executar comandos em outros Pods (para roubar seus tokens de ServiceAccount em `/var/run/secrets/...` ou acessar bancos de dados que só aceitam conexões daqueles Pods), existem dois caminhos de execução remota que o Peirates automatiza: **`exec-via-api` (`21`)** e **`exec-via-kubelet` (`22`)**!

## Por que importa
Com **`exec-via-api` (`21`)**, o Peirates utiliza a sub-rota oficial `pods/exec` do **Kubernetes API Server** (caso a ServiceAccount atual possua o verbo `create` no recurso `pods/exec`).

## Como funciona
Mas o que acontece quando o RBAC do API Server está bem configurado, porém o administrador do cluster cometeu o erro fatal de deixar o daemon **`kubelet` (porta TCP `10250`)** dos nós Worker com **`--anonymous-auth=true` e `--authorization-mode=AlwaysAllow`** (ou acessível sem verificação de permissão)? O comando **`exec-via-kubelet` (`22`)** conecta **diretamente na porta `10250` do Kubelet do nó Worker** (`/run/<namespace>/<pod>/<container>`), executando comandos em qualquer container daquele nó **passando completamente por fora do Kubernetes API Server e dos logs de auditoria do Control Plane**!

## Exemplo
```bash
# Auditar na configuracao de todos os nos do cluster se o Kubelet (porta 10250) exige autorizacao Webhook e desativa acesso anonimo
ps -ef | grep kubelet | grep -E "anonymous-auth|authorization-mode"
# Configuracao segura obrigatoria no config.yaml do Kubelet:
# authentication.anonymous.enabled: false
# authorization.mode: Webhook
```

## Limites e trade-offs
Compreenda por que uma falha de autenticação na porta `10250` do **Kubelet** é classificada como **Crítica (CVSS 9.8+)** em qualquer auditoria CIS Kubernetes Benchmark: como nos nós onde roda o Control Plane (ou onde rodam DaemonSets privilegiados como CNI/CSI) existem Pods com permissões de `cluster-admin`, executar `exec-via-kubelet` contra um desses Pods entrega o domínio total do cluster imediatamente!

## Como verificar
Além de `authentication.anonymous.enabled: false` e `authorization.mode: Webhook` no Kubelet, aplique regras de firewall / NetworkPolicy bloqueando conexões de Pods para a porta `10250` dos nós.

## Conexões
- [[peirates-coleta-credenciais-cloud-imds-aws-gcp-kops-s3-gcs]] — Veja também: Peirates na Nuvem (**AWS EKS / kOps & Google GKE**): Comandos **`aws-get-token`**, **`gcp-get-token`**, **`gcp-attack-kube-env`** e **`aws-attack-kops-1`**.
- [[peirates-escapes-containers-docker-socket-hostpath-hostpid-leakyvessels]] — Veja também: Peirates: Escapes de Container e Comprometimento de Nó (**`attack-pod-hostpath-mount`**, **`leakyvessels` CVE-2024-21626**, **`hostpid-breakout`** e **`docker-socket-breakout`**).
- [[peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos]] — Referência cruzada direta com peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos.
- [[peirates-descoberta-interna-pods-mounts-tcpscan-enumerate-dns]] — Referência cruzada direta com peirates-descoberta-interna-pods-mounts-tcpscan-enumerate-dns.
- [[cdk-pos-exploracao-kubernetes-kcurl-ectl-secrets-rbac-service-probe]] — Referência cruzada direta com cdk-pos-exploracao-kubernetes-kcurl-ectl-secrets-rbac-service-probe.

## Fontes
- [Peirates Official GitHub — Kubernetes Penetration Testing & Privilege Escalation Tool](https://raw.githubusercontent.com/inguardians/peirates/main/README.md) — repositório oficial do Peirates (InGuardians) cobrindo arquitetura, imagem `bustakube/alpine-peirates` e compilação multi-arquitetura; consultado em 2026-10-03.
- [Peirates Official Main Menu Command Reference (`docs/commands/README.md`)](https://raw.githubusercontent.com/inguardians/peirates/main/docs/commands/README.md) — referência oficial de todos os comandos do Peirates cobrindo `sa-menu`, `secret-to-sa`, `aws-get-token`, `gcp-get-token`, `exec-via-kubelet`, `leakyvessels`, `nodefs-steal-secrets` e `kubectl-try-all`; consultado em 2026-10-03.
- [Peirates Official Go Module Specification (`go.mod` — `k8s.io/client-go` & `k8s.io/kubectl`)](https://raw.githubusercontent.com/inguardians/peirates/main/go.mod) — especificação oficial das dependências do Peirates em Go incluindo `k8s.io/kubectl`, `k8s.io/client-go` e `aws-sdk-go`; consultado em 2026-10-03.
