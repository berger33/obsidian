---
id: software.testes.tranche15.000929
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://mswjs.io/guides/best-practices/structuring-handlers", "https://mswjs.io/api/setup-server/listen"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: compor handlers por domínio sem concentrar toda a rede num arquivo

## Em uma frase
Uma suíte grande pode manter handlers em módulos de domínio e compor as listas em um ponto de entrada, em vez de concentrar cada endpoint num único arquivo.

## Por que importa
Agrupamento deixa claro qual parte do produto uma fixture representa e facilita escolher subset de handlers em testes especializados.

## Como funciona
A composição continua produzindo a lista de requests do MSW, portanto duplicatas conflitantes precisam de revisão explícita.

## Exemplo
Separe `user.js` e `checkout.js`, exporte as listas de cada domínio e componha-as num `handlers/index.js` antes de passar ao setupServer.

## Limites e trade-offs
Reutilizar grupos parcialmente pode ativar endpoints que o cenário não deveria chamar e aumentar chance de falso positivo; mantenha a coleção mínima quando o isolamento for importante.

## Como verificar
Liste as rotas cobertas por cada grupo, execute um teste por domínio com `onUnhandledFrame: 'error'` e verifique que endpoints não declarados falham.

## Conexões
- [[msw-http-handlers-no-ponto-de-vista-do-cliente]] — Veja também: MSW: descrever request handler por método e recurso externo.

## Fontes
- [MSW — Structuring handlers](https://mswjs.io/guides/best-practices/structuring-handlers) — handlers de sucesso, overrides e composição por domínio; consultado em 2026-10-02.
- [MSW — listen()](https://mswjs.io/api/setup-server/listen) — início da interceptação e estratégias para frames sem handler; consultado em 2026-10-02.
