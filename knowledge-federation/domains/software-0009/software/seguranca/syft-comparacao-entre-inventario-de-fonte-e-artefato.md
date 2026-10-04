---
id: software.seguranca.tranche17.001620
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

# Syft: Comparação entre inventário de fonte e artefato

## Em uma frase
**Syft — Comparação entre inventário de fonte e artefato:** A diferença entre componentes declarados e empacotados revela drift de build e dependências introduzidas na imagem.

## Por que importa
O recorte de **comparação entre inventário de fonte e artefato** ajuda a produzir inventários reproduzíveis e utilizáveis por scanners e processos de governança de componentes. A equipe registra risco, evidência e responsável.

## Como funciona
Para **comparação entre inventário de fonte e artefato**, identifica a origem, aplica catalogadores compatíveis com o tipo de entrada e serializa os pacotes e metadados em um formato SBOM escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Compare SBOM da imagem de produção com o SBOM do checkout da mesma release antes da aprovação. Teste em staging autorizado.

## Limites e trade-offs
A divergência pode ser esperada por ferramentas de build e bibliotecas do sistema; requer allowlist contextualizada. Exceções exigem responsável e prazo.

## Como verificar
Associe as duas origens ao mesmo commit e documente por que cada componente extra ou ausente é aceitável. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[grype-scan-direto-de-imagem-de-container]] — Complementa o tópico com grype: scan direto de imagem de container.

## Fontes
- [Anchore Syft — Supported Sources](https://github.com/anchore/syft/wiki/supported-sources) — guia do projeto sobre imagens, arquivos, diretórios e arquivos de imagem aceitos como origem; consultado em 2026-10-04.
- [Anchore Syft — Package Cataloger Selection](https://github.com/anchore/syft/wiki/package-cataloger-selection) — guia oficial sobre catalogadores por tipo de origem e seleção de ecossistemas; consultado em 2026-10-04.
