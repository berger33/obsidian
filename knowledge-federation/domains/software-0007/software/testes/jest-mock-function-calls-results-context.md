---
id: software.testes.tranche10.000384
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://jestjs.io/docs/mock-functions", "https://jestjs.io/docs/jest-object"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jest: inspecionar chamadas e resultados de jest.fn

## Em uma frase
Mock functions registram chamadas, resultados, instâncias e contexto this para assertions sobre colaboração.

## Por que importa
Jest precisa aguardar corretamente operações assíncronas e isolar estado de mocks para que uma aprovação corresponda ao caminho realmente executado. Checar somente que uma função mock foi chamada pode ignorar argumento errado ou retorno inesperado.

## Como funciona
Retorne ou aguarde Promises, configure hooks no escopo necessário e trate snapshots e thresholds como evidências revisáveis, não como objetivos isolados. Use assertions específicas como calls e results para o comportamento relevante e defina implementação quando o SUT depende de um retorno.

## Exemplo
Um mock de callback recebe o id esperado e retorna Promise resolvida que controla o estado final do componente.

## Limites e trade-offs
Os exemplos seguem a documentação Jest 30.5; mocks, timers e suporte ESM variam conforme ambiente, transformação e versão do Node. Histórico de chamadas pertence ao estado do mock e deve ser limpo ou recriado entre casos.

## Como verificar
Introduza argumento incorreto e retorno diferente em testes separados para confirmar que cada assertion detecta a divergência certa.

## Conexões
- [[jest-beforeall-nao-compartilha-estado-entre-arquivos]] — Veja também: Jest: tratar beforeAll como escopo do arquivo de teste.
- [[jest-clear-reset-restore-mocks-diferencas]] — Veja também: Jest: distinguir limpar, resetar e restaurar mocks.

## Fontes
- [Jest 30.5 — Mock Functions](https://jestjs.io/docs/mock-functions) — estado de chamadas, resultados, implementações e spies; consultado em 2026-10-02.
- [Jest 30.5 — The Jest object](https://jestjs.io/docs/jest-object) — limpeza, reset, restauração e isolamento de módulos; consultado em 2026-10-02.
