---
id: software.seguranca.tranche17.001616
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

# Syft: Proveniência e metadados da origem

## Em uma frase
**Syft — Proveniência e metadados da origem:** Metadados da fonte ajudam a associar o SBOM a uma imagem, caminho ou artefato específico.

## Por que importa
O recorte de **proveniência e metadados da origem** ajuda a produzir inventários reproduzíveis e utilizáveis por scanners e processos de governança de componentes. A equipe registra risco, evidência e responsável.

## Como funciona
Para **proveniência e metadados da origem**, identifica a origem, aplica catalogadores compatíveis com o tipo de entrada e serializa os pacotes e metadados em um formato SBOM escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Armazene o SBOM de release junto ao digest OCI e ao commit de origem, evitando nome de tag como única chave. Teste em staging autorizado.

## Limites e trade-offs
Metadados só são úteis se o processo de build os preservar e não garantem autoria criptográfica. Exceções exigem responsável e prazo.

## Como verificar
Cheque campos de origem e digest no SBOM e compare com o manifesto de publicação da release. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[syft-identificacao-de-distribuicao-do-sistema-operacional]] — Complementa o tópico com syft: identificação de distribuição do sistema operacional.

## Fontes
- [Anchore Syft — Supported Sources](https://github.com/anchore/syft/wiki/supported-sources) — guia do projeto sobre imagens, arquivos, diretórios e arquivos de imagem aceitos como origem; consultado em 2026-10-04.
- [Anchore Syft — Package Cataloger Selection](https://github.com/anchore/syft/wiki/package-cataloger-selection) — guia oficial sobre catalogadores por tipo de origem e seleção de ecossistemas; consultado em 2026-10-04.
