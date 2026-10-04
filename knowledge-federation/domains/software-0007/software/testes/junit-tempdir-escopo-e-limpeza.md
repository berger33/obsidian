---
id: software.testes.tranche10.000366
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
fontes: ["https://docs.junit.org/6.1.3/writing-tests/built-in-extensions.html", "https://docs.junit.org/6.1.3/extensions/overview.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit: usar @TempDir para arquivos temporários isolados

## Em uma frase
A extensão TempDir fornece diretório temporário a um campo ou parâmetro de teste.

## Por que importa
Testes JUnit expressam contratos executáveis; fontes de argumentos, ciclo de vida e configuração do engine mudam o que cada invocação realmente cobre. Diretórios fixos no workspace podem colidir em execuções paralelas e deixar arquivos de uma execução contaminarem outra.

## Como funciona
Organize cada teste em torno de resultado observável, torne fixtures e extensões explícitas e configure execução paralela ou condicional com escopo deliberado. Injete Path com @TempDir e limite os arquivos criados à invocação ou ao escopo explicitamente escolhido.

## Exemplo
O teste escreve uma configuração temporária no diretório injetado, executa o parser e valida a saída sem depender do caminho absoluto.

## Limites e trade-offs
Esta série usa a documentação JUnit 6.1.3; recursos experimentais e compatibilidade dependem da versão, do engine e do build usados. Uma TempDirFactory customizada tem regras próprias de criação e fechamento; não assuma frequência de instanciação além da documentação.

## Como verificar
Rode o teste em paralelo e verifique que a limpeza e os recursos associados ocorrem no ciclo esperado.

## Conexões
- [[junit-extension-parameter-resolver-explicito]] — Veja também: JUnit: usar ParameterResolver para dependências de teste.
- [[junit-tags-filtrar-testes-por-categoria]] — Veja também: JUnit: selecionar testes por tags sem confundir com suites.

## Fontes
- [JUnit 6.1.3 — Built-in extensions](https://docs.junit.org/6.1.3/writing-tests/built-in-extensions.html) — uso e configuração da extensão @TempDir; consultado em 2026-10-02.
- [JUnit 6.1.3 — Extension model](https://docs.junit.org/6.1.3/extensions/overview.html) — pontos de extensão e integração com o ciclo de execução; consultado em 2026-10-02.
