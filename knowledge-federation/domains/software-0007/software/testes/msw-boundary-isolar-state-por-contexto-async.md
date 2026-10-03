---
id: software.testes.tranche15.000926
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
fontes: ["https://mswjs.io/api/setup-server/boundary", "https://mswjs.io/api/setup-server/use"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW: criar boundary quando handlers de runtime precisam de escopo assíncrono

## Em uma frase
A API `boundary()` permite envolver uma função de modo que o estado do servidor seja delimitado no contexto assíncrono daquela chamada, útil quando execuções concorrentes precisam de overrides independentes.

## Por que importa
Sem isolamento, alterações em handlers podem vazar entre testes concorrentes que compartilham a instância.

## Como funciona
A API `server.boundary()` delimita a rede alterada no callback e nos contextos filhos por AsyncLocalStorage.

## Exemplo
No ambiente Node, envolva a função do caso com `server.boundary(async () => { server.use(...); await fetch(...); })()` e mantenha o lifecycle compartilhado de setupServer separado.

## Limites e trade-offs
boundary() é API exclusiva de Node com setupServer; ela isola comportamento de rede e overrides naquele contexto assíncrono, não banco, globals ou efeitos externos não propagados. Dentro de uma boundary, reset ainda pode ser necessário para restaurar comportamento nessa mesma boundary.

## Como verificar
Execute dois testes concorrentes em Node, cada um dentro de sua boundary e com resposta distinta para a mesma rota; confirme isolamento dos handlers e que fora do escopo permanece o handler base.

## Conexões
- [[msw-close-restaura-fronteira-de-processo]] — Veja também: MSW: fechar a interceptação depois da suite.
- [[msw-handlers-happy-path-e-override-por-teste]] — Veja também: MSW: manter sucesso padrão central e estados excepcionais perto do teste.

## Fontes
- [MSW — boundary()](https://mswjs.io/api/setup-server/boundary) — isolamento de comportamento de rede em escopos assíncronos concorrentes; consultado em 2026-10-02.
- [MSW — use()](https://mswjs.io/api/setup-server/use) — adição e precedência de runtime handlers; consultado em 2026-10-02.
