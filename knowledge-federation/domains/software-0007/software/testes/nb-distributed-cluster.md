---
id: software.testes.tranche20.001457
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

# NBomber: executar em cluster distribuído

## Em uma frase
A execução pode ser distribuída entre agentes coordenados, somando a carga de várias máquinas e agregando os resultados.

## Por que importa
Uma única máquina geradora vira o gargalo antes do serviço testado, e a distribuição permite alcançar taxas maiores.

## Como funciona
Distribua os cenários entre agentes, mantenha a configuração idêntica e verifique que o gerador não é o limitante.

## Exemplo
Picos de alta taxa podem exigir três geradores, com o serviço medido a partir dos resultados agregados.

## Limites e trade-offs
Relógios diferentes entre agentes distorcem as métricas agregadas, e agentes desiguais produzem distribuição irregular da carga.

## Como verificar
Monitore o uso da máquina geradora durante a execução e confirme que ela não está saturada.

## Conexões
- [[nb-data-feeds-and-realism]] — Veja também: NBomber: alimentar cenários com dados.
- [[nb-ci-integration]] — Veja também: NBomber: usar na esteira contínua.

## Fontes
- [NBomber — repositório oficial](https://github.com/PragmaticFlow/NBomber) — código-fonte, integrações e documentação do projeto; consultado em 2026-10-03.
- [NBomber — Pacote publicado](https://www.nuget.org/packages/NBomber) — versões, dependências e documentação do pacote; consultado em 2026-10-03.
