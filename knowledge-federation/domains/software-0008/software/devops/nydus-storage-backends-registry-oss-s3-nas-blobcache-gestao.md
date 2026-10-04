---
id: software.devops.tranche13.001250
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
fontes: ["https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md", "https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md", "https://github.com/dragonflyoss/nydus"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nydus: Backends de Armazenamento (Registry, S3/OSS, NAS, Localfs) e Gestão do BlobCache

## Em uma frase
O `nydusd` abstrai a origem dos chunks de dados por meio de múltiplos backends de armazenamento configuráveis — **Registry OCI** (Docker Hub, Harbor, GHCR, ECR, ACR), **Object Storage** (S3/OSS), **NAS / Shared Disk**, **Localfs** (`nydus-backend-proxy`) e **Dragonfly P2P** — combinados com o diretório local `blobcache`.

## Por que importa
Em ambientes onde todos os nós já compartilham um armazenamento NAS de baixa latência ou um bucket S3 dentro da mesma VPC, buscar os blobs diretamente do S3/NAS pode ser mais rápido e barato do que passar pela camada de API HTTP do registry OCI.

## Como funciona
Na configuração do `nydusd`, define-se o `backend` (`type: "registry"`, `"oss"`, `"s3"` ou `"localfs"`) e o `cache` (`type: "blobcache"`, `work_dir: "/var/lib/nydus/cache"`). Como o design do `blobcache` assume que apenas a fração efetivamente lida da imagem é baixada, o gerenciamento de espaço em disco nos nós é feito pelo coletor de lixo do `nydus-snapshotter`.

## Exemplo
```json
{
  "device": {
    "backend": {
      "type": "registry",
      "config": {
        "scheme": "https",
        "host": "ghcr.io",
        "timeout": 5,
        "connect_timeout": 5
      }
    },
    "cache": {
      "type": "blobcache",
      "config": {
        "work_dir": "/var/lib/nydus/cache"
      }
    }
  }
}
```

## Limites e trade-offs
Deixar o diretório `work_dir` do `blobcache` crescer indefinidamente em nós de longa duração sem habilitar a coleta de lixo de blobs órfãos no `nydus-snapshotter` acaba esgotando o armazenamento local do nó.

## Como verificar
Habilite a política de Garbage Collection no `nydus-snapshotter` para limpar periodicamente blobs do `work_dir` que não pertencem mais a nenhum container ou imagem ativa no `containerd`.

## Conexões
- [[nydus-kata-containers-virtiofs-confidential-containers-isolamento]] — Veja também: Nydus: Aceleração de Kata Containers (virtiofs) e Confidential Containers com Nydus.

## Fontes
- [Nydus Image Service GitHub — README.md (RAFS On-Demand Layer Format, nydusify, nydusd, EROFS/FUSE & Containerd Snapshotter)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md) — README oficial do dragonflyoss/nydus detalhando o formato RAFS, inicialização de containers em milissegundos, ferramentas (nydus-image, nydusd, nydusify, nydusctl) e integração com Harbor e Dragonfly; consultado em 2026-10-03.
- [Nydus Official Architecture — docs/nydus-design.md (Bootstrap vs Data Blobs, Chunk Deduplication, Digest Authentication & Zran)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md) — Documento oficial de design arquitetural do Nydus explicando a separação entre metadados (bootstrap) e dados (blobs de chunks), verificação por Merkle tree e modos FUSE/virtiofs/EROFS; consultado em 2026-10-03.
- [Nydus Image Service — Official GitHub Repository](https://github.com/dragonflyoss/nydus) — Repositório oficial do Nydus no projeto Dragonfly; consultado em 2026-10-03.
