---
id: software.seguranca.tranche17.001612
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

# Syft: Catalogadores de pacotes declarados e instalados

## Em uma frase
**Syft — Catalogadores de pacotes declarados e instalados:** A seleção padrão de catalogadores pode variar conforme o tipo de entrada para incluir software instalado ou dependências declaradas.

## Por que importa
O recorte de **catalogadores de pacotes declarados e instalados** ajuda a produzir inventários reproduzíveis e utilizáveis por scanners e processos de governança de componentes. A equipe registra risco, evidência e responsável.

## Como funciona
Para **catalogadores de pacotes declarados e instalados**, identifica a origem, aplica catalogadores compatíveis com o tipo de entrada e serializa os pacotes e metadados em um formato SBOM escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Analise um projeto Python com `requirements.txt` e compare com a imagem instalada para distinguir dependência declarada de pacote presente. Teste em staging autorizado.

## Limites e trade-offs
Dependência declarada pode não ter sido instalada; pacote instalado pode não ter manifesto de origem preservado. Exceções exigem responsável e prazo.

## Como verificar
Revise o tipo de catalogador e a localização de evidência de cada pacote em uma fixture controlada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[syft-selecao-restrita-de-catalogadores]] — Complementa o tópico com syft: seleção restrita de catalogadores.

## Fontes
- [Anchore Syft — Supported Sources](https://github.com/anchore/syft/wiki/supported-sources) — guia do projeto sobre imagens, arquivos, diretórios e arquivos de imagem aceitos como origem; consultado em 2026-10-04.
- [Anchore Syft — Package Cataloger Selection](https://github.com/anchore/syft/wiki/package-cataloger-selection) — guia oficial sobre catalogadores por tipo de origem e seleção de ecossistemas; consultado em 2026-10-04.
