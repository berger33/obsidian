---
id: software.testes.tranche20.001453
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

# NBomber: falhar o trabalho por limite

## Em uma frase
A execução permite declarar limites sobre as métricas, como percentual de falhas e percentil de latência, avaliados ao final do teste.

## Por que importa
Transformar o critério de desempenho em verificação automática evita que a regressão seja percebida apenas por leitura de relatório.

## Como funciona
Declare limites realistas por cenário, trate a violação como falha do trabalho e revise os limites quando o sistema mudar de forma justificada.

## Exemplo
O trabalho pode falhar quando o percentil de latência passar do limite acordado para a operação crítica.

## Limites e trade-offs
Limites apertados demais tornam a esteira ruidosa, e limites frouxos deixam de detectar degradação relevante.

## Como verificar
Ajuste um limite para um valor que a execução atual viola e confirme que o trabalho falha com mensagem indicando a métrica.

## Conexões
- [[nb-warmup-and-duration]] — Veja também: NBomber: controlar aquecimento e duração.
- [[nb-reports-and-sinks]] — Veja também: NBomber: analisar relatórios e publicar métricas.

## Fontes
- [NBomber — repositório oficial](https://github.com/PragmaticFlow/NBomber) — código-fonte, integrações e documentação do projeto; consultado em 2026-10-03.
- [NBomber — Pacote publicado](https://www.nuget.org/packages/NBomber) — versões, dependências e documentação do pacote; consultado em 2026-10-03.
