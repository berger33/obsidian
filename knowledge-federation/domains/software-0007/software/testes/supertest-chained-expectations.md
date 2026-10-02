---
id: software.testes.tranche15.000871
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

# Supertest: encadear expectativas de resposta

## Em uma frase
O método `expect` permite afirmar status, cabeçalhos e corpo em uma única cadeia encadeada à requisição, com falha apontando a expectativa violada.

## Por que importa
Verificar apenas o status deixa passar respostas com tipo de conteúdo ou corpo errados, e asserções separadas espalham a intenção do contrato em vários pontos do teste.

## Como funciona
Encadeie as condições essenciais do contrato, usando expressão regular ou valor exato para cabeçalhos e confiando no encadeamento para interromper na primeira divergência.

## Exemplo
`request(app).get('/usuarios').expect(200).expect('Content-Type', /json/).expect(res => Array.isArray(res.body));` documenta o contrato em uma leitura.

## Limites e trade-offs
Encadear demais transforma o teste em uma lista de detalhes frágeis; campos voláteis como data ou identificador gerado pedem verificação própria em vez de igualdade fixa.

## Como verificar
Remova deliberadamente um cabeçalho do servidor de teste e confirme que a cadeia falha indicando exatamente qual expectativa não foi satisfeita.

## Conexões
- [[supertest-agent-persistent-cookies]] — Veja também: Supertest: manter sessão com request.agent.
- [[supertest-send-json-body]] — Veja também: Supertest: enviar corpo JSON com send.

## Fontes
- [Supertest — pacote npm](https://www.npmjs.com/package/supertest) — exemplos de request, expect, agent e asserções de resposta; consultado em 2026-10-02.
- [Superagent — documentação](https://visionmedia.github.io/superagent/) — cliente HTTP e métodos herdados usados pelo Supertest; consultado em 2026-10-02.
