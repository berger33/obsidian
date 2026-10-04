---
id: software.testes.tranche20.001452
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

# NBomber: controlar aquecimento e duração

## Em uma frase
A execução pode incluir fase de aquecimento antes da medição e define a duração de cada simulação separadamente.

## Por que importa
Sem aquecimento, as primeiras medições incluem compilação e preenchimento de cache, distorcendo os resultados.

## Como funciona
Use aquecimento quando a primeira execução for mais lenta, documente a fase e compare execuções com a mesma configuração.

## Exemplo
A fase inicial pode preencher o cache do serviço antes da medição, que passa a refletir o regime estável.

## Limites e trade-offs
Medir sem aquecimento em ambientes que aquecem com a carga leva a conclusões erradas sobre capacidade.

## Como verificar
Execute o cenário com e sem aquecimento e compare a latência do primeiro minuto nos dois modos.

## Conexões
- [[nb-steps-and-metrics]] — Veja também: NBomber: dividir o cenário em passos.
- [[nb-assertions-and-thresholds]] — Veja também: NBomber: falhar o trabalho por limite.

## Fontes
- [NBomber — Pacote publicado](https://www.nuget.org/packages/NBomber) — versões, dependências e documentação do pacote; consultado em 2026-10-03.
- [NBomber — repositório oficial](https://github.com/PragmaticFlow/NBomber) — código-fonte, integrações e documentação do projeto; consultado em 2026-10-03.
