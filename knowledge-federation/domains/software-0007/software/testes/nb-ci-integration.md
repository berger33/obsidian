---
id: software.testes.tranche20.001458
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
fontes: ["https://github.com/PragmaticFlow/NBomber", "https://www.nuget.org/packages/NBomber"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# NBomber: usar na esteira contínua

## Em uma frase
A ferramenta integra-se a executores de teste conhecidos, permitindo que a carga faça parte do trabalho automatizado.

## Por que importa
Testes de carga curtos e estáveis na esteira detectam regressões cedo, antes de a degradação chegar ao ambiente publicado.

## Como funciona
Mantenha na esteira uma verificação curta com limites objetivos e reserve cargas longas para execução agendada.

## Exemplo
O trabalho de integração pode rodar um cenário de fumaça de carga por poucos minutos em cada revisão.

## Limites e trade-offs
Execuções longas em cada revisão inviabilizam a esteira, e ambientes compartilhados produzem resultados ruidosos que não representam o sistema.

## Como verificar
Compare o resultado do cenário de fumaça em duas revisões próximas e confirme que a variação é pequena.

## Conexões
- [[nb-distributed-cluster]] — Veja também: NBomber: executar em cluster distribuído.
- [[nb-limits-and-practices]] — Veja também: NBomber: interpretar resultados e reconhecer limites.

## Fontes
- [NBomber — repositório oficial](https://github.com/PragmaticFlow/NBomber) — código-fonte, integrações e documentação do projeto; consultado em 2026-10-03.
- [NBomber — Pacote publicado](https://www.nuget.org/packages/NBomber) — versões, dependências e documentação do pacote; consultado em 2026-10-03.
