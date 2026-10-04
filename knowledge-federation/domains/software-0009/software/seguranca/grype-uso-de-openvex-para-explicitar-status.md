---
id: software.seguranca.tranche17.001627
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

# Grype: Uso de OpenVEX para explicitar status

## Em uma frase
**Grype — Uso de OpenVEX para explicitar status:** VEX pode acrescentar contexto sobre aplicabilidade ou ausência de impacto a uma vulnerabilidade em um produto.

## Por que importa
O recorte de **uso de openvex para explicitar status** ajuda a correlacionar inventário de pacotes com advisories conhecidos e priorizar correções com evidência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **uso de openvex para explicitar status**, recebe uma imagem, diretório ou SBOM, identifica os componentes e compara os resultados com a base local de vulnerabilidades. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Associe uma afirmação VEX a um SBOM de teste e valide que o finding filtrado continua rastreável. Teste em staging autorizado.

## Limites e trade-offs
Declaração VEX exige escopo correto e justificativa; ela não corrige o componente nem elimina o advisory da base. Exceções exigem responsável e prazo.

## Como verificar
Confira identificadores de produto e vulnerabilidade e teste expiração e revisão da declaração. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[grype-filtros-e-excecoes-com-rastreabilidade]] — Complementa o tópico com grype: filtros e exceções com rastreabilidade.

## Fontes
- [Anchore Grype — Repository and Usage](https://github.com/anchore/grype) — repositório oficial com escopos de scan de imagens, sistemas de arquivos e SBOMs; consultado em 2026-10-04.
- [Anchore Grype — Getting Started](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — guia oficial sobre scans de imagens, diretórios e SBOMs e atualização da base de vulnerabilidades; consultado em 2026-10-04.
