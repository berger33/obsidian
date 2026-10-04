---
id: software.testes.tranche10.000367
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
fontes: ["https://docs.junit.org/6.1.3/running-tests/tags.html", "https://docs.junit.org/6.1.3/writing-tests/annotations.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit: selecionar testes por tags sem confundir com suites

## Em uma frase
Tags identificam testes e podem ser usadas pelo runner para incluir ou excluir grupos durante uma execução.

## Por que importa
Testes JUnit expressam contratos executáveis; fontes de argumentos, ciclo de vida e configuração do engine mudam o que cada invocação realmente cobre. Semântica de seleção mal declarada pode excluir validações importantes da CI sem tornar isso evidente no código da suíte.

## Como funciona
Organize cada teste em torno de resultado observável, torne fixtures e extensões explícitas e configure execução paralela ou condicional com escopo deliberado. Aplique tags com vocabulário pequeno e consistente e revise os filtros de include/exclude no build ou launcher.

## Exemplo
Uma execução rápida seleciona unit; um job separado escolhe integration e confirma no relatório quantos testes foram descobertos.

## Limites e trade-offs
Esta série usa a documentação JUnit 6.1.3; recursos experimentais e compatibilidade dependem da versão, do engine e do build usados. Tag não altera o comportamento do teste nem garante que a configuração da CI realmente inclua todos os grupos.

## Como verificar
Compare os testes descobertos por cada job com a política de execução esperada e teste combinações de filtros.

## Conexões
- [[junit-tempdir-escopo-e-limpeza]] — Veja também: JUnit: usar @TempDir para arquivos temporários isolados.
- [[junit-condicional-nao-substitui-diagnostico]] — Veja também: JUnit: reservar condições de execução para requisitos reais.

## Fontes
- [JUnit 6.1.3 — Filtering by tags](https://docs.junit.org/6.1.3/running-tests/tags.html) — marcação e seleção de testes por tags; consultado em 2026-10-02.
- [JUnit 6.1.3 — Annotations](https://docs.junit.org/6.1.3/writing-tests/annotations.html) — semântica das anotações de teste e ciclo de vida; consultado em 2026-10-02.
