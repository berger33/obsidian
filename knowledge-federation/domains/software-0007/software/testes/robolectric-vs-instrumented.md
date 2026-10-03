---
id: software.testes.tranche20.001447
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://robolectric.org/getting-started/", "https://github.com/robolectric/robolectric"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robolectric: escolher entre JVM e execução instrumentada

## Em uma frase
Testes na JVM rodam rápido e cobrem lógica e ciclo de vida simulado; testes instrumentados exercitam o sistema real em aparelho ou emulador.

## Por que importa
A escolha errada de camada deixa a esteira lenta ou cria pontos cegos em comportamentos que só o dispositivo real revela.

## Como funciona
Mantenha a maioria dos casos na JVM, reserve execução instrumentada para integrações com hardware, permissões reais e desempenho.

## Exemplo
Uma verificação de câmera pertence ao aparelho, enquanto a regra de validação da tela pertence à JVM.

## Limites e trade-offs
Tentar simular todos os serviços na JVM leva a sombras complexas e frágeis, e usar apenas aparelho encarece e atrasa cada revisão.

## Como verificar
Classifique os casos existentes por camada e confirme que cada comportamento é verificado onde é reproduzido com fidelidade.

## Conexões
- [[robolectric-frameworks-integration]] — Veja também: Robolectric: integrar com bibliotecas de teste.
- [[robolectric-limits-and-practices]] — Veja também: Robolectric: reconhecer limites.

## Fontes
- [Robolectric — Primeiros passos](https://robolectric.org/getting-started/) — configuração do projeto, executor e ciclo de vida de telas; consultado em 2026-10-03.
- [Robolectric — repositório oficial](https://github.com/robolectric/robolectric) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
