---
id: software.devops.tranche04.000340
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

# Verificação de licenças de dependências e conversão entre formatos de SBOM no Syft

## Em uma frase
A documentação oficial do Syft destaca dois fluxos complementares para governança de cadeia de suprimentos: a **conversão entre formatos de SBOM** (`oss.anchore.com/docs/guides/sbom/conversion/`), que permite transformar um SBOM existente de um padrão para outro sem reanalisar a imagem original, e o **levantamento de licenças** (`oss.anchore.com/docs/guides/license/getting-started/`), que extrai e registra nos campos do SBOM as declarações de licença associadas a cada pacote catalogado.

## Por que importa
Auditorias jurídicas e de conformidade open-source exigem identificar rapidamente se alguma dependência transitiva introduziu uma licença restritiva incompatível com a política da empresa, além de entregar o inventário no formato exato exigido por cada auditor ou cliente.

## Como funciona
Extraia os campos de licença diretamente do SBOM JSON gerado pelo Syft usando receitas `jq` no pipeline de CI e utilize a conversão do Syft quando precisar derivar um arquivo SPDX ou CycloneDX a partir de um SBOM Syft JSON previamente arquivado.

## Exemplo
Antes de aprovar uma release comercial, o pipeline de compliance inspeciona as licenças catalogadas pelo Syft no arquivo SBOM para garantir que nenhuma biblioteca sob licença proibida pela política interna foi incluída na imagem.

## Limites e trade-offs
Valide sempre se o ecossistema da linguagem mantém os arquivos de metadados de licença no artefato final empacotado, pois builds que removem arquivos de manifesto de pacotes impedem a extração automática da licença.

## Como verificar
Consulte os metadados de licença nos pacotes do SBOM gerado pelo Syft com `jq` e teste a geração/conversão para SPDX e CycloneDX confirmando a preservação dos componentes.

## Conexões
- [[syft-seamless-pipeline-integration-with-grype]] — Veja também: Integração direta entre Syft e Grype para desacoplar geração de SBOM e scan de vulnerabilidades.

## Fontes
- [Anchore Syft GitHub — README.md (Features, Ecosystems, Formats & CLI Basics)](https://raw.githubusercontent.com/anchore/syft/main/README.md) — README oficial do Anchore Syft descrevendo geração de SBOM para imagens de contêiner, sistemas de arquivos e arquivos compactados, suporte a dezenas de ecossistemas de pacotes, formatos CycloneDX, SPDX e Syft JSON, conversão entre formatos e atestações in-toto.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Syft Getting Started Guide](https://oss.anchore.com/docs/guides/sbom/getting-started/) — Guia oficial de início rápido do Syft detalhando instalação, geração simultânea de tabela, SPDX-JSON e CycloneDX-JSON, inspeção com jq, escopo squashed padrão versus --scope all-layers, enriquecimento opcional --enrich e operação 100% local.; consultado em 2026-10-03.
- [Anchore Syft — Official GitHub Repository](https://github.com/anchore/syft) — Repositório oficial Apache-2.0 do Syft mantido pela Anchore.; consultado em 2026-10-03.
