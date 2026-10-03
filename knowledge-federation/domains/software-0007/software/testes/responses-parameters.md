---
id: software.testes.tranche22.001635
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://github.com/getsentry/responses/blob/master/README.rst", "https://pypi.org/project/responses/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# responses: o catálogo de parâmetros do Response

## Em uma frase
Os atributos documentados do mock de Response cobrem o essencial do contrato: method, url (string ou expressão regular compilada), body (str, BufferedReader ou Exception), json (configura o Content-Type sozinho), status, content_type (default text/plain), headers e auto_calculate_content_length (desligado por padrão).

## Por que importa
Saber que url aceita regex compilada muda a arquitetura da suíte: um registro cobre N variações de path sem um mock por id.

## Como funciona
Exemplo de exceção como corpo: responses.get(url, body=Exception("...")) dentro de um pytest.raises(Exception) — o README trata "Exception as Response body" como seção própria para simular quebra do servidor.

## Exemplo
A heurística de query string é registrada como parâmetro DEPRECATED (match_querystring): hoje o match de query se expressa por matchers, não por flag.

## Limites e trade-offs
json= escolhe content-type por você; misturar body= manual com json= no mesmo registro gera estado ambíguo que a leitura posterior não desvenda.

## Como verificar
Registre um único Response com url=re.compile(...) e prove que dois endpoints com paths diferentes caem no mesmo mock.

## Conexões
- [[responses-connection-error]] — Veja também: responses: URL sem match é ConnectionError.
- [[responses-matchers]] — Veja também: responses: match() com matchers combináveis.

## Fontes
- [responses — README oficial](https://github.com/getsentry/responses/blob/master/README.rst) — activate, add, atalhos, matchers, registry e passthru; consultado em 2026-10-03.
- [responses — página no PyPI](https://pypi.org/project/responses/) — release canônica e badge do pacote; consultado em 2026-10-03.
