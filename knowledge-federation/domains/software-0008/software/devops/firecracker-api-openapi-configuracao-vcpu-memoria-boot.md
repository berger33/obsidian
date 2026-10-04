---
id: software.devops.tranche08.000712
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

# AWS Firecracker: configuração da microVM via API OpenAPI (vCPUs, memória, CPU templates e boot)

## Em uma frase
O processo VMM do Firecracker é controlado por um endpoint de API REST (especificado em OpenAPI) que configura o número de vCPUs (padrão `1`), tamanho de memória (padrão `128 MiB`), CPU templates, imagem de kernel, rootfs e argumentos de boot.

## Por que importa
Em plataformas de computação serverless que criam centenas de microVMs por minuto, passar dezenas de flags complexas de linha de comando ou arquivos XML estáticos dificulta a automação programática e a modificação a quente de recursos. De acordo com a seção `Features & Capabilities` do README oficial do Firecracker, toda a configuração pré-boot e o controle em tempo de execução ocorrem por chamadas estruturadas à API do VMM.

## Como funciona
Após iniciar o processo `firecracker --api-sock /tmp/firecracker.socket`, o orquestrador no host envia requisições HTTP `PUT`/`PATCH` em JSON para o socket UNIX: (1) `/machine-config` define o número de vCPUs (o padrão é `1`) e o tamanho da memória RAM (o padrão é `128 MiB`), além de permitir aplicar um **CPU template** (`docs/cpu_templates/cpu-templates.md`) para mascarar recursos da CPU e garantir compatibilidade de instruções entre gerações de processadores; (2) `/boot-source` define o caminho da imagem do kernel Linux guest e os argumentos de linha de comando de boot (`boot_args`); (3) `/drives/*` anexa o sistema de arquivos raiz (`rootfs`); e (4) `/actions` com `InstanceStart` dá a partida na microVM (e, em `x86_64`, permite acionar a parada da microVM).

## Exemplo
```bash
# Configurar machine-config (2 vCPUs e 256 MiB de RAM) e dar partida na microVM via socket UNIX da API
curl --unix-socket /tmp/firecracker.socket -i -X PUT "http://localhost/machine-config" \
  -H "Accept: application/json" -H "Content-Type: application/json" \
  -d '{"vcpu_count": 2, "mem_size_mib": 256}'

curl --unix-socket /tmp/firecracker.socket -i -X PUT "http://localhost/actions" \
  -H "Accept: application/json" -H "Content-Type: application/json" \
  -d '{"action_type": "InstanceStart"}'
```

## Limites e trade-offs
Conforme documentado na lista de capacidades da API no README oficial do Firecracker, a ação de parar a microVM via API (`Stop the microVM` / `SendCtrlAltDel`) é suportada apenas na arquitetura `x86_64`; em outras arquiteturas suportadas (como `aarch64`), o encerramento gracioso do convidado deve ser coordenado por dentro do sistema operacional guest (ex.: via `vsock` ou agente interno) antes de encerrar o processo VMM.

## Como verificar
Consulte `GET http://localhost/machine-config` através do `--unix-socket` do Firecracker para confirmar que `vcpu_count` e `mem_size_mib` foram aplicados antes de disparar `InstanceStart`.

## Conexões
- [[firecracker-microvms-kvm-isolamento-serverless-multitenant]] — Veja também: AWS Firecracker: tecnologia de virtualização de microVMs sobre KVM para workloads serverless e multi-tenant.
- [[firecracker-dispositivos-bloco-rede-rate-limiters-rescan]] — Veja também: AWS Firecracker: dispositivos de bloco, interfaces de rede, re-scan dinâmico de disco e Rate Limiters virtio.
- [[firecracker-jailer-isolamento-cgroups-namespaces-seccomp]] — Referência cruzada direta com firecracker-jailer-isolamento-cgroups-namespaces-seccomp.

## Fontes
- [AWS Firecracker GitHub — README.md (MicroVM VMM, OpenAPI Socket, Rate Limiters, Jailer & Tested Platforms)](https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md) — README oficial do AWS Firecracker (Apache-2.0) documentando capacidades da API REST sobre socket UNIX, CPU templates, rate limiters virtio, demand fault paging, processo jailer, seccomp por thread e matriz de plataformas Intel/AMD/Graviton; consultado em 2026-10-03.
- [AWS Firecracker Documentation — Design, Specification & Production Host Setup](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md) — Documentação oficial de design, compromissos de performance (SPECIFICATION.md) e endurecimento de host Linux (prod-host-setup.md) do Firecracker; consultado em 2026-10-03.
- [AWS Firecracker — Official GitHub Repository](https://github.com/firecracker-microvm/firecracker) — Repositório oficial do VMM Firecracker mantido pela AWS; consultado em 2026-10-03.
