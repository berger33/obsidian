---
id: software.seguranca.tranche17.001622
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
fontes: ["https://github.com/anchore/grype", "https://oss.anchore.com/docs/guides/vulnerability/getting-started/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Grype: Análise de SBOM Syft

## Em uma frase
**Grype — Análise de SBOM Syft:** Grype consome SBOM, permitindo separar a etapa de inventário da etapa de correlação com vulnerabilidades.

## Por que importa
O recorte de **análise de sbom syft** ajuda a correlacionar inventário de pacotes com advisories conhecidos e priorizar correções com evidência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **análise de sbom syft**, recebe uma imagem, diretório ou SBOM, identifica os componentes e compara os resultados com a base local de vulnerabilidades. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Gere `sbom.json` com Syft e use `grype sbom:sbom.json` para tornar a análise independente do registry. Teste em staging autorizado.

## Limites e trade-offs
Um SBOM incompleto limita o que Grype pode encontrar; uma correspondência não recupera pacotes omitidos. Exceções exigem responsável e prazo.

## Como verificar
Valide o formato e compare a lista de pacotes com a origem usada para gerar o SBOM. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[grype-scan-de-sistema-de-arquivos]] — Complementa o tópico com grype: scan de sistema de arquivos.

## Fontes
- [Anchore Grype — Repository and Usage](https://github.com/anchore/grype) — repositório oficial com escopos de scan de imagens, sistemas de arquivos e SBOMs; consultado em 2026-10-04.
- [Anchore Grype — Getting Started](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — guia oficial sobre scans de imagens, diretórios e SBOMs e atualização da base de vulnerabilidades; consultado em 2026-10-04.
