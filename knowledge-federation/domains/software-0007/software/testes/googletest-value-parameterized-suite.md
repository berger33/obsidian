---
id: software.testes.tranche13.000733
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://google.github.io/googletest/advanced.html", "https://google.github.io/googletest/reference/testing.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# GoogleTest: instanciar teste para conjunto de valores

## Em uma frase
Teste value-parameterized reutiliza um padrão de fixture e executa para valores fornecidos por gerador.

## Por que importa
Matriz explícita verifica entradas semelhantes sem copiar função de teste e expõe instância específica que falhou.

## Como funciona
Derive de `TestWithParam<T>`, leia `GetParam()` no corpo, defina `TEST_P` e instancie suite em escopo global com gerador e prefixo único.

## Exemplo
Uma rotina de parser pode instanciar formatos válidos e inválidos e produzir resultado separado para cada `Values(...)`.

## Limites e trade-offs
Geradores grandes aumentam tempo e duplicar valores semanticamente equivalentes gera cobertura aparente sem novos limites.

## Como verificar
Inspecione nomes das instâncias e filtre um parâmetro específico para reproduzir o caso sem rodar a matriz inteira.

## Conexões
- [[googletest-fatal-vs-nonfatal]] — Veja também: GoogleTest: escolher ASSERT ou EXPECT pelo fluxo.
- [[googletest-typed-test-known-types]] — Veja também: GoogleTest: compartilhar testes por tipos conhecidos.

## Fontes
- [GoogleTest — Advanced Topics](https://google.github.io/googletest/advanced.html) — typed/value-parameterized tests and advanced assertions; consultado em 2026-10-02.
- [GoogleTest — Testing Reference](https://google.github.io/googletest/reference/testing.html) — test macros, fixtures and parameterized-test APIs; consultado em 2026-10-02.
