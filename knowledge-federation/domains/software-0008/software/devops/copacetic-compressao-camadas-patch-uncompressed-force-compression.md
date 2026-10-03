---
id: software.devops.tranche15.001406
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://project-copacetic.github.io/copacetic/website/quick-start", "https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md", "https://github.com/project-copacetic/copacetic"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Project Copacetic: controle de compressão da camada de patch (`--compression` e `--force-compression`)

## Em uma frase
Em exportações locais, o Copacetic armazena as novas camadas de patch com `--compression=uncompressed` por padrão para garantir leitura confiável por scanners de vulnerabilidades, preservando a compressão original das camadas base.

## Por que importa
Se uma ferramenta de patching recodificasse todas as camadas da imagem base ao aplicar um patch de poucos megabytes, ela alteraria os digests SHA-256 de todas as camadas anteriores, destruindo o cache de camadas nos nós Kubernetes e aumentando o custo de tráfego no registry.

## Como funciona
Por padrão, o `copa` mantém os blobs das camadas base intactos em sua compressão original (gzip ou zstd) e adiciona apenas a camada diferencial. Caso o operador deseje padronizar a compressão de todas as camadas exportadas da plataforma corrigida, pode acionar `--force-compression` junto a `--compression` (por exemplo `gzip` ou `zstd`).

## Exemplo
```bash
copa patch -i docker.io/library/nginx:1.21.6 -r nginx-report.json --compression gzip -t 1.21.6-gzip
```

## Limites e trade-offs
Ativar `--force-compression` re-encoda as camadas exportadas da plataforma corrigida, o que invalida o compartilhamento de blobs preexistentes com a imagem base original no registry.

## Como verificar
Inspecione o manifesto OCI da imagem corrigida (`docker buildx imagetools inspect` ou `crane manifest`) e verifique que os digests das camadas inferiores coincidem com os da imagem original quando `--force-compression` não é utilizado.

## Conexões
- [[copacetic-autodeteccao-instancias-buildkit-docker-buildx-socket]] — Veja também: Project Copacetic: autodeteccão e configuração de endpoints BuildKit (`--addr`).
- [[copacetic-multi-platform-patching-oci-image-index-preservacao]] — Veja também: Project Copacetic: aplicação de patches em imagens multiplataforma e preservação de OCI Image Index.

## Fontes
- [Project Copacetic GitHub — README.md (Direct Container Image Patching, BuildKit Engine, Ubuntu Chiseled Images & Extensible Adapters)](https://project-copacetic.github.io/copacetic/website/quick-start) — README oficial do project-copacetic/copacetic (CNCF Sandbox) detalhando a arquitetura de patching direto sem rebuild, suporte a Ubuntu Chiseled e integração com scanners; consultado em 2026-10-03.
- [Project Copacetic Official Documentation — Quick Start (Targeted vs Comprehensive Patching, Trivy Reports, BuildKit Auto-Detection & Compression)](https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md) — Guia oficial Quick Start do Copacetic demonstrando o fluxo completo de scan com Trivy, patching direcionado (-r) vs abrangente, controle de compressão e verificação; consultado em 2026-10-03.
- [Project Copacetic — Official GitHub Repository](https://github.com/project-copacetic/copacetic) — Repositório oficial Apache-2.0 do Project Copacetic na CNCF; consultado em 2026-10-03.
