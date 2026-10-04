---
id: software.testes.tranche08.000166
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://testing-library.com/docs/guiding-principles/", "https://testing-library.com/docs/react-testing-library/intro/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Testing Library: verificar resultado em vez de detalhe interno

## Em uma frase
Prefira assertions sobre o que aparece ou muda para a pessoa usuária em vez de estado interno ou chamada privada do componente.

## Por que importa
Testes de implementação podem quebrar em refatorações sem alterar o comportamento e, ao mesmo tempo, não detectar interface incorreta.

## Como funciona
Defina ação, estado observável e resultado esperado. Use mocks somente em fronteiras externas relevantes, mantendo a semântica do componente acessível nas consultas.

## Exemplo
Após marcar uma tarefa, verifique estado e texto anunciados; não exija que um hook interno tenha sido chamado uma quantidade específica de vezes.

## Limites e trade-offs
Em alguns casos, uma interação externa específica é parte do contrato e deve ser verificada na fronteira; evite transformar o princípio em proibição absoluta de mocks.

## Como verificar
Faça uma refatoração estrutural sem mudar a UI e observe se o teste continua. Em seguida, altere o comportamento visível e confirme que falha.

## Conexões
- [[playwright-locators-assertions-web-first]] — Veja também: Playwright: locators resilientes e assertions web-first.
- [[flutter-plugin-channel-mock-fronteira]] — Veja também: Flutter: mockar canais de plugin sem alegar teste nativo.

## Fontes
- [Testing Library — Guiding Principles](https://testing-library.com/docs/guiding-principles/) — testes que refletem a utilização observável; consultado em 2026-10-02.
- [Testing Library — React Testing Library](https://testing-library.com/docs/react-testing-library/intro/) — orientação por DOM e comportamento percebido pelo usuário; consultado em 2026-10-02.
