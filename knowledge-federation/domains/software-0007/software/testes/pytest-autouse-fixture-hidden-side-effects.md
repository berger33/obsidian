---
id: software.testes.tranche09.000326
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
fontes: ["https://docs.pytest.org/en/stable/reference/fixtures.html", "https://docs.pytest.org/en/stable/how-to/monkeypatch.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest: limitar efeitos ocultos de fixtures autouse

## Em uma frase
Fixture autouse é aplicada automaticamente dentro do escopo definido e pode preparar ou alterar estado sem aparecer nos argumentos do teste.

## Por que importa
pytest monta dependências via fixtures, e escopo, parâmetros e teardown determinam compartilhamento e limpeza entre testes. Autouse ampla esconde dependências, aumenta custo e pode mudar comportamento de testes não relacionados.

## Como funciona
Declare recursos próximos do consumidor, use fixtures temporárias e parametrização explícita e prefira asserts sobre efeitos observáveis do caso. Reserve-a para invariantes transversais pequenas e use dependência explícita para recursos caros ou mutáveis.

## Exemplo
Fixture autouse zera variável de ambiente global do pacote, enquanto servidor e banco aparecem nos parâmetros dos testes que os usam.

## Limites e trade-offs
Plugins e versão alteram extensões disponíveis; integração com unittest não oferece todas as conveniências de injeção de fixtures do pytest. Autouse não significa escopo global automático; seu alcance continua condicionado ao arquivo, classe ou conftest e ao scope.

## Como verificar
Inspecione setup hooks e execute um teste isolado para ver quais fixtures são ativadas sem solicitação explícita.

## Conexões
- [[pytest-indirect-param-fixture-setup]] — Veja também: pytest: usar indirect parametrization para setup configurável.
- [[pytest-unittest-fixture-injection-limit]] — Veja também: pytest: entender limites de fixtures em unittest.TestCase.

## Fontes
- [pytest — Fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html) — resolução de dependências, escopos e teardown de fixtures; consultado em 2026-10-02.
- [pytest — monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html) — patch controlado de atributos, ambiente e caminhos; consultado em 2026-10-02.
