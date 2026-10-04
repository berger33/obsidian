---
id: software.devops.tranche08.000714
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

# AWS Firecracker: dispositivos vsock, entropia, pmem, serviço de metadados MMDS e hotplug de memória/PCI

## Em uma frase
O Firecracker suporta comunicação host-guest via socket `vsock`, dispositivo de entropia (`virtio-rng`), memória persistente (`pmem`), serviço de metadados guest-facing (`MMDS` em Beta), hotplug de memória (`virtio-mem`) e hotplug PCI em Developer Preview.

## Por que importa
MicroVMs isoladas para funções serverless frequentemente precisam se comunicar com agentes no host sem passar pela pilha TCP/IP de rede do cliente (`vsock`), inicializar geradores criptográficos instantaneamente no boot (`entropy device`), receber credenciais temporárias de IAM (`metadata service`) ou escalar memória verticalmente sob demanda (`memory hotplugging`). O README oficial do Firecracker lista cada uma dessas capacidades.

## Como funciona
Através da API do VMM, o administrador pode habilitar: (1) um socket **`vsock`** (`docs/vsock.md`), criando um canal de comunicação direto por Context ID (CID) e porta entre processos dentro da microVM e um socket UNIX no host; (2) um **dispositivo de entropia** (`docs/entropy.md`) que alimenta o pool de números aleatórios do kernel guest a partir do host; (3) um dispositivo **`pmem`** (`docs/pmem.md`) para mapeamento eficiente de armazenamento; (4) `[BETA]` a árvore de dados do **serviço de metadados voltado ao guest** (MMDS, disponível ao convidado apenas se este recurso for explicitamente configurado); (5) configuração e gerenciamento de **memory hotplugging** (`docs/memory-hotplug.md`); e (6) `[Developer Preview]` **hot-plug e hot-unplug** de dispositivos virtio PCI com a VM em execução (`docs/device-hotplug.md`).

## Exemplo
```bash
# Configurar um dispositivo vsock (guest CID 3) na microVM via API do Firecracker
curl --unix-socket /tmp/firecracker.socket -i -X PUT "http://localhost/vsock" \
  -H "Content-Type: application/json" \
  -d '{"guest_cid": 3, "uds_path": "./v.sock"}'
```

## Limites e trade-offs
Recursos marcados como `[BETA]` (como o serviço de metadados guest-facing) ou `[Developer Preview]` (como o hot-plug e hot-unplug de dispositivos virtio PCI com a VM em execução) podem sofrer evolução de contrato de API entre releases trimestrais e exigem versões de kernel guest compatíveis com os respectivos drivers (`virtio-mem`, PCI hotplug).

## Como verificar
Com o dispositivo `vsock` configurado antes do boot, inicie um ouvinte dentro da microVM e conecte-se a partir do host usando o socket UNIX `uds_path` para validar a troca bidirecional de bytes fora da rede TCP/IP.

## Conexões
- [[firecracker-dispositivos-bloco-rede-rate-limiters-rescan]] — Veja também: AWS Firecracker: dispositivos de bloco, interfaces de rede, re-scan dinâmico de disco e Rate Limiters virtio.
- [[firecracker-jailer-isolamento-cgroups-namespaces-seccomp]] — Veja também: AWS Firecracker: defesa em profundidade em produção com o processo Jailer e filtros seccomp por thread.
- [[firecracker-microvms-kvm-isolamento-serverless-multitenant]] — Referência cruzada direta com firecracker-microvms-kvm-isolamento-serverless-multitenant.
- [[firecracker-api-openapi-configuracao-vcpu-memoria-boot]] — Referência cruzada direta com firecracker-api-openapi-configuracao-vcpu-memoria-boot.

## Fontes
- [AWS Firecracker GitHub — README.md (MicroVM VMM, OpenAPI Socket, Rate Limiters, Jailer & Tested Platforms)](https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md) — README oficial do AWS Firecracker (Apache-2.0) documentando capacidades da API REST sobre socket UNIX, CPU templates, rate limiters virtio, demand fault paging, processo jailer, seccomp por thread e matriz de plataformas Intel/AMD/Graviton; consultado em 2026-10-03.
- [AWS Firecracker Documentation — Design, Specification & Production Host Setup](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md) — Documentação oficial de design, compromissos de performance (SPECIFICATION.md) e endurecimento de host Linux (prod-host-setup.md) do Firecracker; consultado em 2026-10-03.
- [AWS Firecracker — Official GitHub Repository](https://github.com/firecracker-microvm/firecracker) — Repositório oficial do VMM Firecracker mantido pela AWS; consultado em 2026-10-03.
