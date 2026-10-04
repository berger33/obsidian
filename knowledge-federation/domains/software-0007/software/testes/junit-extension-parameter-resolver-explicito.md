---
id: software.testes.tranche10.000365
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
fontes: ["https://docs.junit.org/6.1.3/extensions/overview.html", "https://docs.junit.org/6.1.3/writing-tests/intro.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit: usar ParameterResolver para dependências de teste

## Em uma frase
Extensões Jupiter podem resolver parâmetros de métodos e construtores quando um ParameterResolver registrado declara suporte.

## Por que importa
Testes JUnit expressam contratos executáveis; fontes de argumentos, ciclo de vida e configuração do engine mudam o que cada invocação realmente cobre. Injeção implícita sem extensão visível torna difícil saber de onde vem uma dependência de teste.

## Como funciona
Organize cada teste em torno de resultado observável, torne fixtures e extensões explícitas e configure execução paralela ou condicional com escopo deliberado. Registre a extensão na classe ou instância e implemente critérios de supportsParameter estreitos antes de fornecer o valor.

## Exemplo
Um resolver fornece um cliente fake apenas para parâmetros do tipo e anotação definidos no contexto do teste.

## Limites e trade-offs
Esta série usa a documentação JUnit 6.1.3; recursos experimentais e compatibilidade dependem da versão, do engine e do build usados. Dois resolvers que reivindicam o mesmo parâmetro podem conflitar; lifecycle e ordem de extensões afetam setup e cleanup.

## Como verificar
Remova a extensão e confirme uma falha clara, depois teste parâmetro suportado e não suportado em classes separadas.

## Conexões
- [[junit-parallel-opt-in-modos-e-sincronizacao]] — Veja também: JUnit: configurar paralelismo sem presumir concorrência automática.
- [[junit-tempdir-escopo-e-limpeza]] — Veja também: JUnit: usar @TempDir para arquivos temporários isolados.

## Fontes
- [JUnit 6.1.3 — Extension model](https://docs.junit.org/6.1.3/extensions/overview.html) — pontos de extensão e integração com o ciclo de execução; consultado em 2026-10-02.
- [JUnit 6.1.3 — Writing tests](https://docs.junit.org/6.1.3/writing-tests/intro.html) — modelo de escrita e execução de testes Jupiter; consultado em 2026-10-02.
