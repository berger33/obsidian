---
id: software.seguranca.tranche17.001617
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

# Syft: Identificação de distribuição do sistema operacional

## Em uma frase
**Syft — Identificação de distribuição do sistema operacional:** A detecção da distribuição fornece contexto para interpretar pacotes de sistema e comparar advisories da plataforma.

## Por que importa
O recorte de **identificação de distribuição do sistema operacional** ajuda a produzir inventários reproduzíveis e utilizáveis por scanners e processos de governança de componentes. A equipe registra risco, evidência e responsável.

## Como funciona
Para **identificação de distribuição do sistema operacional**, identifica a origem, aplica catalogadores compatíveis com o tipo de entrada e serializa os pacotes e metadados em um formato SBOM escolhido. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Gere SBOM de uma imagem derivada de uma distribuição conhecida e valide a distribuição identificada com os arquivos de release. Teste em staging autorizado.

## Limites e trade-offs
Imagens mínimas, scratch ou alteradas podem não revelar uma distribuição de forma conclusiva. Exceções exigem responsável e prazo.

## Como verificar
Compare a distro reportada com a imagem base e marque explicitamente casos sem identificação segura. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[syft-pacotes-descobertos-em-binarios]] — Complementa o tópico com syft: pacotes descobertos em binários.

## Fontes
- [Anchore Syft — Supported Sources](https://github.com/anchore/syft/wiki/supported-sources) — guia do projeto sobre imagens, arquivos, diretórios e arquivos de imagem aceitos como origem; consultado em 2026-10-04.
- [Anchore Syft — Package Cataloger Selection](https://github.com/anchore/syft/wiki/package-cataloger-selection) — guia oficial sobre catalogadores por tipo de origem e seleção de ecossistemas; consultado em 2026-10-04.
