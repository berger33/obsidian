---
id: software.devops.tranche13.001243
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

# Nydus: Deduplicação em Nível de Chunk (Cross-Layer e Cross-Image) e Algoritmos de Compressão (LZ4, Zstd, GZip)

## Em uma frase
Ao contrário do modelo OCI tradicional que deduplica apenas camadas inteiras idênticas, o Nydus achata os metadados (`flattened metadata tree`) e aplica deduplicação endereçável por conteúdo em nível de **chunk de 1 MB** tanto entre camadas da mesma imagem (`cross-layer`) quanto entre imagens distintas no mesmo nó (`cross-image`), suportando compressão por chunk.

## Por que importa
No formato OCI padrão, se um único arquivo de 10 KB mudar dentro de uma camada de 500 MB na versão `v1.0.1` da aplicação, o nó precisa baixar novamente os 500 MB inteiros da nova camada.

## Como funciona
No Nydus, os arquivos são divididos em chunks de 1 MB comprimidos individualmente com **LZ4** (`LZ4Block`), **Zstd**, **GZip** ou sem compressão (`None`), e identificados pelo digest criptográfico na `OndiskChunkInfo`. Se a imagem `v1.0.1` compartilha 99% dos chunks de 1 MB com a `v1.0.0` já presente no `blobcache` do nó, apenas os chunks novos são baixados da rede.

## Exemplo
```bash
# Inspecionar a tabela de blobs e estatisticas de chunks de uma imagem Nydus:
nydusify check --target ghcr.io/org/app:v1.0.0-nydus-v6
```

## Limites e trade-offs
Escolher `GZip` em vez de `LZ4Block` ou `Zstd` para os chunks da imagem Nydus aumenta a latência de descompressão de CPU durante leituras aleatórias em tempo de execução.

## Como verificar
Utilize `lz4_block` (padrão focado em velocidade de descompressão) ou `zstd` (melhor taxa de compressão com alta velocidade) ao construir imagens com `nydusify` ou `nydus-image`.

## Conexões
- [[nydus-rafs-v5-fuse-vs-rafs-v6-erofs-in-kernel-performance]] — Veja também: Nydus: Evolução do Formato RAFS v5 (FUSE/virtiofs) para RAFS v6 (EROFS In-Kernel).
- [[nydus-ecossistema-ferramentas-nydusd-nydusify-nydus-image-nydusctl]] — Veja também: Nydus: Ferramentas do Ecossistema (nydusd, nydus-image, nydusify e nydusctl).

## Fontes
- [Nydus Image Service GitHub — README.md (RAFS On-Demand Layer Format, nydusify, nydusd, EROFS/FUSE & Containerd Snapshotter)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md) — README oficial do dragonflyoss/nydus detalhando o formato RAFS, inicialização de containers em milissegundos, ferramentas (nydus-image, nydusd, nydusify, nydusctl) e integração com Harbor e Dragonfly; consultado em 2026-10-03.
- [Nydus Official Architecture — docs/nydus-design.md (Bootstrap vs Data Blobs, Chunk Deduplication, Digest Authentication & Zran)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md) — Documento oficial de design arquitetural do Nydus explicando a separação entre metadados (bootstrap) e dados (blobs de chunks), verificação por Merkle tree e modos FUSE/virtiofs/EROFS; consultado em 2026-10-03.
- [Nydus Image Service — Official GitHub Repository](https://github.com/dragonflyoss/nydus) — Repositório oficial do Nydus no projeto Dragonfly; consultado em 2026-10-03.
