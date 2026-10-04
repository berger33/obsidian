---
id: software.testes.tranche09.000269
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
fontes: ["https://docs.pact.io/pact_broker/webhooks", "https://docs.pact.io/provider"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: tratar webhook como gatilho, não resultado de verificação

## Em uma frase
Webhook do Broker pode iniciar um build de provider quando um contrato requer verificação; compatibilidade só muda após resultado de verificação publicado.

## Por que importa
Pact captura interações relevantes para consumidores concretos e verifica compatibilidade, mas não pretende provar toda a correção funcional do serviço. A entrega do webhook confirma um evento de integração, não que o provider passou nem que seu resultado chegou à matriz.

## Como funciona
Mantenha interações pequenas, prepare provider states determinísticos e publique contratos e resultados com versões identificáveis para a matriz do Broker. Faça o endpoint validar o evento, iniciar CI idempotente e publicar o resultado da versão provider depois do teste terminar.

## Exemplo
Uma pact recém-publicada agenda pipeline de provider; o gate aguarda evidência de verificação correspondente antes de avaliar deploy.

## Limites e trade-offs
O alcance depende das interações declaradas, dos matchers escolhidos, da execução local e da publicação correta de evidências no Broker. Webhooks podem ser repetidos ou atrasados e exigem credenciais, retries e correlação conforme a infraestrutura.

## Como verificar
Simule evento duplicado e falha do build; confirme que há rastreabilidade e que ausência de resultado não vira sucesso implícito.

## Conexões
- [[pact-can-i-deploy-environment-context]] — Veja também: Pact: testar can-i-deploy contra o ambiente real de destino.

## Fontes
- [Pact Broker — Webhooks](https://docs.pact.io/pact_broker/webhooks) — eventos e integração de verificação do provider no CI; consultado em 2026-10-02.
- [Pact — Verifying pacts](https://docs.pact.io/provider) — verificação local do provider, stubs downstream e publicação de resultados; consultado em 2026-10-02.
