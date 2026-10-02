---
id: software.testes.tranche09.000268
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
fontes: ["https://docs.pact.io/pact_broker/can_i_deploy", "https://docs.pact.io/getting_started/terminology"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: testar can-i-deploy contra o ambiente real de destino

## Em uma frase
can-i-deploy consulta a matriz para decidir se uma versão é compatível com os participantes já registrados no ambiente de destino.

## Por que importa
Pact captura interações relevantes para consumidores concretos e verifica compatibilidade, mas não pretende provar toda a correção funcional do serviço. Um resultado positivo para outro ambiente ou conjunto de versões não responde automaticamente à pergunta de produção.

## Como funciona
Mantenha interações pequenas, prepare provider states determinísticos e publique contratos e resultados com versões identificáveis para a matriz do Broker. Registre deploys/releases no Broker e execute a verificação com participante, versão e environment que o release usará.

## Exemplo
Antes de produção, o pipeline avalia a versão candidata contra os consumers e providers registrados em production.

## Limites e trade-offs
O alcance depende das interações declaradas, dos matchers escolhidos, da execução local e da publicação correta de evidências no Broker. A resposta depende dos resultados publicados e do estado atualizado do ambiente; não é teste de smoke nem garantia universal.

## Como verificar
Faça ensaio com combinação compatível e incompatível, confira exit code e verifique se a matriz contém todos os serviços implantados.

## Conexões
- [[pact-publish-version-verification-matrix]] — Veja também: Pact: publicar versões e resultados para compatibilidade.
- [[pact-webhook-provider-verification-feedback]] — Veja também: Pact: tratar webhook como gatilho, não resultado de verificação.

## Fontes
- [Pact Broker — Can I Deploy](https://docs.pact.io/pact_broker/can_i_deploy) — matriz de versões e compatibilidade com o ambiente de deploy; consultado em 2026-10-02.
- [Pact — Terminology](https://docs.pact.io/getting_started/terminology) — interactions, contracts, provider states e verificação; consultado em 2026-10-02.
