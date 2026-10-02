---
id: software.testes.tranche09.000264
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
fontes: ["https://docs.pact.io/provider/using_provider_states_effectively", "https://docs.pact.io/getting_started/terminology"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: preparar provider states determinísticos por interação

## Em uma frase
Provider states nomeiam o estado prévio necessário para reproduzir uma interação, e o código de setup pertence ao provider.

## Por que importa
Pact captura interações relevantes para consumidores concretos e verifica compatibilidade, mas não pretende provar toda a correção funcional do serviço. Compartilhar estado residual entre interações pode fazer a verificação depender da ordem ou passar com dados que o consumer não declarou.

## Como funciona
Mantenha interações pequenas, prepare provider states determinísticos e publique contratos e resultados com versões identificáveis para a matriz do Broker. Implemente setup idempotente por estado, use parâmetros explícitos e limpe dados ao redor de cada verificação.

## Exemplo
Duas interações usam o mesmo endpoint com estados sem pedido e com pedido criado, preparados independentemente antes do replay.

## Limites e trade-offs
O alcance depende das interações declaradas, dos matchers escolhidos, da execução local e da publicação correta de evidências no Broker. Provider state não deve virar mecanismo de teste funcional genérico nem depender de dados de produção.

## Como verificar
Execute cada interação isoladamente e em ordem alterada; falha ou sucesso não deve depender do cenário executado anteriormente.

## Conexões
- [[pact-provider-verify-local-instance]] — Veja também: Pact: verificar contracts contra instância local do provider.
- [[pact-provider-state-false-positive-params]] — Veja também: Pact: evitar falso positivo por parâmetro de busca ignorado.

## Fontes
- [Pact — Using provider states effectively](https://docs.pact.io/provider/using_provider_states_effectively) — configuração de estados provider e risco de falsos positivos; consultado em 2026-10-02.
- [Pact — Terminology](https://docs.pact.io/getting_started/terminology) — interactions, contracts, provider states e verificação; consultado em 2026-10-02.
