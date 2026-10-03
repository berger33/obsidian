---
id: software.devops.tranche08.000724
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
fontes: ["https://raw.githubusercontent.com/google/gvisor/master/README.md", "https://gvisor.dev/docs/architecture_guide/intro/", "https://github.com/google/gvisor"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Google gVisor: modelo de defesa em profundidade, fronteiras do que o gVisor não protege e Runtime Monitoring

## Em uma frase
O gVisor aplica primitivas do kernel Linux (`seccomp-bpf`, namespaces, cgroups, `pivot_root`) como segunda camada de defesa ao redor do próprio Sentry (exigindo exploração dupla para escape), documenta claramente o que está fora de seu escopo e oferece Runtime Monitoring para detecção de intrusão.

## Por que importa
Nenhum mecanismo de isolamento é uma bala de prata contra todas as classes de ataques: arquitetos de segurança precisam compreender exatamente como o Sentry restringe seu próprio acesso ao kernel do host e quais ameaças (como bugs na aplicação dentro do sandbox, falhas antes do runtime iniciar ou ataques de canal lateral de CPU) exigem controles complementares. A seção `What does gVisor not protect against?` do guia oficial de arquitetura detalha essas fronteiras.

## Como funciona
Na arquitetura de **defesa em profundidade** do gVisor, o processo Sentry roda em um user namespace isolado com capabilities mínimas, visão isolada de filesystem (`pivot_root`) e um filtro `seccomp-bpf` estrito que proíbe o próprio Sentry de chamar syscalls como `exec(2)` ou `connect(2)` no host (embora as aplicações dentro do sandbox possam usá-las normalmente, pois são tratadas em Go dentro do Sentry e da pilha de rede em user-space). Assim, para escapar de um sandbox gVisor, um invasor precisaria explorar simultaneamente um bug no kernel Go do Sentry **e** um bug no kernel Linux do host (que não compartilham código). Para detectar comprometimento **dentro** da própria aplicação no sandbox, o gVisor oferece um recurso nativo de **runtime monitoring** (`gvisor.dev/docs/user_guide/runtimemonitor/`).

## Exemplo
```bash
# Testar execução em modo rootless sem privilégios de rede (descarta privilégios antes de rodar código não confiável)
runsc --rootless --network=none do echo "Executando em user namespace isolado com Sentry"
```

## Limites e trade-offs
Conforme documentado oficialmente, existem três áreas onde o gVisor **não** protege sozinho: (1) ataques em componentes de nível superior antes do sandbox entrar em cena (ex.: um exploit no `containerd` que inicie um container sem o `runsc`); (2) ataques de canal lateral de CPU estilo Spectre (mitigados no kernel/hardware do host); e (3) exploits na lógica da própria aplicação dentro do sandbox (ex.: um bug em código PHP rodando com nginx), razão pela qual workloads de clientes diferentes devem sempre rodar em sandboxes separados.

## Como verificar
Inspecione `/proc/<pid-do-sentry>/status` no host durante a execução de um container sob `runsc` para confirmar que o processo Sentry roda em um user namespace não privilegiado com filtro `Seccomp: 2` ativo e capabilities zeradas.

## Conexões
- [[gvisor-runtime-oci-runsc-docker-kubernetes-containerd]] — Veja também: Google gVisor: integração do runtime OCI runsc e containerd-shim-runsc-v1 com Docker e Kubernetes.
- [[gvisor-pilha-rede-userspace-netstack-importacao-branch-go]] — Veja também: Google gVisor: pilha de rede em espaço de usuário (Netstack) e importação via branch sintética @go.
- [[gvisor-arquitetura-sentry-gofer-application-kernel]] — Referência cruzada direta com gvisor-arquitetura-sentry-gofer-application-kernel.
- [[gvisor-plataformas-interceptacao-systrap-kvm]] — Referência cruzada direta com gvisor-plataformas-interceptacao-systrap-kvm.
- [[tetragon-ebpf-observabilidade-seguranca-runtime-enforcement]] — Referência cruzada direta com tetragon-ebpf-observabilidade-seguranca-runtime-enforcement.

## Fontes
- [Google gVisor GitHub — README.md (Application Kernel, runsc, Bazel Build & @go Branch)](https://raw.githubusercontent.com/google/gvisor/master/README.md) — README oficial do Google gVisor detalhando motivação de isolamento, compilação do tarball de release (runsc, containerd-shim-runsc-v1, gvisor-bin) com Docker/Bazel e importação da pilha Netstack via branch @go; consultado em 2026-10-03.
- [Google gVisor Architecture Guide — Introduction to gVisor Security (Sentry, Gofer, Systrap & KVM)](https://gvisor.dev/docs/architecture_guide/intro/) — Guia oficial de arquitetura de segurança do gVisor explicando reimplementação de syscalls no Sentry em Go, processo sidecar Gofer, plataformas Systrap/KVM e fronteiras de proteção; consultado em 2026-10-03.
- [Google gVisor — Official GitHub Repository](https://github.com/google/gvisor) — Repositório oficial Apache-2.0 do Google gVisor; consultado em 2026-10-03.
