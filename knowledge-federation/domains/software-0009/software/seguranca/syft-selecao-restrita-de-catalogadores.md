---
id: software.seguranca.tranche17.001613
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

# Syft: Seleção restrita de catalogadores

## Em uma frase
**Syft — Seleção restrita de catalogadores:** Catalogadores podem ser selecionados por nome ou tag quando se necessita limitar o escopo de uma análise.

## Por que importa
O recorte de **seleção restrita de catalogadores** ajuda a produzir inventários reproduzíveis e utilizáveis por scanners e processos de governança de componentes. A equipe registra risco, evidência e responsável.

## Como funciona
Para **seleção restrita de catalogadores**, identifica a origem, aplica catalogadores compatíveis com o tipo de entrada e serializa os pacotes e metadados em um formato SBOM escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em uma auditoria focada em Go, restrinja catalogadores à tag `go` em uma cópia de teste e compare o resultado com o padrão. Teste em staging autorizado.

## Limites e trade-offs
Restringir catalogadores pode omitir outras linguagens no mesmo artefato e não deve virar configuração geral sem justificativa. Exceções exigem responsável e prazo.

## Como verificar
Compare contagens por ecossistema e preserve a configuração de catalogadores usada para produzir o SBOM. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[syft-exportacao-de-sbom-cyclonedx-e-spdx]] — Complementa o tópico com syft: exportação de sbom cyclonedx e spdx.

## Fontes
- [Anchore Syft — Supported Sources](https://github.com/anchore/syft/wiki/supported-sources) — guia do projeto sobre imagens, arquivos, diretórios e arquivos de imagem aceitos como origem; consultado em 2026-10-04.
- [Anchore Syft — Package Cataloger Selection](https://github.com/anchore/syft/wiki/package-cataloger-selection) — guia oficial sobre catalogadores por tipo de origem e seleção de ecossistemas; consultado em 2026-10-04.
