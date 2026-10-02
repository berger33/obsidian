---
id: software.testes.tranche09.000327
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
fontes: ["https://docs.pytest.org/en/stable/how-to/unittest.html", "https://docs.pytest.org/en/stable/reference/fixtures.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest: entender limites de fixtures em unittest.TestCase

## Em uma frase
pytest pode coletar subclasses unittest.TestCase e aplicar algumas marcas/fixtures autouse, mas não injeta fixtures normais como parâmetros de métodos TestCase.

## Por que importa
pytest monta dependências via fixtures, e escopo, parâmetros e teardown determinam compartilhamento e limpeza entre testes. Migrar parcialmente uma classe para sintaxe pytest pode resultar em argumentos não suportados e parametrização não disponível.

## Como funciona
Declare recursos próximos do consumidor, use fixtures temporárias e parametrização explícita e prefira asserts sobre efeitos observáveis do caso. Mantenha setup unittest convencional ou migre testes para funções/classes nativas pytest antes de exigir fixture injection.

## Exemplo
Método TestCase usa setUp para criar cliente; teste em função pytest recebe fixture client como argumento.

## Limites e trade-offs
Plugins e versão alteram extensões disponíveis; integração com unittest não oferece todas as conveniências de injeção de fixtures do pytest. Marks e autouse têm suporte específico; não presuma igualdade de recursos com funções pytest comuns.

## Como verificar
Rode coleta, confira assinatura e confirme no exemplo mínimo qual setup foi chamado e qual parâmetro é aceito.

## Conexões
- [[pytest-autouse-fixture-hidden-side-effects]] — Veja também: pytest: limitar efeitos ocultos de fixtures autouse.
- [[pytest-monkeypatch-env-teardown]] — Veja também: pytest: escopar monkeypatch de ambiente e dependências.

## Fontes
- [pytest — unittest integration](https://docs.pytest.org/en/stable/how-to/unittest.html) — compatibilidade e limitações de fixtures com unittest.TestCase; consultado em 2026-10-02.
- [pytest — Fixtures reference](https://docs.pytest.org/en/stable/reference/fixtures.html) — resolução de dependências, escopos e teardown de fixtures; consultado em 2026-10-02.
