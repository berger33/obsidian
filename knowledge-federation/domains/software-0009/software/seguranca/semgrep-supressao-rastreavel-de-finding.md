---
id: software.seguranca.tranche18.001709
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

# Semgrep: Supressão rastreável de finding

## Em uma frase
**Semgrep — Supressão rastreável de finding:** Supressões locais podem reduzir um alerta conhecido, mas devem apontar para regra e justificativa de escopo limitado.

## Por que importa
O recorte de **supressão rastreável de finding** ajuda a localizar padrões de risco reproduzíveis e transformar verificações de segurança em regras versionadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **supressão rastreável de finding**, o scanner seleciona linguagens e regras, percorre arquivos elegíveis e reporta os trechos que correspondem às condições declaradas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em uma fixture, suprima apenas o id de regra aprovado e adicione comentário com issue e prazo de revisão. Teste em staging autorizado.

## Limites e trade-offs
Supressões sem justificativa persistem após mudanças no código e podem esconder novos caminhos. Exceções exigem responsável e prazo.

## Como verificar
Faça uma checagem de supressões expiradas e confirme que remover o comentário restaura o finding. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[semgrep-testes-de-regressao-para-regras]] — Complementa o tópico com semgrep: testes de regressão para regras.

## Fontes
- [Semgrep — Run rules](https://semgrep.dev/docs/running-rules) — documentação oficial de regras YAML, regras locais, regrasets e execução; consultado em 2026-10-04.
- [Semgrep — CI overview](https://semgrep.dev/docs/semgrep-ci/overview/) — guia oficial de execução em CI, eventos, escaneamento de código e comportamento de findings; consultado em 2026-10-04.
