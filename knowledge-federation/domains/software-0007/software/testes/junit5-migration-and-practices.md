---
id: software.testes.tranche18.001186
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://junit.org/junit5/docs/current/user-guide/", "https://github.com/junit-team/junit5"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JUnit 5: migrar e manter a suíte

## Em uma frase
A versão atual convive com a anterior por meio de mecanismo de compatibilidade, permitindo migração gradual de classes e asserções.

## Por que importa
Migrar de uma vez em suítes grandes é arriscado, e a compatibilidade possibilita avançar por partes preservando o retorno da esteira.

## Como funciona
Migre por pacote, mantendo a execução dos dois modelos, e converta asserções e regras conforme as substituições recomendadas.

## Exemplo
Um módulo pode ser migrado enquanto outro continua no modelo antigo, com a suíte completa permanecendo executável.

## Limites e trade-offs
Misturar os dois modelos no mesmo arquivo dificulta a leitura, e extensões antigas não têm equivalente direto na versão nova.

## Como verificar
Execute a suíte após migrar um pacote e confirme que o número de casos e o resultado permanecem iguais.

## Conexões
- [[junit5-tagging-and-filtering]] — Veja também: JUnit 5: selecionar testes com etiquetas.

## Fontes
- [JUnit 5 — User Guide](https://junit.org/junit5/docs/current/user-guide/) — anotações, ciclo de vida, asserções, parametrização, extensões e paralelismo; consultado em 2026-10-03.
- [JUnit 5 — repositório oficial](https://github.com/junit-team/junit5) — código-fonte, notas de versão e documentação do projeto; consultado em 2026-10-03.
