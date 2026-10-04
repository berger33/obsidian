---
id: software.devops.tranche08.000713
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

# AWS Firecracker: dispositivos de bloco, interfaces de rede, re-scan dinâmico de disco e Rate Limiters virtio

## Em uma frase
A API do Firecracker permite anexar interfaces de rede e discos somente-leitura ou leitura-escrita baseados em arquivos, trocar o arquivo subjacente, disparar re-scan de tamanho de bloco a quente e aplicar Rate Limiters por largura de banda e IOPS.

## Por que importa
Em um servidor bare-metal que hospeda centenas de microVMs de diferentes tenants, uma única microVM que execute um loop intensivo de gravação em disco ou inundação de pacotes de rede poderia saturar o barramento NVMe ou a placa de rede física do host (noisy neighbor). Segundo a seção `Features & Capabilities` do README oficial do Firecracker, os **rate limiters** embutidos nos dispositivos `virtio` garantem isolamento previsível de I/O sem depender de controladores externos complexos.

## Como funciona
Por meio da API do Firecracker, o host pode: (1) adicionar uma ou mais interfaces de rede virtuais (`virtio-net` conectadas a dispositivos TAP no host); (2) adicionar um ou mais discos (`virtio-block`) em modo leitura-escrita (`read-write`) ou somente-leitura (`read-only`), cada um representado por um dispositivo de bloco apoiado em arquivo no host; (3) alterar o arquivo subjacente (`backing file`) de um dispositivo de bloco antes ou depois do boot do guest; (4) disparar um **re-scan de dispositivo de bloco** enquanto o guest está rodando, permitindo que o SO convidado detecte aumentos de tamanho no arquivo de imagem a quente; e (5) configurar **rate limiters** (baseados em token buckets) para dispositivos virtio, limitando bytes por segundo (largura de banda), operações por segundo (IOPS/pacotes) ou ambos.

## Exemplo
```bash
# Anexar o disco raiz com Rate Limiter de largura de banda e IOPS via API do Firecracker
curl --unix-socket /tmp/firecracker.socket -i -X PUT "http://localhost/drives/rootfs" \
  -H "Content-Type: application/json" \
  -d '{
    "drive_id": "rootfs",
    "path_on_host": "/srv/vm/rootfs.ext4",
    "is_root_device": true,
    "is_read_only": false,
    "rate_limiter": {
      "bandwidth": { "size": 10485760, "refill_time": 1000 },
      "ops": { "size": 500, "refill_time": 1000 }
    }
  }'
```

## Limites e trade-offs
Como cada disco no Firecracker é representado por um dispositivo de bloco apoiado em arquivo (`file-backed block device`) via `virtio-block` (ou `pmem`), compartilhar diretórios dinâmicos de árvore de arquivos do host diretamente com o guest não utiliza `virtio-fs` nativo no Firecracker; para injetar novos pacotes ou expandir armazenamento com a microVM ativa, utiliza-se a troca do `backing file` ou o redimensionamento do arquivo seguido de `PATCH /drives/<id>` para acionar o re-scan.

## Como verificar
Após redimensionar o arquivo de imagem no host e enviar `PATCH` para `/drives/rootfs` no socket da API, execute `lsblk` dentro do guest Linux para confirmar que o novo tamanho do dispositivo de bloco foi reconhecido sem reboot.

## Conexões
- [[firecracker-api-openapi-configuracao-vcpu-memoria-boot]] — Veja também: AWS Firecracker: configuração da microVM via API OpenAPI (vCPUs, memória, CPU templates e boot).
- [[firecracker-vsock-entropy-pmem-metadata-hotplug]] — Veja também: AWS Firecracker: dispositivos vsock, entropia, pmem, serviço de metadados MMDS e hotplug de memória/PCI.
- [[firecracker-microvms-kvm-isolamento-serverless-multitenant]] — Referência cruzada direta com firecracker-microvms-kvm-isolamento-serverless-multitenant.

## Fontes
- [AWS Firecracker GitHub — README.md (MicroVM VMM, OpenAPI Socket, Rate Limiters, Jailer & Tested Platforms)](https://raw.githubusercontent.com/firecracker-microvm/firecracker/main/README.md) — README oficial do AWS Firecracker (Apache-2.0) documentando capacidades da API REST sobre socket UNIX, CPU templates, rate limiters virtio, demand fault paging, processo jailer, seccomp por thread e matriz de plataformas Intel/AMD/Graviton; consultado em 2026-10-03.
- [AWS Firecracker Documentation — Design, Specification & Production Host Setup](https://github.com/firecracker-microvm/firecracker/blob/main/docs/design.md) — Documentação oficial de design, compromissos de performance (SPECIFICATION.md) e endurecimento de host Linux (prod-host-setup.md) do Firecracker; consultado em 2026-10-03.
- [AWS Firecracker — Official GitHub Repository](https://github.com/firecracker-microvm/firecracker) — Repositório oficial do VMM Firecracker mantido pela AWS; consultado em 2026-10-03.
