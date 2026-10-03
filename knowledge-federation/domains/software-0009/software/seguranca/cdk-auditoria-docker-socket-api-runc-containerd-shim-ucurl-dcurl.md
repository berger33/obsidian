---
id: software.seguranca.tranche10.000984
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

# CDK: Comprometimento via **Docker Unix Socket (`docker.sock`, `ucurl`)**, **Docker TCP API (`:2375`, `dcurl`)**, `runc` (`CVE-2019-5736`) e `containerd-shim` (`CVE-2020-15257`)

## Em uma frase
Montar o socket Unix do daemon Docker (**`/var/run/docker.sock`**) dentro de um container (comum em runners de CI/CD mal projetados que fazem *"Docker-in-Docker"* via socket binding ou agentes de monitoramento) equivale a entregar acesso **Root irrestrito sobre o servidor host inteiro** para qualquer processo dentro daquele container!

## Por que importa
O CDK possui tanto módulos de diagnóstico e exploração (**`cdk run docker-sock-check`**, **`cdk run docker-sock-pwn`**, **`cdk run docker-api-pwn`**) quanto os utilitários embutidos **`cdk ucurl`** (cliente HTTP que fala diretamente com sockets Unix como `/var/run/docker.sock` sem precisar do binário `curl --unix-socket`!) e **`cdk dcurl`** (para a API HTTP do Docker na porta `2375`)!

## Como funciona
Adicionalmente, para containers rodando com `hostNetwork: true` sobre versões antigas do `containerd`, o módulo **`cdk run shim-pwn` (`CVE-2020-15257`)** audita sockets abstratos Unix (`@/containerd-shim/...`) acessíveis no namespace de rede do host!

## Exemplo
```bash
# Usar o cliente Unix Socket embutido do CDK (cdk ucurl) para consultar informacoes do daemon Docker caso /var/run/docker.sock esteja exposto
cdk ucurl get /var/run/docker.sock http://127.0.0.1/info ""
```

## Limites e trade-offs
Como substituir o perigoso mount de `/var/run/docker.sock` em pipelines de CI/CD que precisam construir imagens de container dentro do Kubernetes? Use construtores **Daemonless e Rootless em User-Space**, como **Kaniko**, **BuildKit Rootless** ou **Podman/Buildah**, que constroem e enviam imagens OCI para o registry sem jamais tocar no socket do runtime do nó!

## Como verificar
Monitore com **Tracee** ou **KubeArmor** qualquer tentativa de abertura (`openat` / `connect`) em `/var/run/docker.sock`, `/run/containerd/containerd.sock` ou `/var/run/crio/crio.sock` a partir de containers.

## Conexões
- [[cdk-escapes-cgroups-release-agent-userns-cve-2022-0492-lxcfs-procfs]] — Veja também: CDK: Anatomia de Escapes via **Cgroups v1 `release_agent` (`mount-cgroup`)**, **User Namespaces (`CVE-2022-0492`)**, `rewrite-cgroup-devices`, `mount-procfs` e `lxcfs-rw`.
- [[cdk-pos-exploracao-kubernetes-kcurl-ectl-secrets-rbac-service-probe]] — Veja também: CDK para **Kubernetes**: Clientes Nativos **`cdk kcurl`** (API Server), **`cdk ectl`** (`etcd`), Dump de `Secrets`/`ConfigMaps` e Descoberta de Componentes.
- [[cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate]] — Referência cruzada direta com cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate.
- [[peirates-escapes-containers-docker-socket-hostpath-hostpid-leakyvessels]] — Referência cruzada direta com peirates-escapes-containers-docker-socket-hostpath-hostpid-leakyvessels.

## Fontes
- [CDK Official GitHub — Zero-Dependency Container Penetration Toolkit (`evaluate`, `run` & `tool` Modules)](https://raw.githubusercontent.com/cdk-team/CDK/main/README.md) — documentação oficial do CDK cobrindo o avaliador `cdk evaluate`, módulos de escape (capabilities, cgroups, userns, docker.sock, runc, containerd-shim) e utilitários (`kcurl`, `ucurl`, `ectl`, `probe`); consultado em 2026-10-03.
- [CDK Official Go Module Specification (`go.mod`)](https://raw.githubusercontent.com/cdk-team/CDK/main/go.mod) — especificação oficial de pacotes Go do CDK (`containerd`, `gopsutil`, `tcell`, `golang.org/x/sys`); consultado em 2026-10-03.
