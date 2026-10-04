---
id: software.testes.tranche20.001451
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

# NBomber: dividir o cenário em passos

## Em uma frase
Passos separam etapas da operação, cada uma com medidas próprias de latência, contagem e tamanho, agregadas ao resultado do cenário.

## Por que importa
A divisão localiza a etapa responsável pela degradação, separando tempo de conexão de tempo de processamento.

## Como funciona
Nomeie os passos pela operação executada, mantenha poucos passos por cenário e devolva o resultado de cada um.

## Exemplo
O fluxo pode separar autenticação, consulta e envio, mostrando qual etapa cresce quando a carga aumenta.

## Limites e trade-offs
Passos em excesso fragmentam as medidas, e passos que não devolvem resultado perdem a contabilização correspondente.

## Como verificar
Compare a distribuição de latência entre passos em duas cargas distintas e identifique a etapa que degradou.

## Conexões
- [[nb-load-simulations]] — Veja também: NBomber: definir o perfil de carga.
- [[nb-warmup-and-duration]] — Veja também: NBomber: controlar aquecimento e duração.

## Fontes
- [NBomber — Pacote publicado](https://www.nuget.org/packages/NBomber) — versões, dependências e documentação do pacote; consultado em 2026-10-03.
- [NBomber — repositório oficial](https://github.com/PragmaticFlow/NBomber) — código-fonte, integrações e documentação do projeto; consultado em 2026-10-03.
