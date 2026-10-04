---
id: software.seguranca.tranche10.000996
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

# Peirates: Técnicas Avançadas de Escape (**`hostproc-core-pattern-breakout` `29`**, **`hostpid-ptrace-breakout` `32`** e **`hostlog-symlink-read` `33`**)

## Em uma frase
Três módulos avançados do Peirates (`29`, `32` e `33` em `docs/commands/README.md`) demonstram vetores sutis de escape de container que muitos engenheiros de infraestrutura desconhecem!

## Por que importa
O comando **`hostproc-core-pattern-breakout` (`29`)** explora containers onde `/proc/sys/kernel/core_pattern` do host está montado com permissão de escrita: no Linux, quando `core_pattern` começa com o caractere pipe **`|/caminho/no/host/script`**, toda vez que qualquer processo sofre um crash (`SIGSEGV` / `SIGABRT`), **o kernel Linux executa o binário indicado após o `|` como `root` no namespace do host**!

## Como funciona
O comando **`hostpid-ptrace-breakout` (`32`)** obtém um shell no nó a partir de um container não-privilegiado que possui apenas `hostPID: true` + `CAP_SYS_PTRACE` anexando-se a um processo do host; e o comando **`hostlog-symlink-read` (`33`)** explora montagens graváveis de **`/var/log`** do host (comuns em agentes coletores de logs!) criando um **link simbólico (`symlink`)** dentro do diretório de logs do container apontando para um arquivo sensível do host (ex.: `/etc/shadow` ou `/etc/kubernetes/admin.conf`) e lendo-o através da API de logs do Kubelet / `kubectl logs` (`CVE-2018-1002102` / *Log Mount Symlink Traversal*)!

## Exemplo
```bash
# Verificar no host se o /proc/sys/kernel/core_pattern esta protegido e se containers comuns o enxergam como Read-Only (ro)
cat /proc/sys/kernel/core_pattern
mount | grep "/proc/sys"
# Em um container seguro, /proc/sys DEVE estar montado como ro (Read-Only):
# proc on /proc/sys type proc (ro,nosuid,nodev,noexec,relatime)
```

## Limites e trade-offs
Preste muita atenção ao vetor **`hostlog-symlink-read` (`33`)**: nunca monte `/var/log` do host com permissão de escrita (`readOnly: false`) em containers de aplicação! Mesmo agentes DaemonSet de coleta de logs (Fluent Bit, Vector, Promtail) devem montar `/var/log/pods` estritamente como **`readOnly: true`**!

## Como verificar
Monitore com **Tracee** (`core_pattern_modification` e `ptrace_code_injection`) qualquer tentativa de escrita em `core_pattern` ou uso de `ptrace` em produção.

## Conexões
- [[peirates-escapes-containers-docker-socket-hostpath-hostpid-leakyvessels]] — Veja também: Peirates: Escapes de Container e Comprometimento de Nó (**`attack-pod-hostpath-mount`**, **`leakyvessels` CVE-2024-21626**, **`hostpid-breakout`** e **`docker-socket-breakout`**).
- [[peirates-roubo-credenciais-filesystem-no-nodefs-steal-secrets-cert-menu]] — Veja também: Peirates Pós-Escape: Coleta Automatizada de Credenciais do Nó (**`nodefs-steal-secrets` `30`**) e Contextos de Certificados TLS (**`cert-menu` `9`**).
- [[cdk-escapes-cgroups-release-agent-userns-cve-2022-0492-lxcfs-procfs]] — Referência cruzada direta com cdk-escapes-cgroups-release-agent-userns-cve-2022-0492-lxcfs-procfs.

## Fontes
- [Peirates Official GitHub — Kubernetes Penetration Testing & Privilege Escalation Tool](https://raw.githubusercontent.com/inguardians/peirates/main/README.md) — repositório oficial do Peirates (InGuardians) cobrindo arquitetura, imagem `bustakube/alpine-peirates` e compilação multi-arquitetura; consultado em 2026-10-03.
- [Peirates Official Main Menu Command Reference (`docs/commands/README.md`)](https://raw.githubusercontent.com/inguardians/peirates/main/docs/commands/README.md) — referência oficial de todos os comandos do Peirates cobrindo `sa-menu`, `secret-to-sa`, `aws-get-token`, `gcp-get-token`, `exec-via-kubelet`, `leakyvessels`, `nodefs-steal-secrets` e `kubectl-try-all`; consultado em 2026-10-03.
- [Peirates Official Go Module Specification (`go.mod` — `k8s.io/client-go` & `k8s.io/kubectl`)](https://raw.githubusercontent.com/inguardians/peirates/main/go.mod) — especificação oficial das dependências do Peirates em Go incluindo `k8s.io/kubectl`, `k8s.io/client-go` e `aws-sdk-go`; consultado em 2026-10-03.
