---
id: software.seguranca.tranche18.001703
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-18.md"
fontes: ["https://semgrep.dev/docs/running-rules", "https://semgrep.dev/docs/semgrep-ci/overview/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Semgrep: Combinar padrões com contexto

## Em uma frase
**Semgrep — Combinar padrões com contexto:** Combinadores de padrões permitem exigir que uma expressão apareça em um contexto maior ou excluir contextos conhecidos.

## Por que importa
O recorte de **combinar padrões com contexto** ajuda a localizar padrões de risco reproduzíveis e transformar verificações de segurança em regras versionadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **combinar padrões com contexto**, o scanner seleciona linguagens e regras, percorre arquivos elegíveis e reporta os trechos que correspondem às condições declaradas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Limite um finding a uma chamada dentro do handler HTTP, em vez de reportar a mesma função em testes. Teste em staging autorizado.

## Limites e trade-offs
Contexto incompleto pode ocultar caminhos alternativos; exceções sintáticas devem ter justificativa revisada. Exceções exigem responsável e prazo.

## Como verificar
Inclua fixtures com a chamada dentro e fora do contexto para demonstrar a fronteira da regra. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[semgrep-analise-de-taint-com-fontes-e-sinks]] — Complementa o tópico com semgrep: análise de taint com fontes e sinks.

## Fontes
- [Semgrep — Run rules](https://semgrep.dev/docs/running-rules) — documentação oficial de regras YAML, regras locais, regrasets e execução; consultado em 2026-10-04.
- [Semgrep — CI overview](https://semgrep.dev/docs/semgrep-ci/overview/) — guia oficial de execução em CI, eventos, escaneamento de código e comportamento de findings; consultado em 2026-10-04.
