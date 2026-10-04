---
id: software.devops.tranche08.000716
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
fontes: ["https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md", "https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md", "https://github.com/firecracker-microvm/firecracker"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# AWS Firecracker: paginação sob demanda (demand fault paging) e oversubscription de CPU e memória

## Em uma frase
O Firecracker habilita por padrão paginação sob demanda (`demand fault paging`) e oversubscription de CPU, alocando páginas físicas de memória no host apenas à medida que o guest efetivamente as acessa.

## Por que importa
Em plataformas de funções serverless (como AWS Lambda) ou runners de CI efêmeros, milhares de microVMs podem ser configuradas com 512 MiB ou 1 GiB de RAM para absorver picos eventuais, mas consomem apenas 40 MiB na maior parte do tempo e ficam ociosas aguardando requisições. De acordo com a seção `Built-in Capabilities` do README oficial do Firecracker, habilitar demand fault paging e CPU oversubscription por padrão maximiza a taxa de utilização do hardware físico.

## Como funciona
Quando uma microVM é configurada com `mem_size_mib: 1024`, o Firecracker cria o mapeamento de memória virtual anônima (`mmap`), mas não pré-aloca nem trava imediatamente 1 GiB de páginas físicas de RAM no host. Graças ao **demand fault paging**, as páginas físicas do host só são materializadas pelo kernel Linux quando o kernel ou a aplicação convidada dentro da microVM toca naquela região de memória pela primeira vez (gerando um page fault tratado pelo KVM/host). Da mesma forma, como cada vCPU da microVM é apenas uma thread POSIX gerenciada pelo escalonador CFS do kernel Linux hospedeiro, o operador pode alocar mais vCPUs totais entre as microVMs ativas do que o número de cores físicos do servidor (**CPU oversubscription**).

## Exemplo
```bash
# Comparar a memória virtual reservada (VSZ) versus a memória física residente real (RSS) de um processo Firecracker
ps -o pid,comm,vsz,rss -C firecracker
```

## Limites e trade-offs
Quando se utiliza oversubscription agressivo de memória com demand fault paging em um host sem controle de admissão de capacidade, se dezenas de microVMs decidirem alocar toda a sua memória máxima simultaneamente durante um pico de tráfego, a memória física do host pode se esgotar e acionar o OOM Killer do kernel hospedeiro (ou exigir swap/ballooning coordenado pelo agente de nó).

## Como verificar
Inicie uma microVM Firecracker configurada com `512 MiB` de RAM rodando um workload mínimo e verifique na coluna `RSS` do comando `ps` no host que o consumo físico real de memória é uma fração reduzida dos 512 MiB configurados.

## Conexões
- [[firecracker-jailer-isolamento-cgroups-namespaces-seccomp]] — Veja também: AWS Firecracker: defesa em profundidade em produção com o processo Jailer e filtros seccomp por thread.
- [[firecracker-plataformas-testadas-intel-amd-graviton-kernels]] — Veja também: AWS Firecracker: matriz de plataformas bare-metal testadas (Intel, AMD, ARM Graviton) e requisitos de kernel.
- [[firecracker-microvms-kvm-isolamento-serverless-multitenant]] — Referência cruzada direta com firecracker-microvms-kvm-isolamento-serverless-multitenant.
- [[firecracker-api-openapi-configuracao-vcpu-memoria-boot]] — Referência cruzada direta com firecracker-api-openapi-configuracao-vcpu-memoria-boot.
- [[firecracker-especificacao-performance-logging-metricas]] — Referência cruzada direta com firecracker-especificacao-performance-logging-metricas.

## Fontes
- [AWS Firecracker GitHub — README.md (MicroVM VMM, OpenAPI Socket, Rate Limiters, Jailer & Tested Platforms)](https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md) — README oficial do AWS Firecracker (Apache-2.0) documentando capacidades da API REST sobre socket UNIX, CPU templates, rate limiters virtio, demand fault paging, processo jailer, seccomp por thread e matriz de plataformas Intel/AMD/Graviton; consultado em 2026-10-03.
- [AWS Firecracker Documentation — Design, Specification & Production Host Setup](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md) — Documentação oficial de design, compromissos de performance (SPECIFICATION.md) e endurecimento de host Linux (prod-host-setup.md) do Firecracker; consultado em 2026-10-03.
- [AWS Firecracker — Official GitHub Repository](https://github.com/firecracker-microvm/firecracker) — Repositório oficial do VMM Firecracker mantido pela AWS; consultado em 2026-10-03.
