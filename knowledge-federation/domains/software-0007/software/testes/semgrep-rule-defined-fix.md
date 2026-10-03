---
id: software.testes.tranche18.001232
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
fontes: ["https://semgrep.dev/docs/writing-rules/rule-defined-fix", "https://semgrep.dev/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Semgrep: sugerir correção automática

## Em uma frase
Regras podem declarar a substituição apropriada, e a ferramenta aplica a correção diretamente ou mostra a prévia para revisão.

## Por que importa
Sugestões determinísticas reduzem o esforço de correção e tornam a revisão da regra parte do fluxo de trabalho normal.

## Como funciona
Declare a correção na regra, valide com prévia antes de aplicar e revise o resultado como qualquer alteração de código.

## Exemplo
Uma regra pode substituir chamada depreciada pela equivalente atual mantendo os mesmos argumentos.

## Limites e trade-offs
Correções automáticas aplicadas sem revisão podem alterar semântica em casos de borda, e a substituição precisa cobrir apenas os casos seguros.

## Como verificar
Execute a prévia em um repositório de teste e confirme que a correção proposta compila e mantém o comportamento.

## Conexões
- [[semgrep-taint-mode]] — Veja também: Semgrep: analisar fluxo com modo de propagação.
- [[semgrep-ci-integration]] — Veja também: Semgrep: integrar a análise ao pipeline.

## Fontes
- [Semgrep — Rule-defined fix](https://semgrep.dev/docs/writing-rules/rule-defined-fix) — correção definida pela regra, prévia e aplicação automática; consultado em 2026-10-03.
- [Semgrep — Documentation](https://semgrep.dev/docs/) — instalação, execução, integração contínua, supressões e severidade; consultado em 2026-10-03.
