---
id: software.seguranca.tranche17.001611
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

# Syft: Escolha de origem entre imagem, diretório e arquivo

## Em uma frase
**Syft — Escolha de origem entre imagem, diretório e arquivo:** Syft aceita diferentes representações do software; a origem determina quais metadados e pacotes podem ser observados.

## Por que importa
O recorte de **escolha de origem entre imagem, diretório e arquivo** ajuda a produzir inventários reproduzíveis e utilizáveis por scanners e processos de governança de componentes. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escolha de origem entre imagem, diretório e arquivo**, identifica a origem, aplica catalogadores compatíveis com o tipo de entrada e serializa os pacotes e metadados em um formato SBOM escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Gere um SBOM da imagem publicada e outro do diretório-fonte em uma pipeline autorizada e compare o inventário. Teste em staging autorizado.

## Limites e trade-offs
Um diretório de build não é intercambiável com a imagem resultante, que pode incluir camadas e pacotes instalados. Exceções exigem responsável e prazo.

## Como verificar
Confira no documento SBOM os metadados da origem e valide que o alvo usado corresponde ao artefato em produção. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[syft-catalogadores-de-pacotes-declarados-e-instalados]] — Complementa o tópico com syft: catalogadores de pacotes declarados e instalados.

## Fontes
- [Anchore Syft — Supported Sources](https://github.com/anchore/syft/wiki/supported-sources) — guia do projeto sobre imagens, arquivos, diretórios e arquivos de imagem aceitos como origem; consultado em 2026-10-04.
- [Anchore Syft — Package Cataloger Selection](https://github.com/anchore/syft/wiki/package-cataloger-selection) — guia oficial sobre catalogadores por tipo de origem e seleção de ecossistemas; consultado em 2026-10-04.
