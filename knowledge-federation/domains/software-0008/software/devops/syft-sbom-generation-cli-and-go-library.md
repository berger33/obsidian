---
id: software.devops.tranche04.000331
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/anchore/syft/main/README.md", "https://oss.anchore.com/docs/guides/sbom/getting-started/", "https://github.com/anchore/syft"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Syft como CLI e biblioteca Go para geração de SBOM de contêineres, diretórios e arquivos

## Em uma frase
O Syft, mantido pela Anchore sob licença Apache-2.0, é uma ferramenta de linha de comando (fornecida como um único executável compilado sem dependências externas) e uma biblioteca Go para gerar **Software Bill of Materials (SBOM)** — uma lista detalhada de todas as bibliotecas e componentes que compõem um software — a partir de imagens de contêiner (OCI, Docker, Singularity), sistemas de arquivos locais (`syft ./my-project`) e arquivos compactados. Ele é projetado para operar em conjunto com scanners de vulnerabilidade como o Grype para detecção rápida e precisa de riscos na cadeia de suprimentos.

## Por que importa
Sem um inventário completo e automatizado das dependências do sistema operacional e das linguagens de programação empacotadas dentro de uma imagem ou diretório, organizações ficam cegas diante de novas vulnerabilidades críticas (zero-days) ou exigências de conformidade de licenças.

## Como funciona
Instale o binário do Syft nos runners de CI (`curl -sSfL https://get.anchore.io/syft | sudo sh -s -- -b /usr/local/bin`, Homebrew ou imagem oficial) e gere um SBOM para cada imagem de contêiner ou artefato compilado antes da publicação.

## Exemplo
Ao empacotar uma aplicação microsserviço em contêiner, o pipeline executa `syft alpine:latest` (ou a imagem da aplicação) para catalogar todos os pacotes instalados e arquivar o SBOM junto aos artefatos da release.

## Limites e trade-offs
Não limite a geração de SBOM apenas a imagens finais se o seu projeto também distribui diretórios, pacotes ou arquivos `.tar.gz`; o Syft analisa diretamente diretórios (`syft ./my-project`) e arquivos de distribuição.

## Como verificar
Execute `syft alpine:latest` e confirme a listagem imediata em tabela contendo `NAME`, `VERSION` e `TYPE` (como `alpine-baselayout`, `apk-tools`, `busybox` do tipo `apk`).

## Conexões
- [[syft-os-and-language-packaging-ecosystems]] — Veja também: Catalogação multi-ecossistema de pacotes de SO e linguagens de programação no Syft.

## Fontes
- [Anchore Syft GitHub — README.md (Features, Ecosystems, Formats & CLI Basics)](https://raw.githubusercontent.com/anchore/syft/main/README.md) — README oficial do Anchore Syft descrevendo geração de SBOM para imagens de contêiner, sistemas de arquivos e arquivos compactados, suporte a dezenas de ecossistemas de pacotes, formatos CycloneDX, SPDX e Syft JSON, conversão entre formatos e atestações in-toto.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Syft Getting Started Guide](https://oss.anchore.com/docs/guides/sbom/getting-started/) — Guia oficial de início rápido do Syft detalhando instalação, geração simultânea de tabela, SPDX-JSON e CycloneDX-JSON, inspeção com jq, escopo squashed padrão versus --scope all-layers, enriquecimento opcional --enrich e operação 100% local.; consultado em 2026-10-03.
- [Anchore Syft — Official GitHub Repository](https://github.com/anchore/syft) — Repositório oficial Apache-2.0 do Syft mantido pela Anchore.; consultado em 2026-10-03.
