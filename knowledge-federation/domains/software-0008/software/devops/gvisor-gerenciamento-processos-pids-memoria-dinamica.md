---
id: software.devops.tranche08.000728
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

# Google gVisor: tabela própria de PIDs no Sentry, tradução de syscalls não 1-para-1 e elasticidade de memória

## Em uma frase
O gVisor Sentry mantém sua própria tabela virtual de processos e PIDs (invisíveis ao `top` do host), traduz chamadas do container sem mapeamento 1-para-1 com syscalls do host e aloca/libera CPU e memória dinamicamente em tempo de execução.

## Por que importa
Em máquinas virtuais tradicionais, é necessário pré-alocar recursos de máquina para cada VM no host e inicializar um kernel Linux separado, desperdiçando memória quando o container está ocioso; já em containers comuns, os processos do container são processos reais do kernel do host. A documentação de arquitetura do gVisor (`How does gVisor provide isolation?`) explica como o Sentry desacopla processos e syscalls mantendo a elasticidade de uma aplicação comum.

## Como funciona
Quando um processo dentro do sandbox chama `getpid(2)` ou `fork(2)`, o gVisor Sentry intercepta a chamada e consulta ou atualiza sua própria tabela interna de PIDs: os processos do sandbox não são processos reais separados no host (executar `top(1)` no host mostra apenas o processo do Sentry/Gofer, não a árvore interna do container) e `getpid(2)` retorna imediatamente sem fazer nenhuma syscall ao kernel do host. Quando um processo faz `read(2)` em um `pipe(2)` UNIX no qual outro processo do sandbox está fazendo `write(2)`, o Sentry (através do runtime Go) pode invocar a syscall `futex(2)` no host para sincronização e bloqueio — demonstrando que as syscalls feitas pelo Sentry ao host **não mapeiam 1-para-1** com as syscalls feitas pelo container. Como o Sentry é um processo normal de espaço de usuário para o host, ele aloca e devolve memória e CPU dinamicamente conforme a demanda da aplicação.

## Exemplo
```bash
# Verificar dentro do sandbox gVisor a árvore de processos virtualizada pelo Sentry
sudo docker run --rm --runtime=runsc ubuntu ps -ef
```

## Limites e trade-offs
Como os processos internos do container são gerenciados internamente pela tabela de processos do Sentry em Go e não existem como tarefas 1-para-1 visíveis diretamente na tabela global `/proc` do host, ferramentas de observabilidade de nó que tentam inspecionar processos de containers apenas lendo `/proc/<host-pid>` ou enganchando `kprobes` de syscalls da aplicação no kernel do host verão apenas a atividade consolidada do processo `runsc-sandbox` (Sentry).

## Como verificar
Inicie um container sob `--runtime=runsc` executando múltiplos subprocessos `sleep` em background e compare a saída de `docker top <container>` / `docker exec <container> ps aux` com os processos visíveis diretamente no host.

## Conexões
- [[gvisor-isolamento-sistema-arquivos-gofer-mount-namespaces]] — Veja também: Google gVisor: isolamento de sistema de arquivos com o processo sidecar Gofer, VFS em Go e pivot_root.
- [[gvisor-modos-privilegio-reexecucao-rootless-network-none]] — Veja também: Google gVisor: modelo de privilégios na inicialização do runsc, queda de privilégios e modo rootless.
- [[gvisor-arquitetura-sentry-gofer-application-kernel]] — Referência cruzada direta com gvisor-arquitetura-sentry-gofer-application-kernel.
- [[gvisor-plataformas-interceptacao-systrap-kvm]] — Referência cruzada direta com gvisor-plataformas-interceptacao-systrap-kvm.
- [[gvisor-defesa-profundidade-limites-protecao-runtime-monitoring]] — Referência cruzada direta com gvisor-defesa-profundidade-limites-protecao-runtime-monitoring.

## Fontes
- [Google gVisor GitHub — README.md (Application Kernel, runsc, Bazel Build & @go Branch)](https://raw.githubusercontent.com/google/gvisor/master/README.md) — README oficial do Google gVisor detalhando motivação de isolamento, compilação do tarball de release (runsc, containerd-shim-runsc-v1, gvisor-bin) com Docker/Bazel e importação da pilha Netstack via branch @go; consultado em 2026-10-03.
- [Google gVisor Architecture Guide — Introduction to gVisor Security (Sentry, Gofer, Systrap & KVM)](https://gvisor.dev/docs/architecture_guide/intro/) — Guia oficial de arquitetura de segurança do gVisor explicando reimplementação de syscalls no Sentry em Go, processo sidecar Gofer, plataformas Systrap/KVM e fronteiras de proteção; consultado em 2026-10-03.
- [Google gVisor — Official GitHub Repository](https://github.com/google/gvisor) — Repositório oficial Apache-2.0 do Google gVisor; consultado em 2026-10-03.
