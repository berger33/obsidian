---
id: software.testes.tranche12.000575
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://testng.org/annotations.html", "https://testng.org/parameters.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TestNG: DataProvider paralelo sem estado compartilhado

## Em uma frase
Um `DataProvider` pode pedir ao TestNG que execute em paralelo os testes gerados por suas linhas de dados.

## Por que importa
Paralelizar casos reduz tempo, mas transforma variáveis mutáveis, contas e recursos externos compartilhados em possíveis fontes de interferência.

## Como funciona
Ative `parallel=true` somente quando cada invocação puder trabalhar com entradas e recursos independentes; caso contrário, mantenha execução sequencial ou atribua isolamento explícito.

## Exemplo
Uma validação de formatos pode rodar cada entrada em paralelo quando o método usa apenas seus argumentos e não altera um arquivo global de resultados.

## Limites e trade-offs
Uma mesma instância de fixture ou serviço remoto pode receber alterações concorrentes mesmo que cada linha do provider seja diferente.

## Como verificar
Compare a suíte sequencial e paralela com repetição suficiente, use identificadores exclusivos por caso e procure colisões ou resultados dependentes da ordem.

## Conexões
- [[testng-lifecycle-heranca-hooks]] — Veja também: TestNG: ordem de hooks de configuração herdados.
- [[testng-suite-parallel-threadcount]] — Veja também: TestNG: configurar paralelismo de suite conscientemente.

## Fontes
- [TestNG — Annotations](https://testng.org/annotations.html) — ciclo de vida, DataProvider, Factory, Listener e atributos de teste; consultado em 2026-10-02.
- [TestNG — Parameters](https://testng.org/parameters.html) — parâmetros XML, opções, hierarquia de escopo e data providers; consultado em 2026-10-02.
