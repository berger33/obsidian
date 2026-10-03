---
id: software.devops.tranche04.000332
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

# Catalogação multi-ecossistema de pacotes de SO e linguagens de programação no Syft

## Em uma frase
O Syft suporta dezenas de ecossistemas de empacotamento tanto de sistemas operacionais quanto de linguagens de aplicação, incluindo pacotes Alpine (`apk`), Debian/Ubuntu (`dpkg`), Red Hat/Fedora (`rpm`), além de dependências de **Go, Python, Java, JavaScript, Ruby, Rust, PHP, .NET** e outros ecossistemas listados na documentação oficial de capacidades (`oss.anchore.com/docs/capabilities/all-packages/`).

## Por que importa
Imagens modernas de produção frequentemente combinam pacotes de distribuição Linux (`apk`, `dpkg`, `rpm`) com binários compilados em Go ou Rust e bibliotecas de linguagem instaladas via `pip`, `npm` ou `maven`. Um gerador de SBOM que enxergue apenas o gerenciador de pacotes do SO deixaria de fora a maior parte das dependências da aplicação.

## Como funciona
Execute o Syft sobre a imagem final construída (e não apenas sobre o código-fonte isolado) para capturar simultaneamente os pacotes da imagem base do sistema operacional e os artefatos de linguagem copiados nas etapas de build.

## Exemplo
Em uma imagem multi-stage contendo pacotes base Alpine (`apk`), um serviço auxiliar em Go e uma aplicação principal em Python, uma única execução do Syft cataloga os pacotes `apk`, os módulos Go embutidos no binário e os pacotes Python do ambiente virtual.

## Limites e trade-offs
Evite remover metadados essenciais de pacotes (como bancos do `dpkg`/`apk` ou informações de build de binários Go) de forma arbitrária achando que isso melhora a segurança, pois isso apenas impede que ferramentas de SBOM inventariem componentes vulneráveis presentes na imagem.

## Como verificar
Inspecione a coluna `TYPE` na saída do Syft ou no JSON gerado e confirme que tanto os pacotes do sistema operacional quanto os pacotes da linguagem da aplicação foram catalogados.

## Conexões
- [[syft-sbom-generation-cli-and-go-library]] — Veja também: Syft como CLI e biblioteca Go para geração de SBOM de contêineres, diretórios e arquivos.
- [[syft-spdx-cyclonedx-and-syft-json-multi-output]] — Veja também: Emissão simultânea de múltiplos formatos de SBOM: SPDX, CycloneDX, Syft JSON e tabela.

## Fontes
- [Anchore Syft GitHub — README.md (Features, Ecosystems, Formats & CLI Basics)](https://raw.githubusercontent.com/anchore/syft/main/README.md) — README oficial do Anchore Syft descrevendo geração de SBOM para imagens de contêiner, sistemas de arquivos e arquivos compactados, suporte a dezenas de ecossistemas de pacotes, formatos CycloneDX, SPDX e Syft JSON, conversão entre formatos e atestações in-toto.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Syft Getting Started Guide](https://oss.anchore.com/docs/guides/sbom/getting-started/) — Guia oficial de início rápido do Syft detalhando instalação, geração simultânea de tabela, SPDX-JSON e CycloneDX-JSON, inspeção com jq, escopo squashed padrão versus --scope all-layers, enriquecimento opcional --enrich e operação 100% local.; consultado em 2026-10-03.
- [Anchore Syft — Official GitHub Repository](https://github.com/anchore/syft) — Repositório oficial Apache-2.0 do Syft mantido pela Anchore.; consultado em 2026-10-03.
