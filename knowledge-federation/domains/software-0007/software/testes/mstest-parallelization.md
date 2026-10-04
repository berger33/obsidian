---
id: software.testes.tranche15.000936
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-configure", "https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSTest: configurar paralelização

## Em uma frase
A paralelização pode ser declarada por atributo de assembly com escopo e número de trabalhadores, ou configurada globalmente em runsettings ou testconfig.

## Por que importa
Executar classes em paralelo reduz tempo, mas casos que compartilham arquivo, banco ou variável estática passam a falhar de forma intermitente e difícil de atribuir.

## Como funciona
Escolha o escopo adequado, limite os trabalhadores ao ambiente e marque com atributo de exclusão os testes que dependem de recurso único.

## Exemplo
`[assembly: Parallelize(Scope = ExecutionScope.MethodLevel, Workers = 4)]` distribui métodos entre quatro trabalhadores, e um método pode ser excluído com `[DoNotParallelize]`.

## Limites e trade-offs
Configuração no projeto e atributo no código podem se sobrepor; a fonte de configuração global tem precedência em relação ao atributo, o que exige escolher um caminho.

## Como verificar
Rode a suíte em paralelo várias vezes e confirme estabilidade; simule um recurso compartilhado para observar a falha e então aplicar a exclusão correta.

## Conexões
- [[mstest-assertions-and-exceptions]] — Veja também: MSTest: afirmar valores e exceções.
- [[mstest-timeout-and-retry]] — Veja também: MSTest: limitar tempo e tratar repetição.

## Fontes
- [MSTest — Configure](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-configure) — runsettings, testconfig.json, paralelização, timeouts e retries; consultado em 2026-10-02.
- [MSTest — Write tests](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-mstest-writing-tests) — atributos de teste, asserções, dados e organização; consultado em 2026-10-02.
