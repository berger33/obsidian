---
id: software.seguranca.tranche18.001705
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

# Semgrep: Sanitizadores em regras de taint

## Em uma frase
**Semgrep — Sanitizadores em regras de taint:** Sanitizadores permitem modelar transformações que removem ou limitam uma classe específica de entrada perigosa.

## Por que importa
O recorte de **sanitizadores em regras de taint** ajuda a localizar padrões de risco reproduzíveis e transformar verificações de segurança em regras versionadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **sanitizadores em regras de taint**, o scanner seleciona linguagens e regras, percorre arquivos elegíveis e reporta os trechos que correspondem às condições declaradas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Adicione uma função de escaping conhecida ao modelo apenas depois de revisar seu contrato e os contextos suportados. Teste em staging autorizado.

## Limites e trade-offs
Um sanitizador para HTML não torna o mesmo dado seguro para SQL, shell ou URL. Exceções exigem responsável e prazo.

## Como verificar
Crie fixtures por contexto de saída e verifique que a regra ainda sinaliza a sanitização inadequada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[semgrep-selecao-de-rulesets-por-projeto]] — Complementa o tópico com semgrep: seleção de rulesets por projeto.

## Fontes
- [Semgrep — Run rules](https://semgrep.dev/docs/running-rules) — documentação oficial de regras YAML, regras locais, regrasets e execução; consultado em 2026-10-04.
- [Semgrep — CI overview](https://semgrep.dev/docs/semgrep-ci/overview/) — guia oficial de execução em CI, eventos, escaneamento de código e comportamento de findings; consultado em 2026-10-04.
