---
id: software.seguranca.tranche10.000995
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

# Peirates: Escapes de Container e Comprometimento de Nó (**`attack-pod-hostpath-mount`**, **`leakyvessels` CVE-2024-21626**, **`hostpid-breakout`** e **`docker-socket-breakout`**)

## Em uma frase
A seção `Compromise and node operations` (`20` a `33`) do Peirates reúne uma coleção abrangente de módulos de **Container Escape e Escalação para o Nó Host**!

## Por que importa
Primeiro, se a ServiceAccount atual tiver permissão para criar Pods em um namespace que não aplica o perfil **Pod Security Standards `restricted`**, o comando **`attack-pod-hostpath-mount` (`20`)** cria um novo Pod montando a raiz `/` do nó host via volume `hostPath` para comprometer o servidor subjacente!

## Como funciona
Segundo, se o próprio container onde o Peirates já está rodando tiver más configurações ou um runtime vulnerável, o comando **`container-escape-scan` (`25`)** verifica todos os pré-requisitos para os escapes: **`leakyvessels` (`23`, `CVE-2024-21626` — vazamento de file descriptor no `runc` via `WORKDIR /proc/self/fd/N`)**, **`hostpid-breakout` (`24` — entrada no namespace do nó via `nsenter` a partir de um container `privileged` + `hostPID`)**, **`docker-socket-breakout` (`26`)** e **`hostroot-breakout` (`27`)**!

## Exemplo
```bash
# Executar o scanner de pre-requisitos de escape de container do Peirates em modo one-shot (-m)
peirates -m 'container-escape-scan'
```

## Limites e trade-offs
Observe a presença do módulo **`leakyvessels` (`23`)** para a vulnerabilidade crítica **`CVE-2024-21626`** (descoberta na família de falhas *Leaky Vessels* do `runc`): versões do `runc <= 1.1.11` vazavam um descritor de arquivo aberto apontando para `/sys/fs/cgroup` do host durante a inicialização do container, permitindo escapar para o sistema de arquivos do host! Mantenha sempre o `runc` (>= `1.1.12`) e o `containerd` atualizados em todos os nós.

## Como verificar
Combine o `container-escape-scan` do Peirates com o `cdk eva --full` para validar que suas políticas de admissão (`PodSecurity` `restricted`) bloqueiam qualquer criação de Pod com `hostPath`, `hostPID`, `hostNetwork` ou `privileged`.

## Conexões
- [[peirates-execucao-remota-pods-exec-via-api-exec-via-kubelet-10250]] — Veja também: Peirates: Movimentação Lateral e Execução Remota em Pods via **`exec-via-api` (`21`)** e **Kubelet API (`exec-via-kubelet` `22` na Porta `10250`)**.
- [[peirates-escapes-avancados-core-pattern-ptrace-hostlog-symlink]] — Veja também: Peirates: Técnicas Avançadas de Escape (**`hostproc-core-pattern-breakout` `29`**, **`hostpid-ptrace-breakout` `32`** e **`hostlog-symlink-read` `33`**).
- [[peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos]] — Referência cruzada direta com peirates-arquitetura-pentest-kubernetes-serviceaccount-tokens-contextos.
- [[cdk-escapes-cgroups-release-agent-userns-cve-2022-0492-lxcfs-procfs]] — Referência cruzada direta com cdk-escapes-cgroups-release-agent-userns-cve-2022-0492-lxcfs-procfs.

## Fontes
- [Peirates Official GitHub — Kubernetes Penetration Testing & Privilege Escalation Tool](https://raw.githubusercontent.com/inguardians/peirates/main/README.md) — repositório oficial do Peirates (InGuardians) cobrindo arquitetura, imagem `bustakube/alpine-peirates` e compilação multi-arquitetura; consultado em 2026-10-03.
- [Peirates Official Main Menu Command Reference (`docs/commands/README.md`)](https://raw.githubusercontent.com/inguardians/peirates/main/docs/commands/README.md) — referência oficial de todos os comandos do Peirates cobrindo `sa-menu`, `secret-to-sa`, `aws-get-token`, `gcp-get-token`, `exec-via-kubelet`, `leakyvessels`, `nodefs-steal-secrets` e `kubectl-try-all`; consultado em 2026-10-03.
- [Peirates Official Go Module Specification (`go.mod` — `k8s.io/client-go` & `k8s.io/kubectl`)](https://raw.githubusercontent.com/inguardians/peirates/main/go.mod) — especificação oficial das dependências do Peirates em Go incluindo `k8s.io/kubectl`, `k8s.io/client-go` e `aws-sdk-go`; consultado em 2026-10-03.
