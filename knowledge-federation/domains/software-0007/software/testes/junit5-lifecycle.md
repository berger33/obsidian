---
id: software.testes.tranche18.001178
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

# JUnit 5: preparar e limpar nos níveis corretos

## Em uma frase
As anotações de ciclo de vida permitem preparar por método, por classe ou por execução, com controle de herança e de ordem entre extensões.

## Por que importa
O estado compartilhado precisa ser restaurado no nível correspondente para que os casos permaneçam independentes.

## Como funciona
Prepare no nível mais estreito que atenda ao caso, use o nível de classe para recursos custosos e mantenha a limpeza simétrica à preparação.

## Exemplo
Uma conexão de banco pode ser aberta por classe e os registros criados podem ser removidos antes de cada método.

## Limites e trade-offs
Preparação de classe sem limpeza deixa resíduos entre execuções, e a herança de métodos de ciclo de vida pode surpreender quem lê apenas a subclasse.

## Como verificar
Execute a mesma classe isolada e dentro de uma suíte maior e confirme que o resultado não depende de estado residual.

## Conexões
- [[junit5-annotations-basics]] — Veja também: JUnit 5: marcar testes com anotações.
- [[junit5-assertions]] — Veja também: JUnit 5: escrever asserções com mensagens úteis.

## Fontes
- [JUnit 5 — User Guide](https://junit.org/junit5/docs/current/user-guide/) — anotações, ciclo de vida, asserções, parametrização, extensões e paralelismo; consultado em 2026-10-03.
- [JUnit 5 — repositório oficial](https://github.com/junit-team/junit5) — código-fonte, notas de versão e documentação do projeto; consultado em 2026-10-03.
