---
id: software.testes.tranche12.000576
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
fontes: ["https://testng.org/documentation.html", "https://testng.org/annotations.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TestNG: configurar paralelismo de suite conscientemente

## Em uma frase
A suite TestNG configura se métodos, classes, testes ou instâncias são executados em paralelo e quantas threads podem ser usadas.

## Por que importa
A unidade de paralelismo determina o nível em que a concorrência aparece; escolher apenas um número de threads sem entender o escopo pode misturar fixtures incompatíveis.

## Como funciona
Declare `parallel` e `thread-count` no nível de suite, avalie dependências e fixtures com o modo escolhido e mantenha separado o limite de workers da capacidade dos serviços externos.

## Exemplo
Uma suite pode paralelizar classes independentes para acelerar execução sem executar métodos que compartilham a mesma fixture simultaneamente.

## Limites e trade-offs
Aumentar o número de threads pode saturar banco, browser ou quota de API e produzir falhas que parecem defeitos do produto.

## Como verificar
Execute a suite com um caso que registra sua instância e thread, depois repita com o limite de produção e verifique que o isolamento continua correto.

## Conexões
- [[testng-dataprovider-parallel]] — Veja também: TestNG: DataProvider paralelo sem estado compartilhado.
- [[testng-factory-instancias]] — Veja também: TestNG: criar instâncias de teste com `@Factory`.

## Fontes
- [TestNG — Documentation](https://testng.org/documentation.html) — grupos, XML, execução paralela, listeners e relatórios; consultado em 2026-10-02.
- [TestNG — Annotations](https://testng.org/annotations.html) — ciclo de vida, DataProvider, Factory, Listener e atributos de teste; consultado em 2026-10-02.
