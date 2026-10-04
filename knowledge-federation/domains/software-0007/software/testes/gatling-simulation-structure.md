---
id: software.testes.tranche17.001056
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
fontes: ["https://docs.gatling.io/concepts/simulation/", "https://github.com/gatling/gatling"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: organizar a simulação como código

## Em uma frase
A simulação é uma classe executável que reúne o protocolo, os cenários e o perfil de injeção, permitindo versionar o teste de carga junto do serviço.

## Por que importa
Testes de carga mantidos em arquivos de configuração separados envelhecem sem revisão, enquanto código versionado passa pelas mesmas verificações do restante do repositório.

## Como funciona
Declare o protocolo com o endereço base, monte um ou mais cenários e ligue-os ao perfil de injeção no bloco de configuração.

## Exemplo
Uma simulação pode configurar cabeçalhos comuns no protocolo e reaproveitá-los em todos os pedidos, evitando repetição em cada requisição.

## Limites e trade-offs
A classe concentra tudo, e simulações muito grandes dificultam a leitura; a decomposição em partes nomeadas ajuda a manter o teste compreensível.

## Como verificar
Execute a simulação com um cenário mínimo e confirme que o relatório gerado lista a simulação, o cenário e o perfil declarados.

## Conexões
- [[gatling-scenario-flow]] — Veja também: Gatling: descrever a jornada com ações encadeadas.

## Fontes
- [Gatling — Simulation](https://docs.gatling.io/concepts/simulation/) — estrutura da simulação, protocolo, cenários e relatório de execução; consultado em 2026-10-03.
- [Gatling — repositório oficial](https://github.com/gatling/gatling) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
