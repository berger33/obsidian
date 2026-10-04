---
id: software.seguranca.tranche17.001614
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://github.com/anchore/syft/wiki/supported-sources", "https://github.com/anchore/syft/wiki/package-cataloger-selection"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Syft: Exportação de SBOM CycloneDX e SPDX

## Em uma frase
**Syft — Exportação de SBOM CycloneDX e SPDX:** A serialização em um formato padronizado facilita intercâmbio com ferramentas de segurança e inventário.

## Por que importa
O recorte de **exportação de sbom cyclonedx e spdx** ajuda a produzir inventários reproduzíveis e utilizáveis por scanners e processos de governança de componentes. A equipe registra risco, evidência e responsável.

## Como funciona
Para **exportação de sbom cyclonedx e spdx**, identifica a origem, aplica catalogadores compatíveis com o tipo de entrada e serializa os pacotes e metadados em um formato SBOM escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Produza o formato exigido pelo consumidor interno e valide a versão do formato no cabeçalho do arquivo. Teste em staging autorizado.

## Limites e trade-offs
Formatos e versões podem representar metadados de modo diferente; exportação não garante consumo sem perda. Exceções exigem responsável e prazo.

## Como verificar
Valide o arquivo com parser compatível e confirme que pacotes, identificadores e origem sobrevivem à importação. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[syft-identificadores-package-url-e-correspondencia]] — Complementa o tópico com syft: identificadores package url e correspondência.

## Fontes
- [Anchore Syft — Supported Sources](https://github.com/anchore/syft/wiki/supported-sources) — guia do projeto sobre imagens, arquivos, diretórios e arquivos de imagem aceitos como origem; consultado em 2026-10-04.
- [Anchore Syft — Package Cataloger Selection](https://github.com/anchore/syft/wiki/package-cataloger-selection) — guia oficial sobre catalogadores por tipo de origem e seleção de ecossistemas; consultado em 2026-10-04.
