---
id: software.testes.tranche10.000385
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
fontes: ["https://jestjs.io/docs/jest-object", "https://jestjs.io/docs/mock-functions"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jest: distinguir limpar, resetar e restaurar mocks

## Em uma frase
Clear apaga histórico, reset também substitui implementação configurada, e restore devolve implementação original quando a função é spy.

## Por que importa
Jest precisa aguardar corretamente operações assíncronas e isolar estado de mocks para que uma aprovação corresponda ao caminho realmente executado. Usar a operação errada pode apagar comportamento necessário ou deixar um patch ativo depois do teste.

## Como funciona
Retorne ou aguarde Promises, configure hooks no escopo necessário e trate snapshots e thresholds como evidências revisáveis, não como objetivos isolados. Escolha clear para chamadas, reset para histórico mais implementação e restore para desfazer spies sobre objetos reais.

## Exemplo
Após cada caso, restoreAllMocks devolve métodos espiados ao original e o próximo caso cria seu próprio comportamento.

## Limites e trade-offs
Os exemplos seguem a documentação Jest 30.5; mocks, timers e suporte ESM variam conforme ambiente, transformação e versão do Node. Restaurar só tem efeito apropriado para mocks criados por spyOn; uma função mock isolada não tem implementação original a recuperar.

## Como verificar
Verifique chamadas e implementação antes e depois do cleanup e confirme que o objeto real voltou ao comportamento original.

## Conexões
- [[jest-mock-function-calls-results-context]] — Veja também: Jest: inspecionar chamadas e resultados de jest.fn.
- [[jest-fake-timers-timers-pendentes-recursivos]] — Veja também: Jest: controlar timers falsos sem drenar loops recursivos.

## Fontes
- [Jest 30.5 — The Jest object](https://jestjs.io/docs/jest-object) — limpeza, reset, restauração e isolamento de módulos; consultado em 2026-10-02.
- [Jest 30.5 — Mock Functions](https://jestjs.io/docs/mock-functions) — estado de chamadas, resultados, implementações e spies; consultado em 2026-10-02.
