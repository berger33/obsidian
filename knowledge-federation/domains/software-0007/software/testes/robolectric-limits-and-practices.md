---
id: software.testes.tranche20.001448
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

# Robolectric: reconhecer limites

## Em uma frase
A simulação cobre grande parte das interfaces do sistema, mas não reproduz desempenho, hardware, nem o comportamento exato de versões de aparelhos.

## Por que importa
Considerar a suíte de JVM equivalente ao teste em dispositivo cria falsa confiança sobre desempenho e integrações físicas.

## Como funciona
Complemente os testes na JVM com verificação instrumentada nos fluxos críticos e mantenha a suíte rápida para execução frequente.

## Exemplo
Animações e renderizações reais podem diferir da simulação, exigindo verificação em aparelho para as telas mais sensíveis.

## Limites e trade-offs
Sombras podem divergir do sistema real, e o desempenho medido na JVM não representa o do dispositivo.

## Como verificar
Escolha um caso aprovado na JVM e reproduza o mesmo fluxo em aparelho, registrando as diferenças observadas.

## Conexões
- [[robolectric-vs-instrumented]] — Veja também: Robolectric: escolher entre JVM e execução instrumentada.

## Fontes
- [Robolectric — Primeiros passos](https://robolectric.org/getting-started/) — configuração do projeto, executor e ciclo de vida de telas; consultado em 2026-10-03.
- [Robolectric — repositório oficial](https://github.com/robolectric/robolectric) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
