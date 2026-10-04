---
id: software.testes.tranche20.001450
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
fontes: ["https://www.nuget.org/packages/NBomber", "https://github.com/PragmaticFlow/NBomber"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NBomber: definir o perfil de carga

## Em uma frase
As simulações descrevem o ritmo de injeção de iterações, incluindo taxa constante, taxa crescente com rampa e número fixo de cópias.

## Por que importa
Perfis diferentes respondem a perguntas distintas, como capacidade sustentada, ponto de saturação e comportamento sob picos.

## Como funciona
Combine simulações na mesma execução, ajuste taxa e duração ao objetivo e mantenha o ambiente estável durante a medição.

## Exemplo
A execução pode subir em rampa até o limite conhecido e depois manter taxa constante para medir o regime estável.

## Limites e trade-offs
Uma única taxa alta sem rampa não revela onde começa a degradação, e durações curtas capturam apenas o aquecimento.

## Como verificar
Execute o mesmo cenário com taxa constante e com rampa e compare os dois comportamentos observados.

## Conexões
- [[nb-scenarios-basics]] — Veja também: NBomber: escrever um cenário de carga.
- [[nb-steps-and-metrics]] — Veja também: NBomber: dividir o cenário em passos.

## Fontes
- [NBomber — Pacote publicado](https://www.nuget.org/packages/NBomber) — versões, dependências e documentação do pacote; consultado em 2026-10-03.
- [NBomber — repositório oficial](https://github.com/PragmaticFlow/NBomber) — código-fonte, integrações e documentação do projeto; consultado em 2026-10-03.
