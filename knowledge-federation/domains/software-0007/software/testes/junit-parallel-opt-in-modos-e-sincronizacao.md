---
id: software.testes.tranche10.000364
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
fontes: ["https://docs.junit.org/6.1.3/writing-tests/parallel-execution.html", "https://docs.junit.org/6.1.3/writing-tests/test-instance-lifecycle.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit: configurar paralelismo sem presumir concorrência automática

## Em uma frase
A execução paralela do Jupiter é opt-in; habilitar o parâmetro global não torna todos os nós concorrentes por padrão.

## Por que importa
Testes JUnit expressam contratos executáveis; fontes de argumentos, ciclo de vida e configuração do engine mudam o que cada invocação realmente cobre. Uma suíte pode continuar sequencial ou compartilhar recursos sem proteção apesar de uma configuração parcial de paralelismo.

## Como funciona
Organize cada teste em torno de resultado observável, torne fixtures e extensões explícitas e configure execução paralela ou condicional com escopo deliberado. Habilite a propriedade, defina modos de classe e nó e use sincronização declarativa para recursos que não suportam concorrência.

## Exemplo
As classes rodam concorrentemente, mas métodos que acessam o mesmo diretório de fixture declaram execução serial ou recurso sincronizado.

## Limites e trade-offs
Esta série usa a documentação JUnit 6.1.3; recursos experimentais e compatibilidade dependem da versão, do engine e do build usados. A ordem em que threads iniciam não é garantida, e extensões de terceiros podem impor limites adicionais.

## Como verificar
Rode a suíte repetidamente com a configuração final e inspecione colisões de arquivo, banco, porta e estado estático.

## Conexões
- [[junit-per-class-estado-compartilhado]] — Veja também: JUnit: tratar PER_CLASS como estado compartilhado.
- [[junit-extension-parameter-resolver-explicito]] — Veja também: JUnit: usar ParameterResolver para dependências de teste.

## Fontes
- [JUnit 6.1.3 — Parallel execution](https://docs.junit.org/6.1.3/writing-tests/parallel-execution.html) — ativação, modos de execução e sincronização de testes paralelos; consultado em 2026-10-02.
- [JUnit 6.1.3 — Test instance lifecycle](https://docs.junit.org/6.1.3/writing-tests/test-instance-lifecycle.html) — ciclo de vida PER_METHOD/PER_CLASS e estado compartilhado; consultado em 2026-10-02.
