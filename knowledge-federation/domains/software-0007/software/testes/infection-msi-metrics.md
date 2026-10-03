---
id: software.testes.tranche23.001742
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
fontes: ["https://infection.github.io/guide/", "https://infection.github.io/guide/command-line-options.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# As três métricas: MSI, Mutation Code Coverage e Covered Code MSI

## Em uma frase
O Introduction oficial descreve o bloco Metrics com as fórmulas: MSI é TotalDefeatedMutants (KilledCount + TimedOutCount + ErrorCount) dividido pelo TotalMutantsCount — 47% no exemplo — "the primary Mutation Testing metric"; Mutation Code Coverage é a fatia de mutantes coberta por algum teste (TotalMutants - NotCoveredByTests)/TotalMutants, 67% no exemplo, que "on average should be within the same ballpark as your normal code coverage"; e Covered Code MSI restringe o numerador ao denominador coberto — 70% no exemplo, "ignoring not tested code", mostrando "how effective the tests really are".

## Por que importa
A leitura conjunta é onde a ferramenta ensina algo que cobertura sozinha não mostra: a página nota que um gap de 18 pontos entre o 47% de MSI e a cobertura reportada significa que "these unit tests are far less than effective" do que a cobertura sugere — e que interpretado sem contexto, o Covered MSI alto pode mascarar um diretório inteiro fora do teste.

## Como funciona
O detalhe que transforma o resultado em ação vem na mesma seção: os logs listam todas as mutações não detectadas como diffs contra o código original, e examiná-los é o método prescrito para descobrir que mutações específicas ficaram vivas.

## Exemplo
Publique os três números no seu README e versione o log de escapes; depois pegue o diff do primeiro mutante escapado e escreva o teste que o mata — o ciclo completo que a página prescreve, em uma sessão.

## Limites e trade-offs
As fórmulas tratam erro e timeout como derrotas do mutante (contam em TotalDefeated), o que pode inflar um MSI medido sobre ambiente instável — a página define o cálculo, não a validade do resultado em CI ruidoso; valide timeouts antes de cantar taxa de morte.

## Como verificar
Abra a seção Metrics do Introduction oficial e confirme as três fórmulas com os números do exemplo (47/67/70) e a frase sobre interpretar com contexto.

## Conexões
- [[infection-what-infection]] — Veja também: Infection: biblioteca PHP de mutação por AST, CLI na raiz do projeto.
- [[infection-install-phar]] — Veja também: Instalar o phar assinado: GPG, phive, composer e brew.

## Fontes
- [Infection — Introduction do guia oficial](https://infection.github.io/guide/) — mutation testing, os cinco passos, métricas MSI/MCC e playground; consultado em 2026-10-03.
- [Infection — Command line options](https://infection.github.io/guide/command-line-options.html) — threads, test-framework, coverage, git-diff e loggers; consultado em 2026-10-03.
