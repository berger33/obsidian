---
id: software.devops.tranche04.000335
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

# Escopo padrão squashed versus análise de todas as camadas com --scope all-layers no Syft

## Em uma frase
Conforme documentado no Getting Started oficial do Syft, por padrão a ferramenta exibe apenas o software visível na imagem final do contêiner — a representação **"squashed"** (achatada) do sistema de arquivos resultante. Para incluir no SBOM o software presente em **todas as camadas intermediárias da imagem**, independentemente de ter sido deletado ou sobrescrito na camada final, utiliza-se a flag `--scope all-layers` (`syft <image> --scope all-layers`).

## Por que importa
Em um Dockerfile mal estruturado onde ferramentas de compilação, pacotes temporários ou bibliotecas vulneráveis são instalados em uma camada `RUN` e removidos em uma camada `RUN rm ...` posterior, esses arquivos continuam existindo nos blobs das camadas históricas da imagem enviada ao registro. O modo `--scope all-layers` revela tudo o que viaja dentro dos blobs da imagem.

## Como funciona
Use o escopo padrão (`squashed`) para avaliar a superfície de execução ativa do contêiner em produção e execute auditorias com `--scope all-layers` para detectar pacotes ou binários residuais ocultos em camadas intermediárias de imagens que não usaram multi-stage builds adequadamente.

## Exemplo
Durante uma auditoria de segurança de uma imagem legada, `syft app:latest --scope all-layers` revela que um compilador e bibliotecas de desenvolvimento foram instalados na camada 3 e removidos na camada 5, motivando a refatoração para multi-stage build.

## Limites e trade-offs
Evite confundir vulnerabilidades reportadas em `--scope all-layers` (presentes apenas em camadas inferiores ocultas) com pacotes efetivamente acessíveis no filesystem final em execução; documente claramente qual escopo foi utilizado ao compartilhar o SBOM.

## Como verificar
Compare a contagem de pacotes entre `syft <image>` e `syft <image> --scope all-layers` em uma imagem multi-camadas para verificar se existem pacotes ocultos em camadas intermediárias.

## Conexões
- [[syft-jq-inspection-and-pretty-printing-sboms]] — Veja também: Inspeção de pacotes em SPDX e CycloneDX com jq e formatação SYFT_FORMAT_PRETTY=true.
- [[syft-in-toto-signed-sbom-attestations]] — Veja também: Criação de atestações de SBOM assinadas segundo a especificação in-toto com Syft.

## Fontes
- [Anchore Syft GitHub — README.md (Features, Ecosystems, Formats & CLI Basics)](https://raw.githubusercontent.com/anchore/syft/main/README.md) — README oficial do Anchore Syft descrevendo geração de SBOM para imagens de contêiner, sistemas de arquivos e arquivos compactados, suporte a dezenas de ecossistemas de pacotes, formatos CycloneDX, SPDX e Syft JSON, conversão entre formatos e atestações in-toto.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Syft Getting Started Guide](https://oss.anchore.com/docs/guides/sbom/getting-started/) — Guia oficial de início rápido do Syft detalhando instalação, geração simultânea de tabela, SPDX-JSON e CycloneDX-JSON, inspeção com jq, escopo squashed padrão versus --scope all-layers, enriquecimento opcional --enrich e operação 100% local.; consultado em 2026-10-03.
- [Anchore Syft — Official GitHub Repository](https://github.com/anchore/syft) — Repositório oficial Apache-2.0 do Syft mantido pela Anchore.; consultado em 2026-10-03.
