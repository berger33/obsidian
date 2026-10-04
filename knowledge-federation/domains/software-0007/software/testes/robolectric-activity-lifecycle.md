---
id: software.testes.tranche20.001442
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

# Robolectric: controlar o ciclo de vida de telas

## Em uma frase
A biblioteca oferece construção controlada de telas, permitindo criar, iniciar, retomar, pausar e destruir conforme o cenário exige.

## Por que importa
Controlar o ciclo de vida verifica transições que só ocorrem quando o usuário sai e volta à tela, sem depender de interação real.

## Como funciona
Construa a tela pelo controlador, avance pelos estados necessários e verifique o estado resultante em cada transição.

## Exemplo
O teste pode criar a tela, retomá-la, pausá-la e confirmar que o estado salvo é restaurado ao recriá-la.

## Limites e trade-offs
Criar a tela sem percorrer o ciclo esconde defeitos de restauração, e verificar apenas o estado inicial cobre uma fração do comportamento.

## Como verificar
Simule a morte e recriação da tela e confirme que os dados do usuário são restaurados como previsto.

## Conexões
- [[robolectric-shadows]] — Veja também: Robolectric: substituir serviços com sombras.
- [[robolectric-resources-and-qualifiers]] — Veja também: Robolectric: usar recursos e qualificadores.

## Fontes
- [Robolectric — Primeiros passos](https://robolectric.org/getting-started/) — configuração do projeto, executor e ciclo de vida de telas; consultado em 2026-10-03.
- [Robolectric — repositório oficial](https://github.com/robolectric/robolectric) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
