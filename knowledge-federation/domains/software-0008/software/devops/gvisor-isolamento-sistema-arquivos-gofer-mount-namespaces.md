---
id: software.devops.tranche08.000727
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

# Google gVisor: isolamento de sistema de arquivos com o processo sidecar Gofer, VFS em Go e pivot_root

## Em uma frase
No gVisor, o Sentry proíbe chamadas diretas de abertura de arquivos no host e delega o acesso aos volumes OCI configurados para o processo sidecar **Gofer**, enquanto implementa um Virtual File System (VFS) próprio em Go e aplica `pivot_root(2)`.

## Por que importa
Permitir que o processo que executa o kernel do sandbox tenha acesso irrestrito para abrir qualquer caminho no sistema de arquivos do host criaria o risco de que um bug na lógica do Sentry vazasse arquivos do hospedeiro. Segundo a documentação oficial de arquitetura do gVisor (`How does gVisor provide isolation?`), separar o Sentry do processo sidecar Gofer garante que o Sentry opere em um mount namespace totalmente isolado sem acesso direto ao disco do host.

## Como funciona
Quando o `runsc` inicia um container OCI, ele lança o processo **Gofer** como um processo companheiro ligeiramente mais privilegiado que possui visão estritamente limitada aos diretórios que a configuração OCI (`config.json`) determinou que devem ser expostos ao container (usando `pivot_root(2)` para impedir o acesso a qualquer outro diretório do host). O processo **Sentry**, por sua vez, tem chamadas de abertura de arquivos no host bloqueadas por seu filtro `seccomp-bpf`; quando a aplicação dentro do sandbox acessa arquivos do container ou volumes montados, o VFS implementado em Go dentro do Sentry se comunica com o Gofer por um canal IPC restrito para ler ou gravar apenas nos arquivos autorizados, enquanto sistemas de arquivos virtuais como `/proc`, `/sys` e `/dev/shm` são sintetizados inteiramente em memória pelo próprio Sentry.

## Exemplo
```bash
# Inspecionar dentro de um container gVisor que os sistemas de arquivos /proc e /sys são sintetizados pelo Sentry
sudo docker run --rm --runtime=runsc alpine sh -c "mount && cat /proc/version"
```

## Limites e trade-offs
Como toda operação de arquivo em volumes externos que não está em cache no Sentry precisa atravessar a fronteira IPC entre o processo Sentry e o processo Gofer antes de chegar ao sistema de arquivos do host, cargas de trabalho que realizam milhões de pequenas operações `open`/`stat`/`unlink` em volumes montados do host sofrem latência adicional; para arquivos temporários intensivos de build ou banco em memória, usar `tmpfs` (que vive inteiramente na memória do Sentry sem passar pelo Gofer) entrega desempenho muito superior.

## Como verificar
Dentro de um container rodando sob `--runtime=runsc`, compare o desempenho de criação de arquivos em `/tmp` (quando montado como `tmpfs` em memória no Sentry) versus um volume `-v /tmp/host:/vol` intermediado pelo Gofer.

## Conexões
- [[gvisor-build-bazel-docker-testes-macos]] — Veja também: Google gVisor: sistema de build com Bazel/Docker, requisitos (Linux 5.6+) e execução de testes (incluindo macOS).
- [[gvisor-gerenciamento-processos-pids-memoria-dinamica]] — Veja também: Google gVisor: tabela própria de PIDs no Sentry, tradução de syscalls não 1-para-1 e elasticidade de memória.
- [[gvisor-arquitetura-sentry-gofer-application-kernel]] — Referência cruzada direta com gvisor-arquitetura-sentry-gofer-application-kernel.
- [[gvisor-runtime-oci-runsc-docker-kubernetes-containerd]] — Referência cruzada direta com gvisor-runtime-oci-runsc-docker-kubernetes-containerd.

## Fontes
- [Google gVisor GitHub — README.md (Application Kernel, runsc, Bazel Build & @go Branch)](https://raw.githubusercontent.com/google/gvisor/master/README.md) — README oficial do Google gVisor detalhando motivação de isolamento, compilação do tarball de release (runsc, containerd-shim-runsc-v1, gvisor-bin) com Docker/Bazel e importação da pilha Netstack via branch @go; consultado em 2026-10-03.
- [Google gVisor Architecture Guide — Introduction to gVisor Security (Sentry, Gofer, Systrap & KVM)](https://gvisor.dev/docs/architecture_guide/intro/) — Guia oficial de arquitetura de segurança do gVisor explicando reimplementação de syscalls no Sentry em Go, processo sidecar Gofer, plataformas Systrap/KVM e fronteiras de proteção; consultado em 2026-10-03.
- [Google gVisor — Official GitHub Repository](https://github.com/google/gvisor) — Repositório oficial Apache-2.0 do Google gVisor; consultado em 2026-10-03.
