---
id: software.testes.tranche09.000267
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
fontes: ["https://docs.pact.io/provider", "https://docs.pact.io/pact_broker/can_i_deploy"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: publicar versões e resultados para compatibilidade

## Em uma frase
A matriz do Broker depende de pacts publicados e resultados de verificação associados a versões identificáveis de consumer e provider.

## Por que importa
Pact captura interações relevantes para consumidores concretos e verifica compatibilidade, mas não pretende provar toda a correção funcional do serviço. Sem metadados consistentes, a CI pode exibir compatibilidade de uma revisão diferente daquela que será implantada.

## Como funciona
Mantenha interações pequenas, prepare provider states determinísticos e publique contratos e resultados com versões identificáveis para a matriz do Broker. Publique contratos após o teste do consumer e resultados após provider verification, usando a versão e branch do build.

## Exemplo
Duas revisões do consumer são verificadas contra versões do provider; o pipeline relaciona cada linha da matriz ao commit respectivo.

## Limites e trade-offs
O alcance depende das interações declaradas, dos matchers escolhidos, da execução local e da publicação correta de evidências no Broker. Um resultado publicado não demonstra compatibilidade com todo deploy possível se versões ou ambientes registrados estiverem incompletos.

## Como verificar
Compare metadados do artefato, contrato, verificação e código implantável; confirme que o Broker consegue distinguir builds concorrentes.

## Conexões
- [[pact-stub-below-request-validation]] — Veja também: Pact: manter stubs abaixo da validação do request.
- [[pact-can-i-deploy-environment-context]] — Veja também: Pact: testar can-i-deploy contra o ambiente real de destino.

## Fontes
- [Pact — Verifying pacts](https://docs.pact.io/provider) — verificação local do provider, stubs downstream e publicação de resultados; consultado em 2026-10-02.
- [Pact Broker — Can I Deploy](https://docs.pact.io/pact_broker/can_i_deploy) — matriz de versões e compatibilidade com o ambiente de deploy; consultado em 2026-10-02.
