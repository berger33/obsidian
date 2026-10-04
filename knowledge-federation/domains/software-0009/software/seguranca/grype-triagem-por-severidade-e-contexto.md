---
id: software.seguranca.tranche17.001626
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

# Grype: Triagem por severidade e contexto

## Em uma frase
**Grype — Triagem por severidade e contexto:** Severidade ajuda a ordenar trabalho, mas precisa ser combinada com exposição, alcance e criticidade do ativo.

## Por que importa
O recorte de **triagem por severidade e contexto** ajuda a correlacionar inventário de pacotes com advisories conhecidos e priorizar correções com evidência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **triagem por severidade e contexto**, recebe uma imagem, diretório ou SBOM, identifica os componentes e compara os resultados com a base local de vulnerabilidades. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Compare um finding de biblioteca interna com outro em serviço exposto antes de aplicar o mesmo SLA. Teste em staging autorizado.

## Limites e trade-offs
CVSS e fontes de advisory não medem sozinhos risco operacional nem presença do caminho vulnerável. Exceções exigem responsável e prazo.

## Como verificar
Registre a fonte de severidade e a justificativa de priorização além da nota numérica. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[grype-uso-de-openvex-para-explicitar-status]] — Complementa o tópico com grype: uso de openvex para explicitar status.

## Fontes
- [Anchore Grype — Repository and Usage](https://github.com/anchore/grype) — repositório oficial com escopos de scan de imagens, sistemas de arquivos e SBOMs; consultado em 2026-10-04.
- [Anchore Grype — Getting Started](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — guia oficial sobre scans de imagens, diretórios e SBOMs e atualização da base de vulnerabilidades; consultado em 2026-10-04.
