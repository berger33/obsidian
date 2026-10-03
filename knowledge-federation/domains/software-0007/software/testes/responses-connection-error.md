---
id: software.testes.tranche22.001634
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

# responses: URL sem match é ConnectionError

## Em uma frase
A regra de falha do responses é seca: uma tentativa de fetch que não atinge nenhum registro levanta ConnectionError do requests — não há fallback para a rede real durante o mock.

## Por que importa
O teste falha alto e cedo quando o código passa a chamar um endpoint novo não previsto; o mock não deixa request escapulir para produção por acidente.

## Como funciona
O próprio README demonstra o padrão de asserção: with pytest.raises(ConnectionError): requests.get(url_nao_registrada).

## Exemplo
Isso vale para o escopo ativo (decorator ou contexto); fora do escopo do mock, como visto na nota do context manager, a rede real responde.

## Limites e trade-offs
ConnectionError por registro ausente também disfarça bugs de digitação na URL do código — a correção pode vir registrando a URL errada em vez de consertar o cliente.

## Como verificar
Comente um registro de três e confirme que a falha vem no pedido correspondente, não numa asserção posterior.

## Conexões
- [[responses-context-manager]] — Veja também: responses: RequestsMock como contexto.
- [[responses-parameters]] — Veja também: responses: o catálogo de parâmetros do Response.

## Fontes
- [responses — README oficial](https://github.com/getsentry/responses/blob/master/README.rst) — activate, add, atalhos, matchers, registry e passthru; consultado em 2026-10-03.
- [responses — página no PyPI](https://pypi.org/project/responses/) — release canônica e badge do pacote; consultado em 2026-10-03.
