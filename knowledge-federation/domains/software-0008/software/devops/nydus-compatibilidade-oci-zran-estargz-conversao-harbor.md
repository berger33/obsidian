---
id: software.devops.tranche13.001247
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

# Nydus: Compatibilidade com Imagens OCI Nativas (OCI zran), eStargz e Conversão Automática no Harbor

## Em uma frase
Além de seu formato nativo RAFS, o Nydus suporta nativamente imagens **eStargz** e o índice **OCI zran** (que permite fazer lazy pulling diretamente de imagens OCI `tar.gz` existentes sem reempacotar os blobs de dados), além de integrar-se ao **Harbor Acceleration Service** para conversão automática no push.

## Por que importa
Nem sempre uma equipe pode alterar os pipelines de build de centenas de imagens de terceiros para rodar `nydusify` manualmente antes do deploy.

## Como funciona
Com o serviço de aceleração do Harbor (`goharbor/acceleration-service`), sempre que uma imagem OCI comum recebe push no Harbor, um webhook aciona automaticamente o conversor Nydus e publica a variante acelerada no mesmo repositório. Alternativamente, o modo `zran` do Nydus gera apenas um pequeno índice de descompactação aleatória sobre os arquivos `.tar.gz` originais da imagem OCI.

## Exemplo
```bash
# Gerar indice de aceleracao mantendo compatibilidade com camadas OCI:
nydusify convert \
  --source docker.io/library/nginx:1.25 \
  --target registry.internal/library/nginx:1.25-nydus
```

## Limites e trade-offs
Remover a imagem OCI original e publicar exclusivamente camadas Nydus sem manter um OCI Image Index dual-format impede que clientes Docker padrão (que não têm `nydus-snapshotter`) façam pull daquela tag.

## Como verificar
Use a flag `--merge-platform` no `nydusify convert` (ou o Harbor Acceleration Service) para publicar um manifesto OCI Index que contém tanto a imagem OCI padrão quanto a variante Nydus sob a mesma tag.

## Conexões
- [[nydus-prefetch-otimizacao-layout-io-amplification-cold-start]] — Veja também: Nydus: Tabela de Prefetch (PrefetchTable), Amplificação de I/O e Otimização de Leituras no Boot.
- [[nydus-snapshotter-containerd-kubernetes-nerdctl-implantacao]] — Veja também: Nydus: Implantação no Kubernetes e containerd com nydus-snapshotter e nerdctl.

## Fontes
- [Nydus Image Service GitHub — README.md (RAFS On-Demand Layer Format, nydusify, nydusd, EROFS/FUSE & Containerd Snapshotter)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md) — README oficial do dragonflyoss/nydus detalhando o formato RAFS, inicialização de containers em milissegundos, ferramentas (nydus-image, nydusd, nydusify, nydusctl) e integração com Harbor e Dragonfly; consultado em 2026-10-03.
- [Nydus Official Architecture — docs/nydus-design.md (Bootstrap vs Data Blobs, Chunk Deduplication, Digest Authentication & Zran)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md) — Documento oficial de design arquitetural do Nydus explicando a separação entre metadados (bootstrap) e dados (blobs de chunks), verificação por Merkle tree e modos FUSE/virtiofs/EROFS; consultado em 2026-10-03.
- [Nydus Image Service — Official GitHub Repository](https://github.com/dragonflyoss/nydus) — Repositório oficial do Nydus no projeto Dragonfly; consultado em 2026-10-03.
