---
id: software.devops.tranche13.001244
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

# Nydus: Ferramentas do Ecossistema (nydusd, nydus-image, nydusify e nydusctl)

## Em uma frase
O ecossistema de linha de comando do Nydus é composto por quatro binários principais: **`nydusd`** (daemon de user-space que atende requisições FUSE/fscache e busca chunks nos backends), **`nydus-image`** (construtor e inspetor de camadas RAFS), **`nydusify`** (conversor e validador de alto nível para registries OCI) e **`nydusctl`** (cliente CLI para consultar métricas e reconfigurar o `nydusd` em execução).

## Por que importa
Compreender a função exata de cada binário evita confundir a ferramenta de pipeline de CI (`nydusify`) com o daemon de nó (`nydusd`) ou com o utilitário de diagnóstico local (`nydusctl`).

## Como funciona
No pipeline de build/CI ou no serviço de aceleração do Harbor, o `nydusify` puxa a imagem OCI original, invoca `nydus-image create` para gerar os arquivos de metadados (`bootstrap`) e dados (`blob`) e empurra a imagem convertida de volta ao registry. Nos nós do cluster Kubernetes, o `nydus-snapshotter` do `containerd` gerencia processos `nydusd`, que podem ser inspecionados via socket Unix com `nydusctl`.

## Exemplo
```bash
nydusify convert --source alpine:3.19 --target localhost:5000/alpine:3.19-nydus
nydusctl --sock /run/nydusd/nydusd.sock info
nydusctl --sock /run/nydusd/nydusd.sock metrics
```

## Limites e trade-offs
Rodar um processo `nydusd` separado para cada container individual em um nó com centenas de Pods sem ativar o modo de compartilhamento de daemon do `nydus-snapshotter` multiplica o consumo de memória de processos auxiliares no host.

## Como verificar
Configure o `nydus-snapshotter` para compartilhar instâncias do `nydusd` (multi-mount por daemon) e monitore o status via `nydusctl metrics`.

## Conexões
- [[nydus-deduplicacao-chunks-cross-layer-cross-image-compressao]] — Veja também: Nydus: Deduplicação em Nível de Chunk (Cross-Layer e Cross-Image) e Algoritmos de Compressão (LZ4, Zstd, GZip).
- [[nydus-integridade-fim-a-fim-merkle-tree-sha256-blake3]] — Veja também: Nydus: Verificação de Integridade Fim-a-Fim em Tempo de Execução (Árvore de Merkle com SHA-256 e BLAKE3).

## Fontes
- [Nydus Image Service GitHub — README.md (RAFS On-Demand Layer Format, nydusify, nydusd, EROFS/FUSE & Containerd Snapshotter)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md) — README oficial do dragonflyoss/nydus detalhando o formato RAFS, inicialização de containers em milissegundos, ferramentas (nydus-image, nydusd, nydusify, nydusctl) e integração com Harbor e Dragonfly; consultado em 2026-10-03.
- [Nydus Official Architecture — docs/nydus-design.md (Bootstrap vs Data Blobs, Chunk Deduplication, Digest Authentication & Zran)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md) — Documento oficial de design arquitetural do Nydus explicando a separação entre metadados (bootstrap) e dados (blobs de chunks), verificação por Merkle tree e modos FUSE/virtiofs/EROFS; consultado em 2026-10-03.
- [Nydus Image Service — Official GitHub Repository](https://github.com/dragonflyoss/nydus) — Repositório oficial do Nydus no projeto Dragonfly; consultado em 2026-10-03.
