---
id: software.devops.tranche08.000719
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

# AWS Firecracker: integração com runtimes de containers e microVMs (Kata Containers e Flintlock)

## Em uma frase
O Firecracker integra-se a projetos do ecossistema de containers e Kubernetes como o Kata Containers (via hipervisor `fc`) e o Flintlock (gerenciamento de ciclo de vida de microVMs apoiadas em imagens OCI/containerd).

## Por que importa
Embora o binário `firecracker` forneça o VMM de baixo nível ideal para criar uma microVM a partir de um arquivo de kernel e um disco ext4 bruto, equipes que operam plataformas Kubernetes ou GitOps desejam empacotar suas cargas como imagens de container OCI padrão em registries e agendá-las via `kubectl`. Segundo a seção `Overview` do README oficial do Firecracker, integrações como Kata Containers e Flintlock fazem exatamente essa ponte.

## Como funciona
Quando integrado ao **Kata Containers**, o `containerd-shim-kata-v2` (configurado com `configuration-fc.toml`) traduz a especificação do Pod Kubernetes em chamadas para a API do Firecracker e do `jailer`, montando as camadas da imagem OCI do container como dispositivos de bloco mapeados por `devmapper` (já que o Firecracker usa `virtio-block` em vez de `virtio-fs` baseado em PCI) e comunicando-se com o `kata-agent` via `vsock`. Já com o **Flintlock** (`liquidmetal-dev/flintlock`), o Firecracker é utilizado em conjunto com o `containerd` para provisionar e gerenciar microVMs leves cujos discos e kernels são distribuídos como artefatos OCI, viabilizando inclusive provisionamento rápido de nós Kubernetes (Cluster API Provider MicroVM).

## Exemplo
```bash
# Verificar no arquivo de configuração do Kata para Firecracker (configuration-fc.toml) o binário VMM e jailer
grep -E "^(path|jailer_path|valid_jailer_paths)" /opt/kata/share/defaults/kata-containers/configuration-fc.toml
```

## Limites e trade-offs
Ao usar o Firecracker como hipervisor por trás do Kata Containers (`kata-fc`), como o design minimalista do Firecracker omite compartilhamento de diretórios via `virtio-fs`, o `containerd` no nó precisa estar configurado com um snapshotter baseado em dispositivo de bloco (como `devmapper` ou `nydus`/block) em vez do `overlayfs` padrão de diretórios para conseguir anexar o `rootfs` do container à microVM via `virtio-block`.

## Como verificar
No nó configurado para `kata-fc`, confirme que o snapshotter `devmapper` do `containerd` está ativo (`ctr plugins ls | grep devmapper`) e teste a criação de um Pod com `runtimeClassName: kata-fc`.

## Conexões
- [[firecracker-especificacao-performance-logging-metricas]] — Veja também: AWS Firecracker: especificação de performance verificada em CI e sistema de logging e métricas via API.
- [[firecracker-cadencia-releases-politica-seguranca-prod-host-setup]] — Veja também: AWS Firecracker: cadência de releases, configuração segura do host (prod-host-setup) e política de segurança.
- [[firecracker-microvms-kvm-isolamento-serverless-multitenant]] — Referência cruzada direta com firecracker-microvms-kvm-isolamento-serverless-multitenant.
- [[kata-containers-isolamento-vms-leves-arquitetura]] — Referência cruzada direta com kata-containers-isolamento-vms-leves-arquitetura.
- [[kata-hipervisores-configuracao-runtime-agent]] — Referência cruzada direta com kata-hipervisores-configuracao-runtime-agent.

## Fontes
- [AWS Firecracker GitHub — README.md (MicroVM VMM, OpenAPI Socket, Rate Limiters, Jailer & Tested Platforms)](https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md) — README oficial do AWS Firecracker (Apache-2.0) documentando capacidades da API REST sobre socket UNIX, CPU templates, rate limiters virtio, demand fault paging, processo jailer, seccomp por thread e matriz de plataformas Intel/AMD/Graviton; consultado em 2026-10-03.
- [AWS Firecracker Documentation — Design, Specification & Production Host Setup](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md) — Documentação oficial de design, compromissos de performance (SPECIFICATION.md) e endurecimento de host Linux (prod-host-setup.md) do Firecracker; consultado em 2026-10-03.
- [AWS Firecracker — Official GitHub Repository](https://github.com/firecracker-microvm/firecracker) — Repositório oficial do VMM Firecracker mantido pela AWS; consultado em 2026-10-03.
