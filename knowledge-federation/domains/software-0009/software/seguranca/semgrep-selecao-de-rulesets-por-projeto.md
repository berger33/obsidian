---
id: software.seguranca.tranche18.001706
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

# Semgrep: Seleção de rulesets por projeto

## Em uma frase
**Semgrep — Seleção de rulesets por projeto:** Rulesets agrupam regras por linguagem, categoria ou framework e podem ser combinados com regras locais.

## Por que importa
O recorte de **seleção de rulesets por projeto** ajuda a localizar padrões de risco reproduzíveis e transformar verificações de segurança em regras versionadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **seleção de rulesets por projeto**, o scanner seleciona linguagens e regras, percorre arquivos elegíveis e reporta os trechos que correspondem às condições declaradas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em um repositório Python, execute um ruleset aplicável e acrescente uma regra da equipe para uma API interna. Teste em staging autorizado.

## Limites e trade-offs
Ruleset externo pode mudar; depender de um nome sem registrar origem e versão reduz reprodutibilidade. Exceções exigem responsável e prazo.

## Como verificar
Registre as fontes de regras usadas e confira no relatório quais ids foram realmente executados. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[semgrep-escaneamento-em-pull-request]] — Complementa o tópico com semgrep: escaneamento em pull request.

## Fontes
- [Semgrep — Run rules](https://semgrep.dev/docs/running-rules) — documentação oficial de regras YAML, regras locais, regrasets e execução; consultado em 2026-10-04.
- [Semgrep — CI overview](https://semgrep.dev/docs/semgrep-ci/overview/) — guia oficial de execução em CI, eventos, escaneamento de código e comportamento de findings; consultado em 2026-10-04.
