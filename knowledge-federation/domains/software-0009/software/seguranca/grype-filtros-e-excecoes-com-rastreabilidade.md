---
id: software.seguranca.tranche17.001628
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

# Grype: Filtros e exceções com rastreabilidade

## Em uma frase
**Grype — Filtros e exceções com rastreabilidade:** Filtros reduzem ruído quando correspondem a decisão formal, mas podem esconder regressões se forem globais.

## Por que importa
O recorte de **filtros e exceções com rastreabilidade** ajuda a correlacionar inventário de pacotes com advisories conhecidos e priorizar correções com evidência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **filtros e exceções com rastreabilidade**, recebe uma imagem, diretório ou SBOM, identifica os componentes e compara os resultados com a base local de vulnerabilidades. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Aplique uma exceção a um advisory específico em uma fixture e verifique a diferença antes/depois. Teste em staging autorizado.

## Limites e trade-offs
Ignorar por nome de pacote ou severidade pode também silenciar versões e produtos não relacionados. Exceções exigem responsável e prazo.

## Como verificar
Revise o escopo do filtro, dono, motivo, data de validade e teste que detecta a remoção acidental. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[grype-saidas-json-e-sarif]] — Complementa o tópico com grype: saídas json e sarif.

## Fontes
- [Anchore Grype — Repository and Usage](https://github.com/anchore/grype) — repositório oficial com escopos de scan de imagens, sistemas de arquivos e SBOMs; consultado em 2026-10-04.
- [Anchore Grype — Getting Started](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — guia oficial sobre scans de imagens, diretórios e SBOMs e atualização da base de vulnerabilidades; consultado em 2026-10-04.
