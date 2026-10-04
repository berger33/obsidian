---
id: software.testes.mcdc.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md"
fontes: ["https://shemesh.larc.nasa.gov/fm/papers/Hayhurst-2001-tm210876-MCDC.pdf", "https://clang.llvm.org/docs/SourceBasedCodeCoverage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [MC/DC, Modified Condition/Decision Coverage, Cobertura modificada de condição/decisão]
lote: software-testes-2000-0001
---

# MC/DC: efeito independente de cada condição

## Em uma frase
Modified Condition/Decision Coverage exige demonstrar que cada condição de uma decisão pode alterar seu resultado independentemente das demais condições.

## Por que importa
Cobertura de statements ou branches pode não mostrar se cada condição de uma expressão booleana influenciou o resultado. MC/DC é usado em verificação de software crítico, onde decisões complexas e evidências rastreáveis importam. É uma métrica estrutural de adequação, não uma técnica de geração de testes por si só.

## Como funciona
O tutorial da NASA descreve MC/DC como critério que cobre pontos de entrada/saída, resultados de decisões, resultados de condições e o efeito independente de cada condição sobre o resultado da decisão. Para demonstrar independência, escolhem-se casos em que a condição analisada muda, os demais valores relevantes permanecem fixos e a decisão também muda. Clang oferece instrumentação específica com `-fcoverage-mcdc` além das flags de cobertura source-based.

## Exemplo
Para `A || B`, uma demonstração única-causa para `A` compara `(A=True, B=False)` com `(A=False, B=False)`: a decisão muda quando só A muda. Para B, compara `(A=False, B=False)` com `(A=False, B=True)`. A seleção real deve respeitar a semântica da linguagem, short-circuiting e a variante de MC/DC exigida pelo padrão/toolchain.

## Limites e trade-offs
Critérios e convenções — inclusive MC/DC masking versus unique-cause — podem variar por padrão e ferramenta. Curto-circuito e condições dependentes podem limitar pares válidos. MC/DC não prova corretude funcional nem substitui requisitos, testes de integração ou análise de segurança. Confirme rigorosamente a interpretação aplicável à norma e à toolchain do projeto.

## Como verificar
Registre decisões, condições atômicas, pares de independência e critérios usados. Execute a ferramenta com instrumentação adequada, inspecione decisões não cobertas e associe testes a requisitos. Quando um par não puder ser construído por dependência lógica, documente a justificativa e a interpretação aceita pela autoridade de certificação ou pelo padrão do projeto.

## Conexões
- [[cobertura-branches-statement-interpretacao]] — MC/DC é mais específico que statement/branch coverage.
- [[particionamento-equivalencia-valores-fronteira]] — reduz valores de entrada, mas não demonstra independência de condições booleanas.
- [[mutation-testing-eficacia-testes]] — pode investigar se alterações em condições lógicas são detectadas pela suíte.

## Fontes
- [NASA — A Practical Tutorial on Modified Condition/Decision Coverage](https://shemesh.larc.nasa.gov/fm/papers/Hayhurst-2001-tm210876-MCDC.pdf) — definição, relação com outros critérios e exemplos; acesso em 2026-10-01.
- [Clang — Source-based Code Coverage](https://clang.llvm.org/docs/SourceBasedCodeCoverage.html) — uso da flag `-fcoverage-mcdc`; acesso em 2026-10-01.
