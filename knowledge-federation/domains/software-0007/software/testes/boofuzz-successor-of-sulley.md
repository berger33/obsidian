---
id: software.testes.tranche23.001720
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/jtpereyda/boofuzz/blob/master/README.rst", "https://boofuzz.readthedocs.io/en/stable/user/quickstart.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# boofuzz: o sucessor extensível do Sulley, "fuzz everything"

## Em uma frase
O README oficial define o projeto: "a fork of and the successor to the venerable Sulley fuzzing framework", que, além de correções de bugs, mira extensibilidade — "The goal: fuzz everything" — e justifica a existência porque o Sulley, por anos o fuzzer open source preeminente, caiu em desmanutenção; o nome homenageia o único personagem que assustou o próprio Sulley no Monstros S.A.

## Por que importa
Sulley definiu o padrão de fuzzers de protocolo com data generation, crash detection, reset de alvo e gravação de testes; adotar o boofuzz é adotar esse modelo com o checklist de melhorias declarado: documentação online, meios de comunicação arbitrários, serial/ethernet/IP/UDP broadcast nativos, gravação de dados "consistent, thorough, clear", export CSV, instrumentação extensível e muito menos bugs.

## Como funciona
A instalação declarada é um pip install boofuzz — a biblioteca "installs as a Python library used to build fuzzer scripts", isto é, cada campanha de fuzz é um script seu importando o framework, não um binário com config.

## Exemplo
Abra o README e o CHANGELOG do repositório e confira as frases citadas; a lista de features "Unlike Sulley" está em bullets literais na seção homônima.

## Limites e trade-offs
A comparação com o Sulley é o relato do mantenedor — o repositório OpenRCE/sulley existe como histórico, não como baseline medida; a doc não publica benchmarks de detecção contra o antecessor.

## Como verificar
Confirme no README.rst oficial as seções Why, Features (ambas as listas) e Installation, incluindo a frase do pip install.

## Conexões
- [[boofuzz-session-target]] — Veja também: Session é o centro; Target carrega a conexão.

## Fontes
- [boofuzz — README.rst oficial](https://github.com/jtpereyda/boofuzz/blob/master/README.rst) — sucessão ao Sulley, features, instalação e comunidade; consultado em 2026-10-03.
- [boofuzz — Quickstart (Read the Docs)](https://boofuzz.readthedocs.io/en/stable/user/quickstart.html) — Session, Target, conexões, Requests, grafo, resultados e exemplos; consultado em 2026-10-03.
