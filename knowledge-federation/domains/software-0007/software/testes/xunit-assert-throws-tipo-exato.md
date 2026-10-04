---
id: software.testes.tranche11.000509
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
fontes: ["https://api.xunit.net/v3/3.0.0/Xunit.Assert.html", "https://xunit.net/docs/getting-started/v3/getting-started"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# xUnit: afirmar exceção esperada no ponto da chamada

## Em uma frase
Assert.Throws e variantes assíncronas capturam exceção da operação e permitem verificar tipo e conteúdo da falha.

## Por que importa
Try/catch amplo ao redor de várias etapas pode aceitar exceção de setup ou de código que não era alvo do teste.

## Como funciona
Passe apenas a ação sob teste à assertion de exceção e verifique mensagem/código somente quando fizerem parte do contrato.

## Exemplo
Uma chamada de parser inválida deve lançar FormatException; erro de preparação da entrada não pode satisfazer assertion por acidente.

## Limites e trade-offs
Algumas APIs de assertion exigem tipo exato, enquanto outras aceitam subtipos; consulte a variante usada e versão.

## Como verificar
Teste tipo esperado, subtipo não permitido e ausência de exceção e confira em qual linha a falha é apontada.

## Conexões
- [[xunit-outputhelper-saida-associada]] — Veja também: xUnit: associar diagnóstico ao teste com ITestOutputHelper.

## Fontes
- [xUnit.net v3 — Assert API (v3.0.0)](https://api.xunit.net/v3/3.0.0/Xunit.Assert.html) — referência da classe Assert, incluindo Throws, ThrowsAsync e outras assertions síncronas/assíncronas; consultado em 2026-10-02.
- [xUnit.net v3 — Getting Started](https://xunit.net/docs/getting-started/v3/getting-started) — Fact, Theory, dados inline, descoberta e execução de casos; consultado em 2026-10-02.
