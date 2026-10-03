---
id: software.devops.tranche08.000711
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

# AWS Firecracker: tecnologia de virtualização de microVMs sobre KVM para workloads serverless e multi-tenant

## Em uma frase
O Firecracker (criado na AWS para acelerar serviços como AWS Lambda e AWS Fargate e aberto sob licença Apache-2.0) é um Virtual Machine Monitor (VMM) minimalista que usa o Linux KVM para criar e gerenciar microVMs seguras e de baixíssimo overhead.

## Por que importa
Executar funções serverless e containers de múltiplos clientes diferentes no mesmo servidor físico exige a barreira de isolamento de hardware das máquinas virtuais, mas hipervisores tradicionais possuem milhões de linhas de código de emulação de dispositivos legados (BIOS, PCI antigo, USB, placa de som), alto consumo de memória e inicialização lenta. Segundo o README oficial do Firecracker, seu design minimalista exclui dispositivos e funcionalidades desnecessárias para reduzir o footprint de memória, diminuir a superfície de ataque, acelerar o boot e elevar a densidade de hardware.

## Como funciona
O componente principal do Firecracker é um único processo Virtual Machine Monitor (VMM) escrito em Rust que interage com o módulo Kernel Virtual Machine (`KVM`) do kernel Linux hospedeiro para instanciar microVMs. Ao iniciar, o processo Firecracker expõe um endpoint de API HTTP sobre um socket UNIX local no host (especificado no formato OpenAPI em `src/firecracker/swagger/firecracker.yaml`), pelo qual o plano de controle configura vCPUs, memória, rede, blocos, limitadores de taxa e inicia a microVM. Além do uso direto em plataformas FaaS, o Firecracker integra-se a runtimes de containers como **Kata Containers** e **Flintlock**.

## Exemplo
```bash
# Clonar e compilar o binário do Firecracker a partir do código-fonte usando o container oficial devtool
git clone https://github.com/firecracker-microvm/firecracker
cd firecracker
tools/devtool build
toolchain="$(uname -m)-unknown-linux-musl"
ls -lh "build/cargo_target/${toolchain}/debug/firecracker"
```

## Limites e trade-offs
Conforme ressalta a seção `Getting Started` do README oficial, a segurança geral das microVMs Firecracker em computação multi-tenant depende criticamente de um sistema operacional Linux hospedeiro bem configurado (seguindo o guia `docs/prod-host-setup.md`) e do uso do processo `jailer` em produção; além disso, o minimalismo intencional significa que o Firecracker não suporta sistemas operacionais convidados arbitrários que dependam de emulação de BIOS/UEFI legado ou placas gráficas virtuais.

## Como verificar
Verifique a presença e as permissões do dispositivo `/dev/kvm` no host Linux e execute `firecracker --version` no binário compilado ou baixado da página de releases.

## Conexões
- [[firecracker-api-openapi-configuracao-vcpu-memoria-boot]] — Veja também: AWS Firecracker: configuração da microVM via API OpenAPI (vCPUs, memória, CPU templates e boot).
- [[firecracker-jailer-isolamento-cgroups-namespaces-seccomp]] — Referência cruzada direta com firecracker-jailer-isolamento-cgroups-namespaces-seccomp.
- [[kata-hipervisores-configuracao-runtime-agent]] — Referência cruzada direta com kata-hipervisores-configuracao-runtime-agent.

## Fontes
- [AWS Firecracker GitHub — README.md (MicroVM VMM, OpenAPI Socket, Rate Limiters, Jailer & Tested Platforms)](https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md) — README oficial do AWS Firecracker (Apache-2.0) documentando capacidades da API REST sobre socket UNIX, CPU templates, rate limiters virtio, demand fault paging, processo jailer, seccomp por thread e matriz de plataformas Intel/AMD/Graviton; consultado em 2026-10-03.
- [AWS Firecracker Documentation — Design, Specification & Production Host Setup](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md) — Documentação oficial de design, compromissos de performance (SPECIFICATION.md) e endurecimento de host Linux (prod-host-setup.md) do Firecracker; consultado em 2026-10-03.
- [AWS Firecracker — Official GitHub Repository](https://github.com/firecracker-microvm/firecracker) — Repositório oficial do VMM Firecracker mantido pela AWS; consultado em 2026-10-03.
