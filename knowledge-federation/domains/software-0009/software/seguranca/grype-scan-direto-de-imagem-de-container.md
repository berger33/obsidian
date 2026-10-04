---
id: software.seguranca.tranche17.001621
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

# Grype: Scan direto de imagem de container

## Em uma frase
**Grype — Scan direto de imagem de container:** Uma imagem pode ser analisada diretamente para comparar pacotes do sistema e dependências com advisories conhecidos.

## Por que importa
O recorte de **scan direto de imagem de container** ajuda a correlacionar inventário de pacotes com advisories conhecidos e priorizar correções com evidência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **scan direto de imagem de container**, recebe uma imagem, diretório ou SBOM, identifica os componentes e compara os resultados com a base local de vulnerabilidades. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Execute `grype` contra uma imagem fixada por digest em ambiente de teste e retenha os achados associados ao digest. Teste em staging autorizado.

## Limites e trade-offs
Tag mutável pode apontar para conteúdo diferente entre execuções, e o scan não demonstra que o pacote está exposto. Exceções exigem responsável e prazo.

## Como verificar
Repita a análise sobre o mesmo digest e valide um componente vulnerável conhecido no resultado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[grype-analise-de-sbom-syft]] — Complementa o tópico com grype: análise de sbom syft.

## Fontes
- [Anchore Grype — Repository and Usage](https://github.com/anchore/grype) — repositório oficial com escopos de scan de imagens, sistemas de arquivos e SBOMs; consultado em 2026-10-04.
- [Anchore Grype — Getting Started](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — guia oficial sobre scans de imagens, diretórios e SBOMs e atualização da base de vulnerabilidades; consultado em 2026-10-04.
