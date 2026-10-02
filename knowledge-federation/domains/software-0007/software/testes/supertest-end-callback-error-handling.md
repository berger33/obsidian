---
id: software.testes.tranche15.000873
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
fontes: ["https://github.com/ladjs/supertest", "https://nodejs.org/api/test.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Supertest: decidir entre callback e promessa

## Em uma frase
O método `end` recebe callback com erro e resposta e pode ser usado quando o teste precisa de controle explícito, enquanto o estilo de promessa cobre a maioria dos casos.

## Por que importa
Misturar `end` com `await` na mesma requisição não dispara a requisição como esperado e produz teste que passa sem executar a chamada.

## Como funciona
Escolha um estilo por teste: aguarde a promessa da requisição ou passe o callback para `end`, sem combinar os dois nem esquecer de tratar o parâmetro de erro.

## Exemplo
`request(app).get('/saude').end((erro, resposta) => { if (erro) return done(erro); expect(resposta.status).toBe(200); done(); });` mostra o tratamento explícito.

## Limites e trade-offs
Callback sem repasse de erro faz a falha aparecer como timeout do executor, e promessas rejeitadas exigem que o framework de teste realmente aguarde o retorno do caso.

## Como verificar
Force um erro de conexão e confirme que a suíte reporta a causa real, não apenas o tempo esgotado do teste.

## Conexões
- [[supertest-send-json-body]] — Veja também: Supertest: enviar corpo JSON com send.
- [[supertest-multipart-attach]] — Veja também: Supertest: enviar arquivos com attach.

## Fontes
- [Supertest — repositório oficial](https://github.com/ladjs/supertest) — README, opções de uso e integração com servidores e agentes; consultado em 2026-10-02.
- [Node.js — Test runner](https://nodejs.org/api/test.html) — executor de testes nativo do Node.js e suas APIs; consultado em 2026-10-02.
