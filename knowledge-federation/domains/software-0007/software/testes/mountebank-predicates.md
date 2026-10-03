---
id: software.testes.tranche19.001280
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
fontes: ["https://www.mbtest.org/docs/api/predicates", "https://www.mbtest.org/docs/api/stubs"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mountebank: decidir a correspondência com predicados

## Em uma frase
Predicados comparam método, caminho, cabeçalhos, consulta e corpo com operadores de igualdade, padrão, existência e negação.

## Por que importa
Predicados precisos fazem cada stub responder apenas ao caso pretendido, evitando respostas trocadas entre cenários.

## Como funciona
Escreva predicados por aspecto, combine vários no mesmo stub quando a exigência é conjunta e use negação para excluir casos.

## Exemplo
Um stub pode exigir método de envio e corpo com campo obrigatório para decidir entre aceitar e rejeitar a requisição.

## Limites e trade-offs
Predicados amplos correspondem a requisições que deveriam seguir outro caminho, e a ausência de predicado faz o stub casar com tudo.

## Como verificar
Altere um campo do corpo e confirme que a requisição passa a ser atendida pelo stub seguinte, como previsto.

## Conexões
- [[mountebank-stubs]] — Veja também: Mountebank: compor stubs com respostas.
- [[mountebank-proxies]] — Veja também: Mountebank: gravar e reproduzir com proxies.

## Fontes
- [Mountebank — Predicates](https://www.mbtest.org/docs/api/predicates) — operadores de correspondência de requisições; consultado em 2026-10-03.
- [Mountebank — Stubs](https://www.mbtest.org/docs/api/stubs) — stubs, respostas, sequências e stub padrão; consultado em 2026-10-03.
