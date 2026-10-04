---
id: software.testes.tranche09.000263
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
fontes: ["https://docs.pact.io/provider", "https://docs.pact.io/getting_started/terminology"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: verificar contracts contra instância local do provider

## Em uma frase
A verificação deve reproduzir interações contra uma instância local do provider em desenvolvimento ou CI para manter feedback rápido e estado controlável.

## Por que importa
Pact captura interações relevantes para consumidores concretos e verifica compatibilidade, mas não pretende provar toda a correção funcional do serviço. Verificar apenas um provider já implantado dificulta paralelismo, preparação de dados e depuração antes da publicação.

## Como funciona
Mantenha interações pequenas, prepare provider states determinísticos e publique contratos e resultados com versões identificáveis para a matriz do Broker. Suba o serviço no job, carregue pacts selecionados e use banco isolado ou dependências controladas conforme a integração exige.

## Exemplo
CI inicia provider com banco descartável, executa interações publicadas e guarda resultado associado ao commit verificado.

## Limites e trade-offs
O alcance depende das interações declaradas, dos matchers escolhidos, da execução local e da publicação correta de evidências no Broker. Substituir camada de dados pode reduzir fidelidade; não faça isso antes da validação do request que o contrato pretende cobrir.

## Como verificar
Confirme que a instância iniciada corresponde ao código do commit, que dependências estão delimitadas e que os resultados publicados identificam suas versões.

## Conexões
- [[pact-not-functional-provider-test]] — Veja também: Pact: não usar contrato como teste funcional do provider.
- [[pact-provider-state-setup-per-interaction]] — Veja também: Pact: preparar provider states determinísticos por interação.

## Fontes
- [Pact — Verifying pacts](https://docs.pact.io/provider) — verificação local do provider, stubs downstream e publicação de resultados; consultado em 2026-10-02.
- [Pact — Terminology](https://docs.pact.io/getting_started/terminology) — interactions, contracts, provider states e verificação; consultado em 2026-10-02.
