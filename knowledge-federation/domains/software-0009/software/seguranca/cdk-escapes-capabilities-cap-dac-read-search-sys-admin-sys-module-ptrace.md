---
id: software.seguranca.tranche10.000982
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

# CDK & **Linux Capabilities Perigosas**: Auditoria e Exploração de **`CAP_DAC_READ_SEARCH`** (`open_by_handle_at`), **`CAP_SYS_MODULE`**, **`CAP_SYS_ADMIN`** e **`CAP_SYS_PTRACE`**

## Em uma frase
Um erro clássico de configuração de Docker e Kubernetes é conceder capacidades Linux perigosas no `securityContext.capabilities.add` pensando que "não é tão grave quanto rodar com `privileged: true`". Na realidade, várias capacidades individuais equivalem a **Root Total no Host (Container Escape)** — e o `cdk eva` + `cdk run` demonstram exatamente o impacto de cada uma!

## Por que importa
Veja os quatro módulos do CDK para capacidades críticas: **(1) `CAP_DAC_READ_SEARCH` (`cdk run cap-dac-read-search`)** — explora a syscall **`open_by_handle_at(2)`** (técnica *Shocker*) para atravessar a barreira do `chroot`/mount namespace do container e ler qualquer arquivo do sistema de arquivos do host (como `/etc/shadow` ou chaves SSH do nó!); **(2) `CAP_SYS_MODULE`** — permite carregar um módulo de kernel (`.ko`) diretamente no kernel compartilhado do host; **(3) `CAP_SYS_PTRACE` (`cdk run check-ptrace`)** — quando combinado com `hostPID: true`, permite injetar shellcode em processos do host via `ptrace(2)`; e **(4) `CAP_SYS_ADMIN`** — permite montar dispositivos de bloco do host (`cdk run mount-disk`), `procfs` ou `cgroups`!

## Como funciona
Nunca conceda `CAP_SYS_ADMIN`, `CAP_SYS_MODULE`, `CAP_DAC_READ_SEARCH` ou `CAP_SYS_PTRACE` a containers de aplicação!

## Exemplo
```bash
# Demonstrar em ambiente de laboratorio como a capacidade CAP_DAC_READ_SEARCH permite ler arquivos do host via open_by_handle_at
cdk eva
cdk run --list
```

## Limites e trade-offs
Como blindar seus Pods Kubernetes contra todos esses vetores de Capabilities? No manifesto `securityContext` do container, defina sempre **`allowPrivilegeEscalation: false`** e **`capabilities: { drop: ["ALL"] }`** (adicionando de volta no máximo `NET_BIND_SERVICE` se o binário realmente precisar escutar abaixo da porta 1024, embora no Kubernetes seja melhor escutar na porta `8080` e mapear no `Service`!).

## Como verificar
Valide estaticamente nos manifestos YAML com o **KICS (`kics scan -t Kubernetes`)** que nenhum Pod adiciona essas capacidades proibidas.

## Conexões
- [[cdk-arquitetura-container-penetration-toolkit-zero-dependency-evaluate]] — Veja também: **CDK (`cdk-team/CDK`)**: Arquitetura do Toolkit **Zero-Dependency** em Go para Auditoria de Segurança e Pós-Exploração em Containers Slim/Distroless.
- [[cdk-escapes-cgroups-release-agent-userns-cve-2022-0492-lxcfs-procfs]] — Veja também: CDK: Anatomia de Escapes via **Cgroups v1 `release_agent` (`mount-cgroup`)**, **User Namespaces (`CVE-2022-0492`)**, `rewrite-cgroup-devices`, `mount-procfs` e `lxcfs-rw`.

## Fontes
- [CDK Official GitHub — Zero-Dependency Container Penetration Toolkit (`evaluate`, `run` & `tool` Modules)](https://raw.githubusercontent.com/cdk-team/CDK/main/README.md) — documentação oficial do CDK cobrindo o avaliador `cdk evaluate`, módulos de escape (capabilities, cgroups, userns, docker.sock, runc, containerd-shim) e utilitários (`kcurl`, `ucurl`, `ectl`, `probe`); consultado em 2026-10-03.
- [CDK Official Go Module Specification (`go.mod`)](https://raw.githubusercontent.com/cdk-team/CDK/main/go.mod) — especificação oficial de pacotes Go do CDK (`containerd`, `gopsutil`, `tcell`, `golang.org/x/sys`); consultado em 2026-10-03.
