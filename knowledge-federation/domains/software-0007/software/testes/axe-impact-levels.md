---
id: software.testes.tranche18.001219
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

# axe-core: priorizar por impacto

## Em uma frase
Cada violação traz um nível de impacto, e cada elemento afetado inclui seletor, trecho de marcação e resumo da falha.

## Por que importa
O impacto orienta a ordem de correção, e o resumo por elemento transforma a lista em tarefas acionáveis.

## Como funciona
Priorize as violações de impacto alto, use o seletor para localizar o elemento e registre o resumo como descrição do defeito.

## Exemplo
Uma violação crítica de rótulo em campo de formulário pode ser corrigida antes de ajustes de semântica secundária.

## Limites e trade-offs
Impacto não substitui julgamento de uso, e uma violação moderada em fluxo essencial pode ser mais grave do que outra crítica em área pouco usada.

## Como verificar
Escolha uma violação e verifique se o seletor informado aponta exatamente o elemento exibido no navegador.

## Conexões
- [[axe-rule-tags]] — Veja também: axe-core: selecionar regras por etiquetas.
- [[axe-configuration-and-exclusions]] — Veja também: axe-core: configurar regras e excluir trechos.

## Fontes
- [axe-core — JavaScript API](https://github.com/dequelabs/axe-core/blob/develop/doc/API.md) — chamada de análise, opções, etiquetas, impacto e formato do resultado; consultado em 2026-10-03.
- [axe-core — repositório oficial](https://github.com/dequelabs/axe-core) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
