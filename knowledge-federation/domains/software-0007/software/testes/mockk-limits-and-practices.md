---
id: software.testes.tranche20.001428
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
fontes: ["https://github.com/mockk/mockk/blob/master/README.md", "https://github.com/mockk/mockk"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MockK: reconhecer limites

## Em uma frase
Dublês verificam interações no nível da linguagem, sem substituir testes de integração nem comprovar o comportamento do sistema real.

## Por que importa
Testes excessivamente apoiados em dublês passam a descrever a implementação atual e falham a cada refatoração legítima.

## Como funciona
Prefira dublês nas fronteiras externas do sistema, mantenha testes reais para integrações e verifique efeitos observáveis antes das chamadas internas.

## Exemplo
A verificação do cálculo pode depender de um dublê de relógio, enquanto a integração com o banco permanece em teste real.

## Limites e trade-offs
Verificar toda chamada interna transforma refatoração em quebra de teste, e dublar o que poderia ser exercitado de verdade reduz a cobertura útil.

## Como verificar
Escolha um teste com muitos dublês e avalie se parte das dependências poderia usar implementações reais mais simples.

## Conexões
- [[mockk-chained-and-hierarchies]] — Veja também: MockK: encadear dublês e hierarquias.

## Fontes
- [MockK — README oficial](https://github.com/mockk/mockk/blob/master/README.md) — dublês, relaxamento, verificação, objetos e corrotinas; consultado em 2026-10-03.
- [MockK — repositório oficial](https://github.com/mockk/mockk) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
