---
id: software.testes.tranche20.001455
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

# NBomber: medir detalhes de protocolo

## Em uma frase
Extensões adicionam métricas específicas de protocolo, como tempos de conexão, reutilização de conexões e volume trafegado.

## Por que importa
Métricas de protocolo explicam o comportamento observado, distinguindo tempo de rede de tempo de processamento da aplicação.

## Como funciona
Inclua o plugin correspondente ao protocolo testado, interprete as métricas junto do cenário e guarde a configuração com o teste.

## Exemplo
Aumento de latência acompanhado de crescimento no número de conexões novas costuma indicar limite de pool, não de processamento.

## Limites e trade-offs
Ler apenas a latência total esconde a causa, e plugins incompatíveis com a versão podem distorcer as medidas.

## Como verificar
Compare as métricas de conexão em duas taxas de carga e verifique se a reutilização se mantém estável.

## Conexões
- [[nb-reports-and-sinks]] — Veja também: NBomber: analisar relatórios e publicar métricas.
- [[nb-data-feeds-and-realism]] — Veja também: NBomber: alimentar cenários com dados.

## Fontes
- [NBomber — repositório oficial](https://github.com/PragmaticFlow/NBomber) — código-fonte, integrações e documentação do projeto; consultado em 2026-10-03.
- [NBomber — Pacote publicado](https://www.nuget.org/packages/NBomber) — versões, dependências e documentação do pacote; consultado em 2026-10-03.
