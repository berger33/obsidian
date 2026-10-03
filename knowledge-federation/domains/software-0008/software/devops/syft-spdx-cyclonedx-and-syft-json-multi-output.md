---
id: software.devops.tranche04.000333
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

# Emissão simultânea de múltiplos formatos de SBOM: SPDX, CycloneDX, Syft JSON e tabela

## Em uma frase
O guia oficial de Getting Started do Syft demonstra que uma única invocação pode exibir a tabela legível por humanos no `stdout` e gravar simultaneamente arquivos nos dois principais padrões da indústria — **SPDX** (`spdx.dev`) e **CycloneDX** (`cyclonedx.org`) — além do formato nativo **Syft JSON**, usando múltiplas flags `-o`: por exemplo, `syft alpine:latest -o table -o spdx-json=alpine.spdx.json -o cyclonedx-json=alpine.cdx.json`. Além disso, o Syft suporta conversão direta entre formatos de SBOM existentes.

## Por que importa
Enquanto equipes internas de segurança e o scanner Grype aproveitam a riqueza de detalhes do formato nativo Syft JSON ou CycloneDX, clientes corporativos e órgãos regulatórios frequentemente exigem entrega em SPDX-JSON padronizado. Gerar ambos em uma única leitura da imagem economiza tempo de I/O no pipeline.

## Como funciona
Configure o job de build no CI para passar múltiplas flags `-o` (`-o syft-json=sbom.syft.json -o spdx-json=sbom.spdx.json -o cyclonedx-json=sbom.cdx.json`), produzindo todos os artefatos necessários em uma única varredura da imagem.

## Exemplo
Em um pipeline de release de software corporativo, o comando `syft <image> -o spdx-json=./spdx.json -o cyclonedx-json=./cdx.json` gera os dois documentos padrão em poucos segundos sem reprocessar as camadas do contêiner.

## Limites e trade-offs
Não execute o comando `syft` três vezes seguidas sobre a mesma imagem pesada apenas para obter três formatos diferentes; combine todas as saídas desejadas com múltiplas flags `-o` na mesma execução.

## Como verificar
Execute o comando com `-o table -o spdx-json=alpine.spdx.json -o cyclonedx-json=alpine.cdx.json` e verifique que a tabela é impressa no terminal e ambos os arquivos JSON válidos são criados no diretório atual.

## Conexões
- [[syft-os-and-language-packaging-ecosystems]] — Veja também: Catalogação multi-ecossistema de pacotes de SO e linguagens de programação no Syft.
- [[syft-jq-inspection-and-pretty-printing-sboms]] — Veja também: Inspeção de pacotes em SPDX e CycloneDX com jq e formatação SYFT_FORMAT_PRETTY=true.

## Fontes
- [Anchore Syft GitHub — README.md (Features, Ecosystems, Formats & CLI Basics)](https://raw.githubusercontent.com/anchore/syft/main/README.md) — README oficial do Anchore Syft descrevendo geração de SBOM para imagens de contêiner, sistemas de arquivos e arquivos compactados, suporte a dezenas de ecossistemas de pacotes, formatos CycloneDX, SPDX e Syft JSON, conversão entre formatos e atestações in-toto.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Syft Getting Started Guide](https://oss.anchore.com/docs/guides/sbom/getting-started/) — Guia oficial de início rápido do Syft detalhando instalação, geração simultânea de tabela, SPDX-JSON e CycloneDX-JSON, inspeção com jq, escopo squashed padrão versus --scope all-layers, enriquecimento opcional --enrich e operação 100% local.; consultado em 2026-10-03.
- [Anchore Syft — Official GitHub Repository](https://github.com/anchore/syft) — Repositório oficial Apache-2.0 do Syft mantido pela Anchore.; consultado em 2026-10-03.
