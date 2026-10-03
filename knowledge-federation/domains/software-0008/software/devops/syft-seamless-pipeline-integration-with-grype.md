---
id: software.devops.tranche04.000339
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

# Integração direta entre Syft e Grype para desacoplar geração de SBOM e scan de vulnerabilidades

## Em uma frase
O README oficial destaca que o Syft funciona de forma integrada com o scanner de vulnerabilidades **Grype** (`github.com/anchore/grype`). Em vez de o scanner de vulnerabilidades precisar baixar e descompactar novamente todas as camadas pesadas da imagem de contêiner a cada verificação, o Syft gera o SBOM uma única vez durante o build e o Grype consome diretamente esse arquivo SBOM (`grype sbom:./sbom.json` ou `cat ./sbom.json | grype`) para detectar vulnerabilidades em uma fração do tempo.

## Por que importa
Uma imagem de contêiner é construída uma vez, mas novas vulnerabilidades (CVEs) são descobertas todos os dias. Quando o SBOM gerado pelo Syft é armazenado como artefato de release, é possível reescanear toda a frota de imagens em segundos com o Grype a cada atualização do banco de CVEs, sem nunca mais baixar gigabytes de camadas de imagem.

## Como funciona
Gere o SBOM com o Syft no momento do build (preferencialmente em Syft JSON, CycloneDX ou SPDX), armazene-o como artefato imutável e alimente o Grype diretamente com esse SBOM tanto no gate de CI quanto em varreduras diárias contínuas.

## Exemplo
Diariamente às 06h, um job agendado baixa a última base de vulnerabilidades do Grype e varre em menos de um minuto os 200 arquivos `sbom.json` gerados pelo Syft para todas as imagens em execução nos clusters de produção.

## Limites e trade-offs
Para preservar máxima fidelidade de metadados ao alimentar o Grype, gere um arquivo no formato nativo `syft-json` além dos formatos de conformidade SPDX/CycloneDX exigidos externamente.

## Como verificar
Gere um SBOM com `syft alpine:latest -o json > sbom.json`, execute `grype sbom:./sbom.json` e confirme que o Grype analisa os pacotes instantaneamente sem precisar puxar a imagem do registro.

## Conexões
- [[syft-private-registry-authentication-and-scan-targets]] — Veja também: Autenticação em registros privados e variedade de alvos de scan suportados pelo Syft.
- [[syft-license-scanning-and-format-conversion-workflows]] — Veja também: Verificação de licenças de dependências e conversão entre formatos de SBOM no Syft.

## Fontes
- [Anchore Syft GitHub — README.md (Features, Ecosystems, Formats & CLI Basics)](https://raw.githubusercontent.com/anchore/syft/main/README.md) — README oficial do Anchore Syft descrevendo geração de SBOM para imagens de contêiner, sistemas de arquivos e arquivos compactados, suporte a dezenas de ecossistemas de pacotes, formatos CycloneDX, SPDX e Syft JSON, conversão entre formatos e atestações in-toto.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Syft Getting Started Guide](https://oss.anchore.com/docs/guides/sbom/getting-started/) — Guia oficial de início rápido do Syft detalhando instalação, geração simultânea de tabela, SPDX-JSON e CycloneDX-JSON, inspeção com jq, escopo squashed padrão versus --scope all-layers, enriquecimento opcional --enrich e operação 100% local.; consultado em 2026-10-03.
- [Anchore Syft — Official GitHub Repository](https://github.com/anchore/syft) — Repositório oficial Apache-2.0 do Syft mantido pela Anchore.; consultado em 2026-10-03.
