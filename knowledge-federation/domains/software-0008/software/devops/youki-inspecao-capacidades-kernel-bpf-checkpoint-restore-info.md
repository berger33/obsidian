---
id: software.devops.tranche08.000740
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/youki-dev/youki/main/README.md", "https://youki-dev.github.io/youki/user/basic_setup.html", "https://github.com/youki-dev/youki"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Youki: diagnóstico de capacidades do host (CAP_BPF, CAP_PERFMON, CAP_CHECKPOINT_RESTORE) e cgroups via youki info

## Em uma frase
O subcomando `youki info` inspeciona e reporta em um único resumo a versão do runtime, commit, release do kernel, arquitetura, memória total, modo de cgroup (`unified`/hybrid/legacy), status de todos os 7 namespaces Linux e disponibilidade das capabilities modernas `CAP_BPF`, `CAP_PERFMON` e `CAP_CHECKPOINT_RESTORE`.

## Por que importa
Antes de executar workloads avançados que dependem de observabilidade eBPF, profiling de performance ou checkpoint/restore de containers (CRIU) em um nó Linux, o operador precisa verificar rapidamente se o kernel do host suporta os 7 namespaces e as capabilities granulares introduzidas nos kernels Linux modernos. Os detalhes do ambiente no README oficial do `youki` demonstram a saída completa de `./youki info`.

## Como funciona
Quando o operador executa `./youki info`, o binário consulta as interfaces do sistema operacional (`/proc`, `/sys/fs/cgroup`, `uname`) e imprime um relatório estruturado contendo: `Version`, `Commit`, `Kernel-Release`, `Kernel-Version`, `Architecture`, `Operating System`, `Cores`, `Total Memory`, `Cgroup setup` (ex.: `unified` para cgroup v2), `Cgroup mounts`, o status individual de habilitação dos sete `Namespaces` (`mount`, `uts`, `ipc`, `user`, `pid`, `network`, `cgroup`) e a disponibilidade no kernel das três `Capabilities` modernas (`CAP_BPF`, `CAP_PERFMON` e `CAP_CHECKPOINT_RESTORE`).

## Exemplo
```bash
# Verificar no host se todos os 7 namespaces e as capabilities CAP_BPF, CAP_PERFMON e CAP_CHECKPOINT_RESTORE estão disponíveis
./youki info | grep -E "Cgroup setup|mount|uts|ipc|user|pid|network|cgroup|CAP_"
```

## Limites e trade-offs
Se o comando `./youki info` indicar que o namespace `user` não está habilitado no kernel do host ou está bloqueado por políticas sysctl da distribuição (`kernel.unprivileged_userns_clone=0` / `user.max_user_namespaces=0`), a execução de containers em modo rootless (`youki spec --rootless` / `youki run`) falhará até que os user namespaces sejam habilitados no sistema operacional.

## Como verificar
Execute `./youki info` e confirme que todos os sete namespaces reportam `enabled` e que as três capabilities (`CAP_BPF`, `CAP_PERFMON`, `CAP_CHECKPOINT_RESTORE`) reportam `available`.

## Conexões
- [[youki-integracao-containerd-kubernetes-e2e-producao]] — Veja também: Youki: validação nos testes end-to-end do containerd e uso como runtime em clusters Kubernetes.
- [[youki-runtime-oci-rust-seguranca-memoria]] — Referência cruzada direta com youki-runtime-oci-rust-seguranca-memoria.
- [[youki-containers-rootless-integracao-docker-podman]] — Referência cruzada direta com youki-containers-rootless-integracao-docker-podman.
- [[inspektor-requisitos-kernel-linux-btf-core-cilium-ebpf]] — Referência cruzada direta com inspektor-requisitos-kernel-linux-btf-core-cilium-ebpf.

## Fontes
- [Youki GitHub — README.md (OCI Runtime in Rust, Hyperfine Benchmark, Lifecycle, Rootless & Docker/Podman)](https://raw.githubusercontent.com/youki-dev/youki/main/README.md) — README oficial do youki documentando motivação de segurança de memória em Rust, benchmark hyperfine frente a runc e crun, compilação com just, ciclo de vida OCI, modo rootless e youki info; consultado em 2026-10-03.
- [Youki Official User & Developer Documentation — Basic Setup & Architecture](https://youki-dev.github.io/youki/user/basic_setup.html) — Documentação oficial do projeto youki (CNCF Sandbox) e crate associada youki-dev/oci-spec-rs; consultado em 2026-10-03.
- [Youki — Official GitHub Repository](https://github.com/youki-dev/youki) — Repositório oficial Apache-2.0 do runtime OCI youki em Rust; consultado em 2026-10-03.
