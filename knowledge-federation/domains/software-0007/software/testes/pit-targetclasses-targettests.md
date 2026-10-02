---
id: software.testes.tranche12.000594
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
fontes: ["https://pitest.org/quickstart/commandline/", "https://pitest.org/quickstart/maven/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PIT: delimitar classes e testes de mutation testing

## Em uma frase
`targetClasses` e `targetTests` definem, respectivamente, quais classes podem receber mutações e quais testes podem participar da análise.

## Por que importa
Escopo explícito impede que a primeira execução mutacione um sistema inteiro quando a pergunta real trata de um pacote pequeno.

## Como funciona
Use padrões de pacote que correspondam a bytecode compilado, mantenha filtros de teste amplos o suficiente para alcançar esses alvos e revise a saída quando nenhum candidato for encontrado.

## Exemplo
Uma análise local pode limitar `targetClasses` a um pacote de cálculo e usar os testes de domínio que exercitam as regras desse pacote.

## Limites e trade-offs
Filtro estreito demais pode produzir relatório vazio ou deixar código relevante fora; padrão amplo pode alongar a análise além do orçamento disponível.

## Como verificar
Confira o conjunto efetivo de classes mutadas e testes descobertos no relatório antes de confiar na contagem de mutantes.

## Conexões
- [[pit-mutator-groups-esforco]] — Veja também: PIT: selecionar grupos de mutadores conforme a pergunta.
- [[pit-timeouts-mutantes-hang]] — Veja também: PIT: distinguir timeout de mutante sobrevivente.

## Fontes
- [PIT — Command Line Quick Start](https://pitest.org/quickstart/commandline/) — filtros de target classes/tests, execução e parâmetros de linha de comando; consultado em 2026-10-02.
- [PIT — Maven Quick Start](https://pitest.org/quickstart/maven/) — goal mutationCoverage, filtros e modo dry run documentado desde 1.17.3; consultado em 2026-10-02.
