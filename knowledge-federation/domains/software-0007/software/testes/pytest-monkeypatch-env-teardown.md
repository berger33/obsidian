---
id: software.testes.tranche09.000328
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-09.md"
fontes: ["https://docs.pytest.org/en/stable/how-to/monkeypatch.html", "https://docs.pytest.org/en/stable/reference/fixtures.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest: escopar monkeypatch de ambiente e dependências

## Em uma frase
monkeypatch fornece operações controladas para trocar atributos, variáveis de ambiente e caminhos durante teste e desfaz alterações após o escopo.

## Por que importa
pytest monta dependências via fixtures, e escopo, parâmetros e teardown determinam compartilhamento e limpeza entre testes. Patch manual global que não é revertido altera outros casos e torna falhas dependentes da ordem.

## Como funciona
Declare recursos próximos do consumidor, use fixtures temporárias e parametrização explícita e prefira asserts sobre efeitos observáveis do caso. Use fixture monkeypatch ou seu contexto para limitar a alteração à menor parte do teste.

## Exemplo
Um teste define API_BASE_URL com monkeypatch.setenv, chama configuração e confere valor; próximo teste usa o ambiente original.

## Limites e trade-offs
Plugins e versão alteram extensões disponíveis; integração com unittest não oferece todas as conveniências de injeção de fixtures do pytest. Patch pode mudar comportamento de biblioteca e ocultar integração real se aplicado numa fronteira ampla demais.

## Como verificar
Faça assertion durante patch e depois dele, verificando restauração inclusive quando a chamada sob teste lança exceção.

## Conexões
- [[pytest-unittest-fixture-injection-limit]] — Veja também: pytest: entender limites de fixtures em unittest.TestCase.
- [[pytest-xfail-strict-expected-failure]] — Veja também: pytest: ativar strict para xfail não mascarar regressão.

## Fontes
- [pytest — monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html) — patch controlado de atributos, ambiente e caminhos; consultado em 2026-10-02.
- [pytest — Fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html) — resolução de dependências, escopos e teardown de fixtures; consultado em 2026-10-02.
