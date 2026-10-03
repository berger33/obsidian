---
id: software.devops.tranche04.000334
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

# Inspeção de pacotes em SPDX e CycloneDX com jq e formatação SYFT_FORMAT_PRETTY=true

## Em uma frase
A documentação oficial do Syft detalha como extrair e auditar informações de pacotes dos arquivos SBOM gerados usando `jq`: enquanto por padrão o Syft emite JSON compactado em uma única linha para eficiência de armazenamento (podendo-se habilitar indentação legível com a variável de ambiente `SYFT_FORMAT_PRETTY=true`), a estrutura de consulta muda conforme o padrão — no formato **SPDX** os pacotes ficam em `jq '.packages[].name' alpine.spdx.json`, e no formato **CycloneDX** os componentes ficam em `jq '.components[].name' alpine.cdx.json`.

## Por que importa
Conhecer o caminho exato do schema em cada padrão (`.packages[]` no SPDX versus `.components[]` no CycloneDX) evita erros em scripts de auditoria automatizada, gates de conformidade de licenças e pipelines que processam SBOMs com `jq`.

## Como funciona
Em scripts de verificação de CI, utilize `jq '.packages[].name'` para documentos SPDX-JSON e `jq '.components[].name'` para documentos CycloneDX-JSON, ativando `SYFT_FORMAT_PRETTY=true` quando os arquivos forem destinados a inspeção humana em artefatos de build.

## Exemplo
Um script de governança de arquitetura verifica se uma biblioteca banida está presente na release executando `jq -e '.components[] | select(.name == "log4j-core")' app.cdx.json` sobre o SBOM CycloneDX gerado pelo Syft.

## Limites e trade-offs
Não assuma que os campos JSON de SPDX e CycloneDX possuem os mesmos nomes de chave na raiz; adapte sempre os seletores `jq` ao formato específico (`packages` vs `components`).

## Como verificar
Execute `jq '.packages[].name' alpine.spdx.json` e `jq '.components[].name' alpine.cdx.json` sobre os arquivos gerados e confirme que ambos retornam a mesma lista de pacotes catalogados.

## Conexões
- [[syft-spdx-cyclonedx-and-syft-json-multi-output]] — Veja também: Emissão simultânea de múltiplos formatos de SBOM: SPDX, CycloneDX, Syft JSON e tabela.
- [[syft-squashed-default-versus-all-layers-scope]] — Veja também: Escopo padrão squashed versus análise de todas as camadas com --scope all-layers no Syft.

## Fontes
- [Anchore Syft GitHub — README.md (Features, Ecosystems, Formats & CLI Basics)](https://raw.githubusercontent.com/anchore/syft/main/README.md) — README oficial do Anchore Syft descrevendo geração de SBOM para imagens de contêiner, sistemas de arquivos e arquivos compactados, suporte a dezenas de ecossistemas de pacotes, formatos CycloneDX, SPDX e Syft JSON, conversão entre formatos e atestações in-toto.; consultado em 2026-10-03.
- [Anchore Open Source Docs — Syft Getting Started Guide](https://oss.anchore.com/docs/guides/sbom/getting-started/) — Guia oficial de início rápido do Syft detalhando instalação, geração simultânea de tabela, SPDX-JSON e CycloneDX-JSON, inspeção com jq, escopo squashed padrão versus --scope all-layers, enriquecimento opcional --enrich e operação 100% local.; consultado em 2026-10-03.
- [Anchore Syft — Official GitHub Repository](https://github.com/anchore/syft) — Repositório oficial Apache-2.0 do Syft mantido pela Anchore.; consultado em 2026-10-03.
