---
id: software.testes.tranche09.000266
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
fontes: ["https://docs.pact.io/provider", "https://docs.pact.io/provider/using_provider_states_effectively"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: manter stubs abaixo da validação do request

## Em uma frase
Se o provider precisa de stubs, o guia recomenda que validadores e extração do corpo do request ainda sejam exercitados antes da fronteira stubada.

## Por que importa
Pact captura interações relevantes para consumidores concretos e verifica compatibilidade, mas não pretende provar toda a correção funcional do serviço. Stubar cedo demais pode aceitar payload inválido e deixar sem teste a interpretação que o contrato deveria proteger.

## Como funciona
Mantenha interações pequenas, prepare provider states determinísticos e publique contratos e resultados com versões identificáveis para a matriz do Broker. Identifique a primeira dependência downstream e substitua somente chamadas posteriores ao parsing e validação do request.

## Exemplo
O teste envia JSON malformado e espera erro de validação sem invocar o stub de pagamento; o caso válido então alcança o stub.

## Limites e trade-offs
O alcance depende das interações declaradas, dos matchers escolhidos, da execução local e da publicação correta de evidências no Broker. Nem toda arquitetura tem a mesma camada; selecione a fronteira de acordo com onde o serviço extrai e valida conteúdo.

## Como verificar
Envie corpo inválido e válido ao mesmo endpoint e confirme que somente o válido produz chamada observável à dependência stubada.

## Conexões
- [[pact-provider-state-false-positive-params]] — Veja também: Pact: evitar falso positivo por parâmetro de busca ignorado.
- [[pact-publish-version-verification-matrix]] — Veja também: Pact: publicar versões e resultados para compatibilidade.

## Fontes
- [Pact — Verifying pacts](https://docs.pact.io/provider) — verificação local do provider, stubs downstream e publicação de resultados; consultado em 2026-10-02.
- [Pact — Using provider states effectively](https://docs.pact.io/provider/using_provider_states_effectively) — configuração de estados provider e risco de falsos positivos; consultado em 2026-10-02.
