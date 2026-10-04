---
id: software.testes.tranche09.000260
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
fontes: ["https://docs.pact.io/consumer", "https://docs.pact.io/getting_started/terminology"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: capturar a requisição que o cliente realmente envia

## Em uma frase
Um consumer Pact deve exercitar o cliente de API e registrar a interação HTTP que esse código produz contra o mock provider.

## Por que importa
Pact captura interações relevantes para consumidores concretos e verifica compatibilidade, mas não pretende provar toda a correção funcional do serviço. Construir a requisição esperada manualmente sem chamar o cliente deixa bugs de serialização, headers ou parâmetros fora do contrato.

## Como funciona
Mantenha interações pequenas, prepare provider states determinísticos e publique contratos e resultados com versões identificáveis para a matriz do Broker. Execute o método público do cliente com dados representativos e configure o mock para responder apenas à interação esperada.

## Exemplo
O cliente de catálogo recebe filtro e token, envia a query e desserializa uma resposta pactuada em um teste isolado.

## Limites e trade-offs
O alcance depende das interações declaradas, dos matchers escolhidos, da execução local e da publicação correta de evidências no Broker. O contrato protege apenas a interação definida; não valida regras de negócio completas no provider.

## Como verificar
Inspecione pact file e chamadas do teste para garantir que requests foram produzidas pelo código real do consumer e são relevantes a ele.

## Conexões
- [[pact-matchers-consumer-relevant]] — Veja também: Pact: escolher matchers por relevância para o consumidor.

## Fontes
- [Pact — Writing consumer tests](https://docs.pact.io/consumer) — escopo de testes consumer, matching e evitar testes funcionais do provider; consultado em 2026-10-02.
- [Pact — Terminology](https://docs.pact.io/getting_started/terminology) — interactions, contracts, provider states e verificação; consultado em 2026-10-02.
