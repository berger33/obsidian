---
id: software.testes.tranche23.001723
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

# O grafo de Requests decide a ordem do fuzzing

## Em uma frase
Com as mensagens definidas, o mesmo Quickstart conecta tudo à Session: session.connect(user); session.connect(user, passw); session.connect(passw, stor); session.connect(passw, retr) — e a doc traduz a semântica em uma frase: ao fuzzar, o boofuzz "will send user before fuzzing passw, and user and passw before fuzzing stor or retr".

## Por que importa
Protocolos com sessão (autenticação antes de transação) são justamente onde fuzzers de bytes livres morrem; o grafo é como boofuzz preserva pré-condições de estado antes de atacar cada mensagem, mantendo o mutator focado na mensagem corrente.

## Como funciona
O connect é por par de Requests; o grafo resultante é a estrutura que o fuzzer percorre, e o log e web UI de cada run expõem a sequência executada — a mesma Session objeto recebe as arestas e conduz a campanha.

## Exemplo
Adicione uma aresta stor antes de user no seu grafo de teste e observe no log que o servidor rejeita o pacote fora de contexto — depois conserte e veja o mutator atacar o campo val de cada mensagem na ordem correta.

## Limites e trade-offs
A Quickstart descreve a ordem de dependência do grafo, não um motor de transições com guardas — a doc de state machines/validações (callbacks, nota própria) é camada separada; o exemplo FTP tem o grafo mínimo sem ciclos nem condições de retorno.

## Como verificar
Abra a seção do grafo no Quickstart oficial e confirme os quatro calls connect e a frase explicando a ordem de envio.

## Conexões
- [[boofuzz-request-grammar]] — Veja também: Requests com String, Delim e Static: o protocolo como AST.
- [[boofuzz-fuzz-run]] — Veja também: session.fuzz() — e a honestidade do "basic fuzzer".

## Fontes
- [boofuzz — Quickstart (Read the Docs)](https://boofuzz.readthedocs.io/en/stable/user/quickstart.html) — Session, Target, conexões, Requests, grafo, resultados e exemplos; consultado em 2026-10-03.
- [boofuzz — README.rst oficial](https://github.com/jtpereyda/boofuzz/blob/master/README.rst) — sucessão ao Sulley, features, instalação e comunidade; consultado em 2026-10-03.
