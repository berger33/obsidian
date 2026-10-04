---
id: software.testes.tranche22.001573
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://pester.dev/docs/usage/mocking", "https://pester.dev/docs/usage/code-coverage"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pester: Describe, Context e It aninhados

## Em uma frase
A estrutura de suíte do Pester é Describe contendo Context contendo It; cada It é um caso com título legível, e o BeforeAll no topo do Describe prepara estado e faz o dot-sourcing do código sob teste.

## Por que importa
Separar o cenário (Context) da afirmação (It) mantém o relatório legível para gente de negócio e agrupa setups por situação, não por teste.

## Como funciona
Dentro de BeforeAll, o truque documentado é carregar o par de produção com $PSCommandPath.Replace('.Tests.ps1','.ps1'), mantendo teste e código colados no mesmo diretório.

## Exemplo
Context 'When there are Changes' { BeforeEach { Mock Get-Version { return 1.1 } } ... } — cada Context traz seu próprio setup de mocks por caso.

## Limites e trade-offs
O quick start e os exemplos da documentação ainda usam blocos no estilo antigo em alguns trechos; a semântica de isolamento entre BeforeAll e BeforeEach mudou do v4 para o v5 e merece leitura atenta.

## Como verificar
Escreva dois Its que dependem do mesmo mock declarado num BeforeEach e confirme que cada um vê o mock recém-registrado, sem contaminação.

## Conexões
- [[pester-install-module]] — Veja também: Pester: instalação pelo gallery e importação.
- [[pester-assertions-should]] — Veja também: Pester: asserções Should e a mensagem de falha.

## Fontes
- [Pester — Mocking](https://pester.dev/docs/usage/mocking) — Mock, Should-Invoke, escopo, natives e classes; consultado em 2026-10-03.
- [Pester — Code coverage](https://pester.dev/docs/usage/code-coverage) — New-PesterConfiguration, formatos JaCoCo/Cobertura e tracer; consultado em 2026-10-03.
