---
id: software.testes.tranche09.000265
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://docs.pact.io/provider/using_provider_states_effectively", "https://docs.pact.io/provider"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: evitar falso positivo por parâmetro de busca ignorado

## Em uma frase
Um provider pode ignorar parâmetro inválido e ainda responder com um registro que satisfaz uma fixture pequena, fazendo o pact passar por engano.

## Por que importa
Pact captura interações relevantes para consumidores concretos e verifica compatibilidade, mas não pretende provar toda a correção funcional do serviço. Esse caso mostra que resposta aparentemente correta não comprova que a requisição consumer usou o nome de campo aceito.

## Como funciona
Mantenha interações pequenas, prepare provider states determinísticos e publique contratos e resultados com versões identificáveis para a matriz do Broker. Inclua no estado dados que discriminem o filtro e valide no contrato somente os sinais de request/response necessários ao consumer.

## Exemplo
A busca prepara registros Mary e John; a interação por Mary espera somente esse resultado e detecta um filtro ignorado.

## Limites e trade-offs
O alcance depende das interações declaradas, dos matchers escolhidos, da execução local e da publicação correta de evidências no Broker. Se possível, o provider pode expor no resultado os parâmetros efetivamente interpretados; a solução deve corresponder à API real.

## Como verificar
Altere deliberadamente o nome de um parâmetro e confirme que verificação detecta a chamada incorreta em vez de passar com fixture mínima.

## Conexões
- [[pact-provider-state-setup-per-interaction]] — Veja também: Pact: preparar provider states determinísticos por interação.
- [[pact-stub-below-request-validation]] — Veja também: Pact: manter stubs abaixo da validação do request.

## Fontes
- [Pact — Using provider states effectively](https://docs.pact.io/provider/using_provider_states_effectively) — configuração de estados provider e risco de falsos positivos; consultado em 2026-10-02.
- [Pact — Verifying pacts](https://docs.pact.io/provider) — verificação local do provider, stubs downstream e publicação de resultados; consultado em 2026-10-02.
