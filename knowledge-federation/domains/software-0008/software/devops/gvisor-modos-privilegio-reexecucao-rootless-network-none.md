---
id: software.devops.tranche08.000729
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

# Google gVisor: modelo de privilégios na inicialização do runsc, queda de privilégios e modo rootless

## Em uma frase
Na inicialização padrão, o `runsc` utiliza privilégios temporários apenas para configurar a pilha de rede e namespaces do sandbox antes de se re-executar e descartar todos os privilégios antes de qualquer código não confiável rodar, suportando também modo `--rootless --network=none` sem `sudo`.

## Por que importa
Engenheiros de segurança frequentemente questionam por que exemplos de linha de comando do `runsc` utilizam `sudo` se o objetivo é justamente isolar código não confiável. A seção `How can I test gVisor?` do guia oficial de introdução à segurança do gVisor esclarece detalhadamente o ciclo de privilégios da inicialização do sandbox e quando o modo totalmente rootless pode ser usado.

## Como funciona
Os workloads isolados pelo gVisor sempre rodam com capabilities mínimas dentro de um user namespace isolado sob a perspectiva do kernel do host. No entanto, o processo inicial de configuração do sandbox (`sandbox setup`) requer privilégios no host especificamente para configurar a pilha de rede em espaço de usuário (criação/vinculação de interfaces virtuais e namespaces de rede). Assim que a configuração do sandbox é concluída, o `runsc` **re-executa a si mesmo e descarta todos os privilégios** no processo — e isso ocorre **antes** que qualquer código não confiável do container comece a executar. Para sandboxes que não exigem acesso à rede, é possível executar em modo totalmente rootless sem `sudo` usando `runsc --rootless --network=none`.

## Exemplo
```bash
# Executar um comando dentro do sandbox gVisor como usuário comum sem sudo usando --rootless e --network=none
runsc --rootless --network=none do id
```

## Limites e trade-offs
Ao utilizar `runsc --rootless --network=none` para rodar tarefas de computação pura ou processamento de dados sem privilégios de `root` no host, o sandbox fica completamente isolado de rede (`--network=none`); quando o container precisa de conectividade TCP/IP externa, a integração via Docker (`--runtime=runsc`) ou `containerd` realiza o setup privilegiado da interface virtual antes de derrubar os privilégios do processo Sentry.

## Como verificar
Execute `runsc --rootless --network=none do ip addr` como um usuário não privilegiado e confirme que o comando executa sem `sudo` e exibe apenas a interface de loopback isolada.

## Conexões
- [[gvisor-gerenciamento-processos-pids-memoria-dinamica]] — Veja também: Google gVisor: tabela própria de PIDs no Sentry, tradução de syscalls não 1-para-1 e elasticidade de memória.
- [[gvisor-analise-estatica-nogo-governanca-adopters]] — Veja também: Google gVisor: verificadores estáticos de código Go (nogo), governança, ADOPTERS.md e política de segurança.
- [[gvisor-arquitetura-sentry-gofer-application-kernel]] — Referência cruzada direta com gvisor-arquitetura-sentry-gofer-application-kernel.
- [[gvisor-runtime-oci-runsc-docker-kubernetes-containerd]] — Referência cruzada direta com gvisor-runtime-oci-runsc-docker-kubernetes-containerd.
- [[runc-containers-rootless-user-namespaces-configuracao]] — Referência cruzada direta com runc-containers-rootless-user-namespaces-configuracao.

## Fontes
- [Google gVisor GitHub — README.md (Application Kernel, runsc, Bazel Build & @go Branch)](https://raw.githubusercontent.com/google/gvisor/master/README.md) — README oficial do Google gVisor detalhando motivação de isolamento, compilação do tarball de release (runsc, containerd-shim-runsc-v1, gvisor-bin) com Docker/Bazel e importação da pilha Netstack via branch @go; consultado em 2026-10-03.
- [Google gVisor Architecture Guide — Introduction to gVisor Security (Sentry, Gofer, Systrap & KVM)](https://gvisor.dev/docs/architecture_guide/intro/) — Guia oficial de arquitetura de segurança do gVisor explicando reimplementação de syscalls no Sentry em Go, processo sidecar Gofer, plataformas Systrap/KVM e fronteiras de proteção; consultado em 2026-10-03.
- [Google gVisor — Official GitHub Repository](https://github.com/google/gvisor) — Repositório oficial Apache-2.0 do Google gVisor; consultado em 2026-10-03.
