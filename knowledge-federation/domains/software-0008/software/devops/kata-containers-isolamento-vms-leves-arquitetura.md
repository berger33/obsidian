---
id: software.devops.tranche08.000701
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
fontes: ["https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md", "https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md", "https://github.com/kata-containers/kata-containers"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kata Containers: máquinas virtuais leves com isolamento de hardware e experiência de containers

## Em uma frase
O Kata Containers (projeto open-source licenciado sob Apache-2.0, série 2.0+) constrói uma implementação padronizada de máquinas virtuais leves (lightweight VMs) que se comportam e performam como containers, mas entregam o isolamento de workload e a segurança de VMs.

## Por que importa
Em containers tradicionais baseados apenas em namespaces e cgroups (como no `runc` ou `crun`), todos os containers compartilham o mesmo kernel do sistema operacional hospedeiro; uma única vulnerabilidade de escalada no kernel permite escapar do container para o host. Segundo o README oficial do Kata Containers, encapsular o container/Pod dentro de uma máquina virtual leve isolada por hardware combina a agilidade do ecossistema OCI/CRI com a barreira de segurança de virtualização.

## Como funciona
Quando um gerenciador de containers (como `containerd` ou `CRI-O` no Kubernetes via `RuntimeClass`) solicita a criação de um Pod com Kata Containers, o componente `runtime` (ou `runtime-rs` escrito em Rust), atuando como uma implementação de `containerd shimv2`, inicializa um hipervisor configurado (ou o VMM embutido `dragonball`) usando um kernel Linux guest dedicado e uma imagem de mini-SO (`rootfs` ou `initrd` gerada pelo `osbuilder`). Dentro dessa máquina virtual convidada roda o processo `agent` (`kata-agent`), que recebe comandos do shim no host e configura o ambiente de containers OCI dentro da VM isolada.

## Exemplo
```bash
# Verificar no host se o processador e o kernel suportam executar Kata Containers (modo silencioso sem rede)
kata-runtime check --no-network-checks --verbose
```

## Limites e trade-offs
Ao contrário de containers nativos que compartilham a memória do kernel do host sem sobrecarga adicional por Pod, cada Pod executado sob Kata Containers instancia um processo de hipervisor, um kernel guest isolado e o `kata-agent`, aumentando o footprint base de memória RAM por Pod e exigindo suporte a extensões de virtualização de hardware no servidor (ou virtualização aninhada habilitada em máquinas virtuais de nuvem).

## Como verificar
Execute `sudo kata-runtime check` como usuário `root` no servidor Linux para validar o suporte de virtualização de hardware e verificar se não há outro hipervisor incompatível em execução.

## Conexões
- [[kata-requisitos-hardware-arquiteturas-kata-runtime-check]] — Veja também: Kata Containers: suporte multi-arquitetura de virtualização e diagnóstico com kata-runtime check.
- [[kata-componentes-principais-shimv2-runtime-rs-agent-dragonball]] — Referência cruzada direta com kata-componentes-principais-shimv2-runtime-rs-agent-dragonball.
- [[firecracker-microvms-kvm-isolamento-serverless-multitenant]] — Referência cruzada direta com firecracker-microvms-kvm-isolamento-serverless-multitenant.

## Fontes
- [Kata Containers GitHub — README.md (Lightweight VMs, Hardware Requirements, Main & Additional Components)](https://raw.githubusercontent.com/kata-containers/kata-containers/main/README.md) — README oficial do Kata Containers (Apache-2.0) detalhando suporte a arquiteturas de 64 bits (x86_64, aarch64, ppc64le, s390x), kata-runtime check e componentes runtime, runtime-rs, agent, dragonball, osbuilder, kata-ctl e kata-deploy; consultado em 2026-10-03.
- [Kata Containers Design Documentation — Architecture & Configuration](https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture_4.0/architecture.md) — Documentação oficial de arquitetura do Kata Containers (incluindo evolução 4.0 em Rust, containerd shimv2 e configuração de hipervisores); consultado em 2026-10-03.
- [Kata Containers — Official GitHub Repository](https://github.com/kata-containers/kata-containers) — Repositório oficial Apache-2.0 do Kata Containers; consultado em 2026-10-03.
