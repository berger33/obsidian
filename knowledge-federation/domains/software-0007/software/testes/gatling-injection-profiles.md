---
id: software.testes.tranche17.001058
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://docs.gatling.io/concepts/injection/", "https://docs.gatling.io/concepts/simulation/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: escolher o perfil de injeção

## Em uma frase
Os perfis definem como usuários virtuais entram ao longo do tempo, seja em modelo aberto pela taxa de chegada, seja em modelo fechado por usuários simultâneos.

## Por que importa
O formato da carga determina qual propriedade do sistema é exercitada, e usar sempre o mesmo perfil esconde modos distintos de degradação.

## Como funciona
Escolha entre taxa constante, rampa, pico ou escalonamento conforme a pergunta, e nomeie cada etapa para correlacionar com o relatório.

## Exemplo
Uma rampa lenta até um patamar alto revela o ponto em que a latência deixa de ser estável, enquanto um pico curto testa a recuperação.

## Limites e trade-offs
Taxa alta com cenário longo esgota os usuários disponíveis e gera espera no gerador, o que exige acompanhar as métricas do próprio executor.

## Como verificar
Compare dois perfis na mesma simulação e observe como a curva de latência responde a cada formato de chegada.

## Conexões
- [[gatling-scenario-flow]] — Veja também: Gatling: descrever a jornada com ações encadeadas.
- [[gatling-checks]] — Veja também: Gatling: validar respostas com checagens.

## Fontes
- [Gatling — Injection](https://docs.gatling.io/concepts/injection/) — perfis de injeção em modelo aberto e fechado, rampas e picos; consultado em 2026-10-03.
- [Gatling — Simulation](https://docs.gatling.io/concepts/simulation/) — estrutura da simulação, protocolo, cenários e relatório de execução; consultado em 2026-10-03.
