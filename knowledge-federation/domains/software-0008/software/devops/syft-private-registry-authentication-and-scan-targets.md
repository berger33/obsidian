---
id: software.devops.tranche04.000338
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

# Autenticação em registros privados e variedade de alvos de scan suportados pelo Syft

## Em uma frase
Além de imagens públicas, o Syft suporta autenticação nativa em registros de contêineres privados (`oss.anchore.com/docs/guides/private-registries/`) e uma ampla gama de esquemas de alvos de varredura (`scan-targets`), incluindo imagens no daemon Docker ou Podman local, imagens diretamente em registros OCI remotos sem necessidade de daemon local, arquivos tarball OCI/Docker salvos em disco, imagens Singularity (`.sif`), diretórios de sistema de arquivos e arquivos compactados.

## Por que importa
Em runners de CI modernos baseados em Kubernetes (onde não há daemon Docker rodando por questões de segurança), o Syft precisa inspecionar imagens diretamente no registro privado autenticado ou a partir de um tarball OCI gerado pelo BuildKit/Kaniko.

## Como funciona
Configure as credenciais de registro privado padrão (`~/.docker/config.json` ou variáveis de ambiente suportadas pelo Syft) nos jobs de CI para que o Syft leia diretamente as imagens privadas recém-publicadas ou analise o tarball OCI local antes do push.

## Exemplo
Em um job Kubernetes sem Docker daemon, o BuildKit exporta a imagem para o registro privado interno e o passo seguinte executa `syft registry:interno.empresa.local/app@sha256:...` autenticando-se via credenciais montadas do Secret do pipeline.

## Limites e trade-offs
Não instale um daemon Docker completo e privilegiado em um runner de CI apenas para rodar o Syft; utilize o acesso direto a registros OCI ou arquivos de imagem suportados nativamente pela ferramenta.

## Como verificar
Execute o Syft apontando para uma imagem em registro privado autenticado ou tarball OCI local e confirme o carregamento e catalogação completa das camadas (`Loaded image` / `Cataloged contents`).

## Conexões
- [[syft-offline-execution-privacy-and-enrich-flag]] — Veja também: Execução 100% local sem telemetria externa e enriquecimento opcional com --enrich no Syft.
- [[syft-seamless-pipeline-integration-with-grype]] — Veja também: Integração direta entre Syft e Grype para desacoplar geração de SBOM e scan de vulnerabilidades.

## Fontes
- [Anchore Syft GitHub — README.md (Features, Ecosystems, Formats & CLI Basics)](https://raw.githubusercontent.com/anchore/syft/main/README.md) — README oficial do Anchore Syft descrevendo geração de SBOM para imagens de contêiner, sistemas de arquivos e arquivos compactados, suporte a dezenas de ecossistemas de pacotes, formatos CycloneDX, SPDX e Syft JSON, conversão entre formatos e atestações in-toto.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Syft Getting Started Guide](https://oss.anchore.com/docs/guides/sbom/getting-started/) — Guia oficial de início rápido do Syft detalhando instalação, geração simultânea de tabela, SPDX-JSON e CycloneDX-JSON, inspeção com jq, escopo squashed padrão versus --scope all-layers, enriquecimento opcional --enrich e operação 100% local.; consultado em 2026-10-03.
- [Anchore Syft — Official GitHub Repository](https://github.com/anchore/syft) — Repositório oficial Apache-2.0 do Syft mantido pela Anchore.; consultado em 2026-10-03.
