---
id: software.testes.tranche10.000369
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-10.md"
fontes: ["https://docs.junit.org/6.1.3/writing-tests/repeated-tests.html", "https://docs.junit.org/6.1.3/writing-tests/annotations.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit: interpretar cada repetição como invocação identificável

## Em uma frase
@RepeatedTest agenda invocações repetidas de um método e pode expor o número atual e total pelo contexto de repetição.

## Por que importa
Testes JUnit expressam contratos executáveis; fontes de argumentos, ciclo de vida e configuração do engine mudam o que cada invocação realmente cobre. Uma falha intermitente sem índice, dado ou condição observável é difícil de reproduzir a partir do relatório.

## Como funciona
Organize cada teste em torno de resultado observável, torne fixtures e extensões explícitas e configure execução paralela ou condicional com escopo deliberado. Nomeie as repetições e use RepetitionInfo quando a lógica do teste realmente precisa do índice ou da contagem.

## Exemplo
Um teste de retry executa cinco tentativas determinísticas com uma semente fixa e informa qual repetição observou a falha.

## Limites e trade-offs
Esta série usa a documentação JUnit 6.1.3; recursos experimentais e compatibilidade dependem da versão, do engine e do build usados. Repetir poucas vezes não demonstra ausência de flakiness; testes aleatórios ainda precisam registrar seed e ambiente.

## Como verificar
Force falha numa repetição conhecida e confirme que o relatório aponta a invocação e preserva dados para reprodução.

## Conexões
- [[junit-condicional-nao-substitui-diagnostico]] — Veja também: JUnit: reservar condições de execução para requisitos reais.

## Fontes
- [JUnit 6.1.3 — Repeated tests](https://docs.junit.org/6.1.3/writing-tests/repeated-tests.html) — repetições, nomes e contexto de cada invocação; consultado em 2026-10-02.
- [JUnit 6.1.3 — Annotations](https://docs.junit.org/6.1.3/writing-tests/annotations.html) — semântica das anotações de teste e ciclo de vida; consultado em 2026-10-02.
