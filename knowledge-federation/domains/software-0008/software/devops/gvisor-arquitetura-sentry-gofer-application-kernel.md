---
id: software.devops.tranche08.000721
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

# Google gVisor: kernel de aplicação em espaço de usuário escrito em Go (Sentry, Gofer e runsc)

## Em uma frase
O Google gVisor é um kernel de aplicação escrito em linguagem memory-safe (Go) que roda em espaço de usuário e inclui o runtime OCI `runsc`, isolando containers sem passar chamadas de sistema diretamente para o kernel do host.

## Por que importa
Conforme destaca o README oficial do gVisor (`Why does gVisor exist?`), containers tradicionais não são um sandbox: como compartilham um único kernel Linux monolítico, o escape do container é possível com uma única vulnerabilidade de kernel, e filtros como `seccomp-bpf` são difíceis de restringir quando a aplicação precisa de syscalls amplas como `ioctl(2)` ou `io_uring(2)`. Ao mesmo tempo, máquinas virtuais tradicionais exigem pré-alocar recursos fixos e dar boot em um kernel convidado completo. O gVisor adota uma **terceira abordagem distinta**, combinando isolamento estilo VM com a leveza e elasticidade de processos comuns.

## Como funciona
O coração do gVisor é o **gVisor Sentry**, um processo em espaço de usuário escrito em Go que atua como o kernel sob a perspectiva do container isolado: ele intercepta e trata todas as chamadas de sistema (`syscalls`) e faltas de página (`page faults`) da aplicação usando sua própria reimplementação do zero (em Go) da interface de syscalls do Linux, gerenciamento de memória, sistemas de arquivos, pilha de rede (`Netstack`), tabela de processos (PIDs internos que não existem no `top(1)` do host) e sinais. **O gVisor nunca repassa diretamente nenhuma syscall da aplicação para o host**. Para operações de sistema de arquivos que não podem ser atendidas dentro do ambiente ultrarrestrito do Sentry, um processo companheiro chamado **Gofer** intermedia o acesso de forma controlada.

## Exemplo
```bash
# Testar rapidamente o isolamento do gVisor em modo rootless sem rede executando dmesg (que lê o kernel do Sentry)
runsc --rootless --network=none do dmesg
```

## Limites e trade-offs
Como o gVisor Sentry jamais repassa syscalls diretamente ao host, se uma chamada de sistema ou funcionalidade específica do kernel Linux ainda não tiver sido reimplementada no Sentry em Go, a aplicação dentro do sandbox não poderá utilizá-la; além disso, workloads com altíssima taxa de chamadas de sistema intensivas ou I/O pesado de arquivos têm overhead maior que em containers `runc`/`crun` nativos.

## Como verificar
Execute `runsc --rootless --network=none do dmesg` e confirme que a saída exibe as mensagens fictícias geradas pelo kernel do gVisor (`Starting gVisor...`, `Setting up VFS...`, `Ready!`) em vez de `Operation not permitted` do kernel do host.

## Conexões
- [[gvisor-plataformas-interceptacao-systrap-kvm]] — Veja também: Google gVisor: plataformas de interceptação de syscalls e page faults (Systrap padrão e KVM).
- [[gvisor-runtime-oci-runsc-docker-kubernetes-containerd]] — Referência cruzada direta com gvisor-runtime-oci-runsc-docker-kubernetes-containerd.
- [[runc-runtime-oci-referencia-linux-especificacao]] — Referência cruzada direta com runc-runtime-oci-referencia-linux-especificacao.

## Fontes
- [Google gVisor GitHub — README.md (Application Kernel, runsc, Bazel Build & @go Branch)](https://raw.githubusercontent.com/google/gvisor/master/README.md) — README oficial do Google gVisor detalhando motivação de isolamento, compilação do tarball de release (runsc, containerd-shim-runsc-v1, gvisor-bin) com Docker/Bazel e importação da pilha Netstack via branch @go; consultado em 2026-10-03.
- [Google gVisor Architecture Guide — Introduction to gVisor Security (Sentry, Gofer, Systrap & KVM)](https://gvisor.dev/docs/architecture_guide/intro/) — Guia oficial de arquitetura de segurança do gVisor explicando reimplementação de syscalls no Sentry em Go, processo sidecar Gofer, plataformas Systrap/KVM e fronteiras de proteção; consultado em 2026-10-03.
- [Google gVisor — Official GitHub Repository](https://github.com/google/gvisor) — Repositório oficial Apache-2.0 do Google gVisor; consultado em 2026-10-03.
