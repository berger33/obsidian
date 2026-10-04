---
id: software.testes.tranche12.000590
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
fontes: ["https://pitest.org/quickstart/basic_concepts/", "https://pitest.org/quickstart/mutators/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PIT: mutação de bytecode para avaliar assertions

## Em uma frase
PIT aplica mutadores ao bytecode compilado para criar versões pequenas do programa que representam falhas hipotéticas.

## Por que importa
Se uma assertion detecta uma mudança relevante, ela deve falhar contra o mutante; assim, o processo avalia se os testes percebem certas alterações, não apenas se executam linhas.

## Como funciona
Escolha classes-alvo, gere mutações com os operadores configurados e permita que PIT selecione testes que exercitam o código modificado antes de avaliar o resultado.

## Exemplo
Um mutador pode inverter uma condição de fronteira e revelar se a suíte distingue `<` de `<=` no limite de uma regra tarifária.

## Limites e trade-offs
Mutantes são aproximações de defeitos, não catálogo completo de bugs possíveis; compilar o projeto sem informações de depuração necessárias também pode impedir análise correta.

## Como verificar
Inspecione um mutante sobrevivente no relatório, localize a alteração de bytecode representada e confirme que existe uma expectativa que deveria falhar sob aquela mudança.

## Conexões
- [[pit-cobertura-selecao-testes]] — Veja também: PIT: usar cobertura para escolher testes por mutante.

## Fontes
- [PIT — Basic Concepts](https://pitest.org/quickstart/basic_concepts/) — mutantes de bytecode, seleção de testes por cobertura e estados dos resultados; consultado em 2026-10-02.
- [PIT — Mutation Operators](https://pitest.org/quickstart/mutators/) — mutadores disponíveis e grupos DEFAULTS, STRONGER e ALL; consultado em 2026-10-02.
