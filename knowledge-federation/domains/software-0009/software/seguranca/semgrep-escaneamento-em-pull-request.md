---
id: software.seguranca.tranche18.001707
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

# Semgrep: Escaneamento em pull request

## Em uma frase
**Semgrep — Escaneamento em pull request:** Jobs de CI podem ser acionados em push e pull request e podem comparar alterações com uma referência-base.

## Por que importa
O recorte de **escaneamento em pull request** ajuda a localizar padrões de risco reproduzíveis e transformar verificações de segurança em regras versionadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escaneamento em pull request**, o scanner seleciona linguagens e regras, percorre arquivos elegíveis e reporta os trechos que correspondem às condições declaradas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Configure um job de teste para PRs e outro agendado na branch principal, cada um com baseline explícito. Teste em staging autorizado.

## Limites e trade-offs
Um scan diff-aware não substitui o inventário completo da branch principal. Exceções exigem responsável e prazo.

## Como verificar
Compare o resultado do PR com um scan integral e confirme que findings antigos continuam visíveis no baseline. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[semgrep-exclusoes-de-arquivos-do-scan]] — Complementa o tópico com semgrep: exclusões de arquivos do scan.

## Fontes
- [Semgrep — Run rules](https://semgrep.dev/docs/running-rules) — documentação oficial de regras YAML, regras locais, regrasets e execução; consultado em 2026-10-04.
- [Semgrep — CI overview](https://semgrep.dev/docs/semgrep-ci/overview/) — guia oficial de execução em CI, eventos, escaneamento de código e comportamento de findings; consultado em 2026-10-04.
