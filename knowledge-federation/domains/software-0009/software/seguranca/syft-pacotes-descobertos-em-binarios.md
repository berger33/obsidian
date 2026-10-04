---
id: software.seguranca.tranche17.001618
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

# Syft: Pacotes descobertos em binários

## Em uma frase
**Syft — Pacotes descobertos em binários:** Alguns catalogadores conseguem inferir componentes a partir de binários, aumentando a visibilidade quando manifestos não estão disponíveis.

## Por que importa
O recorte de **pacotes descobertos em binários** ajuda a produzir inventários reproduzíveis e utilizáveis por scanners e processos de governança de componentes. A equipe registra risco, evidência e responsável.

## Como funciona
Para **pacotes descobertos em binários**, identifica a origem, aplica catalogadores compatíveis com o tipo de entrada e serializa os pacotes e metadados em um formato SBOM escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Analise um binário de build controlado e compare os componentes inferidos com o grafo de dependências conhecido. Teste em staging autorizado.

## Limites e trade-offs
Inferência por binário pode gerar identificação incompleta ou ambígua e não substitui metadados de compilação. Exceções exigem responsável e prazo.

## Como verificar
Mantenha evidência de localização e método de detecção e classifique resultados inferidos separadamente. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[syft-reprodutibilidade-do-sbom-no-pipeline]] — Complementa o tópico com syft: reprodutibilidade do sbom no pipeline.

## Fontes
- [Anchore Syft — Supported Sources](https://github.com/anchore/syft/wiki/supported-sources) — guia do projeto sobre imagens, arquivos, diretórios e arquivos de imagem aceitos como origem; consultado em 2026-10-04.
- [Anchore Syft — Package Cataloger Selection](https://github.com/anchore/syft/wiki/package-cataloger-selection) — guia oficial sobre catalogadores por tipo de origem e seleção de ecossistemas; consultado em 2026-10-04.
