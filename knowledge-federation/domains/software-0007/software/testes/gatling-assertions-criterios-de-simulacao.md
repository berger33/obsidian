---
id: software.testes.tranche11.000534
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://docs.gatling.io/concepts/assertions/", "https://docs.gatling.io/concepts/checks/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: expressar pass fail com assertions de estatísticas

## Em uma frase
Assertions na Simulation definem critérios sobre estatísticas globais ou escopos como requests/grupos.

## Por que importa
Gatling executa workflows de virtual users, aplica perfis de injeção e mede estatísticas; dados, checks e modelo de chegada determinam se o benchmark representa o workload. Gerar relatório sem threshold pode deixar run com alta taxa de erro ser interpretada como aprovada.

## Como funciona
Modele ações em ordem, armazene atributos por usuário na Session, valide respostas antes de reutilizar extrações e defina assertions de negócio sobre métricas globais ou grupos. Defina limites de erro e latência que correspondam ao SLO e a população executada, com escopo nomeado.

## Exemplo
Teste falha se percentagem global de requests bem-sucedidas cair abaixo do critério definido.

## Limites e trade-offs
Uma simulation aprovada apenas satisfaz as assertions escolhidas no perfil de injeção executado. Sessões e feeders não criam semântica de negócio, e resultados dependem da capacidade do gerador e do alvo. Threshold depende do workload e ambiente; usar percentil médio ou valor sem baseline não cria critério confiável.

## Como verificar
Injete uma falha controlada e confirme que assertion muda o resultado final da execução.

## Conexões
- [[gatling-check-saveas-apos-sucesso]] — Veja também: Gatling: validar resposta antes de guardar valor com saveAs.
- [[gatling-open-closed-injection-model]] — Veja também: Gatling: escolher open ou closed conforme hipótese de carga.

## Fontes
- [Gatling — Assertions](https://docs.gatling.io/concepts/assertions/) — critérios sobre estatísticas da simulação e escopos; consultado em 2026-10-02.
- [Gatling — Checks](https://docs.gatling.io/concepts/checks/) — validação de resposta e extração saveAs condicionada ao sucesso; consultado em 2026-10-02.
