---
id: software.testes.tranche15.000913
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
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://karatelabs.github.io/karate/#data-driven-tests", "https://karatelabs.github.io/karate/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Karate: reutilizar features com call e read

## Em uma frase
`call` executa outra feature como função em contexto isolado, `callonce` reaproveita o resultado e `read` carrega conteúdo de arquivo para os dados do cenário.

## Por que importa
Duplicar fluxos de apoio, como autenticação e carga de massa, cria divergência entre cenários e aumenta o custo de toda mudança de contrato.

## Como funciona
Extraia fluxos reutilizáveis para features próprias, passe parâmetros explícitos e escolha a forma de chamada conforme o resultado precise ser recalculado ou compartilhado.

## Exemplo
`* def token = call read('login.feature')` obtém o resultado da autenticação, e `* def payload = read('dados/pedido.json')` carrega a massa do cenário.

## Limites e trade-offs
Recursos compartilhados criam acoplamento de contrato e podem propagar falhas para muitos cenários; a feature reutilizada precisa ser pequena, estável e coberta por testes próprios.

## Como verificar
Rode o cenário chamador isoladamente e confirme que ele não depende de variável deixada por outra feature nem de estado implícito do runner.

## Conexões
- [[karate-config-js]] — Veja também: Karate: separar configuração por ambiente.
- [[karate-parallel-runner]] — Veja também: Karate: executar features em paralelo.

## Fontes
- [Karate — Data driven tests](https://karatelabs.github.io/karate/#data-driven-tests) — tabelas, Examples, CSV e laços em feature files; consultado em 2026-10-02.
- [Karate — Documentation](https://karatelabs.github.io/karate/) — DSL Gherkin com steps embutidos, asserções, configuração e relatórios; consultado em 2026-10-02.
