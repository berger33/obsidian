---
id: software.testes.tranche11.000459
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/RestAssured.html", "https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/specification/RequestSpecification.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# REST Assured: evitar vazamento de configuração estática entre testes

## Em uma frase
REST Assured expõe defaults estáticos como base URI, filtros e specifications que influenciam requests posteriores.

## Por que importa
Uma alteração de host ou parser em um teste pode contaminar outros casos, sobretudo quando a suíte roda em paralelo.

## Como funciona
Prefira configuração local por request e restaure explicitamente qualquer default global alterado pelo teste.

## Exemplo
Um teste aponta baseUri para um mock local e limpa a configuração no teardown; outro confirma que continua usando seu próprio destino.

## Limites e trade-offs
Reset global durante execução paralela também pode afetar testes em andamento; limpeza não substitui isolamento concorrente.

## Como verificar
Rode a classe em ordem aleatória e com paralelismo habilitado e procure requests enviados ao host de outro cenário.

## Conexões
- [[restassured-auth-por-caso-sem-credencial-em-log]] — Veja também: REST Assured: configurar autenticação por teste e proteger credenciais.

## Fontes
- [REST Assured — RestAssured API](https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/RestAssured.html) — configuração de URI, especificações, parsers, filtros e valores estáticos padrão; consultado em 2026-10-02.
- [REST Assured — RequestSpecification API](https://javadoc.io/doc/io.rest-assured/rest-assured/latest/io/restassured/specification/RequestSpecification.html) — configuração e composição de requests, parâmetros, corpos, headers, filtros e especificações reutilizáveis; consultado em 2026-10-02.
