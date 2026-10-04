---
id: software.devops.tranche08.000715
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

# AWS Firecracker: defesa em profundidade em produção com o processo Jailer e filtros seccomp por thread

## Em uma frase
Para cenários de produção multi-tenant, o Firecracker fornece o binário `jailer` (que aplica barreiras de isolamento via cgroups, namespaces e `chroot` e descarta privilégios antes de executar o VMM) combinado a filtros `seccomp` específicos por thread.

## Por que importa
Embora o KVM isole o código do guest usando virtualização de hardware, o processo VMM do Firecracker roda no espaço de usuário do host; na hipótese extrema de um atacante explorar um bug de emulação virtio para ganhar execução de código dentro do processo VMM, ele ainda precisa ser contido sem acesso ao sistema de arquivos do host ou a outras microVMs. Segundo a seção `Built-in Capabilities` do README oficial do Firecracker, os filtros seccomp por thread e o processo `jailer` formam essa barreira secundária de defesa em profundidade.

## Como funciona
Em produção, em vez de invocar o binário `firecracker` diretamente como `root`, o orquestrador invoca o binário **`jailer`** (`docs/jailer.md`). O `jailer` cria um diretório de jaula isolado para aquela microVM específica, configura os limites de recursos em `cgroups` e o isolamento de `namespaces` (como `net` e `pid`), cria apenas os nós de dispositivo essenciais (`/dev/kvm`, `/dev/net/tun`), executa `chroot` / `pivot_root` para dentro da jaula, reduz seus privilégios mudando para um `uid`/`gid` não privilegiado exclusivo daquela microVM e, por fim, faz `exec` no binário `firecracker`. Dentro do `firecracker`, filtros `seccomp-bpf` avançados e **específicos para cada thread** (thread de VMM, thread de API, threads de vCPU) bloqueiam imediatamente qualquer chamada de sistema que não faça parte da lista mínima estrita daquela thread.

## Exemplo
```bash
# Iniciar uma microVM Firecracker em produção encapsulada pelo processo jailer com UID/GID não privilegiado
sudo jailer --id vm-prod-001 \
  --exec-file /usr/local/bin/firecracker \
  --uid 10001 --gid 10001 \
  --chroot-base-dir /srv/jailer
```

## Limites e trade-offs
Como o `jailer` confina o processo `firecracker` dentro de um diretório `chroot` estrito (`/srv/jailer/firecracker/<id>/root`), o processo VMM não consegue enxergar caminhos arbitrários do host; por isso, a imagem de kernel guest, o arquivo de disco `rootfs` e os arquivos de log/métricas precisam ser vinculados (`hardlink` ou copiados) para dentro da árvore da jaula com permissões do `--uid`/`--gid` antes do boot.

## Como verificar
Inspecione `/proc/<pid-do-firecracker>/status` e `/proc/<pid-do-firecracker>/root` no host enquanto a microVM roda sob o `jailer` para confirmar que o `Uid` efetivo é `10001`, que o `Seccomp` está em modo `2` (filter) e que a raiz está confinada ao diretório da jaula.

## Conexões
- [[firecracker-vsock-entropy-pmem-metadata-hotplug]] — Veja também: AWS Firecracker: dispositivos vsock, entropia, pmem, serviço de metadados MMDS e hotplug de memória/PCI.
- [[firecracker-demand-fault-paging-oversubscription-cpu-memoria]] — Veja também: AWS Firecracker: paginação sob demanda (demand fault paging) e oversubscription de CPU e memória.
- [[firecracker-microvms-kvm-isolamento-serverless-multitenant]] — Referência cruzada direta com firecracker-microvms-kvm-isolamento-serverless-multitenant.
- [[firecracker-api-openapi-configuracao-vcpu-memoria-boot]] — Referência cruzada direta com firecracker-api-openapi-configuracao-vcpu-memoria-boot.
- [[gvisor-arquitetura-sentry-gofer-application-kernel]] — Referência cruzada direta com gvisor-arquitetura-sentry-gofer-application-kernel.

## Fontes
- [AWS Firecracker GitHub — README.md (MicroVM VMM, OpenAPI Socket, Rate Limiters, Jailer & Tested Platforms)](https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md) — README oficial do AWS Firecracker (Apache-2.0) documentando capacidades da API REST sobre socket UNIX, CPU templates, rate limiters virtio, demand fault paging, processo jailer, seccomp por thread e matriz de plataformas Intel/AMD/Graviton; consultado em 2026-10-03.
- [AWS Firecracker Documentation — Design, Specification & Production Host Setup](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md) — Documentação oficial de design, compromissos de performance (SPECIFICATION.md) e endurecimento de host Linux (prod-host-setup.md) do Firecracker; consultado em 2026-10-03.
- [AWS Firecracker — Official GitHub Repository](https://github.com/firecracker-microvm/firecracker) — Repositório oficial do VMM Firecracker mantido pela AWS; consultado em 2026-10-03.
