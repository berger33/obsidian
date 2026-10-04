---
id: software.testes.tranche15.000875
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://www.npmjs.com/package/supertest", "https://visionmedia.github.io/superagent/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Supertest: definir autenticação por cabeçalho

## Em uma frase
O método `set` adiciona cabeçalhos à requisição e é o caminho para enviar token de portador, chave de API ou cabeçalhos condicionais específicos do caso.

## Por que importa
Rotas protegidas precisam ser exercitadas tanto com credencial válida quanto inválida, e um helper único que sempre injeta o token esconde esses cenários negativos.

## Como funciona
Declare o cabeçalho no próprio caso sob teste, usando valores curtos e explícitos, e cubra ausência, expiração e formato inválido em testes separados.

## Exemplo
`request(app).get('/admin').set('Authorization', 'Bearer token-de-teste').expect(200);` demonstra o cabeçalho no ponto de uso.

## Limites e trade-offs
Token fixo no teste não comprova a política real de emissão e expiração; o caso verifica apenas o caminho de autorização configurado no ambiente controlado.

## Como verificar
Rode o caso com e sem o cabeçalho e confirme que a diferença de resposta corresponde ao contrato de autorização.

## Conexões
- [[supertest-multipart-attach]] — Veja também: Supertest: enviar arquivos com attach.
- [[supertest-timeouts]] — Veja também: Supertest: limitar tempo de resposta em teste.

## Fontes
- [Supertest — pacote npm](https://www.npmjs.com/package/supertest) — exemplos de request, expect, agent e asserções de resposta; consultado em 2026-10-02.
- [Superagent — documentação](https://visionmedia.github.io/superagent/) — cliente HTTP e métodos herdados usados pelo Supertest; consultado em 2026-10-02.
