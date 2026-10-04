---
id: software.testes.tranche18.001217
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://github.com/dequelabs/axe-core/blob/develop/doc/API.md", "https://github.com/dequelabs/axe-core"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# axe-core: executar a análise e ler o resultado

## Em uma frase
A chamada de análise recebe contexto e opções e devolve violações, itens aprovados, avisos e regras não aplicáveis.

## Por que importa
A separação entre violações, avisos e itens aprovados evita tratar tudo como erro e permite priorizar o que exige correção.

## Como funciona
Analise o documento ou um trecho, percorra a lista de violações por regra e trate os avisos como levantamento a confirmar.

## Exemplo
Uma análise de página inteira pode confirmar violação de contraste em diversos elementos, agrupada pela mesma regra.

## Limites e trade-offs
Ler apenas a contagem total esconde a distribuição por regra, e avisos ignorados sistematicamente deixam barreiras sem análise.

## Como verificar
Remova a alternativa textual de uma imagem e confirme que a violação correspondente aparece no resultado.

## Conexões
- [[axe-rule-tags]] — Veja também: axe-core: selecionar regras por etiquetas.

## Fontes
- [axe-core — JavaScript API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md) — chamada de análise, opções, etiquetas, impacto e formato do resultado; consultado em 2026-10-03.
- [axe-core — repositório oficial](https://github.com/dequelabs/axe-core) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
