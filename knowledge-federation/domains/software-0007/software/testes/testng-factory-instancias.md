---
id: software.testes.tranche12.000577
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
fontes: ["https://testng.org/annotations.html", "https://testng.org/documentation.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TestNG: criar instâncias de teste com `@Factory`

## Em uma frase
`@Factory` retorna objetos que o TestNG trata como instâncias de classes de teste, enquanto `@DataProvider` fornece argumentos para métodos.

## Por que importa
Separar criação de fixtures da variação de argumentos esclarece quando cada cenário precisa de uma instância configurada de forma diferente.

## Como funciona
Use uma factory para construir array de objetos de teste com parâmetros de construtor e reserve o provider para alimentar invocações de um método já descoberto.

## Exemplo
Uma factory pode criar um teste de repositório por mecanismo de persistência, passando cada implementação no construtor da classe de teste.

## Limites e trade-offs
Criar muitos objetos numa factory pode multiplicar estado que parece comum à classe; combine isso com paralelismo apenas se as instâncias forem realmente independentes.

## Como verificar
Confira quantas instâncias foram descobertas e identifique no relatório qual configuração de construtor originou cada resultado.

## Conexões
- [[testng-suite-parallel-threadcount]] — Veja também: TestNG: configurar paralelismo de suite conscientemente.
- [[testng-listener-eventos-relatorio]] — Veja também: TestNG: usar listeners para observar execução.

## Fontes
- [TestNG — Annotations](https://testng.org/annotations.html) — ciclo de vida, DataProvider, Factory, Listener e atributos de teste; consultado em 2026-10-02.
- [TestNG — Documentation](https://testng.org/documentation.html) — grupos, XML, execução paralela, listeners e relatórios; consultado em 2026-10-02.
