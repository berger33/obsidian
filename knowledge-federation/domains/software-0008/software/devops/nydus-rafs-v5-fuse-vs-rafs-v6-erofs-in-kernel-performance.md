---
id: software.devops.tranche13.001242
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

# Nydus: Evolução do Formato RAFS v5 (FUSE/virtiofs) para RAFS v6 (EROFS In-Kernel)

## Em uma frase
O formato de sistema de arquivos do Nydus possui duas gerações principais: **RAFS v5** (servido em espaço de usuário via protocolo **FUSE** ou **virtiofs** para containers `runc` e Kata Containers) e **RAFS v6** (compatível nativamente com o sistema de arquivos somente leitura **EROFS** com `fscache` dentro do kernel Linux).

## Por que importa
Embora o FUSE em espaço de usuário do RAFS v5 acelere drasticamente o tempo de boot do container, leituras intensivas de pequenos arquivos após o boot sofrem overhead de trocas de contexto entre kernel e user-space.

## Como funciona
No **RAFS v6**, o layout em disco é compatível com o **EROFS** in-kernel combinando `fscache` e `overlayfs`: quando os chunks já estão presentes no cache local do nó, as leituras de arquivos são atendidas diretamente pelo kernel Linux em velocidade nativa de disco sem passar por FUSE, acionando o daemon `nydusd` apenas quando ocorre falta de página (cache miss) que exige buscar o chunk na rede.

## Exemplo
```bash
# Converter uma imagem OCI para o formato Nydus RAFS v6 com nydusify:
nydusify convert \
  --source ghcr.io/org/app:v1.0.0 \
  --target ghcr.io/org/app:v1.0.0-nydus-v6 \
  --fs-version 6
```

## Limites e trade-offs
Tentar montar imagens RAFS v6 em modo EROFS/`fscache` nativo em nós com kernels Linux antigos que não possuem suporte aos módulos `erofs` e `cachefiles` faz a montagem falhar se o fallback FUSE não estiver configurado.

## Como verificar
Verifique a versão do kernel Linux dos nós (recomendado Linux 5.19+ para EROFS sobre `fscache`) ou utilize o modo FUSE quando operar em kernels legados.

## Conexões
- [[nydus-arquitetura-rafs-bootstrap-blobfile-lazy-pulling]] — Veja também: Nydus: Arquitetura RAFS (Bootstrap de Metadados e Blobfile em Chunks de 1 MB) para Lazy Pulling.
- [[nydus-deduplicacao-chunks-cross-layer-cross-image-compressao]] — Veja também: Nydus: Deduplicação em Nível de Chunk (Cross-Layer e Cross-Image) e Algoritmos de Compressão (LZ4, Zstd, GZip).

## Fontes
- [Nydus Image Service GitHub — README.md (RAFS On-Demand Layer Format, nydusify, nydusd, EROFS/FUSE & Containerd Snapshotter)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md) — README oficial do dragonflyoss/nydus detalhando o formato RAFS, inicialização de containers em milissegundos, ferramentas (nydus-image, nydusd, nydusify, nydusctl) e integração com Harbor e Dragonfly; consultado em 2026-10-03.
- [Nydus Official Architecture — docs/nydus-design.md (Bootstrap vs Data Blobs, Chunk Deduplication, Digest Authentication & Zran)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md) — Documento oficial de design arquitetural do Nydus explicando a separação entre metadados (bootstrap) e dados (blobs de chunks), verificação por Merkle tree e modos FUSE/virtiofs/EROFS; consultado em 2026-10-03.
- [Nydus Image Service — Official GitHub Repository](https://github.com/dragonflyoss/nydus) — Repositório oficial do Nydus no projeto Dragonfly; consultado em 2026-10-03.
