---
id: software.seguranca.tranche18.001701
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

# Semgrep: Estrutura de uma regra YAML

## Em uma frase
**Semgrep — Estrutura de uma regra YAML:** Uma regra combina identificador, linguagens, padrão, severidade e mensagem para descrever uma classe de achado.

## Por que importa
O recorte de **estrutura de uma regra yaml** ajuda a localizar padrões de risco reproduzíveis e transformar verificações de segurança em regras versionadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **estrutura de uma regra yaml**, o scanner seleciona linguagens e regras, percorre arquivos elegíveis e reporta os trechos que correspondem às condições declaradas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Crie regra local para uma chamada insegura em fixture pequena e mantenha seu arquivo junto dos testes. Teste em staging autorizado.

## Limites e trade-offs
Identificador ou linguagem incompatível pode deixar a regra sem efeito mesmo que o YAML seja válido. Exceções exigem responsável e prazo.

## Como verificar
Rode a regra contra caso positivo e negativo e confira id, arquivo, linha e texto do finding. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[semgrep-metavariaveis-em-padroes-de-codigo]] — Complementa o tópico com semgrep: metavariáveis em padrões de código.

## Fontes
- [Semgrep — Run rules](https://semgrep.dev/docs/running-rules) — documentação oficial de regras YAML, regras locais, regrasets e execução; consultado em 2026-10-04.
- [Semgrep — CI overview](https://semgrep.dev/docs/semgrep-ci/overview/) — guia oficial de execução em CI, eventos, escaneamento de código e comportamento de findings; consultado em 2026-10-04.
