---
id: software.testes.tranche15.000927
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
fontes: ["https://mswjs.io/guides/best-practices/structuring-handlers", "https://mswjs.io/api/setup-server/use"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: manter sucesso padrão central e estados excepcionais perto do teste

## Em uma frase
A prática recomendada é manter respostas de sucesso no módulo base de handlers e aplicar overrides de rede sob demanda onde o cenário especial é exercitado.

## Por que importa
Essa organização reduz duplicação e torna fácil entender o caminho normal da aplicação, sem criar uma lista central com todos os erros, latências e respostas artificiais possíveis.

## Como funciona
O reset entre casos mantém cada override local ao teste que o introduziu.

## Exemplo
Exporte handlers por domínio, componha uma lista raiz e, no teste de falha, acrescente um `server.use` temporário depois de limpar overrides no teardown de cada caso.

## Limites e trade-offs
Um handler geral muito amplo pode capturar endpoints não relacionados ou ocultar mudança na API; agrupe por domínio e evite uma única função monolítica.

## Como verificar
Revise a lista inicial e a lista de overrides, rode os casos em ordem aleatória e confirme que requests sem handler continuam detectáveis.

## Conexões
- [[msw-boundary-isolar-state-por-contexto-async]] — Veja também: MSW: criar boundary quando handlers de runtime precisam de escopo assíncrono.
- [[msw-http-handlers-no-ponto-de-vista-do-cliente]] — Veja também: MSW: descrever request handler por método e recurso externo.

## Fontes
- [MSW — Structuring handlers](https://mswjs.io/guides/best-practices/structuring-handlers) — handlers de sucesso, overrides e composição por domínio; consultado em 2026-10-02.
- [MSW — use()](https://mswjs.io/api/setup-server/use) — adição e precedência de runtime handlers; consultado em 2026-10-02.
