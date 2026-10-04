---
id: software.testes.tranche19.001279
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://www.mbtest.org/docs/api/stubs", "https://www.mbtest.org/docs/api/overview"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mountebank: compor stubs com respostas

## Em uma frase
Cada stub reúne predicados opcionais e uma lista de respostas, e a primeira resposta é devolvida a cada correspondência.

## Por que importa
A lista de respostas permite simular sequências, incluindo primeira falha e sucesso seguinte, sem reiniciar o serviço.

## Como funciona
Declare stubs específicos antes dos genéricos, use a ordem das respostas para sequências e mantenha a lista curta e legível.

## Exemplo
Um stub pode responder com recurso indisponível na primeira chamada e com sucesso na segunda, verificando a lógica de repetição do cliente.

## Limites e trade-offs
Colocar um stub genérico antes do específico o ofusca, e sequências longas demais tornam o comportamento difícil de prever.

## Como verificar
Invoque o serviço mais vezes do que o número de respostas e confirme qual resposta é servida após o fim da sequência.

## Conexões
- [[mountebank-imposters]] — Veja também: Mountebank: criar serviços virtuais com impostores.
- [[mountebank-predicates]] — Veja também: Mountebank: decidir a correspondência com predicados.

## Fontes
- [Mountebank — Stubs](https://www.mbtest.org/docs/api/stubs) — stubs, respostas, sequências e stub padrão; consultado em 2026-10-03.
- [Mountebank — API overview](https://www.mbtest.org/docs/api/overview) — interface administrativa, criação de impostores e remoção; consultado em 2026-10-03.
