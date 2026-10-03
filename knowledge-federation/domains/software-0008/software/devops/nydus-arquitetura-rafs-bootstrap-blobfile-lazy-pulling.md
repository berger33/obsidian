---
id: software.devops.tranche13.001241
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

# Nydus: Arquitetura RAFS (Bootstrap de Metadados e Blobfile em Chunks de 1 MB) para Lazy Pulling

## Em uma frase
O **Nydus** (`dragonflyoss/nydus`, escrito em Rust) é o serviço de aceleração de imagens de containers do ecossistema Dragonfly que substitui o download sequencial de camadas `tar.gz` inteiras por um sistema de arquivos endereçável por conteúdo no formato **RAFS**, reduzindo o cold start de containers grandes de minutos para segundos.

## Por que importa
Na especificação OCI tradicional, o `containerd` precisa baixar e descompactar no disco local 100% dos gigabytes de uma imagem antes de iniciar o processo do container, mesmo que a execução leia apenas 5% dos arquivos.

## Como funciona
O Nydus divide a imagem de container em duas partes compatíveis com registries OCI: o **bootstrap** (uma árvore de Merkle compacta contendo todos os inodes, diretórios, symlinks, xattrs e hashes dos dados) e um ou mais **blobfiles** (dados dos arquivos fatiados em chunks fixos de 1 MB e deduplicados). Para iniciar o container, basta baixar o pequeno arquivo `bootstrap` de poucos megabytes; os chunks de dados são buscados sob demanda (`on-demand load`) apenas quando o container lê cada arquivo.

## Exemplo
```bash
# Inspecionar um arquivo bootstrap de imagem Nydus com nydus-image:
nydus-image inspect /var/lib/nydus/bootstrap
nydus-image check --bootstrap /var/lib/nydus/bootstrap
```

## Limites e trade-offs
Executar workloads estritamente sensíveis a latência de primeira leitura de arquivo sem habilitar `prefetch` ou `blobcache` local pode introduzir latência de rede no primeiro `read()` de um binário grande.

## Como verificar
Configure sempre o `blobcache` local no `nydusd` e forneça lista de `prefetch` durante a conversão da imagem com `nydusify`.

## Conexões
- [[nydus-rafs-v5-fuse-vs-rafs-v6-erofs-in-kernel-performance]] — Veja também: Nydus: Evolução do Formato RAFS v5 (FUSE/virtiofs) para RAFS v6 (EROFS In-Kernel).

## Fontes
- [Nydus Image Service GitHub — README.md (RAFS On-Demand Layer Format, nydusify, nydusd, EROFS/FUSE & Containerd Snapshotter)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md) — README oficial do dragonflyoss/nydus detalhando o formato RAFS, inicialização de containers em milissegundos, ferramentas (nydus-image, nydusd, nydusify, nydusctl) e integração com Harbor e Dragonfly; consultado em 2026-10-03.
- [Nydus Official Architecture — docs/nydus-design.md (Bootstrap vs Data Blobs, Chunk Deduplication, Digest Authentication & Zran)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md) — Documento oficial de design arquitetural do Nydus explicando a separação entre metadados (bootstrap) e dados (blobs de chunks), verificação por Merkle tree e modos FUSE/virtiofs/EROFS; consultado em 2026-10-03.
- [Nydus Image Service — Official GitHub Repository](https://github.com/dragonflyoss/nydus) — Repositório oficial do Nydus no projeto Dragonfly; consultado em 2026-10-03.
