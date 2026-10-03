---
id: software.testes.tranche15.000928
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
fontes: ["https://mswjs.io/api/http", "https://mswjs.io/guides/best-practices/structuring-handlers"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: descrever request handler por método e recurso externo

## Em uma frase
Handlers de HTTP do MSW associam um método a um padrão de URL e fornecem request e parâmetros ao resolver; escolha se o host faz parte do contrato que o teste quer proteger.

## Por que importa
Um padrão de caminho como `/v1/users/:id` pode ser útil quando a origem é irrelevante.

## Como funciona
Use a URL completa quando o host também deve ser validado, em vez de presumir que todo padrão relativo falhará no runner.

## Exemplo
Se a origem não importa, declare `http.get("/v1/users/:id", ({ params }) => HttpResponse.json({ id: params.id }))`; se importa, use a URL completa e valide método, host, pathname e query que fazem parte do contrato.

## Limites e trade-offs
Padrões amplos podem interceptar tráfego não intencional; use `http.all()` apenas quando qualquer método fizer parte da regra. `onUnhandledFrame` é a política para frames sem handler, não substitui o handler correspondente.

## Como verificar
Faça o cliente emitir a request real e confirme que o padrão é acionado; altere método, host e caminho individualmente para verificar quais dimensões o handler deve restringir.

## Conexões
- [[msw-handlers-happy-path-e-override-por-teste]] — Veja também: MSW: manter sucesso padrão central e estados excepcionais perto do teste.
- [[msw-handlers-organizados-por-dominio]] — Veja também: MSW: compor handlers por domínio sem concentrar toda a rede num arquivo.

## Fontes
- [MSW — http](https://mswjs.io/api/http) — handlers HTTP por método, resolver, parâmetros e opção once; consultado em 2026-10-02.
- [MSW — Structuring handlers](https://mswjs.io/guides/best-practices/structuring-handlers) — handlers de sucesso, overrides e composição por domínio; consultado em 2026-10-02.
