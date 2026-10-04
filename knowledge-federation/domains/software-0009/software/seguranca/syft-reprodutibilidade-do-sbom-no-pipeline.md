---
id: software.seguranca.tranche17.001619
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

# Syft: Reprodutibilidade do SBOM no pipeline

## Em uma frase
**Syft — Reprodutibilidade do SBOM no pipeline:** Versão da ferramenta, origem e conjunto de catalogadores afetam o inventário produzido e precisam ser registrados.

## Por que importa
O recorte de **reprodutibilidade do sbom no pipeline** ajuda a produzir inventários reproduzíveis e utilizáveis por scanners e processos de governança de componentes. A equipe registra risco, evidência e responsável.

## Como funciona
Para **reprodutibilidade do sbom no pipeline**, identifica a origem, aplica catalogadores compatíveis com o tipo de entrada e serializa os pacotes e metadados em um formato SBOM escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Execute Syft duas vezes sobre o mesmo digest com a mesma versão e compare SBOMs após normalizar campos voláteis. Teste em staging autorizado.

## Limites e trade-offs
Diferenças não explicadas podem vir de formato, base de catálogo ou metadados, não necessariamente de mudança do software. Exceções exigem responsável e prazo.

## Como verificar
Automatize comparação de saída e investigue cada diferença de pacote, versão, PURL e localização. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[syft-comparacao-entre-inventario-de-fonte-e-artefato]] — Complementa o tópico com syft: comparação entre inventário de fonte e artefato.

## Fontes
- [Anchore Syft — Supported Sources](https://github.com/anchore/syft/wiki/supported-sources) — guia do projeto sobre imagens, arquivos, diretórios e arquivos de imagem aceitos como origem; consultado em 2026-10-04.
- [Anchore Syft — Package Cataloger Selection](https://github.com/anchore/syft/wiki/package-cataloger-selection) — guia oficial sobre catalogadores por tipo de origem e seleção de ecossistemas; consultado em 2026-10-04.
