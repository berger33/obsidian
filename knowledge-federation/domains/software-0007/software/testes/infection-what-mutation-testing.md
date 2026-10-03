---
id: software.testes.tranche23.001740
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://infection.github.io/guide/", "https://infection.github.io/guide/mutators.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mutation testing: matar mutantes em vez de cobrir linhas

## Em uma frase
O guia oficial define mutation testing como técnica baseada em fault com o critério MSI (Mutation Score Indicator): modificar o programa em pequenas formas — cada versão modificada é um mutante — e executar os mutantes contra a suíte de testes para ver se as falhas semeadas são detectadas; mutante com teste vermelho é "killed", mutante com testes verdes é "escaped", e suítes são medidas pela porcentagem de mutantes que matam.

## Por que importa
A diferença para coverage é de epistemologia: cobertura diz que o código foi executado, MSI diz que o comportamento foi observado — um teste que executa uma linha e ignora seu retorno mede 100% de cobertura e 0% de detecção, exatamente o gap que o guia demonstra comparando 47% de MSI com 67% de cobertura.

## Como funciona
A página ancora a teoria no Mutation Testing Repository da UCL (linkado) e define os mutators como operadores bem definidos que "mimic typical programming errors (such as using the wrong operator or variable name) or force the creation of valuable tests (such as dividing each expression by zero)".

## Exemplo
Antes de instalar qualquer ferramenta, rode o playground público oficial (infection-php.dev) num trecho seu e veja a lista de mutantes gerados — é o modo mais barato de decidir se o custo de revisão dos escapes vale para o seu projeto.

## Limites e trade-offs
A técnica é cara por construção: N mutantes vezes M testes cobertos é o espaço de execução; a doc não esconde, e as opções de paralelismo e recorte por git (notas próprias) existem exatamente para pagar esse custo de forma incremental.

## Como verificar
Abra a seção What is Mutation Testing do Introduction oficial e confirme as definições de mutant, killed, escaped, MSI e a frase dos operadores.

## Conexões
- [[infection-what-infection]] — Veja também: Infection: biblioteca PHP de mutação por AST, CLI na raiz do projeto.

## Fontes
- [Infection — Introduction do guia oficial](https://infection.github.io/guide/) — mutation testing, os cinco passos, métricas MSI/MCC e playground; consultado em 2026-10-03.
- [Infection — Mutators](https://infection.github.io/guide/mutators.html) — famílias de mutadores AST e o comando describe; consultado em 2026-10-03.
