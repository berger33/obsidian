---
id: software.seguranca.tranche18.001708
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

# Semgrep: Exclusões de arquivos do scan

## Em uma frase
**Semgrep — Exclusões de arquivos do scan:** Regras de ignore determinam que arquivos e diretórios não entrem na análise e precisam refletir o escopo pretendido.

## Por que importa
O recorte de **exclusões de arquivos do scan** ajuda a localizar padrões de risco reproduzíveis e transformar verificações de segurança em regras versionadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **exclusões de arquivos do scan**, o scanner seleciona linguagens e regras, percorre arquivos elegíveis e reporta os trechos que correspondem às condições declaradas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Ignore diretório gerado identificado no repositório e registre por que código executável não foi excluído. Teste em staging autorizado.

## Limites e trade-offs
Uma exclusão ampla pode remover código de produção sem alerta. Exceções exigem responsável e prazo.

## Como verificar
Revise a lista de arquivos ignorados no CI e confronte-a com os diretórios de aplicação. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[semgrep-supressao-rastreavel-de-finding]] — Complementa o tópico com semgrep: supressão rastreável de finding.

## Fontes
- [Semgrep — Run rules](https://semgrep.dev/docs/running-rules) — documentação oficial de regras YAML, regras locais, regrasets e execução; consultado em 2026-10-04.
- [Semgrep — CI overview](https://semgrep.dev/docs/semgrep-ci/overview/) — guia oficial de execução em CI, eventos, escaneamento de código e comportamento de findings; consultado em 2026-10-04.
