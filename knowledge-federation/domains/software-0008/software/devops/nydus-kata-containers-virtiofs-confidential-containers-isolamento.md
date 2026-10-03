---
id: software.devops.tranche13.001249
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md", "https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md", "https://github.com/dragonflyoss/nydus"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nydus: Aceleração de Kata Containers (virtiofs) e Confidential Containers com Nydus

## Em uma frase
O Nydus suporta não apenas containers baseados em namespaces do kernel (`runc`), mas também runtimes isolados por máquina virtual leve como **Kata Containers** (via protocolo **virtiofs** e helper `nydus-overlayfs`) e **Confidential Containers**.

## Por que importa
Containers baseados em micro-VMs (Kata Containers) precisam expor o sistema de arquivos raiz da imagem para dentro do kernel guest da VM; baixar gigabytes para dentro da VM antes do boot multiplica a latência de inicialização.

## Como funciona
Com o protocolo `virtiofs` do `nydusd` e o helper de montagem `nydus-overlayfs` do `containerd`, o diretório de montagem RAFS/overlayfs é compartilhado diretamente com a micro-VM do Kata Containers, permitindo lazy pulling de chunks de 1 MB com verificação de integridade fim-a-fim (essencial para Confidential Containers contra adulteração de host).

## Exemplo
```bash
# Verificar no nydusd o suporte e status de sessoes virtiofs/FUSE:
nydusctl --sock /run/nydusd/nydusd.sock info
```

## Limites e trade-offs
Utilizar o protocolo 9p legado no Kata Containers em vez de `virtiofs` ao montar sistemas de arquivos do Nydus degrada severamente a vazão de leitura de arquivos dentro da micro-VM.

## Como verificar
Configure o runtime do Kata Containers para utilizar `virtiofs` integrado ao `nydus-overlayfs` e `nydusd`.

## Conexões
- [[nydus-snapshotter-containerd-kubernetes-nerdctl-implantacao]] — Veja também: Nydus: Implantação no Kubernetes e containerd com nydus-snapshotter e nerdctl.
- [[nydus-storage-backends-registry-oss-s3-nas-blobcache-gestao]] — Veja também: Nydus: Backends de Armazenamento (Registry, S3/OSS, NAS, Localfs) e Gestão do BlobCache.

## Fontes
- [Nydus Image Service GitHub — README.md (RAFS On-Demand Layer Format, nydusify, nydusd, EROFS/FUSE & Containerd Snapshotter)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md) — README oficial do dragonflyoss/nydus detalhando o formato RAFS, inicialização de containers em milissegundos, ferramentas (nydus-image, nydusd, nydusify, nydusctl) e integração com Harbor e Dragonfly; consultado em 2026-10-03.
- [Nydus Official Architecture — docs/nydus-design.md (Bootstrap vs Data Blobs, Chunk Deduplication, Digest Authentication & Zran)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md) — Documento oficial de design arquitetural do Nydus explicando a separação entre metadados (bootstrap) e dados (blobs de chunks), verificação por Merkle tree e modos FUSE/virtiofs/EROFS; consultado em 2026-10-03.
- [Nydus Image Service — Official GitHub Repository](https://github.com/dragonflyoss/nydus) — Repositório oficial do Nydus no projeto Dragonfly; consultado em 2026-10-03.
