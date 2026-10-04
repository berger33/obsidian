---
id: software.testes.tranche18.001185
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

# JUnit 5: selecionar testes com etiquetas

## Em uma frase
As etiquetas classificam testes e podem ser usadas para incluir ou excluir grupos na execução, inclusive por configuração de construção.

## Por que importa
Recortes por tipo, risco ou duração permitem rodar subconjuntos adequados a cada momento sem duplicar arquivos.

## Como funciona
Aplique etiquetas por nível de teste ou área, evite sobreposição desnecessária e declare os filtros na configuração da ferramenta de construção.

## Exemplo
Uma execução rápida pode excluir os casos marcados como integração, deixando-os para a etapa completa.

## Limites e trade-offs
Etiquetas inconsistentes deixam testes fora da seleção sem aviso, e a exclusão excessiva esvazia a verificação do pipeline.

## Como verificar
Liste os casos com a etiqueta pretendida e compare com a intenção antes de fixar o filtro na construção.

## Conexões
- [[junit5-parallel-execution]] — Veja também: JUnit 5: habilitar execução paralela.
- [[junit5-migration-and-practices]] — Veja também: JUnit 5: migrar e manter a suíte.

## Fontes
- [JUnit 5 — User Guide](https://junit.org/junit5/docs/current/user-guide/) — anotações, ciclo de vida, asserções, parametrização, extensões e paralelismo; consultado em 2026-10-03.
- [JUnit 5 — repositório oficial](https://github.com/junit-team/junit5) — código-fonte, notas de versão e documentação do projeto; consultado em 2026-10-03.
