---
id: software.devops.tranche15.001407
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

# Project Copacetic: aplicação de patches em imagens multiplataforma e preservação de OCI Image Index

## Em uma frase
O Copacetic suporta o patching de imagens multiplataforma (como `linux/amd64` e `linux/arm64`), atualizando as arquiteturas selecionadas e preservando inalterados os blobs e compressões das demais plataformas no índice OCI.

## Por que importa
Imagens oficiais no Docker Hub e no GHCR são publicadas como manifest lists cobrindo meia dúzia de arquiteturas; perder o suporte multi-arch ao aplicar um patch de segurança quebraria clusters híbridos com nós x86_64 e ARM64 (como AWS Graviton).

## Como funciona
Ao processar uma imagem referenciada por manifesto multi-arch, o `copa` aplica o fluxo BuildKit para as plataformas alvo (utilizando QEMU ou builders remotos por arquitetura) e reconstrói o OCI Image Index mantendo os descritores originais das plataformas não modificadas.

## Exemplo
```bash
copa patch -i docker.io/library/nginx:1.21.6 --platform linux/amd64,linux/arm64 -t 1.21.6-multiarch
```

## Limites e trade-offs
Aplicar patches para arquiteturas diferentes da CPU do host via emulação QEMU é significativamente mais lento do que usar instâncias nativas de BuildKit por arquitetura configuradas no `buildx`.

## Como verificar
Inspecione o índice gerado com `docker buildx imagetools inspect` e confirme a presença dos manifestos `linux/amd64` e `linux/arm64` atualizados.

## Conexões
- [[copacetic-compressao-camadas-patch-uncompressed-force-compression]] — Veja também: Project Copacetic: controle de compressão da camada de patch (`--compression` e `--force-compression`).
- [[copacetic-arquitetura-extensivel-adaptadores-pkgmgr-scanners]] — Veja também: Project Copacetic: arquitetura extensível de adaptadores de gerenciadores de pacotes e scanners.

## Fontes
- [Project Copacetic GitHub — README.md (Direct Container Image Patching, BuildKit Engine, Ubuntu Chiseled Images & Extensible Adapters)](https://project-copacetic.github.io/copacetic/website/quick-start) — README oficial do project-copacetic/copacetic (CNCF Sandbox) detalhando a arquitetura de patching direto sem rebuild, suporte a Ubuntu Chiseled e integração com scanners; consultado em 2026-10-03.
- [Project Copacetic Official Documentation — Quick Start (Targeted vs Comprehensive Patching, Trivy Reports, BuildKit Auto-Detection & Compression)](https://raw.githubusercontent.com/project-copacetic/copacetic/main/README.md) — Guia oficial Quick Start do Copacetic demonstrando o fluxo completo de scan com Trivy, patching direcionado (-r) vs abrangente, controle de compressão e verificação; consultado em 2026-10-03.
- [Project Copacetic — Official GitHub Repository](https://github.com/project-copacetic/copacetic) — Repositório oficial Apache-2.0 do Project Copacetic na CNCF; consultado em 2026-10-03.
