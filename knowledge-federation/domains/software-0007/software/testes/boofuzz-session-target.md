---
id: software.testes.tranche23.001721
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
fontes: ["https://boofuzz.readthedocs.io/en/stable/user/quickstart.html", "https://github.com/jtpereyda/boofuzz/blob/master/README.rst"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Session é o centro; Target carrega a conexão

## Em uma frase
A doc de quickstart abre com a definição operacional: o objeto Session é "the center of your fuzz… session", criado com um Target que, por sua vez, recebe um objeto de Connection — o exemplo canônico é uma Session com Target com TCPSocketConnection apontando para 127.0.0.1 porta 8021.

## Por que importa
Essa tripla camada separa quem controla a campanha (Session), quem é o alvo (Target) e como se fala com ele (Connection) — a razão de a lista de features prometer "arbitrary communications mediums" sem tocar no motor.

## Como funciona
As conexões implementam a interface ITargetConnection; a página nomeia TCPSocketConnection e suas "sister classes" para UDP, SSL e raw sockets, mais SerialConnection — a cobertura serial/ethernet/IP-layer/UDP broadcast declarada no README é exposta aqui como classe de conexão.

## Exemplo
Instancie a Session do exemplo apontando para um servidor de eco TCP local e chame session.connect de uma Request mínima (nota do grafo) para ver a tripla se fechar; a doc acompanha o objeto no web UI do run.

## Limites e trade-offs
A página de quickstart lista as classes por nome mas a assinatura completa de cada uma mora na referência de API (os links por âncora são para as páginas source/Target etc.); a doc de conexões, citada como destino, é o contrato real de parâmetros.

## Como verificar
Abra a primeira tela do Quickstart oficial e confira a frase da Session, o snippet de três linhas e a lista de classes de conexão.

## Conexões
- [[boofuzz-successor-of-sulley]] — Veja também: boofuzz: o sucessor extensível do Sulley, "fuzz everything".
- [[boofuzz-request-grammar]] — Veja também: Requests com String, Delim e Static: o protocolo como AST.

## Fontes
- [boofuzz — Quickstart (Read the Docs)](https://boofuzz.readthedocs.io/en/stable/user/quickstart.html) — Session, Target, conexões, Requests, grafo, resultados e exemplos; consultado em 2026-10-03.
- [boofuzz — README.rst oficial](https://github.com/jtpereyda/boofuzz/blob/master/README.rst) — sucessão ao Sulley, features, instalação e comunidade; consultado em 2026-10-03.
